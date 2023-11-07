import os
import sys
import re
import multiprocessing

from PySide2.QtCore import  QSize, QFile 
from PySide2.QtSvg import QSvgWidget

import settings
from main import * 
from run_functions import run_worker
from build_functions import build_worker
from ui_utils import get_text, resource_path, set_workflow_page, oninit_checks, load_yaml_config
from aux_classes.checkableComboBox import CheckableComboBox

class UIFunction(MainWindow):

    def initStackTab(main_window):
        """
        Initialize GUI. 
        
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        if not main_window.cfg.settings['init']:
            main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_home)
            main_window.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
            
            main_window.ui.biapy_logo_label.setPixmap(QPixmap(resource_path(os.path.join("images","biapy_logo.png"))))
            main_window.ui.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
            main_window.ui.bn_min.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hide_icon.png"))))

            main_window.ui.bn_home.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","home.png"))))
            main_window.ui.bn_workflow.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","workflow.png"))))
            main_window.ui.bn_goptions.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","goptions.png"))))
            main_window.ui.bn_train.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","train.png"))))
            main_window.ui.bn_test.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","test.png"))))
            main_window.ui.bn_run_biapy.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","run.png"))))

            main_window.ui.left_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","left_arrow.svg"))))
            main_window.ui.right_arrow_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","right_arrow.svg"))))
            main_window.ui.goptions_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            main_window.ui.train_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))
            main_window.ui.test_advanced_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","down_arrow.svg"))))

            UIFunction.init_main_page(main_window)
            oninit_checks(main_window)
            UIFunction.init_workflow_page(main_window)
            UIFunction.init_goptions_page(main_window)
            UIFunction.init_train_page(main_window)
            UIFunction.init_test_page(main_window)
            UIFunction.init_run(main_window)

            main_window.cfg.settings['init'] = True
            main_window.last_selected_workflow = -1

    def obtain_workflow_description(main_window):
        """
        Starts workflow description page. 
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        # Load first time
        if not 'workflow_description_images' in main_window.cfg.settings:
            main_window.cfg.load_workflow_detail_page()

        s_workflow = main_window.cfg.settings['selected_workflow'] 
        if s_workflow < 0:
            s_workflow = len(main_window.cfg.settings['workflow_names'])-1
        if s_workflow == len(main_window.cfg.settings['workflow_names']):
            s_workflow = 0

        workflow_name = main_window.cfg.settings['workflow_names'][s_workflow].replace("\n"," ") 
        workflow_images = main_window.cfg.settings['workflow_description_images'][s_workflow]
        workflow_description = main_window.cfg.settings['workflow_descriptions'][s_workflow]
        workflow_ready_examples = main_window.cfg.settings['ready_to_use_workflows'][s_workflow]
        workflow_doc = main_window.cfg.settings['workflow_description_doc'][s_workflow]
        main_window.workflow_info_exec(workflow_name, workflow_images, workflow_description, workflow_doc,
            workflow_ready_examples)

    ###########
    # Home page 
    ###########
    def init_main_page(main_window):
        """
        Initialize main page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)

        main_window.ui.biapy_github_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","github_icon.svg"))))
        main_window.ui.biapy_github_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_forum_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","forum_icon.svg"))))
        main_window.ui.biapy_forum_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_templates_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","template_icon.svg"))))
        main_window.ui.biapy_templates_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_doc_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","doc_icon.svg"))))
        main_window.ui.biapy_doc_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_notebooks_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","notebook_icon.svg"))))
        main_window.ui.biapy_notebooks_bn.setIconSize(QSize(40, 40))
        main_window.ui.biapy_citation_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","citation_icon.svg"))))
        main_window.ui.biapy_citation_bn.setIconSize(QSize(31, 31))

        main_window.ui.biapy_github_ext_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","open_external_link.svg"))))
        main_window.ui.biapy_forum_ext_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","open_external_link.svg"))))
        main_window.ui.biapy_templates_ext_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","open_external_link.svg"))))
        main_window.ui.biapy_doc_ext_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","open_external_link.svg"))))
        main_window.ui.biapy_notebooks_ext_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","open_external_link.svg"))))
        main_window.ui.biapy_citation_ext_bn.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","open_external_link.svg"))))

        # Create docker logo and text here. This last is necessary to do it here and not in ui_main.py
        # because they are inserted in order 
        dockerlogo = QtCore.QFile(resource_path(os.path.join("images","docker_logo.svg")))
        dockerlogo.open(QtCore.QIODevice.ReadWrite)
        main_window.docker_logo_bytearray_str = dockerlogo.readAll()
        dockerlogo.close()
        main_window.ui.docker_logo = QSvgWidget()
        main_window.ui.docker_logo.setObjectName(u"docker_logo")
        main_window.ui.docker_logo.setMinimumSize(QSize(220, 56))
        main_window.ui.docker_logo.setMaximumSize(QSize(220, 56))
        main_window.ui.docker_logo.load(main_window.docker_logo_bytearray_str)
        main_window.ui.verticalLayout_28.addWidget(main_window.ui.docker_logo, alignment=QtCore.Qt.AlignCenter)

        main_window.ui.docker_status_label = QLabel(main_window.ui.docker_frame)
        main_window.ui.docker_status_label.setObjectName(u"docker_status_label")
        main_window.ui.docker_status_label.setMinimumSize(QSize(0, 0))
        main_window.ui.docker_status_label.setMaximumSize(QSize(16777215, 16777215))
        main_window.ui.docker_status_label.setFont(font)
        main_window.ui.docker_status_label.setAlignment(Qt.AlignCenter)
        main_window.ui.docker_status_label.setWordWrap(True)
        main_window.ui.docker_status_label.setOpenExternalLinks(True)
        main_window.ui.verticalLayout_28.addWidget(main_window.ui.docker_status_label)

        # GPU logo and text
        gpu_icon = QtCore.QFile(resource_path(os.path.join("images","gpu_icon.svg")))
        gpu_icon.open(QtCore.QIODevice.ReadWrite)
        main_window.gpu_icon_bytearray_str = gpu_icon.readAll()
        gpu_icon.close()
        main_window.ui.gpu_icon_label = QSvgWidget()
        main_window.ui.gpu_icon_label.setObjectName(u"gpu_icon_label")
        main_window.ui.gpu_icon_label.setMinimumSize(QSize(122, 80))
        main_window.ui.gpu_icon_label.setMaximumSize(QSize(122, 80))
        main_window.ui.gpu_icon_label.load(main_window.gpu_icon_bytearray_str)
        main_window.ui.verticalLayout_33.addWidget(main_window.ui.gpu_icon_label, alignment=QtCore.Qt.AlignCenter)

        main_window.ui.gpu_status_label = QLabel(main_window.ui.gpu_frame)
        main_window.ui.gpu_status_label.setObjectName(u"gpu_status_label")
        main_window.ui.gpu_status_label.setMinimumSize(QSize(0, 0))
        main_window.ui.gpu_status_label.setFont(font)
        main_window.ui.gpu_status_label.setAlignment(Qt.AlignCenter)
        main_window.ui.gpu_status_label.setWordWrap(True)
        main_window.ui.gpu_status_label.setOpenExternalLinks(True)
        main_window.ui.verticalLayout_33.addWidget(main_window.ui.gpu_status_label)

        # yes no diagram svg
        main_window.ui.yes_no_diagram1_label = QSvgWidget(resource_path(os.path.join("images","bn_images","yes_no_arrow.svg")), parent=main_window.ui.frame_6)
        main_window.ui.yes_no_diagram1_label.setObjectName(u"yes_no_diagram1_label")
        main_window.ui.yes_no_diagram1_label.setGeometry(QRect(180, 30, 121, 120))
        main_window.ui.yes_no_diagram1_label.setMinimumSize(QSize(121, 120))
        main_window.ui.yes_no_diagram1_label.setMaximumSize(QSize(121, 120))
        main_window.ui.yes_no_diagram1_label.raise_()
        main_window.ui.yes_no_diagram2_label = QSvgWidget(resource_path(os.path.join("images","bn_images","yes_no_arrow.svg")), parent=main_window.ui.frame_6)
        main_window.ui.yes_no_diagram2_label.setObjectName(u"yes_no_diagram2_label")
        main_window.ui.yes_no_diagram2_label.setGeometry(QRect(480, 60, 121, 120))
        main_window.ui.yes_no_diagram2_label.setMinimumSize(QSize(121, 120))
        main_window.ui.yes_no_diagram2_label.setMaximumSize(QSize(121, 120))
        main_window.ui.yes_no_diagram2_label.raise_()

    ###############
    # Workflow page 
    ###############
    def init_workflow_page(main_window):
        """
        Initialize workflow page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.workflow_view1_frame.setEnabled(False)
        main_window.ui.workflow_view3_frame.setEnabled(False)

    def move_workflow_view(main_window, isleft):
        main_window.last_selected_workflow = main_window.cfg.settings['selected_workflow']
        if isleft:
            main_window.cfg.settings['selected_workflow'] = main_window.cfg.settings['selected_workflow'] - 1 if main_window.cfg.settings['selected_workflow'] != 0 else len(main_window.cfg.settings['workflow_names'])-1
        else: 
            main_window.cfg.settings['selected_workflow'] = main_window.cfg.settings['selected_workflow'] + 1 if main_window.cfg.settings['selected_workflow'] != len(main_window.cfg.settings['workflow_names'])-1 else 0
        set_workflow_page(main_window)

    ######################
    # General options page 
    ######################
    def init_goptions_page(main_window):
        """
        Initialize general options page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.goptions_advanced_options_scrollarea.setVisible(False)
        main_window.ui.PATHS__CHECKPOINT_FILE__INPUT.setVisible(False)
        main_window.ui.checkpoint_file_path_browse_bn.setVisible(False)
        main_window.ui.checkpoint_file_path_browse_label.setVisible(False)
        main_window.ui.checkpoint_loading_opt_label.setVisible(False)
        main_window.ui.checkpoint_loading_opt_frame.setVisible(False)

        main_window.ui.SYSTEM__NUM_CPUS__INPUT.addItem("All")
        for i in range(multiprocessing.cpu_count()):
            main_window.ui.SYSTEM__NUM_CPUS__INPUT.addItem(str(i+1))

    def change_problem_dimensions(main_window, idx):
        """
        Change all variables in GUI that depend on the image dimension selected. E.g. ``2D`` or ``3D``.

        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.

        idx : int
            Image dimension to work with. If ``0`` means 2D and 3D otherwise. 
        """
        # 2D
        if idx == 0:
            main_window.ui.DATA__PATCH_SIZE__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__PATCH_SIZE__INPUT.setText("(256,256,1)")
            main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1)")
            main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0)")
            main_window.ui.DATA__TRAIN__PADDING__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0)")
            main_window.ui.DATA__VAL__RESOLUTION__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1)")
            main_window.ui.DATA__VAL__OVERLAP__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0)")
            main_window.ui.DATA__VAL__PADDING__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__VAL__PADDING__INPUT.setText("(0,0)")
            main_window.ui.DATA__TEST__RESOLUTION__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1)")
            main_window.ui.DATA__TEST__OVERLAP__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0)")
            main_window.ui.DATA__TEST__PADDING__INPUT.setValidator(main_window.two_pos_number_parenthesis_validator)
            main_window.ui.DATA__TEST__PADDING__INPUT.setText("(0,0)")
            main_window.ui.da_z_flip_label.setVisible(False)
            main_window.ui.AUGMENTOR__ZFLIP__INPUT.setVisible(False)
            main_window.ui.test_2d_as_3d_stack_label.setVisible(True)
            main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT.setVisible(True)
            main_window.ui.test_reduce_memory_label.setVisible(False)
            main_window.ui.TEST__REDUCE_MEMORY__INPUT.setVisible(False)
            main_window.ui.TEST__STATS__PER_PATCH__INPUT.setCurrentText("No")
            main_window.ui.TEST__STATS__MERGE_PATCHES__INPUT.setCurrentText("No")
            main_window.ui.TEST__STATS__FULL_IMG__INPUT.setCurrentText("Yes") 
            main_window.ui.test_full_image_label.setVisible(True)
            main_window.ui.TEST__STATS__FULL_IMG__INPUT.setVisible(True)  
            main_window.ui.inst_seg_yz_filtering_label.setVisible(True) 
            main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT.setVisible(True) 
            main_window.ui.inst_seg_z_filtering_label.setVisible(True) 
            main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT.setVisible(True) 
            main_window.ui.sem_seg_yz_filtering_label.setVisible(True) 
            main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT.setVisible(True) 
            main_window.ui.sem_seg_z_filtering_label.setVisible(True) 
            main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT.setVisible(True) 
            main_window.ui.det_yz_filtering_label.setVisible(True) 
            main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT.setVisible(True) 
            main_window.ui.det_z_filtering_label.setVisible(True) 
            main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT.setVisible(True) 
            if main_window.cfg.settings['selected_workflow'] == 4:
                models = main_window.cfg.settings['sr_2d_models_real_names']
        # 3D
        else:
            main_window.ui.DATA__PATCH_SIZE__INPUT.setValidator(main_window.four_number_parenthesis_validator)
            main_window.ui.DATA__PATCH_SIZE__INPUT.setText("(40,128,128,1)")
            main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__TRAIN__RESOLUTION__INPUT.setText("(1,1,1)")
            main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__TRAIN__OVERLAP__INPUT.setText("(0,0,0)")
            main_window.ui.DATA__TRAIN__PADDING__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__TRAIN__PADDING__INPUT.setText("(0,0,0)")
            main_window.ui.DATA__VAL__RESOLUTION__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__VAL__RESOLUTION__INPUT.setText("(1,1,1)")
            main_window.ui.DATA__VAL__OVERLAP__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__VAL__OVERLAP__INPUT.setText("(0,0,0)")
            main_window.ui.DATA__VAL__PADDING__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__VAL__PADDING__INPUT.setText("(0,0,0)")
            main_window.ui.DATA__TEST__RESOLUTION__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__TEST__RESOLUTION__INPUT.setText("(1,1,1)")
            main_window.ui.DATA__TEST__OVERLAP__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__TEST__OVERLAP__INPUT.setText("(0,0,0)")
            main_window.ui.DATA__TEST__PADDING__INPUT.setValidator(main_window.three_number_parenthesis_validator)
            main_window.ui.DATA__TEST__PADDING__INPUT.setText("(0,0,0)")
            main_window.ui.da_z_flip_label.setVisible(True)
            main_window.ui.AUGMENTOR__ZFLIP__INPUT.setVisible(True)
            main_window.ui.test_2d_as_3d_stack_label.setVisible(False)
            main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT.setVisible(False)
            main_window.ui.test_reduce_memory_label.setVisible(True)
            main_window.ui.TEST__REDUCE_MEMORY__INPUT.setVisible(True)
            main_window.ui.test_full_image_label.setVisible(False)
            main_window.ui.TEST__STATS__FULL_IMG__INPUT.setVisible(False)
            main_window.ui.TEST__STATS__PER_PATCH__INPUT.setCurrentText("Yes")
            main_window.ui.TEST__STATS__MERGE_PATCHES__INPUT.setCurrentText("Yes")
            main_window.ui.TEST__STATS__FULL_IMG__INPUT.setCurrentText("No") 
            main_window.ui.inst_seg_yz_filtering_label.setVisible(False) 
            main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT.setVisible(False) 
            main_window.ui.inst_seg_z_filtering_label.setVisible(False) 
            main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT.setVisible(False) 
            main_window.ui.sem_seg_yz_filtering_label.setVisible(False) 
            main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT.setVisible(False) 
            main_window.ui.sem_seg_z_filtering_label.setVisible(False) 
            main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT.setVisible(False) 
            main_window.ui.det_yz_filtering_label.setVisible(False) 
            main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT.setVisible(False) 
            main_window.ui.det_z_filtering_label.setVisible(False) 
            main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT.setVisible(False) 
            if main_window.cfg.settings['selected_workflow'] == 4:
                models = main_window.cfg.settings['sr_3d_models_real_names']

        if main_window.cfg.settings['selected_workflow'] == 4:
            main_window.ui.MODEL__ARCHITECTURE__INPUT.clear()
            main_window.ui.MODEL__ARCHITECTURE__INPUT.addItems(models)

    ############
    # Train page 
    ############
    def init_train_page(main_window):       
        """
        Initialize train page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """ 
        # Hide validation paths as it is extracted from train by default 
        main_window.ui.DATA__VAL__PATH__LABEL.setVisible(False)
        main_window.ui.DATA__VAL__PATH__INPUT.setVisible(False)
        main_window.ui.val_data_input_browse_bn.setVisible(False)
        main_window.ui.validation_data_gt_label.setVisible(False)
        main_window.ui.DATA__VAL__GT_PATH__INPUT.setVisible(False)
        main_window.ui.val_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.val_in_memory_label.setVisible(False)
        main_window.ui.DATA__VAL__IN_MEMORY__INPUT.setVisible(False)
        main_window.ui.percentage_validation_label.setVisible(True)
        main_window.ui.DATA__VAL__SPLIT_TRAIN__INPUT.setVisible(True)
        main_window.ui.cross_validation_nfolds_label.setVisible(False)
        main_window.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT.setVisible(False)
        main_window.ui.cross_validation_fold_label.setVisible(False)
        main_window.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT.setVisible(False)
        main_window.ui.train_advanced_options_frame.setVisible(False)
        main_window.ui.adamw_weight_decay_label.setVisible(False)
        main_window.ui.TRAIN__W_DECAY__INPUT.setVisible(False)
        main_window.ui.profiler_batch_range_label.setVisible(False)
        main_window.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT.setVisible(False)
        main_window.ui.custom_mean_label.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT.setVisible(False)
        main_window.ui.custom_std_label.setVisible(False)
        main_window.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT.setVisible(False)
        main_window.ui.lr_schel_min_lr_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__MIN_LR__INPUT.setVisible(False)
        main_window.ui.lr_schel_reduce_on_plat_patience_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT.setVisible(False)
        main_window.ui.lr_schel_reduce_on_plat_factor_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT.setVisible(False)
        main_window.ui.lr_schel_warmupcosine_epochs_label.setVisible(False)
        main_window.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT.setVisible(False)
        main_window.ui.da_frame.setVisible(False)
        main_window.ui.da_random_rot_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__RANDOM_ROT_RANGE__INPUT.setVisible(False)
        main_window.ui.da_shear_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__SHEAR_RANGE__INPUT.setVisible(False)
        main_window.ui.da_zoom_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__ZOOM_RANGE__INPUT.setVisible(False)
        main_window.ui.da_shift_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__SHIFT_RANGE__INPUT.setVisible(False)
        main_window.ui.da_shift_range_label.setVisible(False)
        main_window.ui.da_elastic_alpha_label.setVisible(False)
        main_window.ui.AUGMENTOR__E_ALPHA__INPUT.setVisible(False)
        main_window.ui.da_elastic_sigma_label.setVisible(False)
        main_window.ui.AUGMENTOR__E_SIGMA__INPUT.setVisible(False)
        main_window.ui.da_elastic_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__E_MODE__INPUT.setVisible(False)
        main_window.ui.da_gaussian_sigma_label.setVisible(False)
        main_window.ui.AUGMENTOR__G_SIGMA__INPUT.setVisible(False)
        main_window.ui.da_median_blur_k_size_label.setVisible(False)
        main_window.ui.AUGMENTOR__MB_KERNEL__INPUT.setVisible(False)
        main_window.ui.da_motion_blur_k_size_label.setVisible(False)
        main_window.ui.AUGMENTOR__MOTB_K_RANGE__INPUT.setVisible(False)
        main_window.ui.da_gamma_contrast_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__GC_GAMMA__INPUT.setVisible(False)
        main_window.ui.da_brightness_factor_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INPUT.setVisible(False)
        main_window.ui.da_brightness_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT.setVisible(False)
        main_window.ui.da_contrast_factor_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT.setVisible(False)
        main_window.ui.da_contrast_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_MODE__INPUT.setVisible(False)
        main_window.ui.da_brightness_em_factor_label.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_EM_FACTOR__INPUT.setVisible(False)
        main_window.ui.da_brightness_em_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__BRIGHTNESS_EM_MODE__INPUT.setVisible(False)
        main_window.ui.da_contrast_em_factor_label.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_EM_FACTOR__INPUT.setVisible(False)
        main_window.ui.da_contrast_em_mode_label.setVisible(False)
        main_window.ui.AUGMENTOR__CONTRAST_EM_MODE__INPUT.setVisible(False)
        main_window.ui.da_dropout_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__DROP_RANGE__INPUT.setVisible(False)
        main_window.ui.da_cutout_number_iterations_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_SIZE__INPUT.setVisible(False)
        main_window.ui.da_cutout_size_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_NB_ITERATIONS__INPUT.setVisible(False)
        main_window.ui.da_cuout_cval_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_CVAL__INPUT.setVisible(False)
        main_window.ui.da_cutout_to_mask_label.setVisible(False)
        main_window.ui.AUGMENTOR__COUT_APPLY_TO_MASK__INPUT.setVisible(False)
        main_window.ui.da_cutblur_size_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_SIZE__INPUT.setVisible(False)
        main_window.ui.da_cutblut_down_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INPUT.setVisible(False)
        main_window.ui.da_cutblur_inside_label.setVisible(False)
        main_window.ui.AUGMENTOR__CBLUR_INSIDE__INPUT.setVisible(False)
        main_window.ui.da_cutmix_size_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CMIX_SIZE__INPUT.setVisible(False)
        main_window.ui.da_cutnoise_scale_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_SCALE__INPUT.setVisible(False)
        main_window.ui.da_cutnoise_number_iter_label.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT.setVisible(False)
        main_window.ui.da_cutnoise_size_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__CNOISE_SIZE__INPUT.setVisible(False)
        main_window.ui.da_misaligment_rotate_ratio_label.setVisible(False)
        main_window.ui.AUGMENTOR__MS_ROTATE_RATIO__INPUT.setVisible(False)
        main_window.ui.da_misaligment_displacement_label.setVisible(False)
        main_window.ui.AUGMENTOR__MS_DISPLACEMENT__INPUT.setVisible(False)
        main_window.ui.da_missing_sections_iteration_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__MISSP_ITERATIONS__INPUT.setVisible(False)
        main_window.ui.da_grid_ratio_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_RATIO__INPUT.setVisible(False)
        main_window.ui.da_grid_d_range_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_D_RANGE__INPUT.setVisible(False)
        main_window.ui.da_grid_rotate_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_ROTATE__INPUT.setVisible(False)
        main_window.ui.da_grid_invert_label.setVisible(False)
        main_window.ui.AUGMENTOR__GRID_INVERT__INPUT.setVisible(False)
        main_window.ui.da_gaussian_noise_mean_label.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT.setVisible(False)
        main_window.ui.da_gaussian_noise_var_label.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT.setVisible(False)
        main_window.ui.da_gaussian_noise_use_input_img_label.setVisible(False)
        main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT.setVisible(False)
        main_window.ui.da_salt_amount_label.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AMOUNT__INPUT.setVisible(False)
        main_window.ui.da_pepper_amount_label.setVisible(False)
        main_window.ui.AUGMENTOR__PEPPER_AMOUNT__INPUT.setVisible(False)
        main_window.ui.da_salt_pepper_amount_label.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT.setVisible(False)
        main_window.ui.da_salt_pepper_prop_label.setVisible(False)
        main_window.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT.setVisible(False)

        # Semantic seg
        main_window.ui.extract_random_patch_frame_label.setVisible(False)
        main_window.ui.extract_random_patch_frame.setVisible(False)

        # Instance seg
        main_window.ui.PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__LABEL.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT.setVisible(False)

    ###########
    # Test page 
    ###########
    def init_test_page(main_window):
        """
        Initialize test page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.ui.test_data_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        main_window.ui.test_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.use_val_as_test.setVisible(False)
        main_window.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT.setVisible(False)
        main_window.ui.inst_seg_ths_frame.setVisible(False)
        main_window.ui.inst_seg_b_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT.setVisible(False)
        main_window.ui.inst_seg_c_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT.setVisible(False)
        main_window.ui.inst_seg_fore_mask_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT.setVisible(False)
        main_window.ui.inst_seg_p_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT.setVisible(False)
        main_window.ui.inst_seg_d_channel_th_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT.setVisible(False)
        main_window.ui.inst_seg_fore_dil_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT.setVisible(False)
        main_window.ui.inst_seg_fore_ero_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT.setVisible(False)
        main_window.ui.inst_seg_small_obj_fil_before_size_label.setVisible(False)
        main_window.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT.setVisible(False)
        main_window.ui.inst_seg_yz_filtering_size_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INST_SEG__INPUT.setVisible(False)
        main_window.ui.inst_seg_z_filtering_size_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__INST_SEG__INPUT.setVisible(False)
        main_window.ui.inst_seg_voronoi_mask_th_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT.setVisible(False)
        main_window.ui.inst_seg_remove_close_points_radius_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT.setVisible(False)
        main_window.ui.sem_seg_yz_filtering_size_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__SEM_SEG__INPUT.setVisible(False)
        main_window.ui.sem_seg_z_filtering_size_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__SEM_SEG__INPUT.setVisible(False)
        main_window.ui.det_yz_filtering_size_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__DET__INPUT.setVisible(False)
        main_window.ui.det_z_filtering_size_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__DET__INPUT.setVisible(False)
        main_window.ui.det_remove_close_points_radius_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT.setVisible(False)
        main_window.ui.det_watershed_first_dilation_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT.setVisible(False)
        main_window.ui.det_watershed_donuts_classes_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT.setVisible(False)
        main_window.ui.det_watershed_donuts_patch_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT.setVisible(False)
        main_window.ui.det_watershed_donuts_nucleus_diam_label.setVisible(False)
        main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT.setVisible(False)
        main_window.ui.det_data_watetshed_check_label.setVisible(False)
        main_window.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INPUT.setVisible(False)
        main_window.ui.test_advanced_options_frame.setVisible(False)

    def init_run(main_window):
        """
        Initialize run page.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        if len(main_window.cfg.settings['GPUs']) > 0:
            # Create GPU input field
            main_window.ui.gpu_input = CheckableComboBox(main_window.ui.gpu_list_frame)
            main_window.ui.gpu_input.setObjectName(u"gpu_input")
            main_window.ui.gpu_input.setMinimumSize(QSize(400, 30))
            main_window.ui.gpu_input.setMaximumSize(QSize(400, 30))
            font = QFont()
            font.setFamily(u"DejaVu Math TeX Gyre")
            font.setPointSize(12)
            main_window.ui.gpu_input.setFont(font)
            main_window.ui.verticalLayout_40.addWidget(main_window.ui.gpu_input, 0, Qt.AlignHCenter)
            for i, gpu in enumerate(main_window.cfg.settings['GPUs']):
                main_window.ui.gpu_input.addItem("{} : {} ".format(i, gpu.name), check=True if i == 0 else False)
        else:
            main_window.ui.gpu_list_frame.setVisible(False)
            main_window.ui.run_workflow_frame.setFrameShape(QFrame.NoFrame)

    def build_container(main_window):
        """
        Start container bulding process. 
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        main_window.cfg.settings['building_thread'] = None
        main_window.cfg.settings['building_worker'] = None
        main_window.cfg.settings['building_threads'] = QThread()
        outf = main_window.log_dir if main_window.cfg.settings['output_folder'] == "" else main_window.cfg.settings['output_folder']
        main_window.cfg.settings['building_worker'] = build_worker(main_window, main_window.cfg.settings['biapy_container_dockerfile'], 
            main_window.cfg.settings['biapy_container_name'], outf)
        main_window.cfg.settings['building_worker'].moveToThread(main_window.cfg.settings['building_threads'])
        main_window.cfg.settings['building_threads'].started.connect(main_window.cfg.settings['building_worker'].run)
        main_window.cfg.settings['building_worker'].finished_signal.connect(main_window.cfg.settings['building_threads'].quit)
        main_window.cfg.settings['building_worker'].finished_signal.connect(lambda: UIFunction.update_container_status_in_build(main_window, main_window.cfg.settings['building_worker'].finished_good))
        main_window.cfg.settings['building_worker'].close_signal.connect(main_window.cfg.settings['building_worker'].deleteLater) 
        main_window.cfg.settings['building_threads'].finished.connect(main_window.cfg.settings['building_threads'].deleteLater)
        main_window.cfg.settings['building_worker'].update_log_signal.connect(main_window.cfg.settings['building_worker'].gui.update_gui)
        main_window.cfg.settings['building_worker'].update_build_progress_signal.connect(main_window.cfg.settings['building_worker'].gui.update_building_progress)
        main_window.cfg.settings['building_threads'].start()

    def update_container_status_in_build(main_window, signal):
        """
        Updates container status during its building process. 
        
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        
        signal : int
            Signal from the bulding process thread. 
        """
        # If the container was built correctly 
        if signal == 0:
            main_window.cfg.settings['biapy_container_ready'] = True
            main_window.ui.docker_head_label.setText("Dependencies")
            main_window.ui.docker_frame.setStyleSheet("")

    def run_biapy(main_window):
        """
        Run BiaPy container in a different thread.
                
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        # Load the YAML file selected
        r = load_yaml_config(main_window)
        if not r: return
        
        # Job name check
        jobname = get_text(main_window.ui.job_name_input)
        if jobname == "":
            main_window.dialog_exec("Job name can not be empty", "jobname")
            return

        # Output folder check
        if main_window.cfg.settings['output_folder'] == "":
            main_window.dialog_exec("Output folder must be defined", "output_folder")
            return 

        # Docker installation check
        if not main_window.cfg.settings['docker_found']:
            main_window.dialog_exec("Docker installation not found. Please, install it before running BiaPy in its\
                    <a href=\"https://docs.docker.com/get-docker/\">official documentation</a>. Once you have \
                    done that please restart this application.", "docker_installation")
            return
        if not main_window.cfg.settings['biapy_container_ready']:
            main_window.dialog_exec("You need to build BiaPy's container first. You will be redirected yo the main page "
                "so you can do it.", "docker_installation")
            return

        # GPU check
        use_gpu = True
        if len(main_window.cfg.settings['GPUs']) == 0 or len(main_window.ui.gpu_input.currentData()) == 0:
            use_gpu = False 

        # Initialize thread/worker 
        main_window.cfg.settings['running_threads'].append(QThread())
        worker_id = len(main_window.cfg.settings['running_workers'])
        main_window.cfg.settings['running_workers'].append(run_worker(main_window, main_window.cfg.settings['biapy_cfg'], main_window.cfg.settings['biapy_container_name'], 
            worker_id, main_window.cfg.settings['output_folder'], main_window.cfg.settings['user_host'], use_gpu))

        # Set up signals so the mainn thread, in charge of updating the GUI, can do it
        main_window.cfg.settings['running_workers'][worker_id].moveToThread(main_window.cfg.settings['running_threads'][worker_id])
        main_window.cfg.settings['running_threads'][worker_id].started.connect(main_window.cfg.settings['running_workers'][worker_id].run)
        main_window.cfg.settings['running_workers'][worker_id].finished_signal.connect(main_window.cfg.settings['running_threads'][worker_id].quit)
        main_window.cfg.settings['running_workers'][worker_id].finished_signal.connect(main_window.cfg.settings['running_workers'][worker_id].deleteLater)
        main_window.cfg.settings['running_threads'][worker_id].finished.connect(main_window.cfg.settings['running_threads'][worker_id].deleteLater)
        main_window.cfg.settings['running_workers'][worker_id].update_log_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_gui)
        main_window.cfg.settings['running_workers'][worker_id].update_cont_state_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_cont_state)
        main_window.cfg.settings['running_workers'][worker_id].update_train_progress_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_train_progress)
        main_window.cfg.settings['running_workers'][worker_id].update_test_progress_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_test_progress)
        main_window.cfg.settings['running_workers'][worker_id].update_pulling_progress_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.update_pulling_progress)
        main_window.cfg.settings['running_workers'][worker_id].update_pulling_signal.connect(main_window.cfg.settings['running_workers'][worker_id].gui.pulling_progress)
        
        # Start thread 
        main_window.cfg.settings['running_threads'][worker_id].start()
