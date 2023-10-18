import os
import sys
import tempfile
import logging
import traceback
import io

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QThread, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QDesktopServices, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow 
from ui_function import * 
from ui_utils import (examine, mark_syntax_error, expand_hide_advanced_options, buttonPressed, 
    load_yaml_config, resource_path, load_yaml_to_GUI)
from settings import Settings
from widget_conditions import Widget_conditions
from aux_windows import dialog_Ui, workflow_explanation_Ui, yes_no_Ui

os.environ['QT_MAC_WANTS_LAYER'] = '1'

class MainWindow(QMainWindow):
    def __init__(self, log_file, log_dir):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.log_file = log_file
        self.log_dir = log_dir
        self.cfg = Settings()

        # Adjust font cross-platform 
        self.setStyleSheet("QWidget{ font-size:16px;}")
        self.ui.biapy_version.setStyleSheet("QWidget{font-size:10px}")

        # So the error and dialog windows can access it 
        global ui
        ui = self
                
        self.setWindowTitle("BiaPy") 
        UIFunction.initStackTab(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.bn_min.clicked.connect(self.showMinimized)
        self.ui.bn_close.clicked.connect(self.close)

        two_pos_number_regex = QtCore.QRegExp('^\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*$')
        self.two_pos_number_validator = QtGui.QRegExpValidator(two_pos_number_regex)

        two_pos_number_parenthesis_regex = QtCore.QRegExp('^\(\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\)$')
        self.two_pos_number_parenthesis_validator = QtGui.QRegExpValidator(two_pos_number_parenthesis_regex)
        two_number_parenthesis_regex = QtCore.QRegExp('^\(\s*-?[0-9][0-9]*\s*,\s*-?[0-9][0-9]*\s*\)$')
        self.two_number_parenthesis_validator = QtGui.QRegExpValidator(two_number_parenthesis_regex)
        two_pos_0_1_float_number_parenthesis_regex = QtCore.QRegExp('^\(\s*0\.[0-9]*\s*,\s*0\.[0-9]*\s*\)$')
        self.two_pos_0_1_float_number_parenthesis_validator = QtGui.QRegExpValidator(two_pos_0_1_float_number_parenthesis_regex)
        two_0_1_float_number_parenthesis_regex = QtCore.QRegExp('^\(\s*-?0\.[0-9]*\s*,\s*-?0\.[0-9]*\s*\)$')
        self.two_0_1_float_number_parenthesis_validator = QtGui.QRegExpValidator(two_0_1_float_number_parenthesis_regex)
        two_0_2_float_number_parenthesis_regex = QtCore.QRegExp('^\(\s*[0-1]\.[0-9]*\s*,\s*[0-1]\.[0-9]*\s*\)$')
        self.two_0_2_float_number_parenthesis_validator = QtGui.QRegExpValidator(two_0_2_float_number_parenthesis_regex)
        two_pos_float_number_parenthesis_regex = QtCore.QRegExp('^\(\s*[0-9]\.[0-9]*\s*,\s*[0-9]\.[0-9]*\s*\)$')
        self.two_pos_float_number_parenthesis_validator = QtGui.QRegExpValidator(two_pos_float_number_parenthesis_regex)
        three_number_parenthesis_regex = QtCore.QRegExp('^\(\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\)$')
        self.three_number_parenthesis_validator = QtGui.QRegExpValidator(three_number_parenthesis_regex)
        four_number_parenthesis_regex = QtCore.QRegExp('^\(\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\)$')
        self.four_number_parenthesis_validator = QtGui.QRegExpValidator(four_number_parenthesis_regex)

        two_pos_number_bracket_regex = QtCore.QRegExp('^\[\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\]$')
        self.two_pos_number_bracket_validator = QtGui.QRegExpValidator(two_pos_number_bracket_regex)
        no_limit_number_min_one_number_bracket_regex = QtCore.QRegExp('^\[\s*[0-9][0-9]*\s*(,\s*[0-9][0-9]*\s*)*\]$')
        self.no_limit_number_min_one_number_bracket_validator = QtGui.QRegExpValidator(no_limit_number_min_one_number_bracket_regex)
        no_limit_number_bracket_regex = QtCore.QRegExp('^\[\s*[0-9]*\s*(,\s*[0-9]*\s*)*\]$')
        self.no_limit_number_bracket_validator = QtGui.QRegExpValidator(no_limit_number_bracket_regex)
        no_limit_0_1_float_number_bracket_regex = QtCore.QRegExp('^\[\s*0\.[0-9]*\s*(,\s*0\.[0-9]*\s*)*\]$')
        self.no_limit_0_1_float_number_bracket_validator = QtGui.QRegExpValidator(no_limit_0_1_float_number_bracket_regex)
        z_down_bracket_regex = QtCore.QRegExp('^\[\s*[0-2]\s*(,\s*[0-2]\s*)*\]$')
        self.z_down_bracket_validator = QtGui.QRegExpValidator(z_down_bracket_regex)

        self.float_validator = QtGui.QDoubleValidator(0.,1.,3)
        self.large_range_float_validator = QtGui.QDoubleValidator(0.,10.,3)
        self.int_validator = QtGui.QIntValidator(0, 99999)

        # Left buttons
        self.ui.bn_home.clicked.connect(lambda: buttonPressed(self, 'bn_home', 99))
        self.ui.bn_workflow.clicked.connect(lambda: buttonPressed(self, 'bn_workflow', 99))
        self.ui.bn_goptions.clicked.connect(lambda: buttonPressed(self, 'bn_goptions', 99))
        self.ui.bn_train.clicked.connect(lambda: buttonPressed(self, 'bn_train', 99))
        self.ui.bn_test.clicked.connect(lambda: buttonPressed(self, 'bn_test', 99))
        self.ui.bn_run_biapy.clicked.connect(lambda: buttonPressed(self,'bn_run_biapy',99))

        # Home page buttons 
        self.ui.continue_yaml_bn.clicked.connect(lambda: buttonPressed(self,'bn_run_biapy',99))
        self.ui.create_yaml_bn.clicked.connect(lambda: buttonPressed(self, 'bn_workflow', 99))
        self.ui.load_yaml_bn.clicked.connect(lambda: load_yaml_to_GUI(self))
        self.ui.biapy_github_bn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/danifranco/BiaPy")))
        self.ui.biapy_forum_bn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://forum.image.sc/")))
        self.ui.biapy_templates_bn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/danifranco/BiaPy/tree/master/templates")))
        self.ui.biapy_doc_bn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://biapy.readthedocs.io/en/latest/")))
        self.ui.biapy_notebooks_bn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/danifranco/BiaPy/tree/master/notebooks")))
        self.ui.biapy_citation_bn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/danifranco/BiaPy#citation")))

        # Workflow page buttons
        self.ui.left_arrow_bn.clicked.connect(lambda: UIFunction.move_workflow_view(self, True))
        self.ui.right_arrow_bn.clicked.connect(lambda: UIFunction.move_workflow_view(self, False))
        self.ui.continue_bn.clicked.connect(lambda: buttonPressed(self, 'up', -1))
        self.ui.back_bn.clicked.connect(lambda: buttonPressed(self, 'down', -1))
        self.ui.back_bn.setIcon(QIcon(resource_path(os.path.join("images","bn_images", "back.png"))))

        self.ui.window1_bn.clicked.connect(lambda: buttonPressed(self, 'bn_workflow', 99))
        self.ui.window2_bn.clicked.connect(lambda: buttonPressed(self, 'bn_goptions', 99))
        self.ui.window3_bn.clicked.connect(lambda: buttonPressed(self, 'bn_train', 99))
        self.ui.window4_bn.clicked.connect(lambda: buttonPressed(self, 'bn_test', 99))
        
        self.ui.workflow_view2_seemore_bn.clicked.connect(lambda: UIFunction.obtain_workflow_description(self))

        # General options page buttons
        self.ui.seed_input.setValidator(self.int_validator)
        self.ui.MODEL__SAVE_CKPT_FREQ__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__NDIM__INPUT.currentIndexChanged.connect(lambda: self.change_problem_dimensions(self.ui.PROBLEM__NDIM__INPUT.currentIndex()))
        self.change_problem_dimensions(0)
        self.ui.goptions_advanced_bn.clicked.connect(lambda: expand_hide_advanced_options(self, "goptions_advanced_bn", "goptions_advanced_options_scrollarea"))
        self.ui.goptions_browse_yaml_path_bn.clicked.connect(lambda: examine(self, "goptions_browse_yaml_path_input", False))
        self.ui.checkpoint_file_path_browse_bn.clicked.connect(lambda: examine(self, "PATHS__CHECKPOINT_FILE__INPUT"))

        # Train page buttons 
        self.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT.setValidator(self.int_validator)
        self.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT.setValidator(self.int_validator)
        self.ui.DATA__VAL__SPLIT_TRAIN__INPUT.setValidator(self.float_validator)
        self.ui.TRAIN__EPOCHS__INPUT.setValidator(self.int_validator)
        self.ui.TRAIN__ACCUM_ITER__INPUT.setValidator(self.int_validator)
        self.ui.TRAIN__PATIENCE__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__N_CLASSES__INPUT.setValidator(self.float_validator)
        # self.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT.setValidator(self.float_validator)
        # self.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT.setValidator(self.float_validator)
        self.ui.DATA__TRAIN__REPLICATE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__FEATURE_MAPS__INPUT.setValidator(self.no_limit_number_min_one_number_bracket_validator)
        self.ui.MODEL__DROPOUT_VALUES__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.MODEL__KERNEL_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__Z_DOWN__INPUT.setValidator(self.z_down_bracket_validator)
        self.ui.MODEL__VIT_TOKEN_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_EMBED_DIM__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_NUM_LAYERS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_MLP_RATIO__INPUT.setValidator(self.large_range_float_validator)
        self.ui.MODEL__MAE_DEC_HIDDEN_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__MAE_DEC_NUM_LAYERS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__MAE_DEC_NUM_HEADS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__MAE_DEC_MLP_DIMS__INPUT.setValidator(self.int_validator) 
        self.ui.MODEL__VIT_NORM_EPS__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__VIT_NUM_HEADS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__UNETR_VIT_HIDD_MULT__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__UNETR_VIT_NUM_FILTERS__INPUT.setValidator(self.int_validator)
        self.ui.TRAIN__LR__INPUT.setValidator(self.float_validator)
        self.ui.TRAIN__W_DECAY__INPUT.setValidator(self.float_validator)
        self.ui.TRAIN__BATCH_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT.setValidator(self.two_pos_number_validator)
        # self.ui.TRAIN__LR_SCHEDULER__MIN_LR__INPUT.setValidator(self.float_validator)
        # self.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT.setValidator(self.int_validator)
        self.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT.setValidator(self.float_validator)
        # self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT.setValidator(self.int_validator)
        self.ui.AUGMENTOR__DA_PROB__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT.setValidator(self.int_validator)
        self.ui.AUGMENTOR__RANDOM_ROT_RANGE__INPUT.setValidator(self.two_number_parenthesis_validator)
        self.ui.AUGMENTOR__SHEAR__INPUT.setValidator(self.two_number_parenthesis_validator)
        self.ui.AUGMENTOR__ZOOM_RANGE__INPUT.setValidator(self.two_0_2_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__SHIFT_RANGE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__E_ALPHA__INPUT.setValidator(self.two_number_parenthesis_validator)   
        self.ui.AUGMENTOR__G_SIGMA__INPUT.setValidator(self.two_pos_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__MB_KERNEL__INPUT.setValidator(self.two_number_parenthesis_validator)
        self.ui.AUGMENTOR__MOTB_K_RANGE__INPUT.setValidator(self.two_number_parenthesis_validator)
        self.ui.AUGMENTOR__GC_GAMMA__INPUT.setValidator(self.two_pos_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INPUT.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__BRIGHTNESS_EM_FACTOR__INPUT.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__CONTRAST_EM_FACTOR__INPUT.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__DROP_RANGE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__COUT_NB_ITERATIONS__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.AUGMENTOR__COUT_SIZE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__COUT_CVAL__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__CBLUR_SIZE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.AUGMENTOR__CMIX_SIZE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__CNOISE_SCALE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.AUGMENTOR__CNOISE_SIZE__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__MS_DISPLACEMENT__INPUT.setValidator(self.int_validator)
        self.ui.AUGMENTOR__MS_ROTATE_RATIO__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__MISSP_ITERATIONS__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.AUGMENTOR__GRID_RATIO__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__GRID_D_RANGE__INPUT.setValidator(self.two_pos_float_number_parenthesis_validator)
        self.ui.AUGMENTOR__GRID_ROTATE__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__SALT_AMOUNT__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__PEPPER_AMOUNT__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT.setValidator(self.float_validator)
        self.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT.setValidator(self.float_validator) 

        self.ui.DATA__W_FOREGROUND__INPUT.setValidator(self.float_validator)
        self.ui.DATA__W_BACKGROUND__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__SEMANTIC_SEG__IGNORE_CLASS_ID__INPUT.setValidator(self.int_validator)
        self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__SEM_SEG__INPUT.setValidator(self.float_validator)
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__SEM_SEG__INPUT.setValidator(self.int_validator)
        self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__SEM_SEG__INPUT.setValidator(self.int_validator)

        self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__INST_SEG__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS_WEIGHTS__INPUT.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT.setValidator(self.large_range_float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT.setValidator(self.no_limit_number_bracket_validator)
        self.ui.TEST__MATCHING_STATS_THS__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INST_SEG__INPUT.setValidator(self.int_validator)
        self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__INST_SEG__INPUT.setValidator(self.int_validator)
        self.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT.setValidator(self.float_validator)
        # self.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT.setValidator(self.int_validator)
        # self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)

        self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__DET__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__DETECTION__CENTRAL_POINT_DILATION__INPUT.setValidator(self.int_validator)
        self.ui.TEST__DET_MIN_TH_TO_BE_PEAK__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__DET__INPUT.setValidator(self.int_validator)
        self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__DET__INPUT.setValidator(self.int_validator)
        # self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT.setValidator(self.float_validator)
        # self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT.setValidator(self.no_limit_number_bracket_validator)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT.setValidator(self.no_limit_number_bracket_validator)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT.setValidator(self.int_validator)
        self.ui.TEST__DET_TOLERANCE__INPUT.setValidator(self.no_limit_number_min_one_number_bracket_validator)

        self.ui.PROBLEM__DENOISING__N2V_PERC_PIX__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__DENOISING__N2V_NEIGHBORHOOD_RADIUS__INPUT.setValidator(self.int_validator)

        self.condition_db = Widget_conditions()
        self.ui.MODEL__LOAD_CHECKPOINT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["PATHS__CHECKPOINT_FILE__INPUT", "checkpoint_file_path_browse_bn", "checkpoint_file_path_browse_label",
             "checkpoint_loading_opt_label", "checkpoint_loading_opt_frame"]))
        self.ui.job_name_input.textChanged.connect(lambda: mark_syntax_error(self, "job_name_input", ["empty"]))   
        self.ui.goptions_yaml_name_input.textChanged.connect(lambda: mark_syntax_error(self, "goptions_yaml_name_input", ["empty"]))
        self.ui.goptions_browse_yaml_path_input.textChanged.connect(lambda: mark_syntax_error(self, "goptions_browse_yaml_path_input", ["empty"]))      
        self.ui.TRAIN__ENABLE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["train_tab_widget"]))      
        self.ui.train_data_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TRAIN__PATH__INPUT", False))
        self.ui.train_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TRAIN__GT_PATH__INPUT", False))
        self.ui.val_data_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__VAL__PATH__INPUT", False))
        self.ui.val_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__VAL__GT_PATH__INPUT", False))
        self.ui.DATA__TRAIN__IN_MEMORY__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            [], widgets_to_set_cond=[
                (["DATA__VAL__TYPE__INPUT", "Not extracted from train (path needed)"], ["No"])
            ], updated_widget="DATA__TRAIN__IN_MEMORY__INPUT"))
        self.ui.DATA__VAL__TYPE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["percentage_validation_label", "DATA__VAL__SPLIT_TRAIN__INPUT", "cross_validation_nfolds_label", "DATA__VAL__CROSS_VAL_NFOLD__INPUT",
            "cross_validation_fold_label", "DATA__VAL__CROSS_VAL_FOLD__INPUT", "use_val_as_test", "DATA__TEST__USE_VAL_AS_TEST__INPUT",
            "DATA__VAL__PATH__LABEL", "DATA__VAL__PATH__INPUT", "val_data_input_browse_bn", "validation_data_gt_label", "DATA__VAL__GT_PATH__INPUT",
            "val_data_gt_input_browse_bn", "val_in_memory_label", "DATA__VAL__IN_MEMORY__INPUT", "test_data_label", "DATA__TEST__PATH__INPUT",
            "test_data_input_browse_bn", "test_exists_gt_label", "DATA__TEST__LOAD_GT__INPUT", "test_data_gt_label", "DATA__TEST__GT_PATH__INPUT",
            "test_data_gt_input_browse_bn", "test_data_in_memory_label", "DATA__TEST__IN_MEMORY__INPUT", "random_val_label", "DATA__VAL__RANDOM__INPUT",
            "validation_overlap_label", "DATA__VAL__OVERLAP__INPUT", "validation_padding_label", "DATA__VAL__PADDING__INPUT",
            ],
            widgets_to_set_cond=
            [
                (["DATA__TRAIN__IN_MEMORY__INPUT", "Yes"], ["Extract from train (split training)","Extract from train (cross validation)"])
            ], updated_widget="DATA__VAL__TYPE__INPUT"))
        self.ui.train_advanced_bn.clicked.connect(lambda: expand_hide_advanced_options(self, "train_advanced_bn", "train_advanced_options_frame"))
        self.ui.MODEL__ARCHITECTURE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["unet_model_like_frame", "unet_model_like_label", "sr_unet_like_heading", "sr_unet_like_frame", "transformers_frame", "transformers_label", 
            "unetr_vit_hidden_multiple_label", "MODEL__UNETR_VIT_HIDD_MULT__INPUT", "unetr_num_filters_label", "MODEL__UNETR_VIT_NUM_FILTERS__INPUT", 
            "unetr_dec_act_label", "MODEL__UNETR_DEC_ACTIVATION__INPUT", "MODEL__MAE_DEC_HIDDEN_SIZE__INPUT", "MODEL__MAE_DEC_HIDDEN_SIZE__LABEL", 
            "MODEL__MAE_DEC_NUM_LAYERS__INPUT", "MODEL__MAE_DEC_NUM_LAYERS__LABEL", "MODEL__MAE_DEC_NUM_HEADS__INPUT", "MODEL__MAE_DEC_NUM_HEADS__LABEL",
            "MODEL__MAE_DEC_MLP_DIMS__INPUT", "MODEL__MAE_DEC_HIDDEN_SIZE__INPUT", "MODEL__MAE_DEC_MLP_DIMS__LABEL"], 
            widgets_to_set=["transformers_label"]))
        self.ui.TRAIN__OPTIMIZER__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["TRAIN__W_DECAY__INPUT", "adamw_weight_decay_label"]))
        self.ui.TRAIN__PROFILER__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["profiler_batch_range_label", "TRAIN__PROFILER_BATCH_RANGE__INPUT"]))
        self.ui.DATA__NORMALIZATION__TYPE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["custom_mean_label", "DATA__NORMALIZATION__CUSTOM_MEAN__INPUT", "custom_std_label", "DATA__NORMALIZATION__CUSTOM_STD__INPUT"]))
        self.ui.DATA__EXTRACT_RANDOM_PATCH__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["extract_random_patch_frame_label", "extract_random_patch_frame"]))    
        self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            [ "lr_schel_warmupcosine_epochs_label", "TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT",
            "lr_schel_min_lr_label", "TRAIN__LR_SCHEDULER__MIN_LR__INPUT",
            "lr_schel_reduce_on_plat_patience_label", "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT",
            "lr_schel_reduce_on_plat_factor_label", "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT"]))
        self.ui.AUGMENTOR__ENABLE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_frame"]))
        self.ui.AUGMENTOR__RANDOM_ROT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_random_rot_range_label", "AUGMENTOR__RANDOM_ROT_RANGE__INPUT"]))
        self.ui.AUGMENTOR__SHEAR__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_shear_range_label", "AUGMENTOR__SHEAR_RANGE__INPUT"]))
        self.ui.AUGMENTOR__ZOOM__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_zoom_range_label", "AUGMENTOR__ZOOM_RANGE__INPUT"]))
        self.ui.AUGMENTOR__SHIFT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_shift_range_label", "AUGMENTOR__SHIFT_RANGE__INPUT"]))
        self.ui.AUGMENTOR__ELASTIC__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_elastic_alpha_label", "AUGMENTOR__E_ALPHA__INPUT", "da_elastic_sigma_label", "AUGMENTOR__E_SIGMA__INPUT",
            "da_elastic_mode_label", "AUGMENTOR__E_MODE__INPUT"]))
        self.ui.AUGMENTOR__G_BLUR__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_gaussian_sigma_label", "AUGMENTOR__G_SIGMA__INPUT"]))
        self.ui.AUGMENTOR__MEDIAN_BLUR__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_median_blur_k_size_label", "AUGMENTOR__MB_KERNEL__INPUT"]))
        self.ui.AUGMENTOR__MOTION_BLUR__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["da_motion_blur_k_size_label", "AUGMENTOR__MOTB_K_RANGE__INPUT"]))
        self.ui.AUGMENTOR__GAMMA_CONTRAST__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["da_gamma_contrast_range_label", "AUGMENTOR__GC_GAMMA__INPUT"]))
        self.ui.AUGMENTOR__BRIGHTNESS__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_brightness_factor_range_label", "AUGMENTOR__BRIGHTNESS_FACTOR__INPUT", "da_brightness_mode_label", "AUGMENTOR__BRIGHTNESS_MODE__INPUT"]))
        self.ui.AUGMENTOR__CONTRAST__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_contrast_factor_range_label", "AUGMENTOR__CONTRAST_FACTOR__INPUT", "da_contrast_mode_label", "AUGMENTOR__CONTRAST_MODE__INPUT"]))
        self.ui.AUGMENTOR__BRIGHTNESS_EM__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_brightness_em_factor_label", "AUGMENTOR__BRIGHTNESS_EM_FACTOR__INPUT", "da_brightness_em_mode_label",
                "AUGMENTOR__BRIGHTNESS_EM_MODE__INPUT"]))
        self.ui.AUGMENTOR__CONTRAST_EM__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_contrast_em_factor_label","AUGMENTOR__CONTRAST_EM_FACTOR__INPUT","da_contrast_em_mode_label","AUGMENTOR__CONTRAST_EM_MODE__INPUT"]))
        self.ui.AUGMENTOR__DROPOUT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["da_dropout_range_label","AUGMENTOR__DROP_RANGE__INPUT"]))
        self.ui.AUGMENTOR__CUTOUT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_cutout_number_iterations_label","AUGMENTOR__COUT_NB_ITERATIONS__INPUT","da_cutout_size_label", "AUGMENTOR__COUT_SIZE__INPUT",
            "da_cuout_cval_label","AUGMENTOR__COUT_CVAL__INPUT"]))
        self.ui.AUGMENTOR__CUTBLUR__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["da_cutblur_size_range_label","AUGMENTOR__CBLUR_SIZE__INPUT","da_cutblut_down_range_label","AUGMENTOR__CBLUR_DOWN_RANGE__INPUT",
             "da_cutblur_inside_label","AUGMENTOR__CBLUR_INSIDE__INPUT"]))
        self.ui.AUGMENTOR__CUTMIX__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["da_cutmix_size_range_label","AUGMENTOR__CMIX_SIZE__INPUT"]))
        self.ui.AUGMENTOR__CUTNOISE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_cutnoise_scale_range_label","AUGMENTOR__CNOISE_SCALE__INPUT","da_cutnoise_number_iter_label","AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT",
            "da_cutnoise_size_range_label","AUGMENTOR__CNOISE_SIZE__INPUT"]))
        self.ui.AUGMENTOR__MISALIGNMENT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_misaligment_displacement_label","AUGMENTOR__MS_DISPLACEMENT__INPUT","da_misaligment_rotate_ratio_label",
             "AUGMENTOR__MS_ROTATE_RATIO__INPUT"]))
        self.ui.AUGMENTOR__MISSING_SECTIONS__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_missing_sections_iteration_range_label","AUGMENTOR__MISSP_ITERATIONS__INPUT"]))
        self.ui.AUGMENTOR__GRIDMASK__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_grid_ratio_label","AUGMENTOR__GRID_RATIO__INPUT","da_grid_d_range_label","AUGMENTOR__GRID_D_RANGE__INPUT","da_grid_rotate_label",
             "AUGMENTOR__GRID_ROTATE__INPUT","da_grid_invert_label","AUGMENTOR__GRID_INVERT__INPUT"]))
        self.ui.AUGMENTOR__GAUSSIAN_NOISE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_gaussian_noise_mean_label","AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT","da_gaussian_noise_var_label","AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT",
             "da_gaussian_noise_use_input_img_label","AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT"]))
        self.ui.AUGMENTOR__SALT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["da_salt_amount_label","AUGMENTOR__SALT_AMOUNT__INPUT"]))
        self.ui.AUGMENTOR__PEPPER__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_pepper_amount_label","AUGMENTOR__PEPPER_AMOUNT__INPUT"]))
        self.ui.AUGMENTOR__SALT_AND_PEPPER__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["da_salt_pepper_amount_label","AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT","da_salt_pepper_prop_label","AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT"]))
        self.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["ssl_resizing_factor_label","PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INPUT","ssl_noise_label","PROBLEM__SELF_SUPERVISED__NOISE__INPUT"]))
        
        # Test page buttons
        self.ui.TEST__ENABLE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,["test_tab_widget"]))
        self.ui.test_data_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TEST__PATH__INPUT", False))
        self.ui.test_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TEST__GT_PATH__INPUT", False))
        self.ui.DATA__TEST__LOAD_GT__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["inst_seg_metrics_label","inst_seg_metrics_frame","det_metrics_label","det_metrics_frame"]))
        self.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["test_data_label","DATA__TEST__PATH__INPUT","test_data_input_browse_bn","test_exists_gt_label","DATA__TEST__LOAD_GT__INPUT",
             "test_data_gt_label","DATA__TEST__GT_PATH__INPUT","test_data_gt_input_browse_bn","test_data_in_memory_label",
             "DATA__TEST__IN_MEMORY__INPUT"]))
        self.ui.test_advanced_bn.clicked.connect(lambda: expand_hide_advanced_options(self, "test_advanced_bn", "test_advanced_options_frame"))

        self.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["sem_seg_yz_filtering_size_label","TEST__POST_PROCESSING__YZ_FILTERING_SIZE__SEM_SEG__INPUT"]))
        self.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["sem_seg_z_filtering_size_label","TEST__POST_PROCESSING__Z_FILTERING_SIZE__SEM_SEG__INPUT"]))
        self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_b_channel_th_label","PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT","inst_seg_c_channel_th_label",
             "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT","inst_seg_d_channel_th_label","PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT",
             "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT","PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__LABEL",
             "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT", "inst_seg_p_channel_th_label",
             "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT", "inst_seg_repare_large_blobs_label", 
             "TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT","inst_seg_remove_close_points_label",
             "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT", "inst_seg_remove_close_points_radius_label", 
             "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT","inst_seg_fore_mask_th_label",
             "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT","inst_seg_voronoi_label","TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT",
             "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__LABEL","PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT"],
             frames_to_hide_if_empty=["inst_seg_ths_frame"]))
        self.ui.PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_fore_dil_label","PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT", "inst_seg_fore_ero_label",
             "PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT"]))
        self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_small_obj_fil_before_size_label","PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT"]))
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self,
            ["inst_seg_yz_filtering_size_label","TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INST_SEG__INPUT"]))
        self.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_z_filtering_size_label","TEST__POST_PROCESSING__Z_FILTERING_SIZE__INST_SEG__INPUT"]))
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_remove_close_points_radius_label","TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT"]))
        self.ui.TEST__MATCHING_STATS__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_matching_stats_ths_label","TEST__MATCHING_STATS_THS__INPUT","inst_seg_matching_stats_colores_img_ths_label",
             "TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT"]))
        self.ui.TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_voronoi_mask_th_label", "TEST__POST_PROCESSING__VORONOI_TH__INPUT"]))
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["inst_seg_b_channel_th_label", "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT","inst_seg_c_channel_th_label",
             "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT","inst_seg_p_channel_th_label","PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT",
             "inst_seg_d_channel_th_label","PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT","PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT",
             "inst_seg_fore_mask_th_label", "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT"],frames_to_hide_if_empty=["inst_seg_ths_frame"]))

        self.ui.TEST__DET_LOCAL_MAX_COORDS__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["det_min_th_to_be_peak_label","TEST__DET_MIN_TH_TO_BE_PEAK__INPUT"]))
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["det_yz_filtering_size_label","TEST__POST_PROCESSING__YZ_FILTERING_SIZE__DET__INPUT"]))
        self.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["det_z_filtering_size_label","TEST__POST_PROCESSING__Z_FILTERING_SIZE__DET__INPUT"]))
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["det_remove_close_points_radius_label","TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT"]))
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT.currentIndexChanged.connect(lambda: self.condition_db.combobox_hide_visible_action(self, 
            ["det_watershed_first_dilation_label","TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT","det_watershed_donuts_classes_label", 
             "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT", "det_watershed_donuts_patch_label", 
             "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT", "det_watershed_donuts_nucleus_diam_label", 
             "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT", "det_data_watetshed_check_label", 
             "PROBLEM__DETECTION__DATA_CHECK_MW__INPUT"]))
        
        # Run page buttons 
        self.ui.select_yaml_name_label.textChanged.connect(lambda: mark_syntax_error(self, "select_yaml_name_label", ["empty"]))                        
        self.ui.examine_yaml_bn.clicked.connect(lambda: examine(self, "select_yaml_name_label"))
        self.ui.output_folder_bn.clicked.connect(lambda: examine(self, "output_folder_input", False))
        self.ui.output_folder_input.textChanged.connect(lambda: mark_syntax_error(self, "output_folder_input", ["empty"])) 
        self.ui.check_yaml_file_bn.clicked.connect(lambda: load_yaml_config(self, advise_user=True))
        self.ui.run_biapy_docker_bn.clicked.connect(lambda: UIFunction.run_biapy(self))

        self.yes_no = None
        self.diag = None
        self.wokflow_info = None

        self.dragPos = self.pos()
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_empty.mouseMoveEvent = moveWindow
        self.ui.frame_8.mouseMoveEvent = moveWindow
        self.ui.biapy_logo_frame.mouseMoveEvent = moveWindow

    def change_problem_dimensions(self, idx):
        # 2D
        if idx == 0:
            self.ui.DATA__PATCH_SIZE__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__PATCH_SIZE__INPUT.setText("(256,256,1)")
            self.ui.DATA__TRAIN__RESOLUTION__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1)")
            self.ui.DATA__TRAIN__OVERLAP__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0)")
            self.ui.DATA__TRAIN__PADDING__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0)")
            self.ui.DATA__VAL__RESOLUTION__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1)")
            self.ui.DATA__VAL__OVERLAP__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0)")
            self.ui.DATA__VAL__PADDING__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__VAL__PADDING__INPUT.setText("(0,0)")
            self.ui.DATA__TEST__RESOLUTION__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1)")
            self.ui.DATA__TEST__OVERLAP__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0)")
            self.ui.DATA__TEST__PADDING__INPUT.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.DATA__TEST__PADDING__INPUT.setText("(0,0)")
            self.ui.da_z_flip_label.setVisible(False)
            self.ui.AUGMENTOR__ZFLIP__INPUT.setVisible(False)
            self.ui.test_2d_as_3d_stack_label.setVisible(True)
            self.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT.setVisible(True)
            self.ui.test_reduce_memory_label.setVisible(False)
            self.ui.TEST__REDUCE_MEMORY__INPUT.setVisible(False)
            self.ui.TEST__STATS__PER_PATCH__INPUT.setCurrentText("No")
            self.ui.TEST__STATS__MERGE_PATCHES__INPUT.setCurrentText("No")
            self.ui.TEST__STATS__FULL_IMG__INPUT.setCurrentText("Yes") 
            self.ui.test_full_image_label.setVisible(True)
            self.ui.TEST__STATS__FULL_IMG__INPUT.setVisible(True)  
            self.ui.inst_seg_yz_filtering_label.setVisible(True) 
            self.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT.setVisible(True) 
            self.ui.inst_seg_z_filtering_label.setVisible(True) 
            self.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT.setVisible(True) 
            self.ui.sem_seg_yz_filtering_label.setVisible(True) 
            self.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT.setVisible(True) 
            self.ui.sem_seg_z_filtering_label.setVisible(True) 
            self.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT.setVisible(True) 
            self.ui.det_yz_filtering_label.setVisible(True) 
            self.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT.setVisible(True) 
            self.ui.det_z_filtering_label.setVisible(True) 
            self.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT.setVisible(True) 
        # 3D
        else:
            self.ui.DATA__PATCH_SIZE__INPUT.setValidator(self.four_number_parenthesis_validator)
            self.ui.DATA__PATCH_SIZE__INPUT.setText("(40,128,128,1)")
            self.ui.DATA__TRAIN__RESOLUTION__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1,1)")
            self.ui.DATA__TRAIN__OVERLAP__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0,0)")
            self.ui.DATA__TRAIN__PADDING__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0,0)")
            self.ui.DATA__VAL__RESOLUTION__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1,1)")
            self.ui.DATA__VAL__OVERLAP__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0,0)")
            self.ui.DATA__VAL__PADDING__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__VAL__PADDING__INPUT.setText("(0,0,0)")
            self.ui.DATA__TEST__RESOLUTION__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1,1)")
            self.ui.DATA__TEST__OVERLAP__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0,0)")
            self.ui.DATA__TEST__PADDING__INPUT.setValidator(self.three_number_parenthesis_validator)
            self.ui.DATA__TEST__PADDING__INPUT.setText("(0,0,0)")
            self.ui.da_z_flip_label.setVisible(True)
            self.ui.AUGMENTOR__ZFLIP__INPUT.setVisible(True)
            self.ui.test_2d_as_3d_stack_label.setVisible(False)
            self.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT.setVisible(False)
            self.ui.test_reduce_memory_label.setVisible(True)
            self.ui.TEST__REDUCE_MEMORY__INPUT.setVisible(True)
            self.ui.test_full_image_label.setVisible(False)
            self.ui.TEST__STATS__FULL_IMG__INPUT.setVisible(False)
            self.ui.TEST__STATS__PER_PATCH__INPUT.setCurrentText("Yes")
            self.ui.TEST__STATS__MERGE_PATCHES__INPUT.setCurrentText("Yes")
            self.ui.TEST__STATS__FULL_IMG__INPUT.setCurrentText("No") 
            self.ui.inst_seg_yz_filtering_label.setVisible(False) 
            self.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT.setVisible(False) 
            self.ui.inst_seg_z_filtering_label.setVisible(False) 
            self.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT.setVisible(False) 
            self.ui.sem_seg_yz_filtering_label.setVisible(False) 
            self.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT.setVisible(False) 
            self.ui.sem_seg_z_filtering_label.setVisible(False) 
            self.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT.setVisible(False) 
            self.ui.det_yz_filtering_label.setVisible(False) 
            self.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT.setVisible(False) 
            self.ui.det_z_filtering_label.setVisible(False) 
            self.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT.setVisible(False) 

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def dialog_exec(self, message, reason):
        if self.diag is None: 
            self.diag = dialog_Ui(self)

        self.diag.dialog_constrict(message, reason)
        center_window(self.diag, self.geometry())
        self.diag.exec_()

    def workflow_info_exec(self, workflow_name, workflow_images, workflow_description, 
        workflow_doc, workflow_ready_to_use_examples):
        if self.wokflow_info is None: 
            self.wokflow_info = workflow_explanation_Ui()
            
        self.wokflow_info.infoConstrict(workflow_name, workflow_images[0], 
            workflow_images[1], workflow_description, workflow_doc, 
            workflow_ready_to_use_examples)
        center_window(self.wokflow_info, self.geometry())
        self.wokflow_info.exec_()

    def yes_no_exec(self, question):
        if self.yes_no is None: 
            self.yes_no = yes_no_Ui()

        self.yes_no.create_question(question)
        center_window(self.yes_no, self.geometry())
        self.yes_no.exec_()

    def closeEvent(self, event):
        # Find if some window is still running 
        still_running = False
        for x in self.cfg.settings['running_workers']:
            if "run" in x.process_steps: # Means that is running
                still_running = True
                break 

        if still_running:
            self.yes_no_exec("Are you sure you want to exit? All running windows will be stopped")
        else:
            self.yes_no_exec("Are you sure you want to exit?")
        if self.yes_no.answer:
            # Kill all run windows
            for x in self.cfg.settings['running_workers']:
                print("Killing subprocess . . .")
                x.gui.forcing_close = True
                x.gui.close()

            # Finally close the main window    
            self.close()
        else:
            event.ignore()  

