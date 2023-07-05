import os
import sys
import tempfile
import logging
import traceback
import io

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QThread, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow 
from ui_function import * 
from ui_utils import examine, combobox_hide_visible_action, mark_syntax_error, expand_hide_advanced_options, buttonPressed, load_yaml_config
from settings import Settings
from aux_windows import dialog_Ui, error_Ui, workflow_explanation_Ui, yes_no_Ui

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
        self.setStyleSheet("QWidget{font: \"Roboto Mono\", font-size:16px}")
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

        gpu_regex = QtCore.QRegExp('^[0-9][0-9]*\s*(,\s*[0-9][0-9]*\s*)*$')
        self.gpu_validator = QtGui.QRegExpValidator(gpu_regex)

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

        # Workflow page buttons
        self.ui.left_arrow_bn.clicked.connect(lambda: UIFunction.move_workflow_view(self, True))
        self.ui.right_arrow_bn.clicked.connect(lambda: UIFunction.move_workflow_view(self, False))
        self.ui.continue_bn.clicked.connect(lambda: buttonPressed(self, 'up', -1))
        self.ui.back_bn.clicked.connect(lambda: buttonPressed(self, 'down', -1))

        self.ui.workflow_view1_seemore_bn.clicked.connect(lambda: UIFunction.obtain_workflow_description(self, -1))
        self.ui.workflow_view2_seemore_bn.clicked.connect(lambda: UIFunction.obtain_workflow_description(self, 0))
        self.ui.workflow_view3_seemore_bn.clicked.connect(lambda: UIFunction.obtain_workflow_description(self, 1))

        # General options page buttons
        self.ui.gpu_input.setValidator(self.gpu_validator)
        self.ui.seed_input.setValidator(self.int_validator)
        self.ui.dimensions_comboBox.currentIndexChanged.connect(lambda: self.change_problem_dimensions(self.ui.dimensions_comboBox.currentIndex()))
        self.change_problem_dimensions(0)
        self.ui.goptions_advanced_bn.clicked.connect(lambda: expand_hide_advanced_options(self, "goptions_advanced_bn", "goptions_advanced_options_scrollarea"))
        self.ui.goptions_browse_yaml_path_bn.clicked.connect(lambda: examine(self, "goptions_browse_yaml_path_input", False))
        self.ui.checkpoint_file_path_browse_bn.clicked.connect(lambda: examine(self, "checkpoint_file_path_input"))

        # Train page buttons 
        self.ui.cross_validation_nfolds_input.setValidator(self.int_validator)
        self.ui.cross_validation_fold_input.setValidator(self.int_validator)
        self.ui.percentage_validation_input.setValidator(self.float_validator)
        self.ui.number_of_epochs_input.setValidator(self.int_validator)
        self.ui.patience_input.setValidator(self.float_validator)
        self.ui.number_of_classes_input.setValidator(self.float_validator)
        # self.ui.custom_mean_input.setValidator(self.float_validator)
        # self.ui.custom_std_input.setValidator(self.float_validator)
        self.ui.replicate_data_input.setValidator(self.int_validator)
        self.ui.feature_maps_input.setValidator(self.no_limit_number_min_one_number_bracket_validator)
        self.ui.dropout_input.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.kernel_size_input.setValidator(self.int_validator)
        self.ui.z_down_input.setValidator(self.z_down_bracket_validator)
        self.ui.tiramisu_depth_input.setValidator(self.int_validator)
        self.ui.tiramisu_feature_maps_input.setValidator(self.int_validator)
        self.ui.tiramisu_dropout_input.setValidator(self.float_validator)
        self.ui.unetr_token_size_input.setValidator(self.int_validator)
        self.ui.unetr_embed_dims_input.setValidator(self.int_validator)
        self.ui.unetr_depth_input.setValidator(self.int_validator)
        self.ui.unetr_mlp_hidden_units_input.setValidator(self.two_pos_number_bracket_validator)
        self.ui.unetr_num_heads_input.setValidator(self.int_validator)
        self.ui.unetr_vit_hidden_multiple_input.setValidator(self.int_validator)
        self.ui.learning_rate_input.setValidator(self.float_validator)
        self.ui.batch_size_input.setValidator(self.int_validator)
        self.ui.profiler_batch_range_input.setValidator(self.two_pos_number_validator)
        # self.ui.lr_schel_min_lr_input.setValidator(self.float_validator)
        # self.ui.lr_schel_reduce_on_plat_patience_input.setValidator(self.int_validator)
        self.ui.lr_schel_reduce_on_plat_factor_input.setValidator(self.float_validator)
        # self.ui.lr_schel_warmupcosine_lr_input.setValidator(self.float_validator)
        # self.ui.lr_schel_warmupcosine_epochs_input.setValidator(self.int_validator)
        # self.ui.lr_schel_warmupcosine_hold_epochs_input.setValidator(self.int_validator)
        self.ui.da_prob_input.setValidator(self.float_validator)
        self.ui.da_num_samples_check_input.setValidator(self.int_validator)
        self.ui.da_random_rot_range_input.setValidator(self.two_number_parenthesis_validator)
        self.ui.da_shear_range_input.setValidator(self.two_number_parenthesis_validator)
        self.ui.da_zoom_range_input.setValidator(self.two_0_2_float_number_parenthesis_validator)
        self.ui.da_shift_range_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_elastic_alpha_input.setValidator(self.two_number_parenthesis_validator)   
        self.ui.da_gaussian_sigma_input.setValidator(self.two_pos_float_number_parenthesis_validator)
        self.ui.da_median_blur_k_size_input.setValidator(self.two_number_parenthesis_validator)
        self.ui.da_motion_blur_k_size_input.setValidator(self.two_number_parenthesis_validator)
        self.ui.da_gamma_contrast_range_input.setValidator(self.two_pos_float_number_parenthesis_validator)
        self.ui.da_brightness_factor_range_input.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.da_contrast_factor_range_input.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.da_brightness_em_factor_input.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.da_contrast_em_factor_input.setValidator(self.two_0_1_float_number_parenthesis_validator)
        self.ui.da_dropout_range_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_cutout_number_iterations_input.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.da_cutout_size_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_cuout_cval_input.setValidator(self.float_validator)
        self.ui.da_cutblur_size_range_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_cutblut_down_range_input.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.da_cutmix_size_range_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_cutnoise_scale_range_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_cutnoise_number_iter_input.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.da_cutnoise_size_range_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.da_misaligment_displacement_input.setValidator(self.int_validator)
        self.ui.da_misaligment_rotate_ratio_input.setValidator(self.float_validator)
        self.ui.da_missing_sections_iteration_range_input.setValidator(self.two_pos_number_parenthesis_validator)
        self.ui.da_grid_ratio_input.setValidator(self.float_validator)
        self.ui.da_grid_d_range_input.setValidator(self.two_pos_float_number_parenthesis_validator)
        self.ui.da_grid_rotate_input.setValidator(self.float_validator)
        self.ui.da_gaussian_noise_mean_input.setValidator(self.float_validator)
        self.ui.da_gaussian_noise_var_input.setValidator(self.float_validator)
        self.ui.da_salt_amount_input.setValidator(self.float_validator)
        self.ui.da_pepper_amount_input.setValidator(self.float_validator)
        self.ui.da_salt_pepper_amount_input.setValidator(self.float_validator)
        self.ui.da_salt_pepper_prop_input.setValidator(self.float_validator) 

        self.ui.sem_seg_random_patch_fore_weights_input.setValidator(self.float_validator)
        self.ui.sem_seg_random_patch_back_weights_input.setValidator(self.float_validator)
        self.ui.sem_seg_minimum_fore_percentage_input.setValidator(self.float_validator)
        self.ui.sem_seg_yz_filtering_size_input.setValidator(self.int_validator)
        self.ui.sem_seg_z_filtering_size_input.setValidator(self.int_validator)

        self.ui.inst_seg_minimum_fore_percentage_input.setValidator(self.float_validator)
        self.ui.inst_seg_channel_weigths_input.setValidator(self.two_pos_0_1_float_number_parenthesis_validator)
        self.ui.inst_seg_b_channel_th_input.setValidator(self.float_validator)
        self.ui.inst_seg_c_channel_th_input.setValidator(self.float_validator)
        self.ui.inst_seg_d_channel_th_input.setValidator(self.large_range_float_validator)
        self.ui.inst_seg_p_channel_th_input.setValidator(self.float_validator)
        self.ui.inst_seg_fore_mask_th_input.setValidator(self.float_validator)
        self.ui.inst_seg_fore_dil_input.setValidator(self.int_validator)
        self.ui.inst_seg_fore_ero_input.setValidator(self.int_validator)
        self.ui.inst_seg_small_obj_fil_before_size_input.setValidator(self.int_validator)
        self.ui.inst_seg_small_obj_fil_after_size_input.setValidator(self.int_validator)
        self.ui.inst_seg_moph_op_rad_input.setValidator(self.no_limit_number_bracket_validator)
        self.ui.inst_seg_matching_stats_ths_input.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.inst_seg_matching_stats_colores_img_ths_input.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.inst_seg_yz_filtering_size_input.setValidator(self.int_validator)
        self.ui.inst_seg_z_filtering_size_input.setValidator(self.int_validator)
        # self.ui.inst_seg_circularity_filtering_input.setValidator(self.float_validator)
        # self.ui.inst_seg_repare_large_blobs_input.setValidator(self.int_validator)
        # self.ui.inst_seg_remove_close_points_radius_input.setValidator(self.no_limit_0_1_float_number_bracket_validator)

        self.ui.det_minimum_fore_percentage_input.setValidator(self.float_validator)
        self.ui.det_central_point_dilation_input.setValidator(self.int_validator)
        self.ui.det_min_th_to_be_peak_input.setValidator(self.no_limit_0_1_float_number_bracket_validator)
        self.ui.det_yz_filtering_size_input.setValidator(self.int_validator)
        self.ui.det_z_filtering_size_input.setValidator(self.int_validator)
        # self.ui.det_circularity_filtering_input.setValidator(self.float_validator)
        # self.ui.det_remove_close_points_radius_input.setValidator(self.float_validator)
        # self.ui.det_watershed_donuts_classes_input.setValidator(self.no_limit_number_bracket_validator)
        self.ui.det_watershed_donuts_patch_input.setValidator(self.no_limit_number_bracket_validator)
        self.ui.det_watershed_donuts_nucleus_diam_input.setValidator(self.int_validator)
        self.ui.det_tolerance_input.setValidator(self.no_limit_number_min_one_number_bracket_validator)

        self.ui.deno_n2v_perc_pix_input.setValidator(self.float_validator)
        self.ui.deno_n2v_neighborhood_radius_input.setValidator(self.int_validator)

        self.ui.checkpoint_load_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "checkpoint_load_input",
            {"checkpoint_file_path_input": "Yes", "checkpoint_file_path_browse_bn": "Yes", "checkpoint_file_path_browse_label": "Yes"}))
        self.ui.job_name_input.textChanged.connect(lambda: mark_syntax_error(self, "job_name_input", ["empty"]))   
        self.ui.goptions_yaml_name_input.textChanged.connect(lambda: mark_syntax_error(self, "goptions_yaml_name_input", ["empty"]))
        self.ui.goptions_browse_yaml_path_input.textChanged.connect(lambda: mark_syntax_error(self, "goptions_browse_yaml_path_input", ["empty"]))      
        self.ui.enable_train_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "enable_train_input",
            {"train_tab_widget": "Yes"}))        
        self.ui.train_data_input_browse_bn.clicked.connect(lambda: examine(self, "train_data_input", False))
        self.ui.train_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "train_data_gt_input", False))
        self.ui.val_data_input_browse_bn.clicked.connect(lambda: examine(self, "validation_data_input", False))
        self.ui.val_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "validation_data_gt_input", False))
        self.ui.train_in_memory_comboBox.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "train_in_memory_comboBox",
            {"validation_data_label": "No", "validation_data_input": "No", "val_data_input_browse_bn": "No", 
            "validation_data_gt_label": "No", "validation_data_gt_input": "No", "val_data_gt_input_browse_bn": "No", 
            "val_in_memory_label": "No", "val_in_memory_comboBox": "No", "percentage_validation_label": "Yes", 
            "percentage_validation_input": "Yes"},
            frames_dict_values_to_set={"validation_type_comboBox": "Not extracted from train (path needed)"}))
        self.ui.validation_type_comboBox.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "validation_type_comboBox",
            {"percentage_validation_label": "Extract from train (split training)", "percentage_validation_input": "Extract from train (split training)", 
            "cross_validation_nfolds_label": "Extract from train (cross validation)", "cross_validation_nfolds_input": "Extract from train (cross validation)",
            "cross_validation_fold_label": "Extract from train (cross validation)", "cross_validation_fold_input": "Extract from train (cross validation)",
            "use_val_as_test": "Extract from train (cross validation)", "use_val_as_test_input": "Extract from train (cross validation)",
            "validation_data_label": "Not extracted from train (path needed)", "validation_data_input": "Not extracted from train (path needed)", 
            "val_data_input_browse_bn": "Not extracted from train (path needed)", "validation_data_gt_label": "Not extracted from train (path needed)", 
            "validation_data_gt_input": "Not extracted from train (path needed)", "val_data_gt_input_browse_bn": "Not extracted from train (path needed)", 
            "val_in_memory_label": "Not extracted from train (path needed)", "val_in_memory_comboBox": "Not extracted from train (path needed)", 
            "test_data_label": ["Not extracted from train (path needed)","Extract from train (split training)"], 
            "test_data_input": ["Not extracted from train (path needed)","Extract from train (split training)"], 
            "test_data_input_browse_bn": ["Not extracted from train (path needed)","Extract from train (split training)"], 
            "test_exists_gt_label": ["Not extracted from train (path needed)","Extract from train (split training)"], 
            "test_exists_gt_input": ["Not extracted from train (path needed)","Extract from train (split training)"],
            "test_data_gt_label": ["Not extracted from train (path needed)","Extract from train (split training)"], 
            "test_data_gt_input": ["Not extracted from train (path needed)","Extract from train (split training)"], 
            "test_data_gt_input_browse_bn": ["Not extracted from train (path needed)","Extract from train (split training)"],
            "test_data_in_memory_label": ["Not extracted from train (path needed)","Extract from train (split training)"],
            "test_data_in_memory_input": ["Not extracted from train (path needed)","Extract from train (split training)"],
            "random_val_label": ["Extract from train (cross validation)","Extract from train (split training)"],
            "random_val_input": ["Extract from train (cross validation)","Extract from train (split training)"],
            "validation_overlap_label": "Not extracted from train (path needed)", "validation_overlap_input": "Not extracted from train (path needed)", 
            "validation_padding_label": "Not extracted from train (path needed)", "validation_padding_input": "Not extracted from train (path needed)", }))
        self.ui.train_advanced_bn.clicked.connect(lambda: expand_hide_advanced_options(self, "train_advanced_bn", "train_advanced_options_frame"))
        self.ui.model_input.currentIndexChanged.connect(lambda: UIFunction.model_combobox_changed(self, str(self.ui.model_input.currentText())))
        self.ui.profiler_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "profiler_input",
            {"profiler_batch_range_label": "Yes", "profiler_batch_range_input": "Yes"}))
        self.ui.normalization_type_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "normalization_type_input",
            {"custom_mean_label": "custom", "custom_mean_input": "custom", "custom_std_label": "custom", "custom_std_input": "custom"}))
        self.ui.extract_random_patch_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "extract_random_patch_input",
            {"extract_random_patch_frame_label": "Yes", "extract_random_patch_frame": "Yes"}))    
        self.ui.lr_schel_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "lr_schel_input",
            {"lr_schel_warmupcosine_lr_label": "warmupcosine", "lr_schel_warmupcosine_lr_input": "warmupcosine",
             "lr_schel_warmupcosine_epochs_label": "warmupcosine", "lr_schel_warmupcosine_epochs_input": "warmupcosine",\
             "lr_schel_warmupcosine_hold_epochs_label": "warmupcosine", "lr_schel_warmupcosine_hold_epochs_input": "warmupcosine",\
             "lr_schel_min_lr_label": ["warmupcosine","reduceonplateau"], "lr_schel_min_lr_input": ["warmupcosine","reduceonplateau"],
             "lr_schel_reduce_on_plat_patience_label": "reduceonplateau", "lr_schel_reduce_on_plat_patience_input": "reduceonplateau",\
             "lr_schel_reduce_on_plat_factor_label": "reduceonplateau", "lr_schel_reduce_on_plat_factor_input": "reduceonplateau"}))
        self.ui.da_enable_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_enable_input",
            {"da_frame": "Yes"}))
        self.ui.da_random_rot_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_random_rot_input",
            {"da_random_rot_range_label": "Yes", "da_random_rot_range_input": "Yes"}))
        self.ui.da_shear_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_shear_input",
            {"da_shear_range_label": "Yes", "da_shear_range_input": "Yes"}))
        self.ui.da_zoom_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_zoom_input",
            {"da_zoom_range_label": "Yes", "da_zoom_range_input": "Yes"}))
        self.ui.da_shift_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_shift_input",
            {"da_shift_range_label": "Yes", "da_shift_range_input": "Yes"}))
        self.ui.da_elastic_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_elastic_input",
            {"da_elastic_alpha_label": "Yes", "da_elastic_alpha_input": "Yes", "da_elastic_sigma_label": "Yes", "da_elastic_sigma_input": "Yes",\
            "da_elastic_mode_label": "Yes", "da_elastic_mode_input": "Yes"}))
        self.ui.da_gaussian_blur_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_gaussian_blur_input",
            {"da_gaussian_sigma_label": "Yes", "da_gaussian_sigma_input": "Yes"}))
        self.ui.da_median_blur_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_median_blur_input",
            {"da_median_blur_k_size_label": "Yes", "da_median_blur_k_size_input": "Yes"}))
        self.ui.da_motion_blur_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_motion_blur_input",
            {"da_motion_blur_k_size_label": "Yes", "da_motion_blur_k_size_input": "Yes"}))
        self.ui.da_gamma_contrast_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_gamma_contrast_input",
            {"da_gamma_contrast_range_label": "Yes", "da_gamma_contrast_range_input": "Yes"}))
        self.ui.da_brightness_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_brightness_input",
            {"da_brightness_factor_range_label": "Yes", "da_brightness_factor_range_input": "Yes",
             "da_brightness_mode_label": "Yes", "da_brightness_mode_input": "Yes"}))
        self.ui.da_contrast_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_contrast_input",
            {"da_contrast_factor_range_label": "Yes", "da_contrast_factor_range_input": "Yes",
             "da_contrast_mode_label": "Yes", "da_contrast_mode_input": "Yes"}))
        self.ui.da_brightness_em_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_brightness_em_input",
            {"da_brightness_em_factor_label": "Yes", "da_brightness_em_factor_input": "Yes",
             "da_brightness_em_mode_label": "Yes", "da_brightness_em_mode_input": "Yes"}))
        self.ui.da_contrast_em_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_contrast_em_input",
             {"da_contrast_em_factor_label": "Yes", "da_contrast_em_factor_input": "Yes",
             "da_contrast_em_mode_label": "Yes", "da_contrast_em_mode_input": "Yes"}))
        self.ui.da_dropout_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_dropout_input",
            {"da_dropout_range_label": "Yes", "da_dropout_range_input": "Yes"}))
        self.ui.da_cutout_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_cutout_input",
            {"da_cutout_number_iterations_label": "Yes", "da_cutout_number_iterations_input": "Yes",
             "da_cutout_size_label": "Yes", "da_cutout_size_input": "Yes",
             "da_cuout_cval_label": "Yes", "da_cuout_cval_input": "Yes"}))
        self.ui.da_cutblur_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_cutblur_input",
            {"da_cutblur_size_range_label": "Yes", "da_cutblur_size_range_input": "Yes",
             "da_cutblut_down_range_label": "Yes", "da_cutblut_down_range_input": "Yes",
             "da_cutblur_inside_label": "Yes", "da_cutblur_inside_input": "Yes"}))
        self.ui.da_cutmix_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_cutmix_input",
            {"da_cutmix_size_range_label": "Yes", "da_cutmix_size_range_input": "Yes"}))
        self.ui.da_cutnoise_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_cutnoise_input",
            {"da_cutnoise_scale_range_label": "Yes", "da_cutnoise_scale_range_input": "Yes",
             "da_cutnoise_number_iter_label": "Yes", "da_cutnoise_number_iter_input": "Yes",
             "da_cutnoise_size_range_label": "Yes", "da_cutnoise_size_range_input": "Yes"}))
        self.ui.da_misaligment_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_misaligment_input",
            {"da_misaligment_displacement_label": "Yes", "da_misaligment_displacement_input": "Yes",
             "da_misaligment_rotate_ratio_label": "Yes", "da_misaligment_rotate_ratio_input": "Yes"}))
        self.ui.da_missing_sections_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_missing_sections_input",
            {"da_missing_sections_iteration_range_label": "Yes", "da_missing_sections_iteration_range_input": "Yes"}))
        self.ui.da_gridmask_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_gridmask_input",
            {"da_grid_ratio_label": "Yes", "da_grid_ratio_input": "Yes",
             "da_grid_d_range_label": "Yes", "da_grid_d_range_input": "Yes",
             "da_grid_rotate_label": "Yes", "da_grid_rotate_input": "Yes",
             "da_grid_invert_label": "Yes", "da_grid_invert_input": "Yes"}))
        self.ui.da_gaussian_noise_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_gaussian_noise_input",
            {"da_gaussian_noise_mean_label": "Yes", "da_gaussian_noise_mean_input": "Yes",
             "da_gaussian_noise_var_label": "Yes", "da_gaussian_noise_var_input": "Yes",
             "da_gaussian_noise_use_input_img_label": "Yes", "da_gaussian_noise_use_input_img_input": "Yes"}))
        self.ui.da_salt_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_salt_input",
            {"da_salt_amount_label": "Yes", "da_salt_amount_input": "Yes"}))
        self.ui.da_pepper_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_pepper_input",
            {"da_pepper_amount_label": "Yes", "da_pepper_amount_input": "Yes"}))
        self.ui.da_salt_pepper_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "da_salt_pepper_input",
            {"da_salt_pepper_amount_label": "Yes", "da_salt_pepper_amount_input": "Yes",
             "da_salt_pepper_prop_label": "Yes", "da_salt_pepper_prop_input": "Yes"}))

        # Test page buttons
        self.ui.enable_test_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "enable_test_input",
            {"test_tab_widget": "Yes"}))
        self.ui.test_data_input_browse_bn.clicked.connect(lambda: examine(self, "test_data_input", False))
        self.ui.test_data_gt_input_browse_bn.clicked.connect(lambda: examine(self, "test_data_gt_input", False))
        self.ui.test_exists_gt_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "test_exists_gt_input",
            {"test_data_gt_label": "Yes", "test_data_gt_input": "Yes", "test_data_gt_input_browse_bn": "Yes",
             "inst_seg_metrics_label": "Yes", "inst_seg_metrics_frame": "Yes", "det_metrics_label": "Yes", "det_metrics_frame": "Yes"}))
        self.ui.use_val_as_test_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "use_val_as_test_input",
            {"test_data_label": "No", "test_data_input": "No", "test_data_input_browse_bn": "No",
             "test_exists_gt_label": "No", "test_exists_gt_input": "No", 
             "test_data_gt_label": "No", "test_data_gt_input": "No", "test_data_gt_input_browse_bn": "No",
             "test_data_in_memory_label": "No", "test_data_in_memory_input": "No", 
             }))
        self.ui.test_advanced_bn.clicked.connect(lambda: expand_hide_advanced_options(self, "test_advanced_bn", "test_advanced_options_frame"))

        self.ui.sem_seg_yz_filtering_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "sem_seg_yz_filtering_input",
            {"sem_seg_yz_filtering_size_label": "Yes", "sem_seg_yz_filtering_size_input": "Yes"}))
        self.ui.sem_seg_z_filtering_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "sem_seg_z_filtering_input",
            {"sem_seg_z_filtering_size_label": "Yes", "sem_seg_z_filtering_size_input": "Yes"}))

        self.ui.inst_seg_data_channels_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_data_channels_input",
            {"inst_seg_b_channel_th_label": ["BC", "BP", "BD", "BCM", "BCD", "BCDv2","BDv2"], "inst_seg_b_channel_th_input": ["BC", "BP", "BD", "BCM", "BCD", "BCDv2","BDv2"], 
             "inst_seg_c_channel_th_label": ["BC", "BCM", "BCD", "BCDv2"], "inst_seg_c_channel_th_input": ["BC", "BCM", "BCD", "BCDv2"],
             "inst_seg_d_channel_th_label": ["BD", "BCD", "BCDv2","BDv2", "Dv2"], "inst_seg_d_channel_th_input": ["BD", "BCD", "BCDv2","BDv2", "Dv2"], 
             "inst_seg_p_channel_th_label": "BP", "inst_seg_p_channel_th_input": "BP", "inst_seg_repare_large_blobs_label": "BP", "inst_seg_repare_large_blobs_input": "BP",
             "inst_seg_remove_close_points_label": "BP","inst_seg_remove_close_points_input": "BP","inst_seg_remove_close_points_radius_label": "BP", "inst_seg_remove_close_points_radius_input": "BP",
             "inst_seg_fore_mask_th_label": ["BC", "BP", "BD", "BCM", "BCD", "BCDv2","BDv2"], "inst_seg_fore_mask_th_input": ["BC", "BP", "BD", "BCM", "BCD", "BCDv2","BDv2"],
             "inst_seg_voronoi_label": ["BC", "BCM"], "inst_seg_voronoi_input": ["BC", "BCM"]}))
        self.ui.inst_seg_ero_dil_fore_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_ero_dil_fore_input",
            {"inst_seg_fore_dil_label": "Yes", "inst_seg_fore_dil_input": "Yes", 
             "inst_seg_fore_ero_label": "Yes", "inst_seg_fore_ero_input": "Yes"}))
        self.ui.inst_seg_small_obj_fil_before_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_small_obj_fil_before_input",
            {"inst_seg_small_obj_fil_before_size_label": "Yes", "inst_seg_small_obj_fil_before_size_input": "Yes"}))
        self.ui.inst_seg_small_obj_fil_after_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_small_obj_fil_after_input",
            {"inst_seg_small_obj_fil_after_size_label": "Yes", "inst_seg_small_obj_fil_after_size_input": "Yes"}))
        self.ui.inst_seg_yz_filtering_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_yz_filtering_input",
            {"inst_seg_yz_filtering_size_label": "Yes", "inst_seg_yz_filtering_size_input": "Yes"}))
        self.ui.inst_seg_z_filtering_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_z_filtering_input",
            {"inst_seg_z_filtering_size_label": "Yes", "inst_seg_z_filtering_size_input": "Yes"}))
        self.ui.inst_seg_remove_close_points_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_remove_close_points_input",
            {"inst_seg_remove_close_points_radius_label": "Yes", "inst_seg_remove_close_points_radius_input": "Yes"}))
        self.ui.inst_seg_matching_stats_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "inst_seg_matching_stats_input",
            {"inst_seg_matching_stats_ths_label": "Yes", "inst_seg_matching_stats_ths_input": "Yes",
            "inst_seg_matching_stats_colores_img_ths_label": "Yes", "inst_seg_matching_stats_colores_img_ths_input": "Yes",}))

        self.ui.det_local_max_coords_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "det_local_max_coords_input",
            {"det_min_th_to_be_peak_label": "Yes", "det_min_th_to_be_peak_input": "Yes"}))
        self.ui.det_yz_filtering_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "det_yz_filtering_input",
            {"det_yz_filtering_size_label": "Yes", "det_yz_filtering_size_input": "Yes"}))
        self.ui.det_z_filtering_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "det_z_filtering_input",
            {"det_z_filtering_size_label": "Yes", "det_z_filtering_size_input": "Yes"}))
        self.ui.det_remove_close_points_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "det_remove_close_points_input",
            {"det_remove_close_points_radius_label": "Yes", "det_remove_close_points_radius_input": "Yes"}))
        self.ui.det_remove_close_points_input.currentIndexChanged.connect(lambda: combobox_hide_visible_action(self, "det_remove_close_points_input",
            {"det_watershed_first_dilation_label": "Yes", "det_watershed_first_dilation_input": "Yes",
             "det_watershed_donuts_classes_label": "Yes", "det_watershed_donuts_classes_input": "Yes",
             "det_watershed_donuts_patch_label": "Yes", "det_watershed_donuts_patch_input": "Yes",
             "det_watershed_donuts_nucleus_diam_label": "Yes", "det_watershed_donuts_nucleus_diam_input": "Yes",
             "det_data_watetshed_check_label": "Yes", "det_data_watetshed_check_input": "Yes"}))
        
        # Run page buttons 
        self.ui.select_yaml_name_label.textChanged.connect(lambda: mark_syntax_error(self, "select_yaml_name_label", ["empty"]))                        
        self.ui.examine_yaml_bn.clicked.connect(lambda: examine(self, "select_yaml_name_label"))
        self.ui.output_folder_bn.clicked.connect(lambda: examine(self, "output_folder_input", False))
        self.ui.output_folder_input.textChanged.connect(lambda: mark_syntax_error(self, "output_folder_input", ["empty"])) 
        self.ui.check_yaml_file_bn.clicked.connect(lambda: load_yaml_config(self))
        self.ui.run_biapy_docker_bn.clicked.connect(lambda: UIFunction.run_biapy(self))

        self.diag = None
        self.yes_no = None
        self.error = None
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
            self.ui.patch_size_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.patch_size_input.setText("(256,256,1)")
            self.ui.train_resolution_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.train_resolution_input.setText("(1,1)")
            self.ui.train_overlap_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.train_overlap_input.setText("(0,0)")
            self.ui.train_padding_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.train_padding_input.setText("(0,0)")
            self.ui.validation_resolution_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.validation_resolution_input.setText("(1,1)")
            self.ui.validation_overlap_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.validation_overlap_input.setText("(0,0)")
            self.ui.validation_padding_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.validation_padding_input.setText("(0,0)")
            self.ui.test_resolution_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.test_resolution_input.setText("(1,1)")
            self.ui.test_overlap_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.test_overlap_input.setText("(0,0)")
            self.ui.test_padding_input.setValidator(self.two_pos_number_parenthesis_validator)
            self.ui.test_padding_input.setText("(0,0)")
            self.ui.da_z_flip_label.setVisible(False)
            self.ui.da_z_flip_input.setVisible(False)
            self.ui.test_2d_as_3d_stack_label.setVisible(True)
            self.ui.test_2d_as_3d_stack_input.setVisible(True)
            self.ui.test_reduce_memory_label.setVisible(False)
            self.ui.test_reduce_memory_input.setVisible(False)
            self.ui.test_per_patch_input.setCurrentText("No")
            self.ui.test_merge_patches_input.setCurrentText("No")
            self.ui.test_full_image_input.setCurrentText("Yes") 
            self.ui.test_full_image_label.setVisible(True)
            self.ui.test_full_image_input.setVisible(True)  
            self.ui.inst_seg_yz_filtering_label.setVisible(True) 
            self.ui.inst_seg_yz_filtering_input.setVisible(True) 
            self.ui.inst_seg_yz_filtering_size_label.setVisible(True) 
            self.ui.inst_seg_yz_filtering_size_input.setVisible(True) 
            self.ui.inst_seg_z_filtering_label.setVisible(True) 
            self.ui.inst_seg_z_filtering_input.setVisible(True) 
            self.ui.inst_seg_z_filtering_size_label.setVisible(True) 
            self.ui.inst_seg_z_filtering_size_input.setVisible(True) 
            self.ui.sem_seg_yz_filtering_label.setVisible(True) 
            self.ui.sem_seg_yz_filtering_input.setVisible(True) 
            self.ui.sem_seg_yz_filtering_size_label.setVisible(True) 
            self.ui.sem_seg_yz_filtering_size_input.setVisible(True) 
            self.ui.sem_seg_z_filtering_label.setVisible(True) 
            self.ui.sem_seg_z_filtering_input.setVisible(True) 
            self.ui.sem_seg_z_filtering_size_label.setVisible(True) 
            self.ui.sem_seg_z_filtering_size_input.setVisible(True) 
            self.ui.det_yz_filtering_label.setVisible(True) 
            self.ui.det_yz_filtering_input.setVisible(True) 
            self.ui.det_yz_filtering_size_label.setVisible(True) 
            self.ui.det_yz_filtering_size_input.setVisible(True) 
            self.ui.det_z_filtering_label.setVisible(True) 
            self.ui.det_z_filtering_input.setVisible(True) 
            self.ui.det_z_filtering_size_label.setVisible(True) 
            self.ui.det_z_filtering_size_input.setVisible(True) 
        # 3D
        else:
            self.ui.patch_size_input.setValidator(self.four_number_parenthesis_validator)
            self.ui.patch_size_input.setText("(40,128,128,1)")
            self.ui.train_resolution_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.train_resolution_input.setText("(1,1,1)")
            self.ui.train_overlap_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.train_overlap_input.setText("(0,0,0)")
            self.ui.train_padding_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.train_padding_input.setText("(0,0,0)")
            self.ui.validation_resolution_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.validation_resolution_input.setText("(1,1,1)")
            self.ui.validation_overlap_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.validation_overlap_input.setText("(0,0,0)")
            self.ui.validation_padding_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.validation_padding_input.setText("(0,0,0)")
            self.ui.test_resolution_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.test_resolution_input.setText("(1,1,1)")
            self.ui.test_overlap_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.test_overlap_input.setText("(0,0,0)")
            self.ui.test_padding_input.setValidator(self.three_number_parenthesis_validator)
            self.ui.test_padding_input.setText("(0,0,0)")
            self.ui.da_z_flip_label.setVisible(True)
            self.ui.da_z_flip_input.setVisible(True)
            self.ui.test_2d_as_3d_stack_label.setVisible(False)
            self.ui.test_2d_as_3d_stack_input.setVisible(False)
            self.ui.test_reduce_memory_label.setVisible(True)
            self.ui.test_reduce_memory_input.setVisible(True)
            self.ui.test_full_image_label.setVisible(False)
            self.ui.test_full_image_input.setVisible(False)
            self.ui.test_per_patch_input.setCurrentText("Yes")
            self.ui.test_merge_patches_input.setCurrentText("Yes")
            self.ui.test_full_image_input.setCurrentText("No") 
            self.ui.inst_seg_yz_filtering_label.setVisible(False) 
            self.ui.inst_seg_yz_filtering_input.setVisible(False) 
            self.ui.inst_seg_yz_filtering_size_label.setVisible(False) 
            self.ui.inst_seg_yz_filtering_size_input.setVisible(False) 
            self.ui.inst_seg_z_filtering_label.setVisible(False) 
            self.ui.inst_seg_z_filtering_input.setVisible(False) 
            self.ui.inst_seg_z_filtering_size_label.setVisible(False) 
            self.ui.inst_seg_z_filtering_size_input.setVisible(False) 
            self.ui.sem_seg_yz_filtering_label.setVisible(False) 
            self.ui.sem_seg_yz_filtering_input.setVisible(False) 
            self.ui.sem_seg_yz_filtering_size_label.setVisible(False) 
            self.ui.sem_seg_yz_filtering_size_input.setVisible(False) 
            self.ui.sem_seg_z_filtering_label.setVisible(False) 
            self.ui.sem_seg_z_filtering_input.setVisible(False) 
            self.ui.sem_seg_z_filtering_size_label.setVisible(False) 
            self.ui.sem_seg_z_filtering_size_input.setVisible(False) 
            self.ui.det_yz_filtering_label.setVisible(False) 
            self.ui.det_yz_filtering_input.setVisible(False) 
            self.ui.det_yz_filtering_size_label.setVisible(False) 
            self.ui.det_yz_filtering_size_input.setVisible(False) 
            self.ui.det_z_filtering_label.setVisible(False) 
            self.ui.det_z_filtering_input.setVisible(False) 
            self.ui.det_z_filtering_size_label.setVisible(False) 
            self.ui.det_z_filtering_size_input.setVisible(False) 

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def dialog_exec(self, message):
        if self.diag is None: 
            self.diag = dialog_Ui()
            self.diag.setStyleSheet("QWidget{font-size:16px}")

        self.diag.dialog_constrict(message)
        self.diag.exec_()
    
    def error_exec(self, message, reason):
        if self.error is None: 
            self.error = error_Ui(self)
            self.error.setStyleSheet("QWidget{font-size:16px}")

        self.error.error_constrict(message, reason)
        self.error.exec_()

    def workflow_info_exec(self, workflow_name, workflow_images, workflow_description):
        if self.wokflow_info is None: 
            self.wokflow_info = workflow_explanation_Ui()
            self.wokflow_info.setStyleSheet("QWidget{font-size:16px}")

        self.wokflow_info.infoConstrict(workflow_name, workflow_images[0], 
            workflow_images[1], workflow_description)
        self.wokflow_info.exec_()

    def yes_no_exec(self, question):
        if self.yes_no is None: 
            self.yes_no = yes_no_Ui()
            self.yes_no.setStyleSheet("QWidget{font-size:16px}")

        self.yes_no.create_question(question)
        self.yes_no.exec_()

if __name__ == "__main__":
    window = None
    log_dir = os.path.join(tempfile._get_default_tempdir(), "BiaPy")
    log_file = os.path.join(log_dir, "BiaPy_"+next(tempfile._get_candidate_names())) 
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger('BiaPy')
    logging.basicConfig(filename=log_file, level=logging.ERROR)
    try:
        app = QApplication(sys.argv)
        window = MainWindow(log_file, log_dir)
        window.show()
        app.exec_()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except:
        # Log the error
        logger.exception("Main window error:")
        logger.error(traceback.format_exc())
        
        # Advise the user for the error
        error = error_Ui(window) if window is not None else error_Ui()
        error.error_constrict(log_file, "main_window_error")
        error.exec_()
        
        # Print the error in command line for debugging 
        print("Logging into file: {}".format(log_file))
        traceback.print_exc()

