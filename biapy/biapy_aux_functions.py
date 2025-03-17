import os
import math
import functools
import numpy as np
import pandas as pd
from skimage.io import imread
from typing import Optional, Dict, Tuple
from packaging.version import Version
from pathlib import Path
import pooch
import yaml
from logging import Logger

## Copied from BiaPy commit: f2360c1d3796df13614dc8c005299a8989cf27fd (3.5.11)
def check_bmz_model_compatibility_in_GUI(
    model_rdf_file: Dict,
    model_name: str,
    model_version: str,
    biapy_version: str,
    workflow_specs: Dict,
    logger: Logger,
) -> Tuple[bool, Optional[Dict]]:
    """
    Checks one model compatibility with BiaPy by looking at the compatibility file created from the CI. 
    Here just the minimum information is checked, i.e. workflow and dimensions, as more detailed checks 
    are done in the CI.

    Parameters
    ----------
    model_rdf_file : str
        RDF file of the model. 

    model_name : str
        Name of the model.

    model_version : str
        Version of the model.  

    biapy_version : str
        Version of BiaPy to check the compatibility with. 

    logger : Logger
        Logger to log messages.

    workflow_specs : dict
        Specifications of the workflow. If not provided all possible models will be considered.

    Returns
    -------
    consumable : bool
        Whether if the model can be consumed by BiaPy or not with the selected configuration.

    model_rdf : dict
        BMZ model RDF that contains all the information of the model.
    """
    consumable = False

    biapy_model_compatibility_file = f"https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/{model_name}/{model_version}/compatibility/biapy_{biapy_version}.json"
    logger.info(f"Checking BiaPy compatibility file: {biapy_model_compatibility_file}")
    try:
        with open(Path(pooch.retrieve(biapy_model_compatibility_file, known_hash=None)), "rt", encoding="utf8") as stream:
            model_comp_file = yaml.safe_load(stream)
            compatible = True if model_comp_file["status"] == "passed" else False
    except:
        logger.info("There was a problem reading the compatibility file so the model will not be listed as consumible just in case.")  
    
    if not compatible:
        return False, None

    specific_workflow = "all" if workflow_specs is None else workflow_specs["workflow_type"]
    specific_dims = "all" if workflow_specs is None else workflow_specs["ndim"]

    try:
        with open(Path(pooch.retrieve(model_rdf_file, known_hash=None)), "rt", encoding="utf8") as stream:
            model_rdf = yaml.safe_load(stream)
    except:
        logger.info("There was a problem reading the RDF file of the model")  
        return False, None

    # Check problem type
    if (specific_workflow in ["all", "SEMANTIC_SEG"]) and (
        "semantic-segmentation" in model_rdf["tags"]
        or ("segmentation" in model_rdf["tags"] and "instance-segmentation" not in model_rdf["tags"])
    ):
        consumable = True
    elif specific_workflow in ["all", "INSTANCE_SEG"] and "instance-segmentation" in model_rdf["tags"]:
        consumable = True
    elif specific_workflow in ["all", "DETECTION"] and "detection" in model_rdf["tags"]:
        consumable = True
    elif specific_workflow in ["all", "DENOISING"] and "denoising" in model_rdf["tags"]:
        consumable = True
    elif specific_workflow in ["all", "SUPER_RESOLUTION"] and "super-resolution" in model_rdf["tags"]:
        consumable = True
    elif specific_workflow in ["all", "SELF_SUPERVISED"] and "self-supervision" in model_rdf["tags"]:
        consumable = True
    elif specific_workflow in ["all", "CLASSIFICATION"] and "classification" in model_rdf["tags"]:
        consumable = True
    elif specific_workflow in ["all", "IMAGE_TO_IMAGE"] and (
        "pix2pix" in model_rdf["tags"]
        or "image-reconstruction" in model_rdf["tags"]
        or "image-to-image" in model_rdf["tags"]
        or "image-restoration" in model_rdf["tags"]
    ):
        consumable = True

    if not consumable:
        return False, None 

    # Check axes
    axes_order = model_rdf["inputs"][0]["axes"]
    if isinstance(axes_order, list):
        _axes_order = ""
        for axis in axes_order:
            if "type" in axis:
                if axis["type"] == "batch":
                    _axes_order += "b"
                elif axis["type"] == "channel":
                    _axes_order += "c"
                elif "id" in axis:
                    _axes_order += axis["id"]
            elif "id" in axis:
                if axis["id"] == "channel":
                    _axes_order += "c"
                else:
                    _axes_order += axis["id"]
        axes_order = _axes_order

    if specific_dims == "2D":
        if axes_order != "bcyx":
            return False, None
        elif "2d" not in model_rdf["tags"] and "3d" in model_rdf["tags"]:
            return False, None
    elif specific_dims == "3D":
        if axes_order != "bczyx":
            return False, None
        elif "3d" not in model_rdf["tags"] and "2d" in model_rdf["tags"]:
            return False, None
    else:  # All
        if axes_order not in ["bcyx", "bczyx"]:
            return False, None

    return consumable, model_rdf


