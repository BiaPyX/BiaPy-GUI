import os
import sys
import re
import multiprocessing

from PySide2.QtCore import  QSize
from PySide2.QtSvg import QSvgWidget

import settings
from main import * 
from run_functions import run_worker
from build_functions import build_worker
from ui_utils import get_text, resource_path, set_workflow_page, update_container_status, oninit_checks, load_yaml_config
from checkableComboBox import CheckableComboBox

class UIFunction(MainWindow):

    def initStackTab(self):
        if not self.cfg.settings['init']:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
            
            self.ui.biapy_logo_label.setPixmap(QPixmap(resource_path(os.path.join("images","biapy_logo.png"))))
            self.ui.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
            self.ui.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hide_icon.png"))))

            self.ui.bn_home.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","home.png"))))
            self.ui.bn_workflow.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","workflow.png"))))
            self.ui.bn_goptions.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","goptions.png"))))
            self.ui.bn_train.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","train.png"))))
            self.ui.bn_test.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","test.png"))))
            self.ui.bn_run_biapy.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","run.png"))))

            self.ui.left_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","left_arrow.svg"))))
            self.ui.right_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","right_arrow.svg"))))
            self.ui.goptions_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            self.ui.train_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            self.ui.test_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))

            UIFunction.init_main_page(self)
            oninit_checks(self)
            UIFunction.init_workflow_page(self)
            UIFunction.init_goptions_page(self)
            UIFunction.init_train_page(self)
            UIFunction.init_test_page(self)

            self.cfg.settings['init'] = True
    
    def obtain_workflow_description(self):
        """
        Starts workflow description page. 
        """
        # Load first time
        if not 'workflow_description_images' in self.cfg.settings:
            self.cfg.load_workflow_detail_page()

        s_workflow = self.cfg.settings['selected_workflow'] 
        if s_workflow < 0:
            s_workflow = len(self.cfg.settings['workflow_names'])-1
        if s_workflow == len(self.cfg.settings['workflow_names']):
            s_workflow = 0

        workflow_name = self.cfg.settings['workflow_names'][s_workflow].replace("\n"," ") 
        workflow_images = self.cfg.settings['workflow_description_images'][s_workflow]
        workflow_description = self.cfg.settings['workflow_descriptions'][s_workflow]
        workflow_ready_examples = self.cfg.settings['ready_to_use_workflows'][s_workflow]
        workflow_doc = self.cfg.settings['workflow_description_doc'][s_workflow]
        self.workflow_info_exec(workflow_name, workflow_images, workflow_description, workflow_doc,
            workflow_ready_examples)

    ###########
    # Home page 
    ###########
    def init_main_page(self):
        # pixmap = QPixmap(resource_path(os.path.join("images","docker_logo.png")))
        # pixmap = pixmap.scaledToWidth(220,aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)

        self.ui.biapy_github_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","github_icon.svg"))))
        self.ui.biapy_github_bn.setIconSize(QSize(40, 40))
        self.ui.biapy_forum_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","forum_icon.svg"))))
        self.ui.biapy_forum_bn.setIconSize(QSize(40, 40))
        self.ui.biapy_templates_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","template_icon.svg"))))
        self.ui.biapy_templates_bn.setIconSize(QSize(40, 40))
        self.ui.biapy_doc_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","doc_icon.svg"))))
        self.ui.biapy_doc_bn.setIconSize(QSize(40, 40))
        self.ui.biapy_notebooks_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","notebook_icon.svg"))))
        self.ui.biapy_notebooks_bn.setIconSize(QSize(40, 40))
        self.ui.biapy_citation_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","citation_icon.svg"))))
        self.ui.biapy_citation_bn.setIconSize(QSize(31, 31))

        # Create docker logo and text here. This last is necessary to do it here and not in ui_main.py
        # because they are inserted in order 
        self.ui.docker_logo = QSvgWidget(resource_path(os.path.join("images","docker_logo.svg")))
        self.ui.docker_logo.setObjectName(u"docker_logo")
        self.ui.docker_logo.setMinimumSize(QSize(220, 56))
        self.ui.docker_logo.setMaximumSize(QSize(220, 56))
        self.ui.verticalLayout_28.addWidget(self.ui.docker_logo, alignment=QtCore.Qt.AlignCenter)

        self.ui.docker_status_label = QLabel(self.ui.docker_frame)
        self.ui.docker_status_label.setObjectName(u"docker_status_label")
        self.ui.docker_status_label.setMinimumSize(QSize(0, 0))
        self.ui.docker_status_label.setMaximumSize(QSize(16777215, 16777215))
        self.ui.docker_status_label.setFont(font)
        self.ui.docker_status_label.setAlignment(Qt.AlignCenter)
        self.ui.docker_status_label.setWordWrap(True)
        self.ui.docker_status_label.setOpenExternalLinks(True)
        self.ui.verticalLayout_28.addWidget(self.ui.docker_status_label)

        # GPU logo and text
        self.ui.gpu_icon_label = QSvgWidget(resource_path(os.path.join("images","gpu_icon.svg")))
        self.ui.gpu_icon_label.setObjectName(u"gpu_icon_label")
        self.ui.gpu_icon_label.setMinimumSize(QSize(122, 80))
        self.ui.gpu_icon_label.setMaximumSize(QSize(122, 80))
        self.ui.verticalLayout_33.addWidget(self.ui.gpu_icon_label, alignment=QtCore.Qt.AlignCenter)

        self.ui.gpu_status_label = QLabel(self.ui.gpu_frame)
        self.ui.gpu_status_label.setObjectName(u"gpu_status_label")
        self.ui.gpu_status_label.setMinimumSize(QSize(0, 0))
        self.ui.gpu_status_label.setFont(font)
        self.ui.gpu_status_label.setAlignment(Qt.AlignCenter)
        self.ui.gpu_status_label.setWordWrap(True)
        self.ui.gpu_status_label.setOpenExternalLinks(True)
        self.ui.verticalLayout_33.addWidget(self.ui.gpu_status_label)

        # yes no diagram svg
        self.ui.yes_no_diagram1_label = QSvgWidget(resource_path(os.path.join("images","bn_images","yes_no_arrow.svg")), parent=self.ui.frame_6)
        self.ui.yes_no_diagram1_label.setObjectName(u"yes_no_diagram1_label")
        self.ui.yes_no_diagram1_label.setGeometry(QRect(180, 30, 121, 120))
        self.ui.yes_no_diagram1_label.setMinimumSize(QSize(121, 120))
        self.ui.yes_no_diagram1_label.setMaximumSize(QSize(121, 120))
        self.ui.yes_no_diagram1_label.raise_()
        self.ui.yes_no_diagram2_label = QSvgWidget(resource_path(os.path.join("images","bn_images","yes_no_arrow.svg")), parent=self.ui.frame_6)
        self.ui.yes_no_diagram2_label.setObjectName(u"yes_no_diagram2_label")
        self.ui.yes_no_diagram2_label.setGeometry(QRect(480, 60, 121, 120))
        self.ui.yes_no_diagram2_label.setMinimumSize(QSize(121, 120))
        self.ui.yes_no_diagram2_label.setMaximumSize(QSize(121, 120))
        self.ui.yes_no_diagram2_label.raise_()

    ###############
    # Workflow page 
    ###############
    def init_workflow_page(self):
        self.ui.workflow_view1_frame.setEnabled(False)
        self.ui.workflow_view3_frame.setEnabled(False)

    def move_workflow_view(self, isleft):
        if isleft:
            self.cfg.settings['selected_workflow'] = self.cfg.settings['selected_workflow'] - 1 if self.cfg.settings['selected_workflow'] != 0 else len(self.cfg.settings['workflow_names'])-1
        else: 
            self.cfg.settings['selected_workflow'] = self.cfg.settings['selected_workflow'] + 1 if self.cfg.settings['selected_workflow'] != len(self.cfg.settings['workflow_names'])-1 else 0
        set_workflow_page(self)

    ######################
    # General options page 
    ######################
    def init_goptions_page(self):
        self.ui.goptions_advanced_options_scrollarea.setVisible(False)
        self.ui.PATHS__CHECKPOINT_FILE__INPUT.setVisible(False)
        self.ui.checkpoint_file_path_browse_bn.setVisible(False)
        self.ui.checkpoint_file_path_browse_label.setVisible(False)

        self.ui.SYSTEM__NUM_CPUS__INPUT.addItem("All")
        for i in range(multiprocessing.cpu_count()):
            self.ui.SYSTEM__NUM_CPUS__INPUT.addItem(str(i+1))
        
        # Create GPU input field
        self.ui.gpu_input = CheckableComboBox(self.ui.frame_2)
        self.ui.gpu_input.setObjectName(u"gpu_input")
        self.ui.gpu_input.setMinimumSize(QSize(400, 30))
        self.ui.gpu_input.setMaximumSize(QSize(400, 30))
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.ui.gpu_input.setFont(font)
        self.ui.gridLayout_5.addWidget(self.ui.gpu_input, 0, 2, 1, 1)

        for i, gpu in enumerate(self.cfg.settings['GPUs']):
            self.ui.gpu_input.addItem("{} : {} ".format(i, gpu.name), check=True if i == 0 else False)

    ############
    # Train page 
    ############
    def init_train_page(self):        
        # Hide validation paths as it is extracted from train by default 
        self.ui.DATA__VAL__PATH__LABEL.setVisible(False)
        self.ui.DATA__VAL__PATH__INPUT.setVisible(False)
        self.ui.val_data_input_browse_bn.setVisible(False)
        self.ui.validation_data_gt_label.setVisible(False)
        self.ui.DATA__VAL__GT_PATH__INPUT.setVisible(False)
        self.ui.val_data_gt_input_browse_bn.setVisible(False)
        self.ui.val_in_memory_label.setVisible(False)
        self.ui.DATA__VAL__IN_MEMORY__INPUT.setVisible(False)
        self.ui.percentage_validation_label.setVisible(True)
        self.ui.DATA__VAL__SPLIT_TRAIN__INPUT.setVisible(True)
        self.ui.cross_validation_nfolds_label.setVisible(False)
        self.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT.setVisible(False)
        self.ui.cross_validation_fold_label.setVisible(False)
        self.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT.setVisible(False)
        self.ui.train_advanced_options_frame.setVisible(False)
        self.ui.adamw_weight_decay_label.setVisible(False)
        self.ui.TRAIN__W_DECAY__INPUT.setVisible(False)
        self.ui.profiler_batch_range_label.setVisible(False)
        self.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT.setVisible(False)
        self.ui.custom_mean_label.setVisible(False)
        self.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT.setVisible(False)
        self.ui.custom_std_label.setVisible(False)
        self.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT.setVisible(False)
        self.ui.lr_schel_min_lr_label.setVisible(False)
        self.ui.TRAIN__LR_SCHEDULER__MIN_LR__INPUT.setVisible(False)
        self.ui.lr_schel_reduce_on_plat_patience_label.setVisible(False)
        self.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT.setVisible(False)
        self.ui.lr_schel_reduce_on_plat_factor_label.setVisible(False)
        self.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT.setVisible(False)
        self.ui.lr_schel_warmupcosine_lr_label.setVisible(False)
        self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_LR__INPUT.setVisible(False)
        self.ui.lr_schel_warmupcosine_epochs_label.setVisible(False)
        self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT.setVisible(False)
        self.ui.lr_schel_warmupcosine_hold_epochs_label.setVisible(False)
        self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_HOLD_EPOCHS__INPUT.setVisible(False)
        self.ui.da_frame.setVisible(False)
        self.ui.da_random_rot_range_label.setVisible(False)
        self.ui.AUGMENTOR__RANDOM_ROT_RANGE__INPUT.setVisible(False)
        self.ui.da_shear_range_label.setVisible(False)
        self.ui.AUGMENTOR__SHEAR_RANGE__INPUT.setVisible(False)
        self.ui.da_zoom_range_label.setVisible(False)
        self.ui.AUGMENTOR__ZOOM_RANGE__INPUT.setVisible(False)
        self.ui.da_shift_range_label.setVisible(False)
        self.ui.AUGMENTOR__SHIFT_RANGE__INPUT.setVisible(False)
        self.ui.da_shift_range_label.setVisible(False)
        self.ui.da_elastic_alpha_label.setVisible(False)
        self.ui.AUGMENTOR__E_ALPHA__INPUT.setVisible(False)
        self.ui.da_elastic_sigma_label.setVisible(False)
        self.ui.AUGMENTOR__E_SIGMA__INPUT.setVisible(False)
        self.ui.da_elastic_mode_label.setVisible(False)
        self.ui.AUGMENTOR__E_MODE__INPUT.setVisible(False)
        self.ui.da_gaussian_sigma_label.setVisible(False)
        self.ui.AUGMENTOR__G_SIGMA__INPUT.setVisible(False)
        self.ui.da_median_blur_k_size_label.setVisible(False)
        self.ui.AUGMENTOR__MB_KERNEL__INPUT.setVisible(False)
        self.ui.da_motion_blur_k_size_label.setVisible(False)
        self.ui.AUGMENTOR__MOTB_K_RANGE__INPUT.setVisible(False)
        self.ui.da_gamma_contrast_range_label.setVisible(False)
        self.ui.AUGMENTOR__GC_GAMMA__INPUT.setVisible(False)
        self.ui.da_brightness_factor_range_label.setVisible(False)
        self.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INPUT.setVisible(False)
        self.ui.da_brightness_mode_label.setVisible(False)
        self.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT.setVisible(False)
        self.ui.da_contrast_factor_range_label.setVisible(False)
        self.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT.setVisible(False)
        self.ui.da_contrast_mode_label.setVisible(False)
        self.ui.AUGMENTOR__CONTRAST_MODE__INPUT.setVisible(False)
        self.ui.da_brightness_em_factor_label.setVisible(False)
        self.ui.AUGMENTOR__BRIGHTNESS_EM_FACTOR__INPUT.setVisible(False)
        self.ui.da_brightness_em_mode_label.setVisible(False)
        self.ui.AUGMENTOR__BRIGHTNESS_EM_MODE__INPUT.setVisible(False)
        self.ui.da_contrast_em_factor_label.setVisible(False)
        self.ui.AUGMENTOR__CONTRAST_EM_FACTOR__INPUT.setVisible(False)
        self.ui.da_contrast_em_mode_label.setVisible(False)
        self.ui.AUGMENTOR__CONTRAST_EM_MODE__INPUT.setVisible(False)
        self.ui.da_dropout_range_label.setVisible(False)
        self.ui.AUGMENTOR__DROP_RANGE__INPUT.setVisible(False)
        self.ui.da_cutout_number_iterations_label.setVisible(False)
        self.ui.AUGMENTOR__COUT_SIZE__INPUT.setVisible(False)
        self.ui.da_cutout_size_label.setVisible(False)
        self.ui.AUGMENTOR__COUT_NB_ITERATIONS__INPUT.setVisible(False)
        self.ui.da_cuout_cval_label.setVisible(False)
        self.ui.AUGMENTOR__COUT_CVAL__INPUT.setVisible(False)
        self.ui.da_cutout_to_mask_label.setVisible(False)
        self.ui.AUGMENTOR__COUT_APPLY_TO_MASK__INPUT.setVisible(False)
        self.ui.da_cutblur_size_range_label.setVisible(False)
        self.ui.AUGMENTOR__CBLUR_SIZE__INPUT.setVisible(False)
        self.ui.da_cutblut_down_range_label.setVisible(False)
        self.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INPUT.setVisible(False)
        self.ui.da_cutblur_inside_label.setVisible(False)
        self.ui.AUGMENTOR__CBLUR_INSIDE__INPUT.setVisible(False)
        self.ui.da_cutmix_size_range_label.setVisible(False)
        self.ui.AUGMENTOR__CMIX_SIZE__INPUT.setVisible(False)
        self.ui.da_cutnoise_scale_range_label.setVisible(False)
        self.ui.AUGMENTOR__CNOISE_SCALE__INPUT.setVisible(False)
        self.ui.da_cutnoise_number_iter_label.setVisible(False)
        self.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT.setVisible(False)
        self.ui.da_cutnoise_size_range_label.setVisible(False)
        self.ui.AUGMENTOR__CNOISE_SIZE__INPUT.setVisible(False)
        self.ui.da_misaligment_rotate_ratio_label.setVisible(False)
        self.ui.AUGMENTOR__MS_ROTATE_RATIO__INPUT.setVisible(False)
        self.ui.da_misaligment_displacement_label.setVisible(False)
        self.ui.AUGMENTOR__MS_DISPLACEMENT__INPUT.setVisible(False)
        self.ui.da_missing_sections_iteration_range_label.setVisible(False)
        self.ui.AUGMENTOR__MISSP_ITERATIONS__INPUT.setVisible(False)
        self.ui.da_grid_ratio_label.setVisible(False)
        self.ui.AUGMENTOR__GRID_RATIO__INPUT.setVisible(False)
        self.ui.da_grid_d_range_label.setVisible(False)
        self.ui.AUGMENTOR__GRID_D_RANGE__INPUT.setVisible(False)
        self.ui.da_grid_rotate_label.setVisible(False)
        self.ui.AUGMENTOR__GRID_ROTATE__INPUT.setVisible(False)
        self.ui.da_grid_invert_label.setVisible(False)
        self.ui.AUGMENTOR__GRID_INVERT__INPUT.setVisible(False)
        self.ui.da_gaussian_noise_mean_label.setVisible(False)
        self.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT.setVisible(False)
        self.ui.da_gaussian_noise_var_label.setVisible(False)
        self.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT.setVisible(False)
        self.ui.da_gaussian_noise_use_input_img_label.setVisible(False)
        self.ui.AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT.setVisible(False)
        self.ui.da_salt_amount_label.setVisible(False)
        self.ui.AUGMENTOR__SALT_AMOUNT__INPUT.setVisible(False)
        self.ui.da_pepper_amount_label.setVisible(False)
        self.ui.AUGMENTOR__PEPPER_AMOUNT__INPUT.setVisible(False)
        self.ui.da_salt_pepper_amount_label.setVisible(False)
        self.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT.setVisible(False)
        self.ui.da_salt_pepper_prop_label.setVisible(False)
        self.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT.setVisible(False)

        # Semantic seg
        self.ui.extract_random_patch_frame_label.setVisible(False)
        self.ui.extract_random_patch_frame.setVisible(False)

    def model_combobox_changed(self, model_name):
        model_name = self.cfg.translate_model_names(model_name, get_text(self.ui.PROBLEM__NDIM__INPUT)) 

        self.ui.unet_model_like_frame.setVisible(False)
        self.ui.unet_model_like_label.setVisible(False)
        self.ui.tiramisu_frame.setVisible(False)
        self.ui.tiramisu_label.setVisible(False)
        self.ui.transformers_frame.setVisible(False)
        self.ui.transformers_label.setVisible(False)
        self.ui.sr_unet_like_heading.setVisible(False)
        self.ui.sr_unet_like_frame.setVisible(False)

        if model_name in ['unet', 'resunet', 'seunet', 'attention_unet']:
            self.ui.unet_model_like_frame.setVisible(True)
            self.ui.unet_model_like_label.setVisible(True)
            self.ui.sr_unet_like_heading.setVisible(True)
            self.ui.sr_unet_like_frame.setVisible(True)
        elif model_name == "tiramisu":
            self.ui.tiramisu_frame.setVisible(True)
            self.ui.tiramisu_label.setVisible(True)
        elif model_name in ["unetr", "ViT", "mae"]:
            self.ui.transformers_frame.setVisible(True)
            self.ui.transformers_label.setVisible(True)

            if model_name == "unetr":
                self.ui.transformers_label.setText("UNETR")
                self.ui.unetr_vit_hidden_multiple_label.setVisible(True)
                self.ui.MODEL__UNETR_VIT_HIDD_MULT__INPUT.setVisible(True)
                self.ui.unetr_num_filters_label.setVisible(True)
                self.ui.MODEL__UNETR_VIT_NUM_FILTERS__INPUT.setVisible(True)
                self.ui.unetr_dec_act_label.setVisible(True)
                self.ui.MODEL__UNETR_DEC_ACTIVATION__INPUT.setVisible(True)
                self.ui.unetr_dec_kernel_init_label.setVisible(True)
                self.ui.MODEL__UNETR_DEC_KERNEL_INIT__INPUT.setVisible(True)
            else:
                self.ui.unetr_vit_hidden_multiple_label.setVisible(False)
                self.ui.MODEL__UNETR_VIT_HIDD_MULT__INPUT.setVisible(False)
                self.ui.unetr_num_filters_label.setVisible(False)
                self.ui.MODEL__UNETR_VIT_NUM_FILTERS__INPUT.setVisible(False)
                self.ui.unetr_dec_act_label.setVisible(False)
                self.ui.MODEL__UNETR_DEC_ACTIVATION__INPUT.setVisible(False)
                self.ui.unetr_dec_kernel_init_label.setVisible(False)
                self.ui.MODEL__UNETR_DEC_KERNEL_INIT__INPUT.setVisible(False)
                if model_name == "ViT":
                    self.ui.transformers_label.setText("ViT")
                else: # MAE
                    self.ui.transformers_label.setText("MAE")

    ###########
    # Test page 
    ###########
    
    def init_test_page(self):
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.use_val_as_test.setVisible(False)
        self.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT.setVisible(False)
        self.ui.inst_seg_ths_frame.setVisible(False)
        self.ui.inst_seg_b_channel_th_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT.setVisible(False)
        self.ui.inst_seg_c_channel_th_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT.setVisible(False)
        self.ui.inst_seg_fore_mask_th_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT.setVisible(False)
        self.ui.inst_seg_p_channel_th_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT.setVisible(False)
        self.ui.inst_seg_d_channel_th_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT.setVisible(False)
        self.ui.inst_seg_fore_dil_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT.setVisible(False)
        self.ui.inst_seg_fore_ero_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT.setVisible(False)
        self.ui.inst_seg_small_obj_fil_before_size_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT.setVisible(False)
        self.ui.inst_seg_small_obj_fil_after_size_label.setVisible(False)
        self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_AFTER__INPUT.setVisible(False)
        self.ui.inst_seg_yz_filtering_size_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INST_SEG__INPUT.setVisible(False)
        self.ui.inst_seg_z_filtering_size_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__INST_SEG__INPUT.setVisible(False)
        self.ui.inst_seg_voronoi_mask_th_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT.setVisible(False)
        self.ui.inst_seg_remove_close_points_radius_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT.setVisible(False)
        self.ui.sem_seg_yz_filtering_size_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__SEM_SEG__INPUT.setVisible(False)
        self.ui.sem_seg_z_filtering_size_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__SEM_SEG__INPUT.setVisible(False)
        self.ui.det_yz_filtering_size_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__DET__INPUT.setVisible(False)
        self.ui.det_z_filtering_size_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__DET__INPUT.setVisible(False)
        self.ui.det_remove_close_points_radius_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT.setVisible(False)
        self.ui.det_watershed_first_dilation_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT.setVisible(False)
        self.ui.det_watershed_donuts_classes_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT.setVisible(False)
        self.ui.det_watershed_donuts_patch_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT.setVisible(False)
        self.ui.det_watershed_donuts_nucleus_diam_label.setVisible(False)
        self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT.setVisible(False)
        self.ui.det_data_watetshed_check_label.setVisible(False)
        self.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INPUT.setVisible(False)
        self.ui.test_advanced_options_frame.setVisible(False)

    def build_container(self):
        self.cfg.settings['building_thread'] = None
        self.cfg.settings['building_worker'] = None
        self.cfg.settings['building_threads'] = QThread()
        outf = self.log_dir if self.cfg.settings['output_folder'] == "" else self.cfg.settings['output_folder']
        self.cfg.settings['building_worker'] = build_worker(self, self.cfg.settings['biapy_container_dockerfile'], 
            self.cfg.settings['biapy_container_name'], outf)
        self.cfg.settings['building_worker'].moveToThread(self.cfg.settings['building_threads'])
        self.cfg.settings['building_threads'].started.connect(self.cfg.settings['building_worker'].run)
        self.cfg.settings['building_worker'].finished_signal.connect(self.cfg.settings['building_threads'].quit)
        self.cfg.settings['building_worker'].finished_signal.connect(lambda: update_container_status(self, self.cfg.settings['building_worker'].finished_good))
        self.cfg.settings['building_worker'].close_signal.connect(self.cfg.settings['building_worker'].deleteLater) 
        self.cfg.settings['building_threads'].finished.connect(self.cfg.settings['building_threads'].deleteLater)
        self.cfg.settings['building_worker'].update_log_signal.connect(self.cfg.settings['building_worker'].gui.update_gui)
        self.cfg.settings['building_worker'].update_build_progress_signal.connect(self.cfg.settings['building_worker'].gui.update_building_progress)
        self.cfg.settings['building_threads'].start()
        
    def run_biapy(self):
        # Load the YAML file selected
        r = load_yaml_config(self)
        if not r: return
        
        # Job name check
        jobname = get_text(self.ui.job_name_input)
        if jobname == "":
            self.dialog_exec("Job name can not be empty", "jobname")
            return

        # Output folder check
        if self.cfg.settings['output_folder'] == "":
            self.dialog_exec("Output folder must be defined", "output_folder")
            return 

        # Docker installation check
        if not self.cfg.settings['docker_found']:
            self.dialog_exec("Docker installation not found. Please, install it before running BiaPy in its\
                    <a href=\"https://docs.docker.com/get-docker/\">official documentation</a>. Once you have \
                    done that please restart this application.", "docker_installation")
            return
        if not self.cfg.settings['biapy_container_ready']:
            self.dialog_exec("You need to build BiaPy's container first. You will be redirected yo the main page "
                "so you can do it.", "docker_installation")
            return

        # GPU check
        use_gpu = True
        if len(self.cfg.settings['GPUs']) == 0 or len(self.ui.gpu_input.currentData()) == 0:
            use_gpu = False 

        self.cfg.settings['running_threads'].append(QThread())
        worker_id = len(self.cfg.settings['running_workers'])
        self.cfg.settings['running_workers'].append(run_worker(self, self.cfg.settings['biapy_cfg'], self.cfg.settings['biapy_container_name'], 
            worker_id, self.cfg.settings['output_folder'], self.cfg.settings['user_host'], use_gpu))
        self.cfg.settings['running_workers'][worker_id].moveToThread(self.cfg.settings['running_threads'][worker_id])
        self.cfg.settings['running_threads'][worker_id].started.connect(self.cfg.settings['running_workers'][worker_id].run)
        self.cfg.settings['running_workers'][worker_id].finished_signal.connect(self.cfg.settings['running_threads'][worker_id].quit)
        self.cfg.settings['running_workers'][worker_id].finished_signal.connect(self.cfg.settings['running_workers'][worker_id].deleteLater)
        self.cfg.settings['running_threads'][worker_id].finished.connect(self.cfg.settings['running_threads'][worker_id].deleteLater)
        self.cfg.settings['running_workers'][worker_id].update_log_signal.connect(self.cfg.settings['running_workers'][worker_id].gui.update_gui)
        self.cfg.settings['running_workers'][worker_id].update_cont_state_signal.connect(self.cfg.settings['running_workers'][worker_id].gui.update_cont_state)
        self.cfg.settings['running_workers'][worker_id].update_train_progress_signal.connect(self.cfg.settings['running_workers'][worker_id].gui.update_train_progress)
        self.cfg.settings['running_workers'][worker_id].update_test_progress_signal.connect(self.cfg.settings['running_workers'][worker_id].gui.update_test_progress)
        self.cfg.settings['running_workers'][worker_id].update_pulling_progress_signal.connect(self.cfg.settings['running_workers'][worker_id].gui.update_pulling_progress)
        self.cfg.settings['running_workers'][worker_id].update_pulling_signal.connect(self.cfg.settings['running_workers'][worker_id].gui.pulling_progress)
        self.cfg.settings['running_threads'][worker_id].start()