def center_window(widget, geometry):
    window = widget.window()
    window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight,
            QtCore.Qt.AlignCenter,
            window.size(),
            geometry,
        ),
    )
        
if __name__ == "__main__":
    window = None
    log_dir = os.path.join(tempfile._get_default_tempdir(), "BiaPy")
    log_file = os.path.join(log_dir, "BiaPy_"+next(tempfile._get_candidate_names())) 
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger('BiaPy')
    logging.basicConfig(filename=log_file, level=logging.ERROR)
    StyleSheet = """ 
        QComboBox {
            selection-background-color: rgb(64,144,253);
        }
        """

    try:
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(resource_path(os.path.join("images","biapy_logo_icon.ico"))))
        app.setStyleSheet(StyleSheet)
        
        # For disabling wheel in combo boxes
        class WheelEventFilter(QtCore.QObject):
            def eventFilter(self, obj, ev):
                if obj.inherits("QComboBox") and ev.type() == QtCore.QEvent.Wheel:
                    return True
                return False
        filter = WheelEventFilter()
        app.installEventFilter(filter)

        window = MainWindow(log_file, log_dir)
        window.show()

        # Center the main GUI in the middle of the first screen
        all_screens = app.screens()
        center_window(window, all_screens[0].availableGeometry())

        app.exec_()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except:
        # Log the error
        logger.exception("Main window error:")
        logger.error(traceback.format_exc())
        
        # Advise the user for the error
        error = dialog_Ui(window) if window is not None else dialog_Ui()
        error.dialog_constrict(log_file, "main_window_error")
        error.exec_()
        
        # Print the error in command line for debugging 
        print("Logging into file: {}".format(log_file))
        traceback.print_exc()