# Adapted from BiaPy commit: f2360c1d3796df13614dc8c005299a8989cf27fd (3.5.11)
def check_model_restrictions(
    model_rdf: Dict,
    workflow_specs: Dict,
) -> Dict:
    """
    Checks model restrictions to be applied into the current configuration.

    Parameters
    ----------
    model_rdf : dict
        BMZ model RDF that contains all the information of the model.

    workflow_specs : dict
        Specifications of the workflow. If not provided all possible models will be considered.

    Returns
    -------
    option_list: dict
        Variables and values to change in current configuration. These changes
        are imposed by the selected model.
    """
    specific_workflow = workflow_specs["workflow_type"]

    # Version of the model
    model_version = Version(model_rdf["format_version"])
    opts = {}

    # 1) Change PATCH_SIZE with the one stored in the model description. This differs from the code of BiaPy where
    # get_test_inputs() is simply used as there a ModelDescr is build out of the RDF. Here we try to do it manually
    # to avoid fetching files using the network as it may be slow.
    input_image_shape = []
    if "shape" in model_rdf["inputs"][0]:
        input_image_shape = model_rdf["inputs"][0]["shape"]
        # "CebraNET Cellular Membranes in Volume SEM" ('format_version': '0.4.10')
        #   have: {'min': [1, 1, 64, 64, 64], 'step': [0, 0, 16, 16, 16]}
        if isinstance(input_image_shape, dict) and "min" in input_image_shape:
            input_image_shape = input_image_shape["min"]
    else:
        # Check axes and dimension
        input_image_shape = []
        for axis in model_rdf["inputs"][0]["axes"]:
            if "type" in axis:
                if axis["type"] == "batch":
                    input_image_shape += [
                        1,
                    ]
                elif axis["type"] == "channel":
                    input_image_shape += [
                        1,
                    ]
                elif "id" in axis and "size" in axis:
                    if isinstance(axis["size"], int):
                        input_image_shape += [
                            axis["size"],
                        ]
                    elif "min" in axis["size"]:
                        input_image_shape += [
                            axis["size"]["min"],
                        ]
            elif "id" in axis:
                if axis["id"] == "channel":
                    input_image_shape += [
                        1,
                    ]
                else:
                    if isinstance(axis["size"], int):
                        input_image_shape += [
                            axis["size"],
                        ]
                    elif "min" in axis["size"]:
                        input_image_shape += [
                            axis["size"]["min"],
                        ]
    if len(input_image_shape) == 0:
        raise ValueError("Couldn't load input info from BMZ model's RDF: {}".format(model_rdf["inputs"][0]))
    opts["DATA.PATCH_SIZE"] = tuple(input_image_shape[2:]) + (input_image_shape[1],)

    # Capture model kwargs
    if "kwargs" in model_rdf["weights"]["pytorch_state_dict"]:
        model_kwargs = model_rdf["weights"]["pytorch_state_dict"]["kwargs"]
    elif (
        "architecture" in model_rdf["weights"]["pytorch_state_dict"]
        and "kwargs" in model_rdf["weights"]["pytorch_state_dict"]["architecture"]
    ):
        model_kwargs = model_rdf["weights"]["pytorch_state_dict"]["architecture"]["kwargs"]
    else:
        raise ValueError(f"Couldn't extract kwargs from model description.")

    # 2) Workflow specific restrictions
    # Classes in semantic segmentation
    if specific_workflow in ["SEMANTIC_SEG"]:
        # Check number of classes
        classes = -1
        if "n_classes" in model_kwargs:  # BiaPy
            classes = model_kwargs["n_classes"]
        elif "out_channels" in model_kwargs:
            classes = model_kwargs["out_channels"]
        elif "classes" in model_kwargs:
            classes = model_kwargs["classes"]
        if isinstance(classes, list):
            classes = classes[0]

        if not isinstance(classes, int):
            raise ValueError(f"Classes not extracted correctly. Obtained {classes}")
        if specific_workflow == "SEMANTIC_SEG" and classes == -1:
            raise ValueError("Classes not found for semantic segmentation dir. ")

        opts["MODEL.N_CLASSES"] = max(2, classes)

    elif specific_workflow in ["INSTANCE_SEG"]:
        # Assumed it's BC. This needs a more elaborated process. Still deciding this:
        # https://github.com/bioimage-io/spec-bioimage-io/issues/621

        # Defaults
        channels = 2
        channel_code = "BC" 
        classes = 2

        if "out_channels" in model_kwargs:
            channels = model_kwargs["out_channels"]
        elif "output_channels" in model_kwargs:
            channels = model_kwargs["output_channels"]

        if "biapy" in model_rdf["tags"]:
            # CartoCell models
            if (
                "cyst" in model_rdf["tags"]
                and "3d" in model_rdf["tags"]
                and "fluorescence" in model_rdf["tags"]
            ):
                channel_code = "BCM"

            # Handle multihead
            assert isinstance(channels, list)
            if len(channels) == 2:
                classes = channels[-1]
            channels = channels[0]

        else: # for other models set some defaults
            if isinstance(channels, list):
                channels = channels[-1]
            if channels == 1:
                channel_code = "C"
            elif channels == 2:
                channel_code = "BC"
            elif channels == 8:
                channel_code = "A"

        opts["PROBLEM.INSTANCE_SEG.DATA_CHANNELS"] = channel_code
        opts["PROBLEM.INSTANCE_SEG.DATA_CHANNEL_WEIGHTS"] = [1,]*channels
        if classes != 2:
            opts["MODEL.N_CLASSES"] = max(2, classes)
        if channel_code == "A":
            opts["LOSS.CLASS_REBALANCE"] = True

    if "preprocessing" not in model_rdf["inputs"][0]:
        return opts

    preproc_info = model_rdf["inputs"][0]["preprocessing"]
    if len(preproc_info) == 0:
        return opts
    preproc_info = preproc_info[0]

    # 3) Change preprocessing to the one stablished by BMZ by translate BMZ keywords into BiaPy's
    # 'zero_mean_unit_variance' and 'fixed_zero_mean_unit_variance' norms of BMZ can be translated to our 'custom' norm
    # providing mean and std
    key_to_find = "id" if model_version > Version("0.5.0") else "name"
    if key_to_find in preproc_info:
        if preproc_info[key_to_find] in ["fixed_zero_mean_unit_variance", "zero_mean_unit_variance"]:
            if "kwargs" in preproc_info and "mean" in preproc_info["kwargs"]:
                mean = preproc_info["kwargs"]["mean"]
                std = preproc_info["kwargs"]["std"]
            elif "mean" in preproc_info:
                mean = preproc_info["mean"]
                std = preproc_info["std"]
            else:
                mean, std = -1.0, -1.0

            opts["DATA.NORMALIZATION.TYPE"] = "zero_mean_unit_variance"
            opts["DATA.NORMALIZATION.ZERO_MEAN_UNIT_VAR.MEAN_VAL"] = mean
            opts["DATA.NORMALIZATION.ZERO_MEAN_UNIT_VAR.STD_VAL"] = std

        # 'scale_linear' norm of BMZ is close to our 'div' norm (TODO: we need to control the "gain" arg)
        elif preproc_info[key_to_find] == "scale_linear":
            opts["DATA.NORMALIZATION.TYPE"] = "div"

        # 'scale_range' norm of BMZ is as our PERC_CLIP + 'scale_range' norm
        elif preproc_info[key_to_find] == "scale_range":
            opts["DATA.NORMALIZATION.TYPE"] = "scale_range"
            if (
                float(preproc_info["kwargs"]["min_percentile"]) != 0
                or float(preproc_info["kwargs"]["max_percentile"]) != 100
            ):
                opts["DATA.NORMALIZATION.PERC_CLIP"] = True
                opts["DATA.NORMALIZATION.PERC_LOWER"] = float(preproc_info["kwargs"]["min_percentile"])
                opts["DATA.NORMALIZATION.PERC_UPPER"] = float(preproc_info["kwargs"]["max_percentile"])

    return opts


def get_cfg_key_value(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))


