from PySide6.QtWidgets import QLabel
from ui_utils import get_text

class Widget_conditions():
    def __init__(self):

        # Conditions that each widget impose to be visible. 
        # For instance:
        # "A": 
        #  {
        #      "B": ["C", "D"],
        #      "E": ["F", "G", "H"],
        #  },
        # So the widget "A" is visible if two conditions are satisfied: 1) the widget "B" need to have "C" or "D" value and 2) "E" widget
        # need to have a value between "F", "G" or "H".
        self.conditions = {
            "MODEL__BMZ__SOURCE_MODEL_ID__LABEL": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I want to check other online sources"
                    ],
                },
            "MODEL__BMZ__SOURCE_MODEL_ID__INFO": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I want to check other online sources"
                    ],
                },
            "MODEL__BMZ__SOURCE_MODEL_ID__INPUT": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I want to check other online sources"
                    ],
                },
            "MODEL__BMZ__SOURCE_MODEL_ID__BN": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I want to check other online sources"
                    ],
                },
            "MODEL__SOURCE__LABEL": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "MODEL__SOURCE__INFO": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "MODEL__SOURCE__INPUT": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "PATHS__CHECKPOINT_FILE__INPUT": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "PATHS__CHECKPOINT_FILE__INFO": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "checkpoint_file_path_browse_bn": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "checkpoint_file_path_browse_label": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                }, 
            "checkpoint_loading_opt_label": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "checkpoint_loading_opt_frame": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I have a model trained with BiaPy"
                    ],
                },
            "MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__FRAME": 
                {
                    "MODEL__BMZ__EXPORT__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__SOURCE__INPUT": 
                    [
                        "I want to check other online sources"
                    ],
                },
            "MODEL__BMZ__EXPORT__FRAME": 
                {
                    "MODEL__BMZ__EXPORT__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                    "MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__INPUT": 
                    [
                        "No"
                    ],
                },
            "MODEL__BMZ__EXPORT__DOCUMENTATION__LABEL": 
                {
                    "MODEL_AUTOGENERATE_DOC_INPUT": 
                    [
                        "No"
                    ],
                },
            "MODEL__BMZ__EXPORT__DOCUMENTATION__INFO": 
                {
                    "MODEL_AUTOGENERATE_DOC_INPUT": 
                    [
                        "No"
                    ],
                },
            "MODEL__BMZ__EXPORT__DOCUMENTATION__INPUT": 
                {
                    "MODEL_AUTOGENERATE_DOC_INPUT": 
                    [
                        "No"
                    ],
                },
            "MODEL__BMZ__EXPORT__DOCUMENTATION__BN": 
                {
                    "MODEL_AUTOGENERATE_DOC_INPUT": 
                    [
                        "No"
                    ],
                },
            "train_tab_widget": 
                {
                    "TRAIN__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "percentage_validation_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (split training)"
                    ],
                }, 
            "percentage_validation_info": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (split training)"
                    ],
                }, 
            "DATA__VAL__SPLIT_TRAIN__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (split training)"
                    ],
                }, 
            "cross_validation_nfolds_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "cross_validation_nfolds_info": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "DATA__VAL__CROSS_VAL_NFOLD__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "cross_validation_fold_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "cross_validation_fold_info": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "DATA__VAL__CROSS_VAL_FOLD__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "use_val_as_test": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "DATA__TEST__USE_VAL_AS_TEST__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                }, 
            "DATA__TEST__USE_VAL_AS_TEST__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)"
                    ],
                },
            "DATA__VAL__PATH__LABEL": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "DATA__VAL__PATH__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                },
            "DATA__VAL__PATH__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "val_data_input_browse_bn": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "validation_data_gt_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                    "WORKFLOW_SELECTED_LABEL": 
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                }, 
            "validation_data_gt_info": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                    "WORKFLOW_SELECTED_LABEL": 
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                }, 
            "DATA__VAL__GT_PATH__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                    "WORKFLOW_SELECTED_LABEL": 
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                }, 
            "val_data_gt_input_browse_bn": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                    "WORKFLOW_SELECTED_LABEL": 
                    [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ],
                }, 
            "DATA__PREPROCESS__VAL__LABEL": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                },
            "DATA__PREPROCESS__VAL__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                },
            "DATA__PREPROCESS__VAL__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "test_data_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)", 
                        "Extract from train (split training)"
                    ],
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ]
                }, 
            "DATA__TEST__PATH__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)", 
                        "Extract from train (split training)"
                    ],
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ]
                }, 
            "DATA__TEST__PATH__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)", 
                        "Extract from train (split training)"
                    ],
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ]
                }, 
            "test_data_input_browse_bn": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)", 
                        "Extract from train (split training)"
                    ],
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ]
                },  
            "test_exists_gt_label": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "CLASSIFICATION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "DATA__TEST__LOAD_GT__INPUT": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "CLASSIFICATION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "DATA__TEST__LOAD_GT__INFO": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "CLASSIFICATION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "test_data_gt_label": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ],
                    "DATA__TEST__LOAD_GT__INPUT":
                    [
                        "Yes"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "DATA__TEST__GT_PATH__INPUT": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ],
                    "DATA__TEST__LOAD_GT__INPUT":
                    [
                        "Yes"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                },
            "DATA__TEST__GT_PATH__INFO": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ],
                    "DATA__TEST__LOAD_GT__INPUT":
                    [
                        "Yes"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                },
            "test_data_gt_input_browse_bn": 
                {
                    "DATA__TEST__USE_VAL_AS_TEST__INPUT":
                    [
                        "No"
                    ],
                    "DATA__TEST__LOAD_GT__INPUT":
                    [
                        "Yes"
                    ], 
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                },  

            "train_gt_label": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "train_gt_info": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "DATA__TRAIN__GT_PATH__INPUT": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "train_data_gt_input_browse_bn": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "SUPER_RESOLUTION",
                        "IMAGE_TO_IMAGE",
                    ]
                }, 
            "random_val_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)", 
                        "Extract from train (split training)"
                    ],
                }, 
            "DATA__VAL__RANDOM__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)", 
                        "Extract from train (split training)"
                    ],
                }, 
            "DATA__VAL__RANDOM__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Extract from train (cross validation)", 
                        "Extract from train (split training)"
                    ],
                }, 
            
            "validation_overlap_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)", 
                    ],
                }, 
            "DATA__VAL__OVERLAP__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "DATA__VAL__OVERLAP__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "validation_padding_label": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                },
            "DATA__VAL__PADDING__INFO": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "DATA__VAL__PADDING__INPUT": 
                {
                    "DATA__VAL__TYPE__INPUT": 
                    [
                        "Not extracted from train (path needed)"
                    ],
                }, 
            "TRAIN__W_DECAY__INPUT": 
                {
                    "TRAIN__OPTIMIZER__INPUT": 
                    [
                        "ADAMW"
                    ],
                }, 
            "adamw_weight_decay_label": 
                {
                    "TRAIN__OPTIMIZER__INPUT": 
                    [
                        "ADAMW"
                    ],
                }, 
            "TRAIN__W_DECAY__INFO": 
                {
                    "TRAIN__OPTIMIZER__INPUT": 
                    [
                        "ADAMW"
                    ],
                }, 
            "TRAIN__OPT_BETAS__INFO": 
                {
                    "TRAIN__OPTIMIZER__INPUT": 
                    [
                        "ADAMW",
                        "ADAM"
                    ],
                },
            "TRAIN__OPT_BETAS__LABEL": 
                {
                    "TRAIN__OPTIMIZER__INPUT": 
                    [
                        "ADAMW",
                        "ADAM"
                    ],
                },
            "TRAIN__OPT_BETAS__INPUT": 
                {
                    "TRAIN__OPTIMIZER__INPUT": 
                    [
                        "ADAMW",
                        "ADAM"
                    ],
                },
            "TRAIN__BATCH_SIZE__LABEL": 
                {
                    "TRAIN__BATCH_SIZE__CALCULATION__INPUT": 
                    [
                        "No",
                    ],
                },
            "TRAIN__BATCH_SIZE__INFO": 
                {
                    "TRAIN__BATCH_SIZE__CALCULATION__INPUT": 
                    [
                        "No",
                    ],
                },
            "TRAIN__BATCH_SIZE__INPUT": 
                {
                    "TRAIN__BATCH_SIZE__CALCULATION__INPUT": 
                    [
                        "No",
                    ],
                },
            "profiler_batch_range_label": 
                {
                    "TRAIN__PROFILER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TRAIN__PROFILER_BATCH_RANGE__INPUT": 
                {
                    "TRAIN__PROFILER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TRAIN__PROFILER_BATCH_RANGE__INFO": 
                {
                    "TRAIN__PROFILER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__PERC_LOWER__LABEL": 
                {
                    "DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__PERC_LOWER__INFO": 
                {
                    "DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__PERC_CLIP__LOWER_PERC__INPUT": 
                {
                    "DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__PERC_UPPER__LABEL": 
                {
                    "DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__PERC_UPPER__INFO": 
                {
                    "DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__PERC_CLIP__UPPER_PERC__INPUT": 
                {
                    "DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__LABEL": 
                {
                    "DATA__NORMALIZATION__TYPE__INPUT": 
                    [
                        "zero_mean_unit_variance"
                    ],
                }, 
            "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__INPUT": 
                {
                    "DATA__NORMALIZATION__TYPE__INPUT": 
                    [
                        "zero_mean_unit_variance"
                    ],
                }, 
            "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__INFO": 
                {
                    "DATA__NORMALIZATION__TYPE__INPUT": 
                    [
                        "zero_mean_unit_variance"
                    ],
                },
            "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__LABEL": 
                {
                    "DATA__NORMALIZATION__TYPE__INPUT": 
                    [
                        "zero_mean_unit_variance"
                    ],
                }, 
            "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__INPUT": 
                {
                    "DATA__NORMALIZATION__TYPE__INPUT": 
                    [
                        "zero_mean_unit_variance"
                    ],
                }, 
            "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__INFO": 
                {
                    "DATA__NORMALIZATION__TYPE__INPUT": 
                    [
                        "zero_mean_unit_variance"
                    ],
                }, 
            "extract_random_patch_frame_label": 
                {
                    "DATA__EXTRACT_RANDOM_PATCH__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "extract_random_patch_frame": 
                {
                    "DATA__EXTRACT_RANDOM_PATCH__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "lr_schel_warmupcosine_epochs_label": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "warmupcosine"
                    ],
                },  
            "TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "warmupcosine"
                    ],
                },
            "TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INFO": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "warmupcosine"
                    ],
                },
            "lr_schel_min_lr_label": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "warmupcosine",
                        "reduceonplateau"
                    ],
                },
            "TRAIN__LR_SCHEDULER__MIN_LR__INPUT": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "warmupcosine",
                        "reduceonplateau"
                    ],
                }, 
            "TRAIN__LR_SCHEDULER__MIN_LR__INFO": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "warmupcosine",
                        "reduceonplateau"
                    ],
                }, 
            "lr_schel_reduce_on_plat_patience_label": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "reduceonplateau"
                    ],
                }, 
            "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "reduceonplateau"
                    ],
                },
            "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INFO": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "reduceonplateau"
                    ],
                },
            "lr_schel_reduce_on_plat_factor_label": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "reduceonplateau"
                    ],
                }, 
            "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "reduceonplateau"
                    ],
                }, 
            "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INFO": 
                {
                    "TRAIN__LR_SCHEDULER__NAME__INPUT": 
                    [
                        "reduceonplateau"
                    ],
                }, 
            "AUGMENTOR__ENABLE__LABEL": 
                {
                    "AUTOMATIC__AUG__INPUT": 
                    [
                        "Manually"
                    ],
                },
            "AUGMENTOR__ENABLE__INFO": 
                {
                    "AUTOMATIC__AUG__INPUT": 
                    [
                        "Manually"
                    ],
                },
            "AUGMENTOR__ENABLE__INPUT": 
                {
                    "AUTOMATIC__AUG__INPUT": 
                    [
                        "Manually"
                    ],
                },
            "da_frame": 
                {
                    "AUGMENTOR__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                    "AUTOMATIC__AUG__INPUT": 
                    [
                        "Manually"
                    ],
                },
            "da_random_rot_range_label": 
                {
                    "AUGMENTOR__RANDOM_ROT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__RANDOM_ROT_RANGE__INPUT": 
                {
                    "AUGMENTOR__RANDOM_ROT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__RANDOM_ROT_RANGE__INFO": 
                {
                    "AUGMENTOR__RANDOM_ROT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_shear_range_label": 
                {
                    "AUGMENTOR__SHEAR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SHEAR_RANGE__INPUT": 
                {
                    "AUGMENTOR__SHEAR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SHEAR_RANGE__INFO": 
                {
                    "AUGMENTOR__SHEAR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_zoom_range_label": 
                {
                    "AUGMENTOR__ZOOM__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__ZOOM_RANGE__INPUT": 
                {
                    "AUGMENTOR__ZOOM__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__ZOOM_RANGE__INFO": 
                {
                    "AUGMENTOR__ZOOM__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_zoom_in_z_label": 
                {
                    "AUGMENTOR__ZOOM__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__ZOOM_IN_Z__INFO": 
                {
                    "AUGMENTOR__ZOOM__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__ZOOM_IN_Z__INPUT": 
                {
                    "AUGMENTOR__ZOOM__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_shift_range_label": 
                {
                    "AUGMENTOR__SHIFT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SHIFT_RANGE__INPUT": 
                {
                    "AUGMENTOR__SHIFT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SHIFT_RANGE__INFO": 
                {
                    "AUGMENTOR__SHIFT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_elastic_alpha_label": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__E_ALPHA__INPUT": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__E_ALPHA__INFO": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_elastic_sigma_label": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__E_SIGMA__INPUT": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__E_SIGMA__INFO": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_elastic_mode_label": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__E_MODE__INPUT": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__E_MODE__INFO": 
                {
                    "AUGMENTOR__ELASTIC__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_gaussian_sigma_label": 
                {
                    "AUGMENTOR__G_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__G_SIGMA__INPUT": 
                {
                    "AUGMENTOR__G_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__G_SIGMA__INFO": 
                {
                    "AUGMENTOR__G_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_median_blur_k_size_label": 
                {
                    "AUGMENTOR__MEDIAN_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__MB_KERNEL__INPUT": 
                {
                    "AUGMENTOR__MEDIAN_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__MB_KERNEL__INFO": 
                {
                    "AUGMENTOR__MEDIAN_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_motion_blur_k_size_label": 
                {
                    "AUGMENTOR__MOTION_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__MOTB_K_RANGE__INPUT": 
                {
                    "AUGMENTOR__MOTION_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__MOTB_K_RANGE__INFO": 
                {
                    "AUGMENTOR__MOTION_BLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_gamma_contrast_range_label": 
                {
                    "AUGMENTOR__GAMMA_CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GC_GAMMA__INPUT": 
                {
                    "AUGMENTOR__GAMMA_CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GC_GAMMA__INFO": 
                {
                    "AUGMENTOR__GAMMA_CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_brightness_factor_range_label": 
                {
                    "AUGMENTOR__BRIGHTNESS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__BRIGHTNESS_FACTOR__INPUT": 
                {
                    "AUGMENTOR__BRIGHTNESS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__BRIGHTNESS_FACTOR__INFO": 
                {
                    "AUGMENTOR__BRIGHTNESS__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_brightness_mode_label": 
                {
                    "AUGMENTOR__BRIGHTNESS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__BRIGHTNESS_MODE__INPUT": 
                {
                    "AUGMENTOR__BRIGHTNESS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__BRIGHTNESS_MODE__INFO": 
                {
                    "AUGMENTOR__BRIGHTNESS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_contrast_factor_range_label": 
                {
                    "AUGMENTOR__CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CONTRAST_FACTOR__INPUT": 
                {
                    "AUGMENTOR__CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CONTRAST_FACTOR__INFO": 
                {
                    "AUGMENTOR__CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_contrast_mode_label": 
                {
                    "AUGMENTOR__CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CONTRAST_MODE__INPUT": 
                {
                    "AUGMENTOR__CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CONTRAST_MODE__INFO": 
                {
                    "AUGMENTOR__CONTRAST__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_dropout_range_label": 
                {
                    "AUGMENTOR__DROPOUT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__DROP_RANGE__INPUT": 
                {
                    "AUGMENTOR__DROPOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__DROP_RANGE__INFO": 
                {
                    "AUGMENTOR__DROPOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutout_number_iterations_label": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_NB_ITERATIONS__INPUT": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_NB_ITERATIONS__INFO": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutout_size_label": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_SIZE__INPUT": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__COUT_SIZE__INFO": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_cuout_cval_label": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_CVAL__INPUT": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_CVAL__INFO": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutout_to_mask_label": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_APPLY_TO_MASK__INFO": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__COUT_APPLY_TO_MASK__INPUT": 
                {
                    "AUGMENTOR__CUTOUT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutblur_size_range_label": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CBLUR_SIZE__INPUT": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CBLUR_SIZE__INFO": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutblut_down_range_label": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__CBLUR_DOWN_RANGE__INPUT": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CBLUR_DOWN_RANGE__INFO": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutblur_inside_label": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CBLUR_INSIDE__INPUT": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CBLUR_INSIDE__INFO": 
                {
                    "AUGMENTOR__CUTBLUR__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutmix_size_range_label": 
                {
                    "AUGMENTOR__CUTMIX__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CMIX_SIZE__INPUT": 
                {
                    "AUGMENTOR__CUTMIX__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__CMIX_SIZE__INFO": 
                {
                    "AUGMENTOR__CUTMIX__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_cutnoise_scale_range_label": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CNOISE_SCALE__INPUT": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CNOISE_SCALE__INFO": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutnoise_number_iter_label": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CNOISE_NB_ITERATIONS__INFO": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_cutnoise_size_range_label": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__CNOISE_SIZE__INPUT": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__CNOISE_SIZE__INFO": 
                {
                    "AUGMENTOR__CUTNOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_misaligment_displacement_label": 
                {
                    "AUGMENTOR__MISALIGNMENT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__MS_DISPLACEMENT__INPUT": 
                {
                    "AUGMENTOR__MISALIGNMENT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__MS_DISPLACEMENT__INFO": 
                {
                    "AUGMENTOR__MISALIGNMENT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_misaligment_rotate_ratio_label": 
                {
                    "AUGMENTOR__MISALIGNMENT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__MS_ROTATE_RATIO__INPUT": 
                {
                    "AUGMENTOR__MISALIGNMENT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__MS_ROTATE_RATIO__INFO": 
                {
                    "AUGMENTOR__MISALIGNMENT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_missing_sections_iteration_range_label": 
                {
                    "AUGMENTOR__MISSING_SECTIONS__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__MISSP_ITERATIONS__INPUT": 
                {
                    "AUGMENTOR__MISSING_SECTIONS__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__MISSP_ITERATIONS__INFO": 
                {
                    "AUGMENTOR__MISSING_SECTIONS__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_grid_ratio_label": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_RATIO__INPUT": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_RATIO__INFO": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_grid_d_range_label": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_D_RANGE__INPUT": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_D_RANGE__INFO": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_grid_rotate_label": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_ROTATE__INPUT": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_ROTATE__INFO": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_grid_invert_label": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_INVERT__INPUT": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GRID_INVERT__INFO": 
                {
                    "AUGMENTOR__GRIDMASK__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_gaussian_noise_mean_label": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GAUSSIAN_NOISE_MEAN__INFO": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_gaussian_noise_var_label": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__GAUSSIAN_NOISE_VAR__INFO": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_gaussian_noise_use_input_img_label": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INFO": 
                {
                    "AUGMENTOR__GAUSSIAN_NOISE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_salt_amount_label": 
                {
                    "AUGMENTOR__SALT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SALT_AMOUNT__INPUT": 
                {
                    "AUGMENTOR__SALT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SALT_AMOUNT__INFO": 
                {
                    "AUGMENTOR__SALT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_pepper_amount_label": 
                {
                    "AUGMENTOR__PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__PEPPER_AMOUNT__INPUT": 
                {
                    "AUGMENTOR__PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__PEPPER_AMOUNT__INFO": 
                {
                    "AUGMENTOR__PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "da_salt_pepper_amount_label": 
                {
                    "AUGMENTOR__SALT_AND_PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT": 
                {
                    "AUGMENTOR__SALT_AND_PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INFO": 
                {
                    "AUGMENTOR__SALT_AND_PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "da_salt_pepper_prop_label": 
                {
                    "AUGMENTOR__SALT_AND_PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT": 
                {
                    "AUGMENTOR__SALT_AND_PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "AUGMENTOR__SALT_AND_PEPPER_PROP__INFO": 
                {
                    "AUGMENTOR__SALT_AND_PEPPER__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "ssl_resizing_factor_label": 
                {
                    "PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT": 
                    [
                        "crappify"
                    ],
                }, 
            "PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INPUT": 
                {
                    "PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT": 
                    [
                        "crappify"
                    ],
                }, 
            "PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INFO": 
                {
                    "PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT": 
                    [
                        "crappify"
                    ],
                }, 
            "ssl_noise_label": 
                {
                    "PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT": 
                    [
                        "crappify"
                    ],
                }, 
            "PROBLEM__SELF_SUPERVISED__NOISE__INFO": 
                {
                    "PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT": 
                    [
                        "crappify"
                    ],
                }, 
            "PROBLEM__SELF_SUPERVISED__NOISE__INPUT": 
                {
                    "PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT": 
                    [
                        "crappify"
                    ],
                }, 
            "test_tab_widget": 
                {
                    "TEST__ENABLE__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_metrics_label": 
                {
                    "DATA__TEST__LOAD_GT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_metrics_frame": 
                {
                    "DATA__TEST__LOAD_GT__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "det_metrics_label": 
                {
                    "DATA__TEST__LOAD_GT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "det_metrics_frame": 
                {
                    "DATA__TEST__LOAD_GT__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_b_channel_th_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Central points", 
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Central points", 
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Central points", 
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                },
            "inst_seg_c_channel_th_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "inst_seg_d_channel_th_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)", 
                        "Distance map with background (experimental)"
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)", 
                        "Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual",
                        "auto"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)", 
                        "Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual",
                        "auto"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)", 
                        "Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual",
                        "auto"
                    ]
                }, 
            "inst_seg_p_channel_th_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                },
            "inst_seg_repare_large_blobs_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "inst_seg_remove_close_points_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "inst_seg_remove_close_points_radius_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                },
            "inst_seg_fore_mask_th_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Central points", 
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Central points", 
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Central points", 
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT":
                    [
                        "manual"
                    ]
                }, 
            "inst_seg_voronoi_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask"
                    ],
                },
            "TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask"
                    ],
                },
            "TEST__POST_PROCESSING__VORONOI_ON_MASK__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask"
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__LABEL": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",  
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",  
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Distance map", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                        "Binary mask + Distance map with background (experimental)",  
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__LABEL": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Contours", 
                        "Binary mask + Contours + Foreground mask", 
                        "Binary mask + Contours + Distance map", 
                        "Binary mask + Contours + Distance map with background (experimental)",
                    ],
                },
            "inst_seg_fore_dil_label": 
                {
                    "PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_fore_ero_label": 
                {
                    "PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_small_obj_fil_before_size_label": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INFO": 
                {
                    "PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_remove_close_points_radius_label": 
                {
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                }, 
            "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                    "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT": 
                    [
                        "Binary mask + Central points",
                    ],
                }, 
            "inst_seg_matching_stats_ths_label": 
                {
                    "TEST__MATCHING_STATS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__MATCHING_STATS_THS__INPUT": 
                {
                    "TEST__MATCHING_STATS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__MATCHING_STATS_THS__INFO": 
                {
                    "TEST__MATCHING_STATS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "inst_seg_matching_stats_colores_img_ths_label": 
                {
                    "TEST__MATCHING_STATS__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT": 
                {
                    "TEST__MATCHING_STATS__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__MATCHING_STATS_THS_COLORED_IMG__INFO": 
                {
                    "TEST__MATCHING_STATS__INPUT": 
                    [
                        "Yes"
                    ],
                },  
            "inst_seg_voronoi_mask_th_label": 
                {
                    "TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__VORONOI_TH__INPUT": 
                {
                    "TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__VORONOI_TH__INFO": 
                {
                    "TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },  
            "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT": 
                    [
                        "Yes"
                    ],
                },  
            "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT": 
                    [
                        "Yes"
                    ],
                },  
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__LABEL": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT": 
                    [
                        "Yes"
                    ],
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                },
            "det_remove_close_points_radius_label": 
                {
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT": 
                {
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INFO": 
                {
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "det_watershed_first_dilation_label": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INFO": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "det_watershed_donuts_classes_label": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INFO": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "det_watershed_donuts_patch_label": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INFO": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "det_watershed_donuts_nucleus_diam_label": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INFO": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "det_data_watetshed_check_label": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__DETECTION__DATA_CHECK_MW__INPUT": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 
            "PROBLEM__DETECTION__DATA_CHECK_MW__INFO": 
                {
                    "TEST__POST_PROCESSING__DET_WATERSHED__INPUT": 
                    [
                        "Yes"
                    ],
                }, 

            # Model widgets
            "MODEL__ARCHITECTURE__LABEL": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                },
            "MODEL__ARCHITECTURE__INFO": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                },
            "MODEL__ARCHITECTURE__INPUT": 
                {
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                },
            "unet_model_like_frame": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'U-Net', 
                        'Residual U-Net', 
                        'ResUNet++',
                        'ResUNet SE',
                        'U-NeXt V1', 
                        'Attention U-Net', 
                        'MultiResUnet', 
                        'SEUnet', 
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                }, 
            "unet_model_like_label": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'U-Net', 
                        'Residual U-Net', 
                        'ResUNet++',
                        'ResUNet SE',
                        'U-NeXt V1', 
                        'Attention U-Net', 
                        'MultiResUnet', 
                        'SEUnet', 
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                },
            "sr_unet_like_heading": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'U-Net', 
                        'Residual U-Net', 
                        'ResUNet++',
                        'ResUNet SE',
                        'U-NeXt V1', 
                        'Attention U-Net', 
                        'MultiResUnet', 
                        'SEUnet', 
                    ],
                },
            "sr_unet_like_frame": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'U-Net', 
                        'Residual U-Net', 
                        'ResUNet++',
                        'ResUNet SE',
                        'U-NeXt V1', 
                        'Attention U-Net', 
                        'MultiResUnet', 
                        'SEUnet', 
                    ],
                }, 
            "transformers_frame": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                        'UNETR', 
                        'ViT', 
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                }, 
            "transformers_label": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                        'UNETR', 
                        'ViT', 
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                }, 
            "convnext_label": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'U-NeXt V1', 
                        'U-NeXt V2', 
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                }, 
            "convnext_frame": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'U-NeXt V1', 
                        'U-NeXt V2', 
                    ],
                    "LOAD_PRETRAINED_MODEL__INPUT": 
                    [
                        'No', 
                    ],
                }, 
            "unetr_vit_hidden_multiple_label": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_VIT_HIDD_MULT__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                },
            "MODEL__UNETR_VIT_HIDD_MULT__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "unetr_num_filters_label": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_VIT_NUM_FILTERS__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_VIT_NUM_FILTERS__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "unetr_dec_act_label": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_DEC_ACTIVATION__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_DEC_ACTIVATION__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_DEC_KERNEL_SIZE__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_DEC_KERNEL_SIZE__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                }, 
            "MODEL__UNETR_DEC_KERNEL_SIZE__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'UNETR', 
                    ],
                },
            "MODEL__MAE_MASK_TYPE__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_MASK_TYPE__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_MASK_TYPE__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_MASK_RATIO__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                    "MODEL__MAE_MASK_TYPE__INPUT":
                    [
                        'random', 
                    ],
                }, 
            "MODEL__MAE_MASK_RATIO__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                    "MODEL__MAE_MASK_TYPE__INPUT":
                    [
                        'random', 
                    ],
                },
            "MODEL__MAE_MASK_RATIO__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                    "MODEL__MAE_MASK_TYPE__INPUT":
                    [
                        'random', 
                    ],
                },
            "MODEL__MAE_DEC_HIDDEN_SIZE__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_HIDDEN_SIZE__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_HIDDEN_SIZE__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_NUM_LAYERS__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_NUM_LAYERS__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_NUM_LAYERS__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_NUM_HEADS__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_NUM_HEADS__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_NUM_HEADS__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_MLP_DIMS__INPUT": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_MLP_DIMS__INFO": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "MODEL__MAE_DEC_MLP_DIMS__LABEL": 
                {
                    "MODEL__ARCHITECTURE__INPUT": 
                    [
                        'MAE', 
                    ],
                }, 
            "process_by_chunks_label": 
                {
                    "TEST__BY_CHUNKS__ENABLE__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "process_by_chunks_frame": 
                {
                    "TEST__BY_CHUNKS__ENABLE__INPUT": 
                    [
                        'Yes', 
                    ],
                },
            "TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__LABEL": 
                {
                    "TEST__BY_CHUNKS__WORKFLOW_PROCESS__ENABLE__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL": 
                {
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO": 
                {
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT": 
                {
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL": 
                {
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO": 
                {
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT": 
                {
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT": 
                    [
                        'Yes', 
                    ],
                }, 
            "TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INPUT": 
                {
                    "TEST__BY_CHUNKS__WORKFLOW_PROCESS__ENABLE__INPUT": 
                    [
                        'Yes', 
                    ],
                },
            "TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INFO": 
                {
                    "TEST__BY_CHUNKS__WORKFLOW_PROCESS__ENABLE__INPUT": 
                    [
                        'Yes', 
                    ],
                },
            "DATA__PATCH_SIZE__TEST__LABEL": 
                {
                    "TRAIN__ENABLE__INPUT": 
                    [
                        'No', 
                    ],
                },
            "DATA__PATCH_SIZE__TEST__INFO": 
                {
                    "TRAIN__ENABLE__INPUT": 
                    [
                        'No', 
                    ],
                },
            "DATA__PATCH_SIZE__TEST__INPUT": 
                {
                    "TRAIN__ENABLE__INPUT": 
                    [
                        'No', 
                    ],
                },
            "TEST__DET_BLOB_LOG_MIN_SIGMA__LABEL": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_MIN_SIGMA__INPUT": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_MIN_SIGMA__INFO": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_MAX_SIGMA__LABEL": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_MAX_SIGMA__INPUT": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_MAX_SIGMA__INFO": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_NUM_SIGMA__LABEL": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_NUM_SIGMA__INPUT": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_BLOB_LOG_NUM_SIGMA__INFO": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'blob_log', 
                    ],
                },
            "TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__LABEL": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'peak_local_max', 
                    ],
                },
            "TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__INFO": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'peak_local_max', 
                    ],
                },
            "TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__INPUT": 
                {
                    "TEST__DET_POINT_CREATION_FUNCTION__INPUT": 
                    [
                        'peak_local_max', 
                    ],
                },
            "MODEL__N_CLASSES__LABEL": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "CLASSIFICATION",
                    ]
                },
            "MODEL__N_CLASSES__INFO": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "CLASSIFICATION",
                    ]
                },
            "MODEL__N_CLASSES__INPUT": 
                {
                    "WORKFLOW_SELECTED_LABEL": [
                        "SEMANTIC_SEG",
                        "INSTANCE_SEG",
                        "DETECTION",
                        "CLASSIFICATION",
                    ]
                },
            "preprocessing_frame": 
                {
                    "or_operation_mode": True,
                    "DATA__PREPROCESS__TRAIN__INPUT": [
                        "Yes",
                    ],
                    "DATA__PREPROCESS__VAL__INPUT": [
                        "Yes",
                    ],
                },
            "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ORDER__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ORDER__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ORDER__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__MODE__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__MODE__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__MODE__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CVAL__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CVAL__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CVAL__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CLIP__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CLIP__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CLIP__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },

            "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__LABEL": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INFO": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INPUT": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__LABEL": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INFO": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INPUT": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__LABEL": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INFO": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INPUT": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__LABEL": 
                {
                    "DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INFO": 
                {
                    "DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INPUT": 
                {
                    "DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INFO": 
                {
                    "DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__LABEL": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INFO": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INPUT": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__BN": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__LABEL": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INFO": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INPUT": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__LABEL": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INFO": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INPUT": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__LABEL": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INFO": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INPUT": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__LABEL": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INFO": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INPUT": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "preprocessing_test_frame": 
                {
                    "DATA__PREPROCESS__TEST__INPUT": [
                        "Yes",
                    ],
                },
            "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ORDER__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ORDER__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ORDER__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__MODE__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__MODE__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__MODE__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CVAL__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CVAL__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CVAL__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CLIP__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CLIP__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__CLIP__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INFO": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },

            "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INFO": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INFO": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INFO": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INFO": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__BN": 
                {
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INFO": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INFO": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INFO": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__LABEL": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INFO": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INPUT": 
                {
                    "DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT": [
                        "Yes",
                    ]
                },
            "TEST__AUGMENTATION_MODE__LABEL": 
                {
                    "TEST__AUGMENTATION__INPUT": [
                        "Yes",
                    ]
                },
            "TEST__AUGMENTATION_MODE__INFO": 
                {
                    "TEST__AUGMENTATION__INPUT": [
                        "Yes",
                    ]
                },
            "TEST__AUGMENTATION_MODE__INPUT": 
                {
                    "TEST__AUGMENTATION__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL": 
                {
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO": 
                {
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT": 
                {
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL": 
                {
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO": 
                {
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT": 
                {
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__PROPS__LABEL": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__PROPS__INFO": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__PROPS__INPUT": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__VALUES__LABEL": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__VALUES__INFO": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__VALUES__INPUT": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__SIGNS__LABEL": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__SIGNS__INFO": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__SIGNS__INPUT": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__NORM_BEFORE__LABEL": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__NORM_BEFORE__INFO": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TRAIN__FILTER_SAMPLES__NORM_BEFORE__INPUT": 
                {
                    "DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__PROPS__LABEL": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__PROPS__INFO": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__PROPS__INPUT": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__VALUES__LABEL": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__VALUES__INFO": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__VALUES__INPUT": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__SIGNS__LABEL": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__SIGNS__INFO": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__SIGNS__INPUT": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__NORM_BEFORE__LABEL": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__NORM_BEFORE__INFO": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__FILTER_SAMPLES__NORM_BEFORE__INPUT": 
                {
                    "DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },

            "DATA__TEST__FILTER_SAMPLES__PROPS__LABEL": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__PROPS__INFO": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__PROPS__INPUT": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__VALUES__LABEL": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__VALUES__INFO": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__VALUES__INPUT": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__SIGNS__LABEL": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__SIGNS__INFO": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__SIGNS__INPUT": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__NORM_BEFORE__LABEL": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__NORM_BEFORE__INFO": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__TEST__FILTER_SAMPLES__NORM_BEFORE__INPUT": 
                {
                    "DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL": 
                {
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO": 
                {
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT": 
                {
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL": 
                {
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO": 
                {
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
            "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT": 
                {
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT": [
                        "Yes",
                    ]
                },
    }   

    def combobox_hide_visible_action(self, main_window, list_of_widgets_to_update, widgets_to_set_cond=None, 
        widgets_to_set=None, updated_widget=None, frames_to_hide_if_empty=None):
        """
        Decide visibility of widgets deping on the the combobox that has been changed. 

        Parameters
        ----------
        main_window : QT GUI
            Main window.

        list_of_widgets_to_update : List of str
            List of names of widgets to check so their visibility may change. Each condition described in 
            ``self.conditions`` will be checked and if all of them are satisfy the widget will be visible. 
            Each widget conditions' declaration have the following structure:
            "A": { "B": ["C", "D"], "E": ["F", "G", "H"]}. This mean that the widget "A" is visible if two 
            conditions are satisfied: 1) the widget "B" need to have "C" or "D" value and 2) "E" widget
            need to have a value between "F", "G" or "H".
            If ``or_operation_mode`` property exist, the AND condition is changed to OR.

        widgets_to_set_cond : List of tuples, optional
            List of tuples containing the widgets that need to be set with an specific value. 
            For this option ``updated_widget`` need to be provided also. 
            E.g. (["A", "B"], ["C"]) means that widget "A" will be changed to value "B" if 
            the ``updated_widget`` has value ``C``. 

        widgets_to_set : List of str, optional
            List of names of widgets to set them to the value of ``updated_widget``. 

        updated_widget : str, optional
            Name of the widget that called the function. Is an auxiliary variable for
            ``widgets_to_set_cond`` and ``widgets_to_set`` to set widgets to an specific value. 

        frames_to_hide_if_empty : List of str, optional
            List of names of widgets to be checked if all their values are visible or not to 
            hide it also. 
        """  
        if widgets_to_set_cond is not None and updated_widget is None:
            raise ValueError("''updated_widget' need to be declared when 'widgets_to_set_cond' is set")
        if updated_widget is not None and updated_widget is None:
            raise ValueError("''updated_widget' need to be declared when 'updated_widget' is set")

        for widget in list_of_widgets_to_update:
            visible = True

            if widget not in self.conditions:
                raise ValueError("{} widget not declared yet".format(widget))

            # Check conditions
            if 'or_operation_mode' in self.conditions[widget]:
                visible = False
                for cond_widget in self.conditions[widget]:
                    if cond_widget != 'or_operation_mode':
                        value = str(get_text(getattr(main_window.ui, cond_widget)))
                        if value in self.conditions[widget][cond_widget]:
                            visible = True  
                            break      
            else:
                for cond_widget in self.conditions[widget]:
                    value = str(get_text(getattr(main_window.ui, cond_widget)))
                    if value not in self.conditions[widget][cond_widget]:
                        visible = False  
                        break  
        
            getattr(main_window.ui, widget).setVisible(visible)        

        # Widgets to set with a value based on condition
        if updated_widget is not None and widgets_to_set_cond is not None:
            cbox_value = str(get_text(getattr(main_window.ui, updated_widget)))
            for tup in widgets_to_set_cond:
                if cbox_value in tup[1]:
                    getattr(main_window.ui, tup[0][0]).setCurrentText(tup[0][1]) 

        # Widgets to set with a value
        if updated_widget is not None and widgets_to_set is not None:
            cbox_value = str(get_text(getattr(main_window.ui, updated_widget)))
            for wid in widgets_to_set:
                getattr(main_window.ui, wid).setCurrentText(cbox_value)
                 
        # Frames to hide if all the childs are not visible 
        if frames_to_hide_if_empty is not None:
            for frame in frames_to_hide_if_empty:
                all_conditions = []
                for x in getattr(main_window.ui, frame).findChildren(QLabel):
                    all_conditions.append(x.isVisibleTo(getattr(main_window.ui, frame)) )
                if any(all_conditions):
                    getattr(main_window.ui, frame).setVisible(True)
                else:
                    getattr(main_window.ui, frame).setVisible(False)

        