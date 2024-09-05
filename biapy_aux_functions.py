import os
import functools
import numpy as np
import pandas as pd
from skimage.io import imread

from typing import Optional, Dict, Tuple, List
from packaging.version import Version
from bioimageio.core.digest_spec import get_test_inputs

## Copied from BiaPy commit: ada4f14cf13f5d2b74d66e1f9aa2b526a133f296 (3.5.1)
def check_bmz_model_compatibility(
    model_rdf: Dict,
    workflow_specs: Optional[Dict] = None,
) -> Tuple[List[str], bool, str]:
    """
    Checks one model compatibility with BiaPy by looking at its RDF file provided by BMZ. This function is the one
    used in BMZ's continuous integration with BiaPy.

    Parameters
    ----------
    model_rdf : dict
        BMZ model RDF that contains all the information of the model.

    workflow_specs : dict
        Specifications of the workflow. If not provided all possible models will be considered.

    Returns
    -------
    preproc_info: dict of str
        Preprocessing names that the model is using.

    error : bool
        Whether if there is a problem to consume the model in BiaPy or not.

    reason_message: str
        Reason why the model can not be consumed (if any).
    """
    specific_workflow = "all" if workflow_specs is None else workflow_specs["workflow_type"]
    specific_dims = "all" if workflow_specs is None else workflow_specs["ndim"]
    ref_classes = "all" if workflow_specs is None else workflow_specs["nclasses"]

    error = False
    reason_message = ""
    preproc_info = []

    # Accepting models that are exported in pytorch_state_dict and with just one input
    if "pytorch_state_dict" in model_rdf["weights"] and len(model_rdf["inputs"]) == 1:
        
        model_version = Version("0.5")
        if "format_version" in model_rdf:
            model_version = Version(model_rdf["format_version"])

        # Check problem type
        if (specific_workflow in ["all", "SEMANTIC_SEG"]) and (
            "semantic-segmentation" in model_rdf["tags"] or "segmentation" in model_rdf["tags"]
        ):
            # Check number of classes
            classes = -1
            if "kwargs" in model_rdf["weights"]["pytorch_state_dict"]:
                if "n_classes" in model_rdf["weights"]["pytorch_state_dict"]["kwargs"]: # BiaPy
                    classes = model_rdf["weights"]["pytorch_state_dict"]["kwargs"]["n_classes"]
                elif "out_channels" in model_rdf["weights"]["pytorch_state_dict"]["kwargs"]:
                    classes = model_rdf["weights"]["pytorch_state_dict"]["kwargs"]["out_channels"]
                elif "classes" in model_rdf["weights"]["pytorch_state_dict"]["kwargs"]:
                    classes = model_rdf["weights"]["pytorch_state_dict"]["kwargs"]["classes"]
                
            if classes != -1:
                if ref_classes != "all":
                    if classes > 2 and ref_classes != classes:
                        reason_message += f"[{specific_workflow}] 'MODEL.N_CLASSES' does not match network's output classes. Please check it!\n"
                        error = True
                    else:
                        reason_message += f"[{specific_workflow}] BiaPy works only with one channel for the binary case (classes <= 2) so will adapt the output to match the ground truth data\n"
            else:
                reason_message += f"[{specific_workflow}] Couldn't find the classes this model is returning so please be aware to match it\n"
                error = True

        elif specific_workflow in ["all", "INSTANCE_SEG"] and "instance-segmentation" in model_rdf["tags"]:
            pass
        elif specific_workflow in ["all", "DETECTION"] and "detection" in model_rdf["tags"]:
            pass
        elif specific_workflow in ["all", "DENOISING"] and "denoising" in model_rdf["tags"]:
            pass
        elif specific_workflow in ["all", "SUPER_RESOLUTION"] and "super-resolution" in model_rdf["tags"]:
            pass
        elif specific_workflow in ["all", "SELF_SUPERVISED"] and "self-supervision" in model_rdf["tags"]:
            pass
        elif specific_workflow in ["all", "CLASSIFICATION"] and "classification" in model_rdf["tags"]:
            pass
        elif specific_workflow in ["all", "IMAGE_TO_IMAGE"] and (
            "pix2pix" in model_rdf["tags"]
            or "image-reconstruction" in model_rdf["tags"]
            or "image-to-image" in model_rdf["tags"]
            or "image-restoration" in model_rdf["tags"]
        ):
            pass
        else:
            reason_message += "[{}] no workflow tag recognized in {}.\n".format(specific_workflow, model_rdf["tags"])
            error = True

        # Check axes and dimension
        if model_version > Version("0.5.0"):
            axes_order = ""
            for axis in model_rdf["inputs"][0]["axes"]:
                if 'type' in axis:
                    if axis['type'] == "batch":
                        axes_order += "b"
                    elif axis['type'] == "channel":
                        axes_order += "c"
                    elif 'id' in axis:
                        axes_order += axis['id']
                elif 'id' in axis:
                    if axis['id'] == "channel":
                        axes_order += "c"
                    else:
                        axes_order += axis['id']
        else:
            axes_order = model_rdf["inputs"][0]["axes"]
        if specific_dims == "2D":
            if axes_order != "bcyx":
                error = True
                reason_message += f"[{specific_workflow}] In a 2D problem the axes need to be 'bcyx', found {axes_order}\n"
            elif "2d" not in model_rdf["tags"]:
                error = True
                reason_message += f"[{specific_workflow}] Selected model seems to not be 2D\n"
        elif specific_dims == "3D":
            if axes_order != "bczyx":
                error = True
                reason_message += f"[{specific_workflow}] In a 3D problem the axes need to be 'bczyx', found {axes_order}\n"
            elif "3d" not in model_rdf["tags"]:
                error = True
                reason_message += f"[{specific_workflow}] Selected model seems to not be 3D\n"
        else:  # All
            if axes_order not in ["bcyx", "bczyx"]:
                error = True
                reason_message += f"[{specific_workflow}] Accepting models only with ['bcyx', 'bczyx'] axis order, found {axes_order}\n"

        # Check preprocessing
        if "preprocessing" in model_rdf["inputs"][0]:
            preproc_info = model_rdf["inputs"][0]["preprocessing"]
            if isinstance(preproc_info, list) and len(preproc_info) > 1:
                error = True
                reason_message += f"[{specific_workflow}] More than one preprocessing from BMZ not implemented yet {axes_order}\n"

            key_to_find = "id" if model_version > Version("0.5.0") else "name"

            if key_to_find in preproc_info:
                if preproc_info[key_to_find] not in [
                    "zero_mean_unit_variance",
                    "fixed_zero_mean_unit_variance",
                    "scale_range",
                    "scale_linear",
                ]:
                    error = True
                    reason_message += f"[{specific_workflow}] Not recognized preprocessing found: {preproc_info[key_to_find]}\n"
            else:
                error = True
                reason_message += f"[{specific_workflow}] Not recognized preprocessing structure found: {preproc_info}\n"

        # Check post-processing
        if model_version > Version("0.5.0"):
            if (
                "postprocessing" in model_rdf["weights"]["pytorch_state_dict"]["architecture"]["kwargs"]
                and model_rdf["weights"]["pytorch_state_dict"]["architecture"]["kwargs"]["postprocessing"] is not None
            ):
                error = True
                reason_message += f"[{specific_workflow}] Currently no postprocessing is supported. Found: {model_rdf['weights']['pytorch_state_dict']['kwargs']['postprocessing']}\n"
        else:
            if (
                "postprocessing" in model_rdf["weights"]["pytorch_state_dict"]["kwargs"]
                and model_rdf["weights"]["pytorch_state_dict"]["kwargs"]["postprocessing"] is not None
            ):
                error = True
                reason_message += f"[{specific_workflow}] Currently no postprocessing is supported. Found: {model_rdf['weights']['pytorch_state_dict']['kwargs']['postprocessing']}\n"
    else:
        error = True
        reason_message += f"[{specific_workflow}] pytorch_state_dict not found in model RDF\n"

    return preproc_info, error, reason_message

