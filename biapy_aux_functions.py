import os
import numpy as np
from skimage.io import imread

from typing import Optional, Dict, Tuple, List
from packaging.version import Version

## Copied from BiaPy commit: 0ed2222869300316839af7202ce1d55761c6eb88 (3.5.1)
def check_bmz_model_compatibility(
    model_rdf: Dict,
    workflow_specs: Optional[Dict] = None,
) -> Tuple[List[str], bool, str]:
    """
    Checks model compatibility with BiaPy.

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
        Whether it there is a problem to consume the model in BiaPy or not.

    reason_message: str
        Reason why the model can not be consumed if there is any.
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
            for preprocs in model_rdf["inputs"][0]["preprocessing"]:
                key_to_find = "id" if model_version > Version("0.5.0") else "name"

                if key_to_find in preprocs:
                    if preprocs[key_to_find] not in [
                        "zero_mean_unit_variance",
                        "fixed_zero_mean_unit_variance",
                        "scale_range",
                        "scale_linear",
                    ]:
                        error = True
                        reason_message += f"[{specific_workflow}] Not recognized preprocessing found: {preprocs[key_to_find]}\n"
                        break
                else:
                    error = True
                    reason_message += f"[{specific_workflow}] Not recognized preprocessing structure found: {preprocs}\n"
                    break

                preproc_info = preprocs

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


def check_images(data_dir, is_mask=False, semantic_mask=False, is_3d=False):
    print(f"Checking images from {data_dir}")
    
    nclasses = 0
    channel_expected = -1
    data_range_expected = -1
    error = False
    error_message = ""

    try:
        ids = sorted(next(os.walk(data_dir))[2])
    except Exception as exc:
        error = True
        error_message = f"Something strange happens when listing files in {data_dir}. Error:\n{exc}"

    if len(ids) == 0:
        error = True
        error_message = f"No images found in dir {data_dir}"
 
    for id_ in ids:
        img_path = os.path.join(data_dir, id_)
        if id_.endswith(".npy"):
            img = np.load(img_path)
        else:
            try:
                img = imread(img_path)
            except Exception:
                error = True
                error_message = f"Couldn't load image: {img_path}"
                break 

        img = np.squeeze(img)

        # Shape adjust
        if not is_3d:
            if img.ndim > 3:
                error = True
                error_message = f"The following image appears to be 2D, but you selected a 2D problem under the 'Dimension' question: {img_path}"

            if img.ndim == 2:
                img = np.expand_dims(img, -1)
            else:
                if img.shape[0] <= 3:
                    img = img.transpose((1, 2, 0))
        else:
            if img.ndim < 3:
                error = True
                error_message = f"The following image appears to be 2D, but you selected a 3D problem under the 'Dimension' question: {img_path}"

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

        # Channel check
        if channel_expected == -1:
            channel_expected = img.shape[-1]
        if img.shape[-1] != channel_expected:
            error = True
            error_message = "All images need to have the same number of channels and represent same information to "\
                "ensure the deep learning model can be trained correctly. However, the following image (with "\
                f"{channel_expected} channels) appears to have a different number of channels than the first image "\
                f"(with {img.shape[-1]} channels) in the folder: {img_path}"

        # Data range check
        if not is_mask:
            if data_range_expected == -1:
                data_range_expected = data_range(img)
            drange = data_range(img)
            if data_range_expected != drange:
                error = True
                error_message = "All images must be within the same data range. However, the following image (with a "\
                    f"range of {drange}) appears to be in a different data range than the first image (with a range "\
                    f"of {data_range_expected}) in the folder: {img_path}"

        if error:
            break 

        if semantic_mask:
            nclasses = max(nclasses, len(np.unique(img)))
        
    constraints = [
        ["DATA.PATCH_SIZE_C", channel_expected],
        ["MODEL.N_CLASSES", nclasses],
    ]
    return error, error_message, constraints

def check_csv_files(folder):
    print("Checking CSV files . . .")
    import pdb; pdb.set_trace()

def check_classification_images(folder):
    print("Checking classification images . . .")
    import pdb; pdb.set_trace()

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