def check_images(data_dir, is_mask=False, mask_type="", is_3d=False, dir_name=None):
    """
    Check images in folder.

    Parameters
    ----------
    data_dir : str
        Directory to check images from.

    is_mask : bool, optional
        Whether the images to check are masks and not raw images. It disables data range checking.

    mask_type : bool, optional
        Whether the images to check are semantic masks (``semantic_mask``) or instace masks (``instance_mask``).
        It checks the number of classes within masks.

    is_3d: bool, optional
        Whether to expect to read 3D images or 2D.

    dir_name : str, optional
        Name of the directory processed.

    Returns
    -------
    error : bool
        ``True`` if something went wrong during folder check.

    error_message: str
        Reason of the error (if any).

    constraints: dict
        BiaPy variables to set. This info is extracted from the images read. E.g. ``{"DATA.PATCH_SIZE": 1}``

    sample_info : dict
        Information of the samples within the directory analized. Keys:
            * ``'total_samples'``: total number of samples in the directory.
            * ``'crop_shape'``: shape of the crop used to analize the samples.
            * ``'dir_name'``: name of the directory analized.
    """
    assert mask_type in ["", "semantic_mask", "instance_mask"]

    print(f"Checking images from {data_dir}")

    nclasses = 2
    channel_expected = -1
    data_range_expected = -1

    try:
        ids = sorted(next(os.walk(data_dir))[2])
    except Exception as exc:
        error_message = f"Something strange happens when listing files in {data_dir}. Error:\n{exc}"
        return True, error_message, {}, {}

    if len(ids) == 0:
        error_message = f"No images found in folder:\n{data_dir}"
        return True, error_message, {}, {}

    # To calculate the number os samples that can be extracted in the same way as BiaPy does. This is useful to
    # calculate later the batch size.
    total_samples = 0
    crop_shape = (256, 256, 1) if not is_3d else (20, 128, 128, 1)
    crop_funct = crop_3D_data_with_overlap if is_3d else crop_data_with_overlap

    shapes = []
    for id_ in ids:
        img_path = os.path.join(data_dir, id_)
        if id_.endswith(".npy"):
            img = np.load(img_path)
        else:
            try:
                img = imread(img_path)
            except Exception:
                error_message = f"Couldn't load image:\n{img_path}"
                return True, error_message, {}, {}

        # Shape adjust
        if not is_3d:
            img = ensure_2d_shape(img.squeeze(), path=img_path)
        else:
            img = ensure_3d_shape(img.squeeze(), path=img_path)

        # Channel check
        if channel_expected == -1:
            channel_expected = img.shape[-1]
        if img.shape[-1] != channel_expected:
            error_message = (
                f"All images need to have the same number of channels and represent same information to "
                "ensure the deep learning model can be trained correctly. However, the current image (with "
                f"{channel_expected} channels) appears to have a different number of channels than the first image"
                f"(with {img.shape[-1]} channels) in the folder. Current image:\n{img_path}"
            )
            return True, error_message, {}, {}
        shapes.append(img.shape)

        # Data range check
        if not is_mask:
            if data_range_expected == -1:
                data_range_expected = data_range(img)
            drange = data_range(img)
            if data_range_expected != drange:
                error_message = (
                    f"All images must be within the same data range. However, the current image (with a "
                    f"range of {drange}) appears to be in a different data range than the first image (with a range "
                    f"of {data_range_expected}) in the folder. Current image:\n{img_path}"
                )
                return True, error_message, {}, {}

        if mask_type == "semantic_mask":
            if channel_expected != 1:
                error_message = f"Semantic masks are expected to have just one channel. Image analized:\n{img_path}"
                return True, error_message, {}, {}
            else:
                nclasses = max(nclasses, len(np.unique(img)))
        elif mask_type == "instance_mask":
            if channel_expected == 2:
                nclasses = max(nclasses, len(np.unique(img[..., 1])))
            else:
                if channel_expected != 1:
                    error_message = (
                        f"Instance masks are expected to have one or two channels. In case two channels are provided "
                        "the first one must have the instance IDs and one their corresponding semantic (class) labels. "
                        f"Image analized:\n{img_path}"
                    )
                    return True, error_message, {}, {}

        # Calculate number of samples that can be extracted here
        img = pad_and_reflect(img, crop_shape, verbose=False)
        if img.shape != crop_shape[:-1] + (img.shape[-1],):
            crop_coords = crop_funct(
                np.expand_dims(img, axis=0) if not is_3d else img,
                crop_shape[:-1] + (img.shape[-1],),
                verbose=False,
                load_data=False,
            )
            total_samples += len(crop_coords)
        else:
            total_samples += 1

    constraints = {
        "DATA.PATCH_SIZE_C": channel_expected,
    }
    if nclasses > 2:
        constraints["MODEL.N_CLASSES"] = nclasses

    if dir_name is not None:
        constraints[dir_name] = len(ids)
        constraints[dir_name + "_path"] = data_dir
        constraints[dir_name + "_path_shapes"] = shapes

    return False, "", constraints, {"total_samples": total_samples, "crop_shape": crop_shape, "dir_name": dir_name}


def ensure_2d_shape(img, path=None):
    """
    Read an image from a given path.

    Parameters
    ----------
    img : ndarray
        Image read.

    path : str
        Path of the image (just use to print possible errors).

    Returns
    -------
    img : Numpy 3D array
        Image read. E.g. ``(y, x, num_classes)``.
    """
    if img.ndim > 3:
        if path is not None:
            m = "Read image seems to be 3D. Image shape is: {}.\nImage path:\n{}".format(img.shape, path)
        else:
            m = "Read image seems to be 3D. Image shape is: {}".format(img.shape)
        raise ValueError(m)

    if img.ndim == 2:
        img = np.expand_dims(img, -1)
    else:
        # Ensure channel axis is always in the first position (assuming Z is already set)
        min_val = min(img.shape)
        channel_pos = img.shape.index(min_val)
        if channel_pos != 2:
            new_pos = [x for x in range(3) if x != channel_pos] + [
                channel_pos,
            ]
            img = img.transpose(new_pos)
    return img


def ensure_3d_shape(img, path=None):
    """
    Read an image from a given path.

    Parameters
    ----------
    img : ndarray
        Image read.

    path : str
        Path of the image (just use to print possible errors).

    Returns
    -------
    img : Numpy 4D array
        Image read. E.g. ``(z, y, x, num_classes)``.
    """
    if img.ndim < 3:
        if path:
            m = "Read image seems to be 2D: {}. Path: {}".format(img.shape, path)
        else:
            m = "Read image seems to be 2D: {}".format(img.shape)
        raise ValueError(m)

    if img.ndim == 3:
        # Ensure Z axis is always in the first position
        min_val = min(img.shape)
        z_pos = img.shape.index(min_val)
        if z_pos != 0:
            new_pos = [
                z_pos,
            ] + [x for x in range(3) if x != z_pos]
            img = img.transpose(new_pos)

        img = np.expand_dims(img, -1)
    else:
        # Ensure channel axis is always in the first position (assuming Z is already set)
        min_val = min(img.shape)
        channel_pos = img.shape.index(min_val)
        if channel_pos != 3:
            new_pos = [x for x in range(4) if x != channel_pos] + [
                channel_pos,
            ]
            img = img.transpose(new_pos)
    return img