# Adapted from BiaPy commit: ada4f14cf13f5d2b74d66e1f9aa2b526a133f296 (3.5.1)
def check_model_restrictions(
    model_rdf,
):
    """
    Checks model restrictions to be applied into the current configuration.

    Parameters
    ----------
    model_rdf : BMZ model
        RDF of BMZ model. 
 
    Returns
    -------
    option_list: dict
        variables and values to change in current configuration. These changes
        are imposed by the selected model. 
    """
    opts = {}    

    # 1) Change PATCH_SIZE with the one stored in the RDF
    inputs = get_test_inputs(model_rdf)
    if "input0" in inputs.members:
        input_image_shape = inputs.members["input0"]._data.shape
    elif "raw" in inputs.members:
        input_image_shape = inputs.members["raw"]._data.shape
    else:
        raise ValueError(f"Couldn't load input info from BMZ model's RDF: {inputs}")   
    opts["DATA.PATCH_SIZE"] = input_image_shape[2:] + (input_image_shape[1],)

    preproc_info = model_rdf.inputs[0].preprocessing
    if len(preproc_info) == 0:
        return opts
    
    # 2) Change preprocessing to the one stablished by BMZ by translate BMZ keywords into BiaPy's
    if len(preproc_info) > 0:
        # 'zero_mean_unit_variance' and 'fixed_zero_mean_unit_variance' norms of BMZ can be translated to our 'custom' norm 
        # providing mean and std
        if preproc_info["name"] in ["fixed_zero_mean_unit_variance", "zero_mean_unit_variance"]:
            if (
                "kwargs" in preproc_info
                and "mean" in preproc_info["kwargs"]
            ):
                mean = preproc_info["kwargs"]["mean"]
                std = preproc_info["kwargs"]["std"]
            elif "mean" in preproc_info:
                mean = preproc_info["mean"]
                std = preproc_info["std"]
            else:
                mean, std = -1., -1.

            opts["DATA.NORMALIZATION.TYPE"] = "custom"
            opts["DATA.NORMALIZATION.CUSTOM_MEAN"] = mean
            opts["DATA.NORMALIZATION.CUSTOM_STD"] = std

        # 'scale_linear' norm of BMZ is close to our 'div' norm (TODO: we need to control the "gain" arg)
        elif preproc_info["name"] == "scale_linear":
            opts["DATA.NORMALIZATION.TYPE"] = "div"

        # 'scale_range' norm of BMZ is as our PERC_CLIP + 'scale_range' norm
        elif preproc_info["name"] == "scale_range":
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
    return functools.reduce(_getattr, [obj] + attr.split('.'))

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
        return True, error_message, {}    

    if len(ids) == 0:
        error_message = f"No images found in folder:\n{data_dir}"
        return True, error_message, {}    

    for id_ in ids:
        img_path = os.path.join(data_dir, id_)
        if id_.endswith(".npy"):
            img = np.load(img_path)
        else:
            try:
                img = imread(img_path)
            except Exception:
                error_message = f"Couldn't load image:\n{img_path}"
                return True, error_message, {}    

        # Shape adjust
        if not is_3d:
            img = ensure_2d_shape(img.squeeze(), path=img_path)
        else:
            img = ensure_3d_shape(img.squeeze(), path=img_path)

        # Channel check
        if channel_expected == -1:
            channel_expected = img.shape[-1]
        if img.shape[-1] != channel_expected:
            error_message = f"All images need to have the same number of channels and represent same information to "\
                "ensure the deep learning model can be trained correctly. However, the current image (with "\
                f"{channel_expected} channels) appears to have a different number of channels than the first image"\
                f"(with {img.shape[-1]} channels) in the folder. Current image:\n{img_path}"
            return True, error_message, {}    

        # Data range check
        if not is_mask:
            if data_range_expected == -1:
                data_range_expected = data_range(img)
            drange = data_range(img)
            if data_range_expected != drange:
                error_message = f"All images must be within the same data range. However, the current image (with a "\
                    f"range of {drange}) appears to be in a different data range than the first image (with a range "\
                    f"of {data_range_expected}) in the folder. Current image:\n{img_path}"
                return True, error_message, {}    

        if mask_type == "semantic_mask":
            if channel_expected != 1:
                error_message = f"Semantic masks are expected to have just one channel. Image analized:\n{img_path}"
                return True, error_message, {}    
            else:
                nclasses = max(nclasses, len(np.unique(img)))
        elif mask_type == "instance_mask":
            if channel_expected == 2:
                nclasses = max(nclasses, len(np.unique(img[...,1])))
            else:
                if channel_expected != 1:
                    error_message = f"Instance masks are expected to have one or two channels. In case two channels are provided "\
                        "the first one must have the instance IDs and one their corresponding semantic (class) labels. "\
                        f"Image analized:\n{img_path}"
                    return True, error_message, {}    

    constraints = {"DATA.PATCH_SIZE_C": channel_expected, }
    if nclasses > 2:
        constraints["MODEL.N_CLASSES"] = nclasses

    if dir_name is not None:
        constraints[dir_name] = len(ids)
        constraints[dir_name+"_path"] = data_dir

    return False, "", constraints

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
            m = "Read image seems to be 3D:\n{}.\nPath:\n{}".format(img.shape, path)
        else:
            m = "Read image seems to be 3D:\n{}".format(img.shape)
        raise ValueError(m)

    if img.ndim == 2:
        img = np.expand_dims(img, -1)
    else:
        if img.shape[0] <= 3:
            img = img.transpose((1, 2, 0))
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
        if path is not None:
            m = "Read image seems to be 2D:\n{}.\nPath:\n{}".format(img.shape, path)
        else:
            m = "Read image seems to be 2D:\n{}".format(img.shape)
        raise ValueError(m)

    if img.ndim == 3:
        img = np.expand_dims(img, -1)
    else:
        min_val = min(img.shape)
        channel_pos = img.shape.index(min_val)
        if channel_pos != 3 and img.shape[channel_pos] <= 4:
            new_pos = [x for x in range(4) if x != channel_pos] + [
                channel_pos,
            ]
            img = img.transpose(new_pos)
    return img

