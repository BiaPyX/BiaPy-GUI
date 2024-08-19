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