def check_csv_files(data_dir: str, is_3d: bool = False, dir_name: Optional[str] = None) -> Tuple[bool, str, Dict, Dict]:
    """
    Check CSV files in folder.

    Parameters
    ----------
    data_dir : str
        Directory to check images from.

    is_3d: bool, optional
        Whether to expect to read 3D images or 2D.

    dir_name : str, optional
        Name of the directory processed.

    Returns
    -------
    error : bool
        ``True`` if something went wrong during folder check.

    error_message: str
        Reason of the error (if any).

    constraints: dict
        BiaPy variables to set. This info is extracted from the images read. E.g. ``{"DATA.PATCH_SIZE": 1}``

    sample_info : dict
        Information of the samples within the directory analized. Keys:
            * ``'total_samples'``: total number of samples in the directory.
            * ``'crop_shape'``: shape of the crop used to analize the samples.
            * ``'dir_name'``: name of the directory analized.
    """
    print("Checking CSV files . . .")
    nclasses = 0
    try:
        ids = sorted(next(os.walk(data_dir))[2])
    except Exception as exc:
        error_message = f"Something strange happens when listing files in folder:\n{data_dir}.\nError:\n{exc}"
        return True, error_message, {}, {}

    if len(ids) == 0:
        error_message = f"No images found in folder:\n{data_dir}"
        return True, error_message, {}, {}

    req_columns = ["axis-0", "axis-1"] if not is_3d else ["axis-0", "axis-1", "axis-2"]

    classes_found = []
    for id_ in ids:
        csv_path = os.path.join(data_dir, id_)
        try:
            df = pd.read_csv(csv_path)
        except Exception:
            error_message = f"Couldn't load CSV file:\n{csv_path}"
            return True, error_message, {}, {}

        df = df.dropna()

        # Check columns in csv
        # Discard first index column to not have error if it is not sorted
        p_number = df.iloc[:, 0].to_list()
        df = df.rename(columns=lambda x: x.strip())  # trim spaces in column names
        columns_present = [x.lower() for x in df.columns]
        cols_not_in_file = [x for x in req_columns if x not in columns_present]
        if len(cols_not_in_file) > 0:
            if len(cols_not_in_file) == 1:
                error_message = f"'{cols_not_in_file[0]}' column is not present in CSV file:\n{csv_path}"
            else:
                error_message = f"{cols_not_in_file} columns are not present in CSV file:\n{csv_path}"
            return True, error_message, {}, {}

        # Check class in columns
        if "class" in columns_present:
            df["class"] = df["class"].astype("int")
            class_point = np.array(df["class"])

            uniq = np.sort(np.unique(class_point))
            for c in uniq:
                if c not in classes_found:
                    classes_found.append(c)

    nclasses = len(classes_found)

    constraints = {}
    if "class" in columns_present:
        constraints["MODEL.N_CLASSES"] = int(nclasses)
    if dir_name is not None:
        constraints[dir_name] = len(ids)
        constraints[dir_name + "_path"] = data_dir

    crop_shape = (0, 0, 0) if not is_3d else (0, 0, 0, 0)
    return False, "", constraints, {"total_samples": len(ids), "crop_shape": crop_shape, "dir_name": dir_name}


def check_classification_images(data_dir, is_3d=False, dir_name=None):
    """
    Check classification images in folder.

    Parameters
    ----------
    data_dir : str
        Directory to check images from.

    is_3d: bool, optional
        Whether to expect to read 3D images or 2D.

    dir_name : str, optional
        Name of the directory processed.

    Returns
    -------
    error : bool
        ``True`` if something went wrong during folder check.

    error_message: str
        Reason of the error (if any).

    constraints: dict
        BiaPy variables to set. This info is extracted from the images read. E.g. ``{"DATA.PATCH_SIZE": 1}``
    """
    print("Checking classification images . . .")

    channel_expected = -1
    data_range_expected = -1
    class_names = sorted(next(os.walk(data_dir))[1])
    if len(class_names) < 1:
        error_message = "There is no folder/class in folder:\n{}".format(data_dir)
        return True, error_message, {}, {}

    tot_samples = 0
    # Loop over each class/folder
    for folder in class_names:
        class_folder = os.path.join(data_dir, folder)
        print(f"Analizing folder {class_folder}")

        ids = sorted(next(os.walk(class_folder))[2])
        if len(ids) == 0:
            error_message = "There are no images in class folder:\n{}".format(class_folder)
            return True, error_message, {}, {}
        else:
            print("Found {} samples".format(len(ids)))

        # Check images of each class/folder
        tot_samples += len(ids)
        for id_ in ids:
            img_path = os.path.join(class_folder, id_)
            if id_.endswith(".npy"):
                img = np.load(img_path)
            else:
                try:
                    img = imread(img_path)
                except Exception:
                    error_message = f"Couldn't load image:\n{img_path}"
                    return True, error_message, {}, {}

            img = np.squeeze(img)
            # Shape adjust
            if not is_3d:
                img = ensure_2d_shape(img.squeeze(), path=img_path)
            else:
                img = ensure_3d_shape(img.squeeze(), path=img_path)

            # Channel check
            if channel_expected == -1:
                channel_expected = img.shape[-1]
            if img.shape[-1] != channel_expected:
                error_message = (
                    "All images need to have the same number of channels and represent same information to "
                    "ensure the deep learning model can be trained correctly. However, the following image (with "
                    f"{channel_expected} channels) appears to have a different number of channels than the first image "
                    f"(with {img.shape[-1]} channels) in the folder:\n{img_path}"
                )
                return True, error_message, {}, {}

            # Data range check
            if data_range_expected == -1:
                data_range_expected = data_range(img)
            drange = data_range(img)
            if data_range_expected != drange:
                error_message = (
                    "All images must be within the same data range. However, the following image (with a "
                    f"range of {drange}) appears to be in a different data range than the first image (with a range "
                    f"of {data_range_expected}) in the folder:\n{img_path}"
                )
                return True, error_message, {}, {}

    constraints = {
        "DATA.PATCH_SIZE_C": channel_expected,
        "MODEL.N_CLASSES": len(class_names),
    }
    if dir_name is not None:
        constraints[dir_name] = tot_samples
        constraints[dir_name + "_path"] = data_dir

    return False, "", constraints, {"total_samples": tot_samples, "crop_shape": (256, 256, 1), "dir_name": dir_name}


def data_range(x):
    if not isinstance(x, np.ndarray):
        raise ValueError("Input array of type {} and not numpy array".format(type(x)))
    if check_value(x, (0, 1)):
        return "01 range"
    elif check_value(x, (0, 255)):
        return "uint8 range"
    elif check_value(x, (0, 65535)):
        return "uint16 range"
    else:
        return "none_range"