def check_csv_files(data_dir, is_3d=False, dir_name=None):
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
    """
    print("Checking CSV files . . .")
    nclasses = 0
    try:
        ids = sorted(next(os.walk(data_dir))[2])
    except Exception as exc:
        error_message = f"Something strange happens when listing files in folder:\n{data_dir}.\nError:\n{exc}"
        return True, error_message, {}  
    
    if len(ids) == 0:
        error_message = f"No images found in folder:\n{data_dir}"
        return True, error_message, {}  
    
    req_columns = ["axis-0", "axis-1"] if not is_3d else ["axis-0", "axis-1", "axis-2"] 

    for id_ in ids:
        csv_path = os.path.join(data_dir, id_)
        try:
            df = pd.read_csv(csv_path)
        except Exception:
            error_message = f"Couldn't load CSV file:\n{csv_path}"
            return True, error_message, {}  
         
        df = df.dropna()
      
        # Check columns in csv
        # Discard first index column to not have error if it is not sorted
        p_number = df.iloc[:, 0].to_list()
        df = df.rename(columns=lambda x: x.strip())  # trim spaces in column names
        cols_not_in_file = [x for x in req_columns if x not in df.columns]
        if len(cols_not_in_file) > 0:
            if len(cols_not_in_file) == 1:
                error_message = f"'{cols_not_in_file[0]}' column is not present in CSV file:\n{csv_path}"
            else:
                error_message = f"{cols_not_in_file} columns are not present in CSV file:\n{csv_path}"
            return True, error_message, {}  
        
        # Check class in columns
        if 'class' in df.columns:
            df["class"] = df["class"].astype("int")
            class_point = np.array(df["class"])

            uniq = np.sort(np.unique(class_point))
            if uniq[0] != 1:
                error_message = f"Class number must start with 1 in CSV file:\n{csv_path}"
                return True, error_message, {}  
            if not all(uniq == np.array(range(1, uniq.max()+ 1))):
                error_message = f"Classes must be consecutive, e.g [1,2,3,4,...]. Given {uniq} in CSV file:\n{csv_path}"
                return True, error_message, {}  
            
            nclasses = uniq.max()


    constraints = {}
    if 'class' in df.columns:
        constraints["MODEL.N_CLASSES"] = nclasses
    if dir_name is not None:
        constraints[dir_name] = len(ids)
        constraints[dir_name+"_path"] = data_dir

    return False, "", constraints


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
        return True, error_message, {}  
    
    tot_samples = 0
    # Loop over each class/folder
    for folder in class_names:
        class_folder = os.path.join(data_dir, folder)
        print(f"Analizing folder {class_folder}")
        
        ids = sorted(next(os.walk(class_folder))[2])
        if len(ids) == 0:
            error_message = "There are no images in class folder:\n{}".format(class_folder)
            return True, error_message, {}  
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
                    return True, error_message, {}  

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
                error_message = "All images need to have the same number of channels and represent same information to "\
                    "ensure the deep learning model can be trained correctly. However, the following image (with "\
                    f"{channel_expected} channels) appears to have a different number of channels than the first image "\
                    f"(with {img.shape[-1]} channels) in the folder:\n{img_path}"
                return True, error_message, {}  
            
            # Data range check
            if data_range_expected == -1:
                data_range_expected = data_range(img)
            drange = data_range(img)
            if data_range_expected != drange:
                error_message = "All images must be within the same data range. However, the following image (with a "\
                    f"range of {drange}) appears to be in a different data range than the first image (with a range "\
                    f"of {data_range_expected}) in the folder:\n{img_path}"
                return True, error_message, {}  
        
    constraints = {
        "DATA.PATCH_SIZE_C": channel_expected,
        "MODEL.N_CLASSES": len(class_names),
    }
    if dir_name is not None:
        constraints[dir_name] = tot_samples
        constraints[dir_name+"_path"] = data_dir

    return False, "", constraints

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