from __future__ import annotations
import os
import sys
import json
import darkdetect
from platformdirs import user_cache_dir
import logging
import traceback
import qdarktheme
from datetime import datetime
from PySide6.QtCore import Qt, QSize, QRect, QRegularExpression, QObject, QEvent, QUrl
from PySide6.QtGui import (
    QDesktopServices,
    QColor,
    QIcon,
    QPixmap,
    QRegularExpressionValidator,
    QDoubleValidator,
    QIntValidator,
    QCloseEvent,
    QCursor,
)
from PySide6.QtWidgets import (
    QFrame,
    QApplication,
    QStackedWidget,
    QWidget,
    QSplashScreen,
    QPushButton,
    QMainWindow,
    QToolTip,
    QStyle,
    QApplication,
)
from logging import Logger
from typing import (
    List,
    Dict,
)

import ui_function
from ui_utils import (
    examine,
    mark_syntax_error,
    expand_hide_advanced_options,
    change_page,
    get_git_revision_short_hash,
    load_yaml_config,
    resource_path,
    load_yaml_to_GUI,
    set_text,
    start_wizard_questionary,
    change_wizard_page,
    eval_wizard_answer,
    clear_answers,
    check_models_from_other_sources,
    check_data_from_path,
    export_wizard_summary,
    wizard_path_changed,
    save_biapy_config,
)
from settings import Settings
from widget_conditions import Widget_conditions
from ui.ui_main import Ui_MainWindow
from ui.aux_windows import (
    dialog_Ui,
    workflow_explanation_Ui,
    yes_no_Ui,
    spinner_Ui,
    basic_Ui,
    model_card_carrousel_Ui,
    tour_window_Ui,
)

os.environ["QT_MAC_WANTS_LAYER"] = "1"


class MainWindow(QMainWindow):
    def __init__(self, logger: Logger, log_info: Dict, theme: str):
        """
        Main window constructor.

        Parameters
        ----------
        logger : str
            Logger to log the file to log all the information.

        log_info : dict
            Logging information.

        theme : str
            Theme of the GUI.
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.logger = logger
        self.log_info = log_info
        self.cfg = Settings()
        self.theme = theme

        self.workflow_view_queue = None
        self.observer1 = None
        self.observer2 = None
        self.observer3 = None
        self.observer4 = None

        # Adjust font cross-platform
        self.setStyleSheet("QWidget{ font-size:16px;}")
        self.ui.biapy_version.setStyleSheet("QWidget{font-size:10px}")

        # So the error and dialog windows can access it
        global ui
        ui = self
        self.UIFunction = ui_function.UIFunction(self)

        self.setWindowTitle("BiaPy")
        self.UIFunction.initStackTab()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.ui.bn_min.clicked.connect(self.showMinimized)
        self.ui.bn_close.clicked.connect(self.close)

        two_pos_number_regex = QRegularExpression("^\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*$")  # type: ignore
        self.two_pos_number_validator = QRegularExpressionValidator(two_pos_number_regex)

        two_pos_number_parenthesis_regex = QRegularExpression("^\(\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\)$")  # type: ignore
        self.two_pos_number_parenthesis_validator = QRegularExpressionValidator(two_pos_number_parenthesis_regex)
        two_number_parenthesis_regex = QRegularExpression("^\(\s*-?[0-9][0-9]*\s*,\s*-?[0-9][0-9]*\s*\)$")  # type: ignore
        self.two_number_parenthesis_validator = QRegularExpressionValidator(two_number_parenthesis_regex)
        two_pos_0_1_float_number_parenthesis_regex = QRegularExpression("^\(\s*0\.[0-9]*\s*,\s*0\.[0-9]*\s*\)$")  # type: ignore
        self.two_pos_0_1_float_number_parenthesis_validator = QRegularExpressionValidator(
            two_pos_0_1_float_number_parenthesis_regex
        )
        two_0_1_float_number_parenthesis_regex = QRegularExpression("^\(\s*-?0\.[0-9]*\s*,\s*-?0\.[0-9]*\s*\)$")  # type: ignore
        self.two_0_1_float_number_parenthesis_validator = QRegularExpressionValidator(
            two_0_1_float_number_parenthesis_regex
        )
        two_0_2_float_number_parenthesis_regex = QRegularExpression("^\(\s*[0-1]\.[0-9]*\s*,\s*[0-1]\.[0-9]*\s*\)$")  # type: ignore
        self.two_0_2_float_number_parenthesis_validator = QRegularExpressionValidator(
            two_0_2_float_number_parenthesis_regex
        )
        two_pos_float_number_parenthesis_regex = QRegularExpression("^\(\s*[0-9]\.[0-9]*\s*,\s*[0-9]\.[0-9]*\s*\)$")  # type: ignore
        self.two_pos_float_number_parenthesis_validator = QRegularExpressionValidator(
            two_pos_float_number_parenthesis_regex
        )
        three_number_parenthesis_regex = QRegularExpression("^\(\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\)$")  # type: ignore
        self.three_number_parenthesis_validator = QRegularExpressionValidator(three_number_parenthesis_regex)
        four_number_parenthesis_regex = QRegularExpression("^\(\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\)$")  # type: ignore
        self.four_number_parenthesis_validator = QRegularExpressionValidator(four_number_parenthesis_regex)

        two_pos_number_bracket_regex = QRegularExpression("^\[\s*[0-9][0-9]*\s*,\s*[0-9][0-9]*\s*\]$")  # type: ignore
        self.two_pos_number_bracket_validator = QRegularExpressionValidator(two_pos_number_bracket_regex)
        no_limit_number_min_one_number_bracket_regex = QRegularExpression("^\[\s*[0-9][0-9]*\s*(,\s*[0-9][0-9]*\s*)*\]$")  # type: ignore
        self.no_limit_number_min_one_number_bracket_validator = QRegularExpressionValidator(
            no_limit_number_min_one_number_bracket_regex
        )
        no_limit_number_bracket_regex = QRegularExpression("^\[\s*[0-9]*\s*(,\s*[0-9]*\s*)*\]$")  # type: ignore
        self.no_limit_number_bracket_validator = QRegularExpressionValidator(no_limit_number_bracket_regex)
        no_limit_0_1_float_number_bracket_regex = QRegularExpression("^\[\s*0\.[0-9]*\s*(,\s*0\.[0-9]*\s*)*\]$")  # type: ignore
        self.no_limit_0_1_float_number_bracket_validator = QRegularExpressionValidator(
            no_limit_0_1_float_number_bracket_regex
        )
        z_down_bracket_regex = QRegularExpression("^\[\s*[0-2]\s*(,\s*[0-2]\s*)*\]$")  # type: ignore
        self.z_down_bracket_validator = QRegularExpressionValidator(z_down_bracket_regex)

        self.float_validator = QDoubleValidator(0.0, 1.0, 3)
        self.large_range_float_validator = QDoubleValidator(0.0, 10.0, 3)
        self.int_validator = QIntValidator(0, 99999)

        # Left buttons
        self.ui.bn_home.clicked.connect(lambda: change_page(self, "bn_home", 99))
        self.ui.bn_wizard.clicked.connect(lambda: change_page(self, "bn_wizard", 99))
        self.ui.bn_workflow.clicked.connect(lambda: change_page(self, "bn_workflow", 99))
        self.ui.bn_goptions.clicked.connect(lambda: change_page(self, "bn_goptions", 99))
        self.ui.bn_train.clicked.connect(lambda: change_page(self, "bn_train", 99))
        self.ui.bn_test.clicked.connect(lambda: change_page(self, "bn_test", 99))
        self.ui.bn_run_biapy.clicked.connect(lambda: change_page(self, "bn_run_biapy", 99))

        # Home page buttons
        self.ui.create_yaml_bn.clicked.connect(lambda: change_page(self, "bn_workflow", 99))
        self.ui.load_yaml_bn.clicked.connect(lambda: load_yaml_to_GUI(self))
        self.ui.biapy_github_bn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/BiaPyX/BiaPy"))
        )
        self.ui.biapy_forum_bn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://forum.image.sc/tag/biapy"))
        )
        self.ui.biapy_templates_bn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/BiaPyX/BiaPy/tree/master/templates"))
        )
        self.ui.biapy_doc_bn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://biapy.readthedocs.io/en/latest/"))
        )
        self.ui.biapy_notebooks_bn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/BiaPyX/BiaPy/tree/master/notebooks"))
        )
        self.ui.biapy_citation_bn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://www.biorxiv.org/content/10.1101/2024.02.03.576026v2"))
        )
        self.ui.main_window_wizard_question_wizard_icon.clicked.connect(lambda: change_page(self, "bn_wizard", 99))

        # Wizard page buttons
        self.ui.wizard_start_bn.clicked.connect(lambda: start_wizard_questionary(self))
        self.ui.wizard_back_bn.clicked.connect(
            lambda: change_wizard_page(self, self.cfg.settings["wizard_question_index"], False, added_val=-1)
        )
        self.ui.wizard_cont_bn.clicked.connect(
            lambda: change_wizard_page(self, self.cfg.settings["wizard_question_index"], False, added_val=1)
        )
        self.ui.wizard_question_answer.currentIndexChanged.connect(lambda: eval_wizard_answer(self))
        self.ui.wizard_summary_back_bn.clicked.connect(
            lambda: change_wizard_page(self, self.cfg.settings["wizard_question_index"], False, added_val=0)
        )
        self.ui.wizard_summary_back_bn.setIcon(QIcon(resource_path(os.path.join("images", "bn_images", "back.png"))))
        self.ui.wizard_clear_answers_bn.clicked.connect(lambda: clear_answers(self))
        self.ui.wizard_path_input_bn.clicked.connect(lambda: wizard_path_changed(self, "wizard_path_input", False))
        self.allow_change_wizard_question_answer = False
        self.not_allow_change_question = False
        self.ui.wizard_question_wizard_icon.clicked.connect(lambda: self.UIFunction.display_wizard_help_window())
        self.ui.wizard_path_input.textChanged.connect(lambda: eval_wizard_answer(self))
        self.ui.wizard_model_check_bn.clicked.connect(lambda: check_models_from_other_sources(self))
        self.ui.wizard_model_browse_bn.clicked.connect(lambda: examine(self, "wizard_model_input", True))
        self.ui.wizard_path_check.clicked.connect(lambda: check_data_from_path(self))
        self.ui.summary_end_bn.clicked.connect(lambda: export_wizard_summary(self))
        self.ui.wizard_browse_yaml_path_bn.clicked.connect(
            lambda: examine(self, "wizard_browse_yaml_path_input", False)
        )

        # Workflow page buttons
        self.ui.left_arrow_bn.clicked.connect(lambda: self.UIFunction.move_workflow_view(False))
        self.ui.right_arrow_bn.clicked.connect(lambda: self.UIFunction.move_workflow_view(True))
        self.ui.continue_bn.clicked.connect(lambda: change_page(self, "up", -1))
        self.ui.back_bn.clicked.connect(lambda: change_page(self, "down", -1))
        self.ui.back_bn.setIcon(QIcon(resource_path(os.path.join("images", "bn_images", "back.png"))))

        self.ui.window1_bn.clicked.connect(lambda: change_page(self, "bn_workflow", 99))
        self.ui.window2_bn.clicked.connect(lambda: change_page(self, "bn_goptions", 99))
        self.ui.window3_bn.clicked.connect(lambda: change_page(self, "bn_train", 99))
        self.ui.window4_bn.clicked.connect(lambda: change_page(self, "bn_test", 99))

        self.ui.workflow_view1_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(0))
        self.ui.workflow_view2_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(1))
        self.ui.workflow_view3_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(2))
        self.ui.workflow_view4_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(3))
        self.ui.workflow_view5_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(4))
        self.ui.workflow_view6_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(5))
        self.ui.workflow_view7_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(6))
        self.ui.workflow_view8_seemore_bn.clicked.connect(lambda: self.UIFunction.obtain_workflow_description(7))

        # General options page buttons
        self.ui.SYSTEM__SEED__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__SAVE_CKPT_FREQ__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__NDIM__INPUT.currentIndexChanged.connect(
            lambda: self.UIFunction.change_problem_dimensions(self.ui.PROBLEM__NDIM__INPUT.currentIndex())
        )
        self.UIFunction.change_problem_dimensions(0)
        self.ui.goptions_advanced_bn.clicked.connect(
            lambda: expand_hide_advanced_options(self, "goptions_advanced_bn", "goptions_advanced_options_scrollarea")
        )
        self.ui.goptions_browse_yaml_path_bn.clicked.connect(
            lambda: examine(self, "goptions_browse_yaml_path_input", False)
        )
        self.ui.checkpoint_file_path_browse_bn.clicked.connect(lambda: examine(self, "PATHS__CHECKPOINT_FILE__INPUT"))
        self.ui.MODEL__BMZ__SOURCE_MODEL_ID__BN.clicked.connect(
            lambda: check_models_from_other_sources(self, from_wizard=False)
        )
        self.ui.MODEL__BMZ__EXPORT__DOCUMENTATION__BN.clicked.connect(
            lambda: examine(self, "MODEL__BMZ__EXPORT__DOCUMENTATION__INPUT")
        )

        # Train page buttons
        self.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT.setValidator(self.int_validator)
        self.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT.setValidator(self.int_validator)
        self.ui.DATA__VAL__SPLIT_TRAIN__INPUT.setValidator(self.float_validator)
        self.ui.TRAIN__EPOCHS__INPUT.setValidator(self.int_validator)
        self.ui.TRAIN__ACCUM_ITER__INPUT.setValidator(self.int_validator)
        # self.ui.TRAIN__PATIENCE__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__N_CLASSES__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__N_CLASSES__INST_SEG__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__N_CLASSES__DET__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__N_CLASSES__CLS__INPUT.setValidator(self.int_validator)

        # self.ui.DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__INPUT.setValidator(self.float_validator)
        # self.ui.DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__INPUT.setValidator(self.float_validator)
        self.ui.DATA__PREPROCESS__RESIZE__CVAL__INPUT.setValidator(self.float_validator)
        self.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INPUT.setValidator(self.int_validator)
        self.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INPUT.setValidator(self.float_validator)
        self.ui.DATA__PREPROCESS__RESIZE__CVAL__TEST__INPUT.setValidator(self.float_validator)
        self.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INPUT.setValidator(self.int_validator)
        self.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INPUT.setValidator(self.float_validator)
        self.ui.DATA__TRAIN__REPLICATE__INPUT.setValidator(self.int_validator)
        # self.ui.MODEL__FEATURE_MAPS__INPUT.setValidator(self.no_limit_number_min_one_number_bracket_validator)
        # self.ui.MODEL__DROPOUT_VALUES__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.MODEL__KERNEL_SIZE__INPUT.setValidator(self.int_validator)
        # self.ui.MODEL__Z_DOWN__INPUT.setValidator(self.z_down_bracket_validator)
        self.ui.MODEL__VIT_TOKEN_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_EMBED_DIM__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_NUM_LAYERS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_MLP_RATIO__INPUT.setValidator(self.large_range_float_validator)
        self.ui.MODEL__MAE_MASK_RATIO__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__MAE_DEC_HIDDEN_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__MAE_DEC_NUM_LAYERS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__MAE_DEC_NUM_HEADS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__MAE_DEC_MLP_DIMS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__CONVNEXT_SD_PROB__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__CONVNEXT_LAYER_SCALE__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__CONVNEXT_STEM_K_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__VIT_NORM_EPS__INPUT.setValidator(self.float_validator)
        self.ui.MODEL__VIT_NUM_HEADS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__UNETR_VIT_HIDD_MULT__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__UNETR_VIT_NUM_FILTERS__INPUT.setValidator(self.int_validator)
        self.ui.MODEL__UNETR_DEC_KERNEL_SIZE__INPUT.setValidator(self.int_validator)
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
        self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNEL_WEIGHTS__INPUT.setValidator(
            self.two_pos_0_1_float_number_parenthesis_validator
        )
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT.setValidator(self.large_range_float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT.setValidator(self.int_validator)
        self.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT.setValidator(self.no_limit_number_bracket_validator)
        # self.ui.TEST__MATCHING_STATS_THS__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        # self.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT.setValidator(self.float_validator)
        # self.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT.setValidator(self.int_validator)
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT.setValidator(self.int_validator)

        self.ui.TEST__DET_MIN_TH_TO_BE_PEAK__INPUT.setValidator(self.float_validator)
        self.ui.TEST__DET_BLOB_LOG_MIN_SIGMA__INPUT.setValidator(self.int_validator)
        self.ui.TEST__DET_BLOB_LOG_MAX_SIGMA__INPUT.setValidator(self.int_validator)
        self.ui.TEST__DET_BLOB_LOG_NUM_SIGMA__INPUT.setValidator(self.int_validator)
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT.setValidator(self.int_validator)
        # self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT.setValidator(self.no_limit_number_bracket_validator)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT.setValidator(
            self.no_limit_number_bracket_validator
        )
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT.setValidator(self.int_validator)
        self.ui.TEST__DET_TOLERANCE__INPUT.setValidator(self.int_validator)
        self.ui.TEST__BY_CHUNKS__FLUSH_EACH__INPUT.setValidator(self.int_validator)

        self.ui.PROBLEM__DENOISING__N2V_PERC_PIX__INPUT.setValidator(self.float_validator)
        self.ui.PROBLEM__DENOISING__N2V_NEIGHBORHOOD_RADIUS__INPUT.setValidator(self.int_validator)

        self.condition_db = Widget_conditions()

        self.ui.LOAD_PRETRAINED_MODEL__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "MODEL__SOURCE__LABEL",
                    "MODEL__SOURCE__INFO",
                    "MODEL__SOURCE__INPUT",
                    "checkpoint_file_path_browse_label",
                    "PATHS__CHECKPOINT_FILE__INFO",
                    "PATHS__CHECKPOINT_FILE__INPUT",
                    "checkpoint_file_path_browse_bn",
                    "checkpoint_loading_opt_label",
                    "checkpoint_loading_opt_frame",
                    "MODEL__BMZ__SOURCE_MODEL_ID__LABEL",
                    "MODEL__BMZ__SOURCE_MODEL_ID__INFO",
                    "MODEL__BMZ__SOURCE_MODEL_ID__INPUT",
                    "MODEL__BMZ__SOURCE_MODEL_ID__BN",
                    "MODEL__ARCHITECTURE__LABEL",
                    "MODEL__ARCHITECTURE__INFO",
                    "MODEL__ARCHITECTURE__INPUT",
                    "unet_model_like_frame",
                    "unet_model_like_label",
                    "transformers_frame",
                    "transformers_label",
                    "convnext_label",
                    "convnext_frame",
                ],
                widgets_to_set_cond=[(["MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__INPUT", "No"], ["No"])],
                updated_widget="LOAD_PRETRAINED_MODEL__INPUT",
            )
        )

        self.ui.MODEL__SOURCE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "checkpoint_file_path_browse_label",
                    "PATHS__CHECKPOINT_FILE__INFO",
                    "PATHS__CHECKPOINT_FILE__INPUT",
                    "checkpoint_file_path_browse_bn",
                    "checkpoint_loading_opt_label",
                    "checkpoint_loading_opt_frame",
                    "MODEL__BMZ__SOURCE_MODEL_ID__LABEL",
                    "MODEL__BMZ__SOURCE_MODEL_ID__INFO",
                    "MODEL__BMZ__SOURCE_MODEL_ID__INPUT",
                    "MODEL__BMZ__SOURCE_MODEL_ID__BN",
                    "MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__FRAME",
                ],
                widgets_to_set_cond=[
                    (["MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__INPUT", "No"], ["I have a model trained with BiaPy"])
                ],
                updated_widget="MODEL__SOURCE__INPUT",
            )
        )

        self.ui.MODEL__BMZ__EXPORT__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__FRAME",
                    "MODEL__BMZ__EXPORT__FRAME",
                    "MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__FRAME",
                ],
            )
        )
        self.ui.MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["MODEL__BMZ__EXPORT__FRAME"])
        )
        self.ui.MODEL_AUTOGENERATE_DOC_INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "MODEL__BMZ__EXPORT__DOCUMENTATION__LABEL",
                    "MODEL__BMZ__EXPORT__DOCUMENTATION__INFO",
                    "MODEL__BMZ__EXPORT__DOCUMENTATION__INPUT",
                    "MODEL__BMZ__EXPORT__DOCUMENTATION__BN",
                ],
            )
        )

        self.ui.job_name_input.textChanged.connect(lambda: mark_syntax_error(self, "job_name_input", ["empty"]))
        self.ui.goptions_yaml_name_input.textChanged.connect(
            lambda: mark_syntax_error(self, "goptions_yaml_name_input", ["empty"])
        )
        self.ui.goptions_browse_yaml_path_input.textChanged.connect(
            lambda: mark_syntax_error(self, "goptions_browse_yaml_path_input", ["empty"])
        )
        self.ui.TRAIN__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["train_tab_widget"])
        )
        self.ui.train_data_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TRAIN__PATH__INPUT", False))
        self.ui.train_data_gt_input_browse_bn.clicked.connect(
            lambda: examine(self, "DATA__TRAIN__GT_PATH__INPUT", False)
        )
        self.ui.val_data_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__VAL__PATH__INPUT", False))
        self.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__BN.clicked.connect(
            lambda: examine(self, "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INPUT", False)
        )
        self.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__BN.clicked.connect(
            lambda: examine(self, "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INPUT", False)
        )
        self.ui.val_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__VAL__GT_PATH__INPUT", False))
        self.ui.DATA__VAL__TYPE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "percentage_validation_label",
                    "percentage_validation_info",
                    "DATA__VAL__SPLIT_TRAIN__INPUT",
                    "cross_validation_nfolds_label",
                    "cross_validation_nfolds_info",
                    "DATA__VAL__CROSS_VAL_NFOLD__INPUT",
                    "cross_validation_fold_label",
                    "cross_validation_fold_info",
                    "DATA__VAL__CROSS_VAL_FOLD__INPUT",
                    "DATA__VAL__PATH__LABEL",
                    "DATA__VAL__PATH__INFO",
                    "DATA__VAL__PATH__INPUT",
                    "val_data_input_browse_bn",
                    "validation_data_gt_label",
                    "validation_data_gt_info",
                    "DATA__VAL__GT_PATH__INPUT",
                    "val_data_gt_input_browse_bn",
                    "random_val_label",
                    "DATA__VAL__RANDOM__INPUT",
                    "DATA__VAL__RANDOM__INFO",
                    "validation_overlap_label",
                    "DATA__VAL__OVERLAP__INFO",
                    "DATA__VAL__OVERLAP__INPUT",
                    "validation_padding_label",
                    "DATA__VAL__PADDING__INFO",
                    "DATA__VAL__PADDING__INPUT",
                ],
            )
        )
        self.ui.train_advanced_bn.clicked.connect(
            lambda: expand_hide_advanced_options(self, "train_advanced_bn", "train_advanced_options_frame")
        )
        self.ui.MODEL__ARCHITECTURE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "unet_model_like_frame",
                    "unet_model_like_label",
                    "sr_unet_like_heading",
                    "sr_unet_like_frame",
                    "transformers_frame",
                    "transformers_label",
                    "unetr_vit_hidden_multiple_label",
                    "MODEL__UNETR_VIT_HIDD_MULT__INFO",
                    "MODEL__UNETR_VIT_HIDD_MULT__INPUT",
                    "unetr_num_filters_label",
                    "MODEL__UNETR_VIT_NUM_FILTERS__INFO",
                    "MODEL__UNETR_VIT_NUM_FILTERS__INPUT",
                    "unetr_dec_act_label",
                    "MODEL__UNETR_DEC_ACTIVATION__INFO",
                    "MODEL__UNETR_DEC_ACTIVATION__INPUT",
                    "MODEL__UNETR_DEC_KERNEL_SIZE__LABEL",
                    "MODEL__UNETR_DEC_KERNEL_SIZE__INFO",
                    "MODEL__UNETR_DEC_KERNEL_SIZE__INPUT",
                    "MODEL__MAE_MASK_TYPE__LABEL",
                    "MODEL__MAE_MASK_TYPE__INFO",
                    "MODEL__MAE_MASK_TYPE__INPUT",
                    "MODEL__MAE_MASK_RATIO__INPUT",
                    "MODEL__MAE_MASK_RATIO__LABEL",
                    "MODEL__MAE_MASK_RATIO__INFO",
                    "MODEL__MAE_DEC_HIDDEN_SIZE__INPUT",
                    "MODEL__MAE_DEC_HIDDEN_SIZE__LABEL",
                    "MODEL__MAE_DEC_HIDDEN_SIZE__INFO",
                    "MODEL__MAE_DEC_NUM_LAYERS__INPUT",
                    "MODEL__MAE_DEC_NUM_LAYERS__LABEL",
                    "MODEL__MAE_DEC_NUM_LAYERS__INFO",
                    "MODEL__MAE_DEC_NUM_HEADS__INPUT",
                    "MODEL__MAE_DEC_NUM_HEADS__LABEL",
                    "MODEL__MAE_DEC_NUM_HEADS__INFO",
                    "MODEL__MAE_DEC_MLP_DIMS__INPUT",
                    "MODEL__MAE_DEC_MLP_DIMS__INFO",
                    "MODEL__MAE_DEC_MLP_DIMS__LABEL",
                    "convnext_label",
                    "convnext_frame",
                ],
                widgets_to_set_cond=[
                    (["PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT", "masking"], ["MAE"]),
                    (
                        ["PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT", "crappify"],
                        ["U-Net", "Residual U-Net", "ResUNet++", "Attention U-Net", "MultiResUnet", "SEUnet", "UNETR"],
                    ),
                ],
                updated_widget="MODEL__ARCHITECTURE__INPUT",
            )
        )
        self.ui.TRAIN__OPTIMIZER__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TRAIN__W_DECAY__INPUT",
                    "adamw_weight_decay_label",
                    "TRAIN__W_DECAY__INFO",
                    "TRAIN__OPT_BETAS__INPUT",
                    "TRAIN__OPT_BETAS__LABEL",
                    "TRAIN__OPT_BETAS__INFO",
                ],
            )
        )
        self.ui.TRAIN__BATCH_SIZE__CALCULATION__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["TRAIN__BATCH_SIZE__LABEL", "TRAIN__BATCH_SIZE__INFO", "TRAIN__BATCH_SIZE__INPUT"]
            )
        )
        self.ui.TRAIN__PROFILER__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "profiler_batch_range_label",
                    "TRAIN__PROFILER_BATCH_RANGE__INPUT",
                    "TRAIN__PROFILER_BATCH_RANGE__INFO",
                ],
            )
        )
        self.ui.DATA__NORMALIZATION__PERC_CLIP__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__NORMALIZATION__PERC_LOWER__LABEL",
                    "DATA__NORMALIZATION__PERC_LOWER__INFO",
                    "DATA__NORMALIZATION__PERC_CLIP__LOWER_PERC__INPUT",
                    "DATA__NORMALIZATION__PERC_UPPER__LABEL",
                    "DATA__NORMALIZATION__PERC_UPPER__INFO",
                    "DATA__NORMALIZATION__PERC_CLIP__UPPER_PERC__INPUT",
                ],
            )
        )
        self.ui.DATA__NORMALIZATION__TYPE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__LABEL",
                    "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__INPUT",
                    "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__MEAN_VAL__INFO",
                    "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__LABEL",
                    "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__INPUT",
                    "DATA__NORMALIZATION__ZERO_MEAN_UNIT_VAR__STD_VAL__INFO",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__TRAIN__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["preprocessing_frame"])
        )
        self.ui.DATA__PREPROCESS__VAL__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["preprocessing_frame"])
        )
        self.ui.DATA__PREPROCESS__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["preprocessing_test_frame"])
        )
        self.ui.DATA__PREPROCESS__RESIZE__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__LABEL",
                    "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INFO",
                    "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT",
                    "DATA__PREPROCESS__RESIZE__ORDER__LABEL",
                    "DATA__PREPROCESS__RESIZE__ORDER__INFO",
                    "DATA__PREPROCESS__RESIZE__ORDER__INPUT",
                    "DATA__PREPROCESS__RESIZE__MODE__LABEL",
                    "DATA__PREPROCESS__RESIZE__MODE__INFO",
                    "DATA__PREPROCESS__RESIZE__MODE__INPUT",
                    "DATA__PREPROCESS__RESIZE__CVAL__LABEL",
                    "DATA__PREPROCESS__RESIZE__CVAL__INFO",
                    "DATA__PREPROCESS__RESIZE__CVAL__INPUT",
                    "DATA__PREPROCESS__RESIZE__CLIP__LABEL",
                    "DATA__PREPROCESS__RESIZE__CLIP__INFO",
                    "DATA__PREPROCESS__RESIZE__CLIP__INPUT",
                    "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__LABEL",
                    "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INFO",
                    "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INPUT",
                    "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__LABEL",
                    "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INFO",
                    "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__LABEL",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INFO",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INPUT",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__LABEL",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INFO",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INPUT",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__LABEL",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INFO",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__LABEL",
                    "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INFO",
                    "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__LABEL",
                    "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INFO",
                    "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__LABEL",
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INFO",
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INPUT",
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__BN",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__CLAHE__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__LABEL",
                    "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INFO",
                    "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INPUT",
                    "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__LABEL",
                    "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INFO",
                    "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__CANNY__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__LABEL",
                    "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INFO",
                    "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INPUT",
                    "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__LABEL",
                    "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INFO",
                    "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT",
                    "DATA__PREPROCESS__RESIZE__ORDER__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__ORDER__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__ORDER__TEST__INPUT",
                    "DATA__PREPROCESS__RESIZE__MODE__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__MODE__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__MODE__TEST__INPUT",
                    "DATA__PREPROCESS__RESIZE__CVAL__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__CVAL__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__CVAL__TEST__INPUT",
                    "DATA__PREPROCESS__RESIZE__CLIP__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__CLIP__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__CLIP__TEST__INPUT",
                    "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INPUT",
                    "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__LABEL",
                    "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INFO",
                    "DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__LABEL",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INFO",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INPUT",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__LABEL",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INFO",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INPUT",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__LABEL",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INFO",
                    "DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__LABEL",
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INFO",
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INPUT",
                    "DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__BN",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__LABEL",
                    "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INFO",
                    "DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INPUT",
                    "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__LABEL",
                    "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INFO",
                    "DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INPUT",
                ],
            )
        )
        self.ui.DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__LABEL",
                    "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INFO",
                    "DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INPUT",
                    "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__LABEL",
                    "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INFO",
                    "DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INPUT",
                ],
            )
        )
        self.ui.TEST__AUGMENTATION__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                ["TEST__AUGMENTATION_MODE__LABEL", "TEST__AUGMENTATION_MODE__INFO", "TEST__AUGMENTATION_MODE__INPUT"],
            )
        )
        self.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL",
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO",
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT",
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL",
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO",
                    "DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT",
                ],
            )
        )
        self.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL",
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO",
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT",
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL",
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO",
                    "DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT",
                ],
            )
        )

        self.ui.DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__TRAIN__FILTER_SAMPLES__PROPS__LABEL",
                    "DATA__TRAIN__FILTER_SAMPLES__PROPS__INFO",
                    "DATA__TRAIN__FILTER_SAMPLES__PROPS__INPUT",
                    "DATA__TRAIN__FILTER_SAMPLES__VALUES__LABEL",
                    "DATA__TRAIN__FILTER_SAMPLES__VALUES__INFO",
                    "DATA__TRAIN__FILTER_SAMPLES__VALUES__INPUT",
                    "DATA__TRAIN__FILTER_SAMPLES__SIGNS__LABEL",
                    "DATA__TRAIN__FILTER_SAMPLES__SIGNS__INFO",
                    "DATA__TRAIN__FILTER_SAMPLES__SIGNS__INPUT",
                    "DATA__TRAIN__FILTER_SAMPLES__NORM_BEFORE__LABEL",
                    "DATA__TRAIN__FILTER_SAMPLES__NORM_BEFORE__INFO",
                    "DATA__TRAIN__FILTER_SAMPLES__NORM_BEFORE__INPUT",
                ],
            )
        )

        self.ui.DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__VAL__FILTER_SAMPLES__PROPS__LABEL",
                    "DATA__VAL__FILTER_SAMPLES__PROPS__INFO",
                    "DATA__VAL__FILTER_SAMPLES__PROPS__INPUT",
                    "DATA__VAL__FILTER_SAMPLES__VALUES__LABEL",
                    "DATA__VAL__FILTER_SAMPLES__VALUES__INFO",
                    "DATA__VAL__FILTER_SAMPLES__VALUES__INPUT",
                    "DATA__VAL__FILTER_SAMPLES__SIGNS__LABEL",
                    "DATA__VAL__FILTER_SAMPLES__SIGNS__INFO",
                    "DATA__VAL__FILTER_SAMPLES__SIGNS__INPUT",
                    "DATA__VAL__FILTER_SAMPLES__NORM_BEFORE__LABEL",
                    "DATA__VAL__FILTER_SAMPLES__NORM_BEFORE__INFO",
                    "DATA__VAL__FILTER_SAMPLES__NORM_BEFORE__INPUT",
                ],
            )
        )

        self.ui.DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__TEST__FILTER_SAMPLES__PROPS__LABEL",
                    "DATA__TEST__FILTER_SAMPLES__PROPS__INFO",
                    "DATA__TEST__FILTER_SAMPLES__PROPS__INPUT",
                    "DATA__TEST__FILTER_SAMPLES__VALUES__LABEL",
                    "DATA__TEST__FILTER_SAMPLES__VALUES__INFO",
                    "DATA__TEST__FILTER_SAMPLES__VALUES__INPUT",
                    "DATA__TEST__FILTER_SAMPLES__SIGNS__LABEL",
                    "DATA__TEST__FILTER_SAMPLES__SIGNS__INFO",
                    "DATA__TEST__FILTER_SAMPLES__SIGNS__INPUT",
                    "DATA__TEST__FILTER_SAMPLES__NORM_BEFORE__LABEL",
                    "DATA__TEST__FILTER_SAMPLES__NORM_BEFORE__INFO",
                    "DATA__TEST__FILTER_SAMPLES__NORM_BEFORE__INPUT",
                ],
            )
        )

        self.ui.MODEL__MAE_MASK_TYPE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["MODEL__MAE_MASK_RATIO__LABEL", "MODEL__MAE_MASK_RATIO__INFO", "MODEL__MAE_MASK_RATIO__INPUT"]
            )
        )

        self.ui.DATA__EXTRACT_RANDOM_PATCH__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["extract_random_patch_frame_label", "extract_random_patch_frame"]
            )
        )
        self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "lr_schel_warmupcosine_epochs_label",
                    "TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT",
                    "TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INFO",
                    "lr_schel_min_lr_label",
                    "TRAIN__LR_SCHEDULER__MIN_LR__INPUT",
                    "TRAIN__LR_SCHEDULER__MIN_LR__INFO",
                    "lr_schel_reduce_on_plat_patience_label",
                    "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT",
                    "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INFO",
                    "lr_schel_reduce_on_plat_factor_label",
                    "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT",
                    "TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INFO",
                ],
            )
        )
        self.ui.AUTOMATIC__AUG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["AUGMENTOR__ENABLE__INPUT", "AUGMENTOR__ENABLE__INFO", "AUGMENTOR__ENABLE__LABEL", "da_frame"]
            )
        )
        self.ui.AUGMENTOR__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["da_frame"])
        )
        self.ui.AUGMENTOR__RANDOM_ROT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_random_rot_range_label",
                    "AUGMENTOR__RANDOM_ROT_RANGE__INPUT",
                    "AUGMENTOR__RANDOM_ROT_RANGE__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__SHEAR__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_shear_range_label", "AUGMENTOR__SHEAR_RANGE__INPUT", "AUGMENTOR__SHEAR_RANGE__INFO"]
            )
        )
        self.ui.AUGMENTOR__ZOOM__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_zoom_range_label",
                    "AUGMENTOR__ZOOM_RANGE__INPUT",
                    "AUGMENTOR__ZOOM_RANGE__INFO",
                    "da_zoom_in_z_label",
                    "AUGMENTOR__ZOOM_IN_Z__INFO",
                    "AUGMENTOR__ZOOM_IN_Z__INPUT",
                ],
            )
        )
        self.ui.AUGMENTOR__SHIFT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_shift_range_label", "AUGMENTOR__SHIFT_RANGE__INPUT", "AUGMENTOR__SHIFT_RANGE__INFO"]
            )
        )
        self.ui.AUGMENTOR__ELASTIC__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_elastic_alpha_label",
                    "AUGMENTOR__E_ALPHA__INPUT",
                    "AUGMENTOR__E_ALPHA__INFO",
                    "da_elastic_sigma_label",
                    "AUGMENTOR__E_SIGMA__INPUT",
                    "da_elastic_mode_label",
                    "AUGMENTOR__E_MODE__INPUT",
                    "AUGMENTOR__E_MODE__INFO",
                    "AUGMENTOR__E_SIGMA__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__G_BLUR__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_gaussian_sigma_label", "AUGMENTOR__G_SIGMA__INPUT", "AUGMENTOR__G_SIGMA__INFO"]
            )
        )
        self.ui.AUGMENTOR__MEDIAN_BLUR__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_median_blur_k_size_label", "AUGMENTOR__MB_KERNEL__INPUT"]
            )
        )
        self.ui.AUGMENTOR__MOTION_BLUR__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_motion_blur_k_size_label", "AUGMENTOR__MOTB_K_RANGE__INPUT", "AUGMENTOR__MOTB_K_RANGE__INFO"]
            )
        )
        self.ui.AUGMENTOR__GAMMA_CONTRAST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_gamma_contrast_range_label", "AUGMENTOR__GC_GAMMA__INPUT", "AUGMENTOR__GC_GAMMA__INFO"]
            )
        )
        self.ui.AUGMENTOR__BRIGHTNESS__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_brightness_factor_range_label",
                    "AUGMENTOR__BRIGHTNESS_FACTOR__INPUT",
                    "AUGMENTOR__BRIGHTNESS_FACTOR__INFO",
                    "da_brightness_mode_label",
                    "AUGMENTOR__BRIGHTNESS_MODE__INPUT",
                    "AUGMENTOR__BRIGHTNESS_MODE__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__CONTRAST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_contrast_factor_range_label",
                    "AUGMENTOR__CONTRAST_FACTOR__INPUT",
                    "da_contrast_mode_label",
                    "AUGMENTOR__CONTRAST_FACTOR__INFO",
                    "AUGMENTOR__CONTRAST_MODE__INPUT",
                    "AUGMENTOR__CONTRAST_MODE__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__DROPOUT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_dropout_range_label", "AUGMENTOR__DROP_RANGE__INPUT", "AUGMENTOR__DROP_RANGE__INFO"]
            )
        )
        self.ui.AUGMENTOR__CUTOUT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_cutout_number_iterations_label",
                    "AUGMENTOR__COUT_NB_ITERATIONS__INPUT",
                    "AUGMENTOR__COUT_NB_ITERATIONS__INFO",
                    "da_cutout_size_label",
                    "AUGMENTOR__COUT_SIZE__INPUT",
                    "AUGMENTOR__COUT_SIZE__INFO",
                    "da_cuout_cval_label",
                    "AUGMENTOR__COUT_CVAL__INPUT",
                    "AUGMENTOR__COUT_CVAL__INFO",
                    "da_cutout_to_mask_label",
                    "AUGMENTOR__COUT_APPLY_TO_MASK__INFO",
                    "AUGMENTOR__COUT_APPLY_TO_MASK__INPUT",
                ],
            )
        )
        self.ui.AUGMENTOR__CUTBLUR__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_cutblur_size_range_label",
                    "AUGMENTOR__CBLUR_SIZE__INPUT",
                    "AUGMENTOR__CBLUR_SIZE__INFO",
                    "da_cutblut_down_range_label",
                    "AUGMENTOR__CBLUR_DOWN_RANGE__INPUT",
                    "AUGMENTOR__CBLUR_DOWN_RANGE__INFO",
                    "da_cutblur_inside_label",
                    "AUGMENTOR__CBLUR_INSIDE__INPUT",
                    "AUGMENTOR__CBLUR_INSIDE__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__CUTMIX__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_cutmix_size_range_label", "AUGMENTOR__CMIX_SIZE__INPUT", "AUGMENTOR__CMIX_SIZE__INFO"]
            )
        )
        self.ui.AUGMENTOR__CUTNOISE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_cutnoise_scale_range_label",
                    "AUGMENTOR__CNOISE_SCALE__INPUT",
                    "AUGMENTOR__CNOISE_SCALE__INFO",
                    "da_cutnoise_number_iter_label",
                    "AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT",
                    "AUGMENTOR__CNOISE_NB_ITERATIONS__INFO",
                    "da_cutnoise_size_range_label",
                    "AUGMENTOR__CNOISE_SIZE__INPUT",
                    "AUGMENTOR__CNOISE_SIZE__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__MISALIGNMENT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_misaligment_displacement_label",
                    "AUGMENTOR__MS_DISPLACEMENT__INPUT",
                    "AUGMENTOR__MS_DISPLACEMENT__INFO",
                    "da_misaligment_rotate_ratio_label",
                    "AUGMENTOR__MS_ROTATE_RATIO__INFO",
                    "AUGMENTOR__MS_ROTATE_RATIO__INPUT",
                ],
            )
        )
        self.ui.AUGMENTOR__MISSING_SECTIONS__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_missing_sections_iteration_range_label",
                    "AUGMENTOR__MISSP_ITERATIONS__INPUT",
                    "AUGMENTOR__MISSP_ITERATIONS__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__GRIDMASK__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_grid_ratio_label",
                    "AUGMENTOR__GRID_RATIO__INPUT",
                    "AUGMENTOR__GRID_RATIO__INFO",
                    "da_grid_d_range_label",
                    "AUGMENTOR__GRID_D_RANGE__INPUT",
                    "AUGMENTOR__GRID_D_RANGE__INFO",
                    "da_grid_rotate_label",
                    "AUGMENTOR__GRID_ROTATE__INPUT",
                    "AUGMENTOR__GRID_ROTATE__INFO",
                    "da_grid_invert_label",
                    "AUGMENTOR__GRID_INVERT__INPUT",
                    "AUGMENTOR__GRID_INVERT__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__GAUSSIAN_NOISE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_gaussian_noise_mean_label",
                    "AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT",
                    "AUGMENTOR__GAUSSIAN_NOISE_MEAN__INFO",
                    "da_gaussian_noise_var_label",
                    "AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT",
                    "AUGMENTOR__GAUSSIAN_NOISE_VAR__INFO",
                    "da_gaussian_noise_use_input_img_label",
                    "AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT",
                    "AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INFO",
                ],
            )
        )
        self.ui.AUGMENTOR__SALT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_salt_amount_label", "AUGMENTOR__SALT_AMOUNT__INPUT", "AUGMENTOR__SALT_AMOUNT__INFO"]
            )
        )
        self.ui.AUGMENTOR__PEPPER__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["da_pepper_amount_label", "AUGMENTOR__PEPPER_AMOUNT__INPUT", "AUGMENTOR__PEPPER_AMOUNT__INFO"]
            )
        )
        self.ui.AUGMENTOR__SALT_AND_PEPPER__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "da_salt_pepper_amount_label",
                    "AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT",
                    "AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INFO",
                    "da_salt_pepper_prop_label",
                    "AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT",
                    "AUGMENTOR__SALT_AND_PEPPER_PROP__INFO",
                ],
            )
        )
        self.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "ssl_resizing_factor_label",
                    "PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INPUT",
                    "PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INFO",
                    "ssl_noise_label",
                    "PROBLEM__SELF_SUPERVISED__NOISE__INPUT",
                    "PROBLEM__SELF_SUPERVISED__NOISE__INFO",
                ],
                widgets_to_set_cond=[
                    (["MODEL__ARCHITECTURE__INPUT", "Attention U-Net"], ["crappify"]),
                    (["MODEL__ARCHITECTURE__INPUT", "MAE"], ["masking"]),
                ],
                updated_widget="PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT",
            )
        )

        # Test page buttons
        self.ui.TEST__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(self, ["test_tab_widget"])
        )
        self.ui.test_data_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TEST__PATH__INPUT", False))
        self.ui.test_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "DATA__TEST__GT_PATH__INPUT", False))
        self.ui.DATA__TEST__LOAD_GT__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_metrics_label",
                    "inst_seg_metrics_frame",
                    "det_metrics_label",
                    "det_metrics_frame",
                    "test_data_gt_label",
                    "DATA__TEST__GT_PATH__INPUT",
                    "DATA__TEST__GT_PATH__INFO",
                    "test_data_gt_input_browse_bn",
                ],
            )
        )
        self.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "test_data_label",
                    "DATA__TEST__PATH__INPUT",
                    "test_data_input_browse_bn",
                    "DATA__TEST__PATH__INFO",
                    "test_exists_gt_label",
                    "DATA__TEST__LOAD_GT__INPUT",
                    "DATA__TEST__LOAD_GT__INFO",
                    "test_data_gt_label",
                    "DATA__TEST__GT_PATH__INPUT",
                    "DATA__TEST__GT_PATH__INFO",
                    "test_data_gt_input_browse_bn",
                    "validation_overlap_label",
                ],
            )
        )
        self.ui.test_advanced_bn.clicked.connect(
            lambda: expand_hide_advanced_options(self, "test_advanced_bn", "test_advanced_options_frame")
        )
        self.ui.TEST__BY_CHUNKS__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["process_by_chunks_label", "process_by_chunks_frame"]
            )
        )
        self.ui.DATA__TEST__INPUT_ZARR_MULTIPLE_DATA__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__LABEL",
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INFO",
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT",
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__LABEL",
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INFO",
                    "DATA__TEST__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT",
                ],
            )
        )
        self.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__LABEL",
                    "TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INPUT",
                    "TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INFO",
                ],
            )
        )
        self.ui.TRAIN__ENABLE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self, ["DATA__PATCH_SIZE__TEST__LABEL", "DATA__PATCH_SIZE__TEST__INFO", "DATA__PATCH_SIZE__TEST__INPUT"]
            )
        )

        self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_b_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INFO",
                    "inst_seg_c_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INFO",
                    "inst_seg_d_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INFO",
                    "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__LABEL",
                    "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INFO",
                    "inst_seg_p_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INFO",
                    "inst_seg_repare_large_blobs_label",
                    "TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT",
                    "TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INFO",
                    "inst_seg_remove_close_points_label",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INFO",
                    "inst_seg_remove_close_points_radius_label",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INFO",
                    "inst_seg_fore_mask_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INFO",
                    "inst_seg_voronoi_label",
                    "TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT",
                    "TEST__POST_PROCESSING__VORONOI_ON_MASK__INFO",
                    "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__LABEL",
                    "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INFO",
                    "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT",
                ],
                frames_to_hide_if_empty=["inst_seg_ths_frame"],
            )
        )
        self.ui.PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_fore_dil_label",
                    "PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT",
                    "PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INFO",
                    "inst_seg_fore_ero_label",
                    "PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT",
                    "PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INFO",
                ],
            )
        )
        self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_small_obj_fil_before_size_label",
                    "PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INFO",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_remove_close_points_radius_label",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INFO",
                ],
            )
        )
        self.ui.TEST__MATCHING_STATS__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_matching_stats_ths_label",
                    "TEST__MATCHING_STATS_THS__INPUT",
                    "TEST__MATCHING_STATS_THS__INFO",
                    "inst_seg_matching_stats_colores_img_ths_label",
                    "TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT",
                    "TEST__MATCHING_STATS_THS_COLORED_IMG__INFO",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_voronoi_mask_th_label",
                    "TEST__POST_PROCESSING__VORONOI_TH__INPUT",
                    "TEST__POST_PROCESSING__VORONOI_TH__INFO",
                ],
            )
        )
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "inst_seg_b_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INFO",
                    "inst_seg_c_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INFO",
                    "inst_seg_p_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INFO",
                    "inst_seg_d_channel_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT",
                    "PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT",
                    "inst_seg_fore_mask_th_label",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT",
                    "PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INFO",
                ],
                frames_to_hide_if_empty=["inst_seg_ths_frame"],
            )
        )

        self.ui.TEST__DET_POINT_CREATION_FUNCTION__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__DET_BLOB_LOG_MIN_SIGMA__LABEL",
                    "TEST__DET_BLOB_LOG_MIN_SIGMA__INPUT",
                    "TEST__DET_BLOB_LOG_MIN_SIGMA__INFO",
                    "TEST__DET_BLOB_LOG_MAX_SIGMA__LABEL",
                    "TEST__DET_BLOB_LOG_MAX_SIGMA__INPUT",
                    "TEST__DET_BLOB_LOG_MAX_SIGMA__INFO",
                    "TEST__DET_BLOB_LOG_NUM_SIGMA__LABEL",
                    "TEST__DET_BLOB_LOG_NUM_SIGMA__INPUT",
                    "TEST__DET_BLOB_LOG_NUM_SIGMA__INFO",
                    "TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__LABEL",
                    "TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__INFO",
                    "TEST__DET_PEAK_LOCAL_MAX_MIN_DISTANCE__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INFO",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INFO",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INPUT",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__LABEL",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INFO",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INFO",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INPUT",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__LABEL",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INFO",
                    "TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INPUT",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "det_remove_close_points_radius_label",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT",
                    "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INFO",
                ],
            )
        )
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT.currentIndexChanged.connect(
            lambda: self.condition_db.combobox_hide_visible_action(
                self,
                [
                    "det_watershed_first_dilation_label",
                    "TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT",
                    "TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INFO",
                    "det_watershed_donuts_classes_label",
                    "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT",
                    "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INFO",
                    "det_watershed_donuts_patch_label",
                    "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT",
                    "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INFO",
                    "det_watershed_donuts_nucleus_diam_label",
                    "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT",
                    "TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INFO",
                    "det_data_watetshed_check_label",
                    "PROBLEM__DETECTION__DATA_CHECK_MW__INPUT",
                    "PROBLEM__DETECTION__DATA_CHECK_MW__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INPUT",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__LABEL",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INFO",
                    "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INPUT",
                ],
            )
        )

        # Info icons
        info_icon = QIcon(self.cfg.settings["info_image"])
        info_icon_clicked = self.cfg.settings["info_image_clicked"]

        def inspect_all_widgets(main_widget):
            for widget in main_widget.children():
                if isinstance(widget, QPushButton):
                    if "_info" in widget.objectName().lower():
                        # Set info icon
                        widget.setIcon(info_icon)
                        widget.setIconSize(QSize(30, 30))
                        # Set instant tooltip
                        widget.clicked.connect(lambda checked, a=widget.objectName(): self.showInstantToolTip(a))
                        widget.setStyleSheet(
                            "QPushButton {\n"
                            "  border-radius: 5px;\n"
                            "  border: none;\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "    border: 1px solid rgb(110, 110, 110);\n"
                            "}"
                            "QPushButton:pressed {\n"
                            f"   icon: url({info_icon_clicked});\n"
                            f"   icon-size: 30px;\n"
                            "}"
                        )

                if isinstance(widget, QFrame) or isinstance(widget, QStackedWidget) or isinstance(widget, QWidget):
                    inspect_all_widgets(widget)

        inspect_all_widgets(self.ui.page_create_yaml)
        inspect_all_widgets(self.ui.page_run_biapy)
        inspect_all_widgets(self.ui.wizard_start_page_paths_frame)

        # Run page buttons
        self.ui.select_yaml_name_label.textChanged.connect(
            lambda: mark_syntax_error(self, "select_yaml_name_label", ["empty"])
        )
        self.ui.examine_yaml_bn.clicked.connect(lambda: examine(self, "select_yaml_name_label"))
        self.ui.output_folder_bn.clicked.connect(lambda: examine(self, "output_folder_input", False))
        self.ui.output_folder_input.textChanged.connect(
            lambda: mark_syntax_error(self, "output_folder_input", ["empty"])
        )
        self.ui.check_yaml_file_bn.clicked.connect(lambda: load_yaml_config(self, advise_user=True))
        self.ui.run_biapy_docker_bn.clicked.connect(lambda: self.UIFunction.run_biapy())

        self.yes_no = None
        self.diag = None
        self.wokflow_info = None
        self.spinner = None
        self.basic_dialog = None
        self.model_carrousel_dialog = None
        self.tour = None

        # Variable to store model cards
        self.model_cards = None

        # Variables to control the threads/workers of spin window
        self.thread_spin = None
        self.worker_spin = None

        self.external_model_restrictions = None
        self.pretrained_model_need_to_check = None

        # Options to allow user moving the GUI
        self.dragPos = self.pos()

        def moveWindow(event):
            """
            Moves the window.

            Parameters
            ----------
            event: QCloseEvent
                Event that called this function.
            """
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        self.ui.frame_empty.mouseMoveEvent = moveWindow
        self.ui.frame_8.mouseMoveEvent = moveWindow
        self.ui.biapy_logo_frame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event: QCloseEvent):
        """
        Mouse press event handler to grad the GUI.

        Parameters
        ----------
        event: QCloseEvent
            Mouse drag event.
        """
        self.dragPos = event.globalPosition().toPoint()

    def tour_exec(self):
        """
        Starts the tour window.
        """
        if self.tour is None:
            self.tour = tour_window_Ui(self.cfg.settings["dot_images"], self)

        self.tour.set_biapy_version(self.cfg.settings["biapy_gui_version"])
        center_window(self.tour, self.geometry())
        self.tour.exec()

        # Save users election
        data = {
            "HIDE_TOUR_WINDOW": self.tour.basic_window.dont_show_message_checkbox.checkState() == Qt.Checked,
        }
        save_biapy_config(self, data, self.cfg.settings["biapy_gui_version"])

    def dialog_exec(self, message: str, reason: str):
        """
        Starts a dialog to inform the user of something.

        Parameters
        ----------
        message : str
            Message to be displayed for the user.

        reason : str
            Reason code.
        """
        if self.diag is None:
            self.diag = dialog_Ui(self)

        self.diag.dialog_constrict(message, reason)
        center_window(self.diag, self.geometry())
        self.diag.exec()

    def workflow_info_exec(
        self,
        workflow_name: str,
        workflow_images: List[QPixmap],
        workflow_description: str,
        workflow_doc: str,
        workflow_ready_to_use_examples: List[Dict],
    ):
        """
        Starts a new window with the workflow's description.

        Parameters
        ----------
        workflow_name : str
            Name of the workflow.

        workflow_images : List of QPixmap
            images of the workflow to use to fill the GUI.

        workflow_description : str
            Description of the workflow.

        workflow_doc : str
            Link to the workflow's documentation.

        workflow_ready_to_use_examples : List of dict
            Ready-to-use example information to display.
        """
        if self.wokflow_info is None:
            self.wokflow_info = workflow_explanation_Ui(self)

        self.wokflow_info.infoConstrict(
            workflow_name,
            workflow_images[0],
            workflow_images[1],
            workflow_description,
            workflow_doc,
            workflow_ready_to_use_examples,
        )
        center_window(self.wokflow_info, self.geometry())
        self.wokflow_info.exec()

    def yes_no_exec(self, question: str):
        """
        Starts a dialog with a yes or no question to be answered by the user.

        Parameters
        ----------
        question : str
            Question formulation.
        """
        if self.yes_no is None:
            self.yes_no = yes_no_Ui()

        self.yes_no.create_question(question)
        center_window(self.yes_no, self.geometry())
        self.yes_no.exec()

    def basic_dialog_exec(self, text: str):
        """
        Starts a basic dialog to display additional information such as for wizard page questions.

        Parameters
        ----------
        text : str
            Text to display.
        """
        if self.basic_dialog is None:
            self.basic_dialog = basic_Ui()

        self.basic_dialog.set_info(text)
        center_window(self.basic_dialog, self.geometry())
        self.basic_dialog.exec()

    def add_model_card(
        self,
        model_count: int,
        model_info: Dict,
        from_wizard: bool,
    ):
        """
        Add model card to model carrousel window. This function is called by model chgecking thread.

        Parameters
        ----------
        model_count : int
            Number of the model.

        model_info : dict
            Information of the model. Expected keys are:
            * ``'name'``: str, name of the model.
            * ``'source'`` : str, source of the model. Options are ['BioImage Model Zoo', 'TorchVision']
            * ``'description'``, str, description of the model.
            * ``'nickname'`` : str, nickname of the model.
            * ``'url'``: str (optional), URL link to the model.
            * ``'nickname_icon'`` : str (optional), nickname icon of the model. Only available in 'BioImage Model Zoo' models.
            * ``'id'``: str (optional), DOI of the model. Only available in 'BioImage Model Zoo' models.
            * ``'covers'``: str (optional), main cover of the model. Only available in 'BioImage Model Zoo' models.
            * ``'id'``: str (optional), DOI of the model. Only available in 'BioImage Model Zoo' models.
            * ``'imposed_vars'``: dict (optional), imposed variables by the model. E.g. patch size, normalization etc.
            * ``'restrictions'``: list of dicts (optional), restrictions imposed by the model. Only available in 'TorchVision' models.

        from_wizard : bool
            Whether if this function was called from the wizard or not.
        """
        if self.model_carrousel_dialog is None:
            self.model_carrousel_dialog = model_card_carrousel_Ui(self)

        self.model_carrousel_dialog.create_model_card(model_count, model_info, from_wizard=from_wizard)

    def model_carrousel_dialog_exec(self):
        """
        Starts a window providing model cards from sources like BioImage Model Zoo and Torchvision.
        """
        if self.model_carrousel_dialog is None:
            self.model_carrousel_dialog = model_card_carrousel_Ui(self)

        center_window(self.model_carrousel_dialog, self.geometry())
        self.model_carrousel_dialog.exec()

    def select_external_model(
        self, model_selected: str, model_source: str, model_restrictions: List[Dict], from_wizard: bool = True
    ):
        """
        Add model card to model carrousel window. This function is called by model chgecking thread.

        Parameters
        ----------
        model_selected : str
            Name of the model to select.

        model_source : str
            Source of the model. Options are ['BioImage Model Zoo', 'TorchVision']

        model_restrictions : list of dicts
            Restrictions imposed by the model.

        from_wizard : bool
            Whether if this function was called from the wizard or not.
        """

        self.yes_no_exec(f"Do you want to select '{model_selected}' model\nfrom {model_source}?")
        assert self.yes_no
        if self.yes_no.answer:
            if from_wizard:
                set_text(self.ui.wizard_model_input, model_selected + " ({})".format(model_source))
                if "BioImage Model Zoo" == model_source:
                    self.cfg.settings["wizard_answers"]["MODEL.SOURCE"] = "bmz"
                    self.cfg.settings["wizard_answers"]["MODEL.BMZ.SOURCE_MODEL_ID"] = model_selected
                else:
                    self.cfg.settings["wizard_answers"]["MODEL.SOURCE"] = "torchvision"
                    self.cfg.settings["wizard_answers"]["MODEL.TORCHVISION_MODEL_NAME"] = model_selected

                self.cfg.settings["wizard_answers"]["model_restrictions"] = model_restrictions
                self.cfg.settings["wizard_answers"]["MODEL.LOAD_CHECKPOINT"] = False

                # Mark section as answered in TOC and remember answer
                index = self.cfg.settings["wizard_from_question_index_to_toc"][
                    self.cfg.settings["wizard_question_index"]
                ]
                self.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(64, 144, 253))
                self.cfg.settings["wizard_question_answered_index"][
                    self.cfg.settings["wizard_question_index"]
                ] = model_selected
            else:
                set_text(self.ui.MODEL__BMZ__SOURCE_MODEL_ID__INPUT, model_selected + " ({})".format(model_source))
                self.external_model_restrictions = model_restrictions

            # Close window
            assert self.model_carrousel_dialog
            self.model_carrousel_dialog.close()

    def update_variable_in_GUI(self, variable_name: str, variable_value: str):
        """
        Update a GUI's variable called ``variable_name`` with ``variable_value``.

        Parameters
        ----------
        variable_name : str
            Variable name to change.

        variable_value : str
            Variable value to set.

        Returns
        -------
        err : str
            Error given in the process. It is ``None`` if not error was thrown.
        """
        err = set_text(getattr(self.ui, variable_name), str(variable_value))
        self.thread_queue.put(err)
        return err

    def spinner_exec(self):
        """
        Runs the spin window.
        """
        if self.spinner is None:
            self.spinner = spinner_Ui(self)

        center_window(self.spinner, self.geometry())

        self.spinner.start()
        self.spinner.exec()

    def loading_phase(self, signal: int):
        """
        Activates and deactivates the main window. Useful for the spin window to wait until a process
        is done.

        Parameters
        ----------
        signal : int
            Signal emited by a thread. If 0 means that the main window needs to be disabled and enabled
            otherwise.
        """
        if signal == 0:
            self.ui.centralwidget.setEnabled(False)
            self.spinner_exec()
        else:
            assert self.spinner
            self.spinner.close()
            self.ui.centralwidget.setEnabled(True)

    def report_yaml_load(self, errors: str, yaml_file: str):
        """
        Report to the user the result of loading the YAML file. If an error was found a dialog
        will be launched.

        Parameters
        ----------
        errors : List of str
            List of errors loading the YAML file.

        yaml_file : str
            Path to the YAML configuration file loaded.
        """
        if len(errors) == 0:
            self.yaml_file = yaml_file
            self.dialog_exec(
                "Configuration file succesfully loaded! You will "
                "be redirected to the workflow page so you can modify the configuration.",
                "inform_user_and_go",
            )
            self.cfg.settings["yaml_config_file_path"] = os.path.dirname(self.yaml_file)
            self.ui.goptions_browse_yaml_path_input.setText(os.path.normpath(os.path.dirname(self.yaml_file)))
            self.ui.goptions_yaml_name_input.setText(os.path.normpath(os.path.basename(self.yaml_file)))
        else:
            self.dialog_exec(errors, "load_yaml_ok_but_errors")

    def external_model_list_built(self, model_count: int):
        """
        Show to the user all models prepared until ``model_count`` or a message if no models are available to show.

        Parameters
        ----------
        model_count : int
            Number of models to show.
        """
        if model_count > 0:
            if self.pretrained_model_need_to_check is not None:
                assert self.model_carrousel_dialog
                self.model_carrousel_dialog.show_models(model_count)
            self.pretrained_model_need_to_check = model_count
            self.model_carrousel_dialog_exec()
        else:
            self.dialog_exec(
                "There are no models in the BioImage Model Zoo or Torchvision that are compatible with BiaPy "
                "for the selected workflow characteristics.",
                "inform_user",
            )

    def closeEvent(self, event: QCloseEvent):
        """
        Manages closing event to ensure all threads are killed.

        Parameters
        ----------
        event: QCloseEvent
            Main window of the application.
        """
        # Find if some window is still running
        still_running = False
        for x in self.cfg.settings["running_workers"]:
            if "run" in x.process_steps:  # Means that is running
                still_running = True
                break

        if still_running:
            self.yes_no_exec("Are you sure you want to exit? All running windows will be stopped")
        else:
            self.yes_no_exec("Are you sure you want to exit?")
        assert self.yes_no
        if self.yes_no.answer:
            # Kill all run windows
            for x in self.cfg.settings["running_workers"]:
                self.logger.info("Killing subprocess . . .")
                x.gui.forcing_close = True
                x.gui.close()

            # Ensure there is no spin process there
            if self.thread_spin is not None:
                try:
                    self.thread_spin.quit()
                except Exception as e:
                    self.logger.error(f"Possible expected error during thread_spin deletion: {e}")
            # Finally close the main window
            QApplication.quit()
        else:
            event.ignore()

    def check_new_gui_version(self):
        """
        Checks if there is a new version of the GUI by looking at the github version tags.
        """
        # Changed version
        sha, vtag = get_git_revision_short_hash(self)
        self.logger.info(f"Local GUI version: {self.cfg.settings['biapy_gui_version']}")
        self.logger.info(f"Remote last version's hash: {sha}")
        self.logger.info(f"Remote last version: {vtag}")
        if sha is not None and vtag is not None and vtag > self.cfg.settings["biapy_gui_version"]:
            self.dialog_exec(
                "There is a new version of BiaPy's graphical user interface available. Please, "
                "download it <a href='https://biapyx.github.io'>here</a>",
                reason="inform_user",
            )

    def showInstantToolTip(self, gui_widget_name: str):
        """
        Shows the tooTip of a widget.

        Parameters
        ----------
        gui_widget_name : str
            Name of the QWidget selected to show the tooltip.
        """
        QToolTip.showText(
            QCursor.pos(),
            getattr(self.ui, gui_widget_name).toolTip(),
        )


def center_window(widget: QWidget, geometry: QRect):
    """
    Centers the given window.

    Parameters
    ----------
    widget : QWidget
        Widget to center.

    geometry : QRect
        Screen geometry.
    """
    window = widget.window()
    assert window
    window.setGeometry(
        QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            window.size(),
            geometry,
        ),
    )


if __name__ == "__main__":
    # os.environ["QT_SCALE_FACTOR"] = "1"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)

    # Setup theme
    theme = "light"  # force light theme
    qdarktheme.setup_theme(theme)
    system_theme = darkdetect.theme().lower()
    print(f"System theme detected: {system_theme} ; Forced theme: {theme}")

    splash = QSplashScreen(
        QPixmap(resource_path(os.path.join("images", "splash_screen", "biapy_splash_logo.png"))),
        Qt.WindowStaysOnTopHint,
    )
    splash.show()

    app.processEvents()

    window = None

    # Log output to file
    biapy_dir = user_cache_dir("biapy")
    log_dir = os.path.join(biapy_dir, "logs")
    time_now = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_file = os.path.join(log_dir, f"biapy_{time_now}")
    config_file = os.path.join(biapy_dir, f"config.json")
    os.makedirs(biapy_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    log_info = {
        "biapy_dir": biapy_dir,
        "log_dir": log_dir,
        "log_file": log_file,
        "config_file": config_file,
    }

    logging.basicConfig(filename=log_file, format="%(asctime)s %(message)s", filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Log to console
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

    app.setWindowIcon(QIcon(resource_path(os.path.join("images", "splash_screen", "biapy_logo_icon.ico"))))

    # For disabling wheel in combo boxes
    class WheelEventFilter(QObject):
        def eventFilter(self, obj, ev):
            if obj.inherits("QComboBox") and ev.type() == QEvent.Wheel:
                return True
            return False

    filter = WheelEventFilter()
    app.installEventFilter(filter)

    window = MainWindow(logger, log_info, system_theme)
    window.show()
    splash.finish(window)

    # Center the main GUI in the middle of the first screen
    all_screens = app.screens()
    center_window(window, all_screens[0].availableGeometry())

    # Check new versions of the GUI
    window.check_new_gui_version()

    # Start tour window
    save_biapy_config(window, {}, str(window.cfg.settings["biapy_gui_version"]))
    hide_tour = False
    version = ""
    try:
        with open(log_info["config_file"], "r") as file:
            data = json.load(file)
            hide_tour = bool(data["HIDE_TOUR_WINDOW"])
            version = str(data["GUI_VERSION"])
    except:
        pass

    if version != str(window.cfg.settings["biapy_gui_version"]):
        hide_tour = False

    if not hide_tour:
        window.tour_exec()

    def excepthook(exc_type, exc_value, exc_tb):
        tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        logger.info("error message:\n", tb)
        tb += f"\nYou can also provide the log error here: \n{log_file}\n"
        tb += "\nExiting BiaPy as its functionality may be damaged!\n"

        # Log the error in stderr
        logger.error(" Main window error:\n" + "".join(traceback.format_exception(exc_type, exc_value, exc_tb)))

        assert window
        window.dialog_exec(
            f"Unexpected error. Please contact BiaPy developers with the following error: \n{tb}", "unexpected_error"
        )
        QApplication.quit()

    sys.excepthook = excepthook

    sys.exit(app.exec())