def check_value(value, value_range=(0, 1)):
    """
    Checks if a value is within a range
    """
    if isinstance(value, list) or isinstance(value, tuple):
        for i in range(len(value)):
            if isinstance(value[i], np.ndarray):
                if value_range[0] <= np.min(value[i]) or np.max(value[i]) <= value_range[1]:
                    return False
            else:
                if not (value_range[0] <= value[i] <= value_range[1]):
                    return False
        return True
    else:
        if isinstance(value, np.ndarray):
            if value_range[0] <= np.min(value) and np.max(value) <= value_range[1]:
                return True
        else:
            if value_range[0] <= value <= value_range[1]:
                return True
        return False


# Copied from BiaPy commit: 284ec3838766392c9a333ac9d27b55816a267bb9 (3.5.2)
def crop_data_with_overlap(
    data, crop_shape, data_mask=None, overlap=(0, 0), padding=(0, 0), verbose=True, load_data=True
):
    """
    Crop data into small square pieces with overlap. The difference with :func:`~crop_data` is that this function
    allows you to create patches with overlap.

    The opposite function is :func:`~merge_data_with_overlap`.

    Parameters
    ----------
    data : 4D Numpy array
        Data to crop. E.g. ``(num_of_images, y, x, channels)``.

    crop_shape : 3 int tuple
        Shape of the crops to create. E.g. ``(y, x, channels)``.

    data_mask : 4D Numpy array, optional
        Data mask to crop. E.g. ``(num_of_images, y, x, channels)``.

    overlap : Tuple of 2 floats, optional
        Amount of minimum overlap on x and y dimensions. The values must be on range ``[0, 1)``, that is, ``0%`` or
        ``99%`` of overlap. E. g. ``(y, x)``.

    padding : tuple of ints, optional
        Size of padding to be added on each axis ``(y, x)``. E.g. ``(24, 24)``.

    verbose : bool, optional
         To print information about the crop to be made.

    load_data : bool, optional
        Whether to create the patches or not. It saves memory in case you only need the coordiantes of the cropped patches.

    Returns
    -------
    cropped_data : 4D Numpy array, optional
        Cropped image data. E.g. ``(num_of_images, y, x, channels)``. Returned if ``load_data`` is ``True``.

    cropped_data_mask : 4D Numpy array, optional
        Cropped image data masks. E.g. ``(num_of_images, y, x, channels)``. Returned if ``load_data`` is ``True``
        and ``data_mask`` is provided.

    crop_coords : list of dict
        Coordinates of each crop where the following keys are available:
            * ``"z"``: image used to extract the crop.
            * ``"y_start"``: starting point of the patch in Y axis.
            * ``"y_end"``: end point of the patch in Y axis.
            * ``"x_start"``: starting point of the patch in X axis.
            * ``"x_end"``: end point of the patch in X axis.

    Examples
    --------
    ::

        # EXAMPLE 1
        # Divide in crops of (256, 256) a given data with the minimum overlap
        X_train = np.ones((165, 768, 1024, 1))
        Y_train = np.ones((165, 768, 1024, 1))

        X_train, Y_train = crop_data_with_overlap(X_train, (256, 256, 1), Y_train, (0, 0))

        # Notice that as the shape of the data has exact division with the wnanted crops shape so no overlap will be
        # made. The function will print the following information:
        #     Minimum overlap selected: (0, 0)
        #     Real overlapping (%): (0.0, 0.0)
        #     Real overlapping (pixels): (0.0, 0.0)
        #     (3, 4) patches per (x,y) axis
        #     **** New data shape is: (1980, 256, 256, 1)


        # EXAMPLE 2
        # Same as example 1 but with 25% of overlap between crops
        X_train, Y_train = crop_data_with_overlap(X_train, (256, 256, 1), Y_train, (0.25, 0.25))

        # The function will print the following information:
        #     Minimum overlap selected: (0.25, 0.25)
        #     Real overlapping (%): (0.33203125, 0.3984375)
        #     Real overlapping (pixels): (85.0, 102.0)
        #     (4, 6) patches per (x,y) axis
        #     **** New data shape is: (3960, 256, 256, 1)


        # EXAMPLE 3
        # Same as example 1 but with 50% of overlap between crops
        X_train, Y_train = crop_data_with_overlap(X_train, (256, 256, 1), Y_train, (0.5, 0.5))

        # The function will print the shape of the created array. In this example:
        #     Minimum overlap selected: (0.5, 0.5)
        #     Real overlapping (%): (0.59765625, 0.5703125)
        #     Real overlapping (pixels): (153.0, 146.0)
        #     (6, 8) patches per (x,y) axis
        #     **** New data shape is: (7920, 256, 256, 1)


        # EXAMPLE 4
        # Same as example 2 but with 50% of overlap only in x axis
        X_train, Y_train = crop_data_with_overlap(X_train, (256, 256, 1), Y_train, (0.5, 0))

        # The function will print the shape of the created array. In this example:
        #     Minimum overlap selected: (0.5, 0)
        #     Real overlapping (%): (0.59765625, 0.0)
        #     Real overlapping (pixels): (153.0, 0.0)
        #     (6, 4) patches per (x,y) axis
        #     **** New data shape is: (3960, 256, 256, 1)
    """

    if data.ndim != 4:
        raise ValueError("data expected to be 4 dimensional, given {}".format(data.shape))
    if data_mask is not None:
        if data.ndim != 4:
            raise ValueError("data mask expected to be 4 dimensional, given {}".format(data_mask.shape))
        if data.shape[:-1] != data_mask.shape[:-1]:
            raise ValueError(
                "data and data_mask shapes mismatch: {} vs {}".format(data.shape[:-1], data_mask.shape[:-1])
            )

    for i, p in enumerate(padding):
        if p >= crop_shape[i] // 2:
            raise ValueError(
                "'Padding' can not be greater than the half of 'crop_shape'. Max value for this {} input shape is {}".format(
                    crop_shape, [(crop_shape[0] // 2) - 1, (crop_shape[1] // 2) - 1]
                )
            )
    if len(crop_shape) != 3:
        raise ValueError("crop_shape expected to be of length 3, given {}".format(crop_shape))
    if crop_shape[0] > data.shape[1]:
        raise ValueError(
            "'crop_shape[0]' {} greater than {} (you can reduce 'DATA.PATCH_SIZE' or use 'DATA.REFLECT_TO_COMPLETE_SHAPE')".format(
                crop_shape[0], data.shape[1]
            )
        )
    if crop_shape[1] > data.shape[2]:
        raise ValueError(
            "'crop_shape[1]' {} greater than {} (you can reduce 'DATA.PATCH_SIZE' or use 'DATA.REFLECT_TO_COMPLETE_SHAPE')".format(
                crop_shape[1], data.shape[2]
            )
        )
    if (overlap[0] >= 1 or overlap[0] < 0) or (overlap[1] >= 1 or overlap[1] < 0):
        raise ValueError("'overlap' values must be floats between range [0, 1)")

    if verbose:
        print("### OV-CROP ###")
        print("Cropping {} images into {} with overlapping. . .".format(data.shape, crop_shape))
        print("Minimum overlap selected: {}".format(overlap))
        print("Padding: {}".format(padding))

    if (overlap[0] >= 1 or overlap[0] < 0) and (overlap[1] >= 1 or overlap[1] < 0):
        raise ValueError("'overlap' values must be floats between range [0, 1)")

    padded_data = np.pad(
        data,
        ((0, 0), (padding[1], padding[1]), (padding[0], padding[0]), (0, 0)),
        "reflect",
    )
    if data_mask is not None:
        padded_data_mask = np.pad(
            data_mask,
            ((0, 0), (padding[1], padding[1]), (padding[0], padding[0]), (0, 0)),
            "reflect",
        )

    # Calculate overlapping variables
    overlap_x = 1 if overlap[0] == 0 else 1 - overlap[0]
    overlap_y = 1 if overlap[1] == 0 else 1 - overlap[1]

    # Y
    step_y = int((crop_shape[0] - padding[0] * 2) * overlap_y)
    crops_per_y = math.ceil(data.shape[1] / step_y)
    last_y = 0 if crops_per_y == 1 else (((crops_per_y - 1) * step_y) + crop_shape[0]) - padded_data.shape[1]
    ovy_per_block = last_y // (crops_per_y - 1) if crops_per_y > 1 else 0
    step_y -= ovy_per_block
    last_y -= ovy_per_block * (crops_per_y - 1)

    # X
    step_x = int((crop_shape[1] - padding[1] * 2) * overlap_x)
    crops_per_x = math.ceil(data.shape[2] / step_x)
    last_x = 0 if crops_per_x == 1 else (((crops_per_x - 1) * step_x) + crop_shape[1]) - padded_data.shape[2]
    ovx_per_block = last_x // (crops_per_x - 1) if crops_per_x > 1 else 0
    step_x -= ovx_per_block
    last_x -= ovx_per_block * (crops_per_x - 1)

    # Real overlap calculation for printing
    real_ov_y = ovy_per_block / (crop_shape[0] - padding[0] * 2)
    real_ov_x = ovx_per_block / (crop_shape[1] - padding[1] * 2)

    if verbose:
        print("Real overlapping (%): {}".format(real_ov_x, real_ov_y))
        print(
            "Real overlapping (pixels): {}".format(
                (crop_shape[1] - padding[1] * 2) * real_ov_x,
                (crop_shape[0] - padding[0] * 2) * real_ov_y,
            )
        )
        print("{} patches per (x,y) axis".format(crops_per_x, crops_per_y))

    total_vol = data.shape[0] * (crops_per_x) * (crops_per_y)
    if load_data:
        cropped_data = np.zeros((total_vol,) + crop_shape, dtype=data.dtype)
        if data_mask is not None:
            cropped_data_mask = np.zeros(
                (total_vol,) + crop_shape[:2] + (data_mask.shape[-1],),
                dtype=data_mask.dtype,
            )

    crop_coords = []
    c = 0
    for z in range(data.shape[0]):
        for y in range(crops_per_y):
            for x in range(crops_per_x):
                d_y = 0 if (y * step_y + crop_shape[0]) < padded_data.shape[1] else last_y
                d_x = 0 if (x * step_x + crop_shape[1]) < padded_data.shape[2] else last_x

                if load_data:
                    cropped_data[c] = padded_data[
                        z,
                        y * step_y - d_y : y * step_y + crop_shape[0] - d_y,
                        x * step_x - d_x : x * step_x + crop_shape[1] - d_x,
                    ]

                if load_data and data_mask is not None:
                    cropped_data_mask[c] = padded_data_mask[
                        z,
                        y * step_y - d_y : y * step_y + crop_shape[0] - d_y,
                        x * step_x - d_x : x * step_x + crop_shape[1] - d_x,
                    ]

                crop_coords.append(
                    {
                        "z": z,
                        "y_start": y * step_y - d_y,
                        "y_end": y * step_y + crop_shape[0] - d_y,
                        "x_start": x * step_x - d_x,
                        "x_end": x * step_x + crop_shape[1] - d_x,
                    }
                )

                c += 1

    if verbose:
        print("**** New data shape is: {}".format(cropped_data.shape))
        print("### END OV-CROP ###")

    if load_data:
        if data_mask is not None:
            return cropped_data, cropped_data_mask, crop_coords
        else:
            return cropped_data, crop_coords
    else:
        return crop_coords


# Copied from BiaPy commit: 284ec3838766392c9a333ac9d27b55816a267bb9 (3.5.2)
def crop_3D_data_with_overlap(
    data,
    vol_shape,
    data_mask=None,
    overlap=(0, 0, 0),
    padding=(0, 0, 0),
    verbose=True,
    median_padding=False,
    load_data=True,
):
    """
    Crop 3D data into smaller volumes with a defined overlap. The opposite function is :func:`~merge_3D_data_with_overlap`.

    Parameters
    ----------
    data : 4D Numpy array
        Data to crop. E.g. ``(z, y, x, channels)``.

    vol_shape : 4D int tuple
        Shape of the volumes to create. E.g. ``(z, y, x, channels)``.

    data_mask : 4D Numpy array, optional
        Data mask to crop. E.g. ``(z, y, x, channels)``.

    overlap : Tuple of 3 floats, optional
        Amount of minimum overlap on x, y and z dimensions. The values must be on range ``[0, 1)``, that is, ``0%``
        or ``99%`` of overlap. E.g. ``(z, y, x)``.

    padding : tuple of ints, optional
        Size of padding to be added on each axis ``(z, y, x)``. E.g. ``(24, 24, 24)``.

    verbose : bool, optional
        To print information about the crop to be made.

    median_padding : bool, optional
        If ``True`` the padding value is the median value. If ``False``, the added values are zeroes.

    load_data : bool, optional
        Whether to create the patches or not. It saves memory in case you only need the coordiantes of the cropped patches.

    Returns
    -------
    cropped_data : 5D Numpy array, optional
        Cropped image data. E.g. ``(vol_number, z, y, x, channels)``. Returned if ``load_data`` is ``True``.

    cropped_data_mask : 5D Numpy array, optional
        Cropped image data masks. E.g. ``(vol_number, z, y, x, channels)``. Returned if ``load_data`` is ``True``
        and ``data_mask`` is provided.

    crop_coords : list of dict
        Coordinates of each crop where the following keys are available:
            * ``"z_start"``: starting point of the patch in Z axis.
            * ``"z_end"``: end point of the patch in Z axis.
            * ``"y_start"``: starting point of the patch in Y axis.
            * ``"y_end"``: end point of the patch in Y axis.
            * ``"x_start"``: starting point of the patch in X axis.
            * ``"x_end"``: end point of the patch in X axis.

    Examples
    --------
    ::

        # EXAMPLE 1
        # Following the example introduced in load_and_prepare_3D_data function, the cropping of a volume with shape
        # (165, 1024, 765) should be done by the following call:
        X_train = np.ones((165, 768, 1024, 1))
        Y_train = np.ones((165, 768, 1024, 1))
        X_train, Y_train = crop_3D_data_with_overlap(X_train, (80, 80, 80, 1), data_mask=Y_train,
                                                     overlap=(0.5,0.5,0.5))
        # The function will print the shape of the generated arrays. In this example:
        #     **** New data shape is: (2600, 80, 80, 80, 1)

    A visual explanation of the process:

    .. image:: ../../img/crop_3D_ov.png
        :width: 80%
        :align: center

    Note: this image do not respect the proportions.
    ::

        # EXAMPLE 2
        # Same data crop but without overlap

        X_train, Y_train = crop_3D_data_with_overlap(X_train, (80, 80, 80, 1), data_mask=Y_train, overlap=(0,0,0))

        # The function will print the shape of the generated arrays. In this example:
        #     **** New data shape is: (390, 80, 80, 80, 1)
        #
        # Notice how differs the amount of subvolumes created compared to the first example

        #EXAMPLE 2
        #In the same way, if the addition of (64,64,64) padding is required, the call should be done as shown:
        X_train, Y_train = crop_3D_data_with_overlap(
             X_train, (80, 80, 80, 1), data_mask=Y_train, overlap=(0.5,0.5,0.5), padding=(64,64,64))
    """

    if verbose:
        print("### 3D-OV-CROP ###")
        print("Cropping {} images into {} with overlapping . . .".format(data.shape, vol_shape))
        print("Minimum overlap selected: {}".format(overlap))
        print("Padding: {}".format(padding))

    if data.ndim != 4:
        raise ValueError("data expected to be 4 dimensional, given {}".format(data.shape))
    if data_mask is not None:
        if data_mask.ndim != 4:
            raise ValueError("data_mask expected to be 4 dimensional, given {}".format(data_mask.shape))
        if data.shape[:-1] != data_mask.shape[:-1]:
            raise ValueError(
                "data and data_mask shapes mismatch: {} vs {}".format(data.shape[:-1], data_mask.shape[:-1])
            )
    if len(vol_shape) != 4:
        raise ValueError("vol_shape expected to be of length 4, given {}".format(vol_shape))
    if vol_shape[0] > data.shape[0]:
        raise ValueError(
            "'vol_shape[0]' {} greater than {} (you can reduce 'DATA.PATCH_SIZE' or use 'DATA.REFLECT_TO_COMPLETE_SHAPE')".format(
                vol_shape[0], data.shape[0]
            )
        )
    if vol_shape[1] > data.shape[1]:
        raise ValueError(
            "'vol_shape[1]' {} greater than {} (you can reduce 'DATA.PATCH_SIZE' or use 'DATA.REFLECT_TO_COMPLETE_SHAPE')".format(
                vol_shape[1], data.shape[1]
            )
        )
    if vol_shape[2] > data.shape[2]:
        raise ValueError(
            "'vol_shape[2]' {} greater than {} (you can reduce 'DATA.PATCH_SIZE' or use 'DATA.REFLECT_TO_COMPLETE_SHAPE')".format(
                vol_shape[2], data.shape[2]
            )
        )
    if (
        (overlap[0] >= 1 or overlap[0] < 0)
        or (overlap[1] >= 1 or overlap[1] < 0)
        or (overlap[2] >= 1 or overlap[2] < 0)
    ):
        raise ValueError("'overlap' values must be floats between range [0, 1)")
    for i, p in enumerate(padding):
        if p >= vol_shape[i] // 2:
            raise ValueError(
                "'Padding' can not be greater than the half of 'vol_shape'. Max value for this {} input shape is {}".format(
                    vol_shape,
                    [
                        (vol_shape[0] // 2) - 1,
                        (vol_shape[1] // 2) - 1,
                        (vol_shape[2] // 2) - 1,
                    ],
                )
            )

    padded_data = np.pad(
        data,
        (
            (padding[0], padding[0]),
            (padding[1], padding[1]),
            (padding[2], padding[2]),
            (0, 0),
        ),
        "reflect",
    )
    if data_mask is not None:
        padded_data_mask = np.pad(
            data_mask,
            (
                (padding[0], padding[0]),
                (padding[1], padding[1]),
                (padding[2], padding[2]),
                (0, 0),
            ),
            "reflect",
        )
    if median_padding:
        padded_data[0 : padding[0], :, :, :] = np.median(data[0, :, :, :])
        padded_data[padding[0] + data.shape[0] : 2 * padding[0] + data.shape[0], :, :, :] = np.median(data[-1, :, :, :])
        padded_data[:, 0 : padding[1], :, :] = np.median(data[:, 0, :, :])
        padded_data[:, padding[1] + data.shape[1] : 2 * padding[1] + data.shape[0], :, :] = np.median(data[:, -1, :, :])
        padded_data[:, :, 0 : padding[2], :] = np.median(data[:, :, 0, :])
        padded_data[:, :, padding[2] + data.shape[2] : 2 * padding[2] + data.shape[2], :] = np.median(data[:, :, -1, :])
    padded_vol_shape = vol_shape

    # Calculate overlapping variables
    overlap_z = 1 if overlap[0] == 0 else 1 - overlap[0]
    overlap_y = 1 if overlap[1] == 0 else 1 - overlap[1]
    overlap_x = 1 if overlap[2] == 0 else 1 - overlap[2]

    # Z
    step_z = int((vol_shape[0] - padding[0] * 2) * overlap_z)
    vols_per_z = math.ceil(data.shape[0] / step_z)
    last_z = 0 if vols_per_z == 1 else (((vols_per_z - 1) * step_z) + vol_shape[0]) - padded_data.shape[0]
    ovz_per_block = last_z // (vols_per_z - 1) if vols_per_z > 1 else 0
    step_z -= ovz_per_block
    last_z -= ovz_per_block * (vols_per_z - 1)

    # Y
    step_y = int((vol_shape[1] - padding[1] * 2) * overlap_y)
    vols_per_y = math.ceil(data.shape[1] / step_y)
    last_y = 0 if vols_per_y == 1 else (((vols_per_y - 1) * step_y) + vol_shape[1]) - padded_data.shape[1]
    ovy_per_block = last_y // (vols_per_y - 1) if vols_per_y > 1 else 0
    step_y -= ovy_per_block
    last_y -= ovy_per_block * (vols_per_y - 1)

    # X
    step_x = int((vol_shape[2] - padding[2] * 2) * overlap_x)
    vols_per_x = math.ceil(data.shape[2] / step_x)
    last_x = 0 if vols_per_x == 1 else (((vols_per_x - 1) * step_x) + vol_shape[2]) - padded_data.shape[2]
    ovx_per_block = last_x // (vols_per_x - 1) if vols_per_x > 1 else 0
    step_x -= ovx_per_block
    last_x -= ovx_per_block * (vols_per_x - 1)

    # Real overlap calculation for printing
    real_ov_z = ovz_per_block / (vol_shape[0] - padding[0] * 2)
    real_ov_y = ovy_per_block / (vol_shape[1] - padding[1] * 2)
    real_ov_x = ovx_per_block / (vol_shape[2] - padding[2] * 2)
    if verbose:
        print("Real overlapping (%): {}".format((real_ov_z, real_ov_y, real_ov_x)))
        print(
            "Real overlapping (pixels): {}".format(
                (
                    (vol_shape[0] - padding[0] * 2) * real_ov_z,
                    (vol_shape[1] - padding[1] * 2) * real_ov_y,
                    (vol_shape[2] - padding[2] * 2) * real_ov_x,
                )
            )
        )
        print("{} patches per (z,y,x) axis".format((vols_per_z, vols_per_x, vols_per_y)))

    total_vol = vols_per_z * vols_per_y * vols_per_x
    if load_data:
        cropped_data = np.zeros((total_vol,) + padded_vol_shape, dtype=data.dtype)
        if data_mask is not None:
            cropped_data_mask = np.zeros(
                (total_vol,) + padded_vol_shape[:3] + (data_mask.shape[-1],),
                dtype=data_mask.dtype,
            )

    c = 0
    crop_coords = []
    for z in range(vols_per_z):
        for y in range(vols_per_y):
            for x in range(vols_per_x):
                d_z = 0 if (z * step_z + vol_shape[0]) < padded_data.shape[0] else last_z
                d_y = 0 if (y * step_y + vol_shape[1]) < padded_data.shape[1] else last_y
                d_x = 0 if (x * step_x + vol_shape[2]) < padded_data.shape[2] else last_x

                if load_data:
                    cropped_data[c] = padded_data[
                        z * step_z - d_z : z * step_z + vol_shape[0] - d_z,
                        y * step_y - d_y : y * step_y + vol_shape[1] - d_y,
                        x * step_x - d_x : x * step_x + vol_shape[2] - d_x,
                    ]

                crop_coords.append(
                    {
                        "z_start": z * step_z - d_z,
                        "z_end": z * step_z + vol_shape[0] - d_z,
                        "y_start": y * step_y - d_y,
                        "y_end": y * step_y + vol_shape[1] - d_y,
                        "x_start": x * step_x - d_x,
                        "x_end": x * step_x + vol_shape[2] - d_x,
                    }
                )

                if load_data and data_mask is not None:
                    cropped_data_mask[c] = padded_data_mask[
                        z * step_z - d_z : (z * step_z) + vol_shape[0] - d_z,
                        y * step_y - d_y : y * step_y + vol_shape[1] - d_y,
                        x * step_x - d_x : x * step_x + vol_shape[2] - d_x,
                    ]
                c += 1

    if verbose:
        print("**** New data shape is: {}".format(cropped_data.shape))
        print("### END 3D-OV-CROP ###")

    if load_data:
        if data_mask is not None:
            return cropped_data, cropped_data_mask, crop_coords
        else:
            return cropped_data, crop_coords
    else:
        return crop_coords


# Copied from BiaPy commit: 284ec3838766392c9a333ac9d27b55816a267bb9 (3.5.2)
def pad_and_reflect(img, crop_shape, verbose=False):
    """
    Load data from a directory.

    Parameters
    ----------
    img : 3D/4D Numpy array
        Image to pad. E.g. ``(y, x, channels)`` or ``(z, y, x, channels)``.

    crop_shape : Tuple of 3/4 int, optional
        Shape of the subvolumes to create when cropping.  E.g. ``(y, x, channels)`` or ``(z, y, x, channels)``.

    verbose : bool, optional
        Whether to output information.

    Returns
    -------
    img : 3D/4D Numpy array
        Image padded. E.g. ``(y, x, channels)`` for 2D and ``(z, y, x, channels)`` for 3D.
    """
    if img.ndim == 4 and len(crop_shape) != 4:
        raise ValueError(
            f"'crop_shape' needs to have 4 values as the input array has 4 dims. Provided crop_shape: {crop_shape}"
        )
    if img.ndim == 3 and len(crop_shape) != 3:
        raise ValueError(
            f"'crop_shape' needs to have 3 values as the input array has 3 dims. Provided crop_shape: {crop_shape}"
        )

    if img.ndim == 4:
        if img.shape[0] < crop_shape[0]:
            diff = crop_shape[0] - img.shape[0]
            o_shape = img.shape
            img = np.pad(img, ((diff, 0), (0, 0), (0, 0), (0, 0)), "reflect")
            if verbose:
                print("Reflected from {} to {}".format(o_shape, img.shape))

        if img.shape[1] < crop_shape[1]:
            diff = crop_shape[1] - img.shape[1]
            o_shape = img.shape
            img = np.pad(img, ((0, 0), (diff, 0), (0, 0), (0, 0)), "reflect")
            if verbose:
                print("Reflected from {} to {}".format(o_shape, img.shape))

        if img.shape[2] < crop_shape[2]:
            diff = crop_shape[2] - img.shape[2]
            o_shape = img.shape
            img = np.pad(img, ((0, 0), (0, 0), (diff, 0), (0, 0)), "reflect")
            if verbose:
                print("Reflected from {} to {}".format(o_shape, img.shape))
    else:
        if img.shape[0] < crop_shape[0]:
            diff = crop_shape[0] - img.shape[0]
            o_shape = img.shape
            img = np.pad(img, ((diff, 0), (0, 0), (0, 0)), "reflect")
            if verbose:
                print("Reflected from {} to {}".format(o_shape, img.shape))

        if img.shape[1] < crop_shape[1]:
            diff = crop_shape[1] - img.shape[1]
            o_shape = img.shape
            img = np.pad(img, ((0, 0), (diff, 0), (0, 0)), "reflect")
            if verbose:
                print("Reflected from {} to {}".format(o_shape, img.shape))
    return img
