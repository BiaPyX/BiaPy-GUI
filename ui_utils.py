import os 
import sys
import traceback
import docker
import ast 
import GPUtil

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import *

import settings
from biapy_config import Config
from biapy_check_configuration import check_configuration

def examine(main_window, save_in_obj_tag=None, is_file=True):
    if not is_file:
        out = QFileDialog.getExistingDirectory(main_window, 'Select a directory')
        out_write = os.path.basename(os.path.normpath(out))
    else:
        out = QFileDialog.getOpenFileName()[0]
        out_write = os.path.basename(out)

    if out == "": return # If no file was selected 

    if save_in_obj_tag is not None:
        getattr(main_window.ui, save_in_obj_tag).setText(out)
        if save_in_obj_tag == "train_data_input":
            main_window.cfg.settings['train_data_input_path'] = out 
        elif save_in_obj_tag == "train_data_gt_input":
            main_window.cfg.settings['train_data_gt_input_path'] = out 
        elif save_in_obj_tag == "validation_data_input":
            main_window.cfg.settings['validation_data_input_path'] = out 
        elif save_in_obj_tag == "validation_data_gt_input":
            main_window.cfg.settings['validation_data_gt_input_path'] = out 
        elif save_in_obj_tag == "test_data_input":
            main_window.cfg.settings['test_data_input_path'] = out 
        elif save_in_obj_tag == "test_data_gt_input":
            main_window.cfg.settings['test_data_gt_input_path'] = out  

def combobox_hide_visible_action(main_window, combobox, frames_dict, frames_dict_values_to_set=None):
    for key in frames_dict:
        visible_values = frames_dict[key]
        if not isinstance(visible_values, list):
            visible_values = [visible_values]
        if main_window.cfg.settings['selected_workflow'] in [3,5,6]:
            if '_gt_' in key:
                vis = False
            else:
                vis = True if str(getattr(main_window.ui, combobox).currentText()) in visible_values else False
        else:
            vis = True if str(getattr(main_window.ui, combobox).currentText()) in visible_values else False
        getattr(main_window.ui, key).setVisible(vis)

    if frames_dict_values_to_set is not None:
        for key in frames_dict_values_to_set:
            getattr(main_window.ui, key).setCurrentText(frames_dict_values_to_set[key]) 

def mark_syntax_error(main_window, obj, validator_type=["empty"]):
    error = False
    for v in validator_type:
        if v == "empty" and get_text(getattr(main_window.ui, obj)) == "":
            error = True
        elif v == "exists" and not os.path.exists(get_text(getattr(main_window.ui, obj))):
            error = True
    if error:
        getattr(main_window.ui, obj).setStyleSheet("border: 2px solid red;")
    else:
        getattr(main_window.ui, obj).setStyleSheet("")

        out = get_text(getattr(main_window.ui, obj))
        if obj == "goptions_browse_yaml_path_input":
            main_window.cfg.settings['yaml_config_file_path'] = out
        elif obj == "select_yaml_name_label":
            out_write = os.path.basename(out)
            main_window.cfg.settings['yaml_config_filename'] = out_write
            main_window.cfg.settings['yaml_config_file_path'] = os.path.dirname(out)
            main_window.ui.job_name_input.setPlainText(os.path.splitext(out_write)[0]+"_experiment")
        elif obj == "output_folder_input":
            main_window.cfg.settings['output_folder'] = out 

def expand_hide_advanced_options(main_window, advanced_options_bn_tag, advanced_options_frame_tag):
    expand = not getattr(main_window.ui, advanced_options_frame_tag).isVisible()
    getattr(main_window.ui, advanced_options_bn_tag).setIcon(main_window.cfg.settings['advanced_frame_images'][0] if expand else main_window.cfg.settings['advanced_frame_images'][1])
    getattr(main_window.ui, advanced_options_frame_tag).setVisible(expand)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def buttonPressed(self, buttonName, to_page):
    for each in self.ui.frame_bottom_west.findChildren(QFrame):
        if "biapy" not in each.objectName() or "frame_run_biapy" == each.objectName():
            each.setStyleSheet("background:rgb(64,144,253)")

    # Use global page_number to move as the user selected continue button
    if to_page == -1:
        move = True
        # if page_number != 1:
        #     move = UIFunction.check_input(self, page_number)
        # Do not move until the errors are corrected 
        if not move: return

        if buttonName == "up":
            self.cfg.settings['page_number'] += 1
        else:
            self.cfg.settings['page_number'] -= 1
        to_page = self.cfg.settings['page_number']

    if buttonName=='bn_home' or (buttonName=='down' and to_page == 0):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
        self.cfg.settings['page_number'] = 0

    elif buttonName=='bn_workflow' or ('bn_' not in buttonName and to_page == 1):
        self.cfg.load_workflow_page()
        self.ui.continue_bn.setText("Continue")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
        self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.workflow_selection_page)
        self.ui.frame_workflow.setStyleSheet("background:rgb(255,255,255)") 
        set_workflow_page(self)
        self.cfg.settings['page_number'] = 1
        adjust_window_progress(self)

    elif buttonName=='bn_goptions' or ('bn_' not in buttonName and to_page == 2):
        self.ui.continue_bn.setText("Continue")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
        self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.goptions_page)
        self.ui.frame_goptions.setStyleSheet("background:rgb(255,255,255)") 
        self.cfg.settings['page_number'] = 2
        adjust_window_progress(self)

    elif buttonName=='bn_train' or ('bn_' not in buttonName and to_page == 3):
        self.ui.continue_bn.setText("Continue")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
        self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.train_page)
        self.ui.frame_train.setStyleSheet("background:rgb(255,255,255)") 
        self.cfg.settings['page_number'] = 3
        adjust_window_progress(self)

    elif buttonName=='bn_test' or ('bn_' not in buttonName and to_page == 4):
        self.ui.continue_bn.setText("Generate YAML")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_create_yaml)
        self.ui.stackedWidget_create_yaml_frame.setCurrentWidget(self.ui.test_page)
        self.ui.frame_test.setStyleSheet("background:rgb(255,255,255)") 
        self.cfg.settings['page_number'] = 4
        adjust_window_progress(self)

    elif buttonName=='bn_run_biapy' or ('bn_' not in buttonName and to_page == 5):            
        error = False
        if ('bn_' not in buttonName and to_page == 5):
            error = create_yaml_file(self)

        # If there is an error do not make the movement, as the error dialog will redirect the user to the 
        # field that raises the error 
        if not error:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_run_biapy)
            self.ui.frame_run_biapy.setStyleSheet("background:rgb(255,255,255)") 
            self.cfg.settings['page_number'] = 5

    move_between_pages(self, to_page)

def set_workflow_page(self):
    # Left view
    self.ui.workflow_view1_label.setPixmap(self.cfg.settings['workflow_images'][self.cfg.settings['selected_workflow']-1])
    self.ui.workflow_view1_name_label.setText(self.cfg.settings['workflow_names'][self.cfg.settings['selected_workflow']-1])

    # Mid view
    self.ui.workflow_view2_label.setPixmap(self.cfg.settings['workflow_images'][self.cfg.settings['selected_workflow']])
    self.ui.workflow_view2_name_label.setText(self.cfg.settings['workflow_names'][self.cfg.settings['selected_workflow']])

    # Right view
    p = self.cfg.settings['selected_workflow']+1 if self.cfg.settings['selected_workflow']+1 < len(self.cfg.settings['workflow_names']) else 0
    self.ui.workflow_view3_label.setPixmap(self.cfg.settings['workflow_images'][p])
    self.ui.workflow_view3_name_label.setText(self.cfg.settings['workflow_names'][p])     

def adjust_window_progress(self):
    self.ui.window1_bn.setIcon(self.cfg.settings['dot_images'][0] if self.cfg.settings['page_number'] >= 1 else self.cfg.settings['dot_images'][1])
    self.ui.window2_bn.setIcon(self.cfg.settings['dot_images'][0] if self.cfg.settings['page_number'] >= 2 else self.cfg.settings['dot_images'][1])
    self.ui.window3_bn.setIcon(self.cfg.settings['dot_images'][0] if self.cfg.settings['page_number'] >= 3 else self.cfg.settings['dot_images'][1])
    self.ui.window4_bn.setIcon(self.cfg.settings['dot_images'][0] if self.cfg.settings['page_number'] >= 4 else self.cfg.settings['dot_images'][1])

def move_between_pages(self, to_page):
    # Semantic seg
    if self.cfg.settings['selected_workflow'] == 0:
        jobname = "my_semantic_segmentation"
        models = self.cfg.settings['semantic_models']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_semantic_seg_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_semantic_seg_page)
        # Train page
        self.ui.train_gt_label.setText("Input label folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.train_data_gt_input.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input label folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input label folder")
        self.ui.test_exists_gt_label.setText("Do you have test labels?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.test_exists_gt_input.setVisible(True)
    # Instance seg
    elif self.cfg.settings['selected_workflow'] == 1:
        jobname = "my_instance_segmentation"
        models = self.cfg.settings['instance_models']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_instance_seg_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_instance_seg_page)
        # Train page
        self.ui.train_gt_label.setText("Input label folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.train_data_gt_input.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input label folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input label folder")
        self.ui.test_exists_gt_label.setText("Do you have test labels?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.test_exists_gt_input.setVisible(True)
    # Detection
    elif self.cfg.settings['selected_workflow'] == 2:
        jobname = "my_detection"
        models = self.cfg.settings['detection_models']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_detection_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_detection_page)
        # Train page
        self.ui.train_gt_label.setText("Input CSV folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.train_data_gt_input.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input CSV folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input CSV folder")
        self.ui.test_exists_gt_label.setText("Do you have CSV files for test data?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.test_exists_gt_input.setVisible(True)
    # Denoising
    elif self.cfg.settings['selected_workflow'] == 3:
        jobname = "my_denoising"
        models = self.cfg.settings['denoising_models']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_denoising_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_denoising_page)
        # Train page
        self.ui.train_gt_label.setVisible(False)
        self.ui.train_data_gt_input.setVisible(False)
        self.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.test_data_gt_input.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.test_exists_gt_label.setVisible(False)
        self.ui.test_exists_gt_input.setVisible(False)
    # Super resolution
    elif self.cfg.settings['selected_workflow'] == 4:
        jobname = "my_super_resolution"
        models = self.cfg.settings['sr_models']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_sr_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_sr_page)
        # Train page
        self.ui.train_gt_label.setText("Input high-resolution image folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.train_data_gt_input.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input high-resolution image folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input high-resolution image folder")
        self.ui.test_exists_gt_label.setText("Do you have high-resolution test data?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.test_exists_gt_input.setVisible(True)
    # Self-supevised learning
    elif self.cfg.settings['selected_workflow'] == 5:
        jobname = "my_self_supervised_learning"
        models = self.cfg.settings['ssl_models']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_ssl_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_ssl_page)
        # Train page
        self.ui.train_gt_label.setVisible(False)
        self.ui.train_data_gt_input.setVisible(False)
        self.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.test_data_gt_input.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.test_exists_gt_label.setVisible(False)
        self.ui.test_exists_gt_input.setVisible(False)
    # Classification
    elif self.cfg.settings['selected_workflow'] == 6:
        jobname = "my_classification"
        models = self.cfg.settings['classification_models']
        goptions_tab_widget_visible = True
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_classification_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_classification_page)
        # Train page
        self.ui.train_gt_label.setVisible(False)
        self.ui.train_data_gt_input.setVisible(False)
        self.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.test_data_gt_input.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.test_exists_gt_label.setText("Is the test separated in classes?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.test_exists_gt_input.setVisible(True)

    actual_name = get_text(self.ui.job_name_input)
    if actual_name in ["", "my_semantic_segmentation", "my_instance_segmentation", "my_detection", "my_denoising", \
        "my_super_resolution", "my_self_supervised_learning", "my_classification"]:
        if to_page == 5:
            self.ui.job_name_input.setPlainText(jobname)

    # General options page
    if to_page == 2:
        self.ui.goptions_advanced_options_scrollarea.setVisible(False)

    # Train page
    self.ui.model_input.clear()
    self.ui.model_input.addItems(models)

def update_container_status(self, signal):
    # If the container was built correctly 
    if signal == 0:
        self.cfg.settings['biapy_container_ready'] = True
        self.ui.docker_head_label.setText("Dependencies")
        self.ui.docker_frame.setStyleSheet("")

def oninit_checks(self):
    # Docker check
    try:
        docker_client = docker.from_env()
        self.cfg.settings['docker_found'] = True
    except:
        self.cfg.settings['docker_found'] = False
        print(traceback.format_exc())
    if self.cfg.settings['docker_found']:
        self.ui.docker_status_label.setText("<br>Docker installation found")
        self.cfg.settings['biapy_container_ready'] = True
        self.ui.docker_head_label.setText("Docker dependency")
        self.ui.docker_frame.setStyleSheet("#gpu_frame { border: 3px solid green; border-radius: 25px;}")
    else:
        self.ui.docker_status_label.setText("Docker installation not found. Please, install it before running BiaPy in \
                <a href=\"https://biapy.readthedocs.io/en/latest/get_started/installation.html#docker-installation/\">its documentation</a>. \
                Once you have done that please restart this application.")
        self.ui.docker_head_label.setText("Docker dependency error")
        self.ui.docker_frame.setStyleSheet("#docker_frame { border: 3px solid red; border-radius: 25px;}")

    # GPU check
    self.cfg.settings['GPUs'] = GPUtil.getGPUs()
    if len(self.cfg.settings['GPUs']) > 0:
        if len(self.cfg.settings['GPUs']) == 1:
            self.ui.gpu_status_label.setText("1 NVIDIA GPU card found")
        else:
            self.ui.gpu_status_label.setText("{} NVIDIA GPU cards found".format(len(self.cfg.settings['GPUs'])))
        self.ui.gpu_head_label.setText("GPU dependency")
        self.ui.gpu_frame.setStyleSheet("#gpu_frame { border: 3px solid green; border-radius: 25px;}")
    else:
        self.ui.gpu_status_label.setText("No NVIDIA GPU card was found. BiaPy will run on the CPU, which is much slower!")
        self.ui.gpu_head_label.setText("GPU dependency error")
        self.ui.gpu_frame.setStyleSheet("#gpu_frame { border: 3px solid red; border-radius: 25px;}")


def get_text(obj):
    if isinstance(obj, QComboBox):
        return obj.currentText()
    elif isinstance(obj, QLineEdit):
        return obj.text()
    else: #QTextBrowser
        return obj.toPlainText()
        
def create_yaml_file(self):        
    biapy_config = {}

    # System
    biapy_config['SYSTEM'] = {}
    
    cpus = get_text(self.ui.maxcpu_combobox)
    cpus = -1 if cpus == "all" else int(cpus)
    biapy_config['SYSTEM']['NUM_CPUS'] = cpus

    # Problem specification
    workflow_names_yaml = ['SEMANTIC_SEG', 'INSTANCE_SEG', 'DETECTION', 'DENOISING', 'SUPER_RESOLUTION', 
        'SELF_SUPERVISED', 'CLASSIFICATION']
    biapy_config['PROBLEM'] = {}
    biapy_config['PROBLEM']['TYPE'] = workflow_names_yaml[self.cfg.settings['selected_workflow']]
    biapy_config['PROBLEM']['NDIM'] = get_text(self.ui.dimensions_comboBox)

    ### INSTANCE_SEG
    if self.cfg.settings['selected_workflow'] == 1:
        biapy_config['PROBLEM']['INSTANCE_SEG'] = {}
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNELS'] = get_text(self.ui.inst_seg_data_channels_input)
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNEL_WEIGHTS'] = get_text(self.ui.inst_seg_channel_weigths_input) 
        if get_text(self.ui.inst_seg_contour_mode_combobox) != "thick":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CONTOUR_MODE'] = get_text(self.ui.inst_seg_contour_mode_combobox)

        if 'B' in get_text(self.ui.inst_seg_data_channels_input):
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_BINARY_MASK'] = float(get_text(self.ui.inst_seg_b_channel_th_input))
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_FOREGROUND'] = float(get_text(self.ui.inst_seg_fore_mask_th_input))
        if 'C' in get_text(self.ui.inst_seg_data_channels_input):
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_CONTOUR'] = float(get_text(self.ui.inst_seg_c_channel_th_input))
        if 'D' in get_text(self.ui.inst_seg_data_channels_input):    
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_DISTANCE'] = float(get_text(self.ui.inst_seg_d_channel_th_input))
        if 'P' in get_text(self.ui.inst_seg_data_channels_input): 
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_POINTS'] = float(get_text(self.ui.inst_seg_p_channel_th_input))
        if get_text(self.ui.inst_seg_small_obj_fil_before_input) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_BEFORE_MW'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_BEFORE'] = int(get_text(self.ui.inst_seg_small_obj_fil_before_size_input))
        if get_text(self.ui.inst_seg_small_obj_fil_after_input) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_AFTER_MW'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_AFTER'] = int(get_text(self.ui.inst_seg_small_obj_fil_after_size_input))
        if get_text(self.ui.inst_seg_moph_op_input) != "[]":
            biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_SEQUENCE'] = ast.literal_eval(get_text(self.ui.inst_seg_moph_op_input) )
        if get_text(self.ui.inst_seg_moph_op_rad_input) != "[]":
            biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_RADIUS'] =  ast.literal_eval(get_text(self.ui.inst_seg_moph_op_rad_input))
        if get_text(self.ui.inst_seg_ero_dil_fore_input) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['ERODE_AND_DILATE_FOREGROUND'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_EROSION_RADIUS'] = int(get_text(self.ui.inst_seg_fore_dil_input))
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_DILATION_RADIUS'] = int(get_text(self.ui.inst_seg_fore_ero_input))

        # biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_OPTIMIZE_THS'] = False
        # biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHECK_MW'] = True
        
    ### DETECTION
    elif self.cfg.settings['selected_workflow'] == 2:
        biapy_config['PROBLEM']['DETECTION'] = {}
        biapy_config['PROBLEM']['DETECTION']['CENTRAL_POINT_DILATION'] = int(get_text(self.ui.det_central_point_dilation_input))
        biapy_config['PROBLEM']['DETECTION']['CHECK_POINTS_CREATED'] = True if get_text(self.ui.det_central_point_dilation_input) == "Yes" else False
        if get_text(self.ui.det_data_watetshed_check_input) == "Yes" and get_text(self.ui.det_watershed_input) == "Yes":
            biapy_config['PROBLEM']['DETECTION']['DATA_CHECK_MW'] = True

    ### DENOISING
    elif self.cfg.settings['selected_workflow'] == 3:
        biapy_config['PROBLEM']['DENOISING'] = {}
        biapy_config['PROBLEM']['DENOISING']['N2V_PERC_PIX'] = float(get_text(self.ui.deno_n2v_perc_pix_input))
        biapy_config['PROBLEM']['DENOISING']['N2V_MANIPULATOR'] = get_text(self.ui.deno_n2v_manipulator_input)
        biapy_config['PROBLEM']['DENOISING']['N2V_NEIGHBORHOOD_RADIUS'] = int(get_text(self.ui.deno_n2v_neighborhood_radius_input))
        biapy_config['PROBLEM']['DENOISING']['N2V_STRUCTMASK'] = True if get_text(self.ui.deno_n2v_neighborhood_struct_input) == "Yes" else False

    ### SUPER_RESOLUTION
    elif self.cfg.settings['selected_workflow'] == 4:
        biapy_config['PROBLEM']['SUPER_RESOLUTION'] = {}
        biapy_config['PROBLEM']['SUPER_RESOLUTION']['UPSCALING'] = int(get_text(self.ui.sr_upscaling_input))

    ### SELF_SUPERVISED
    elif self.cfg.settings['selected_workflow'] == 5:
        biapy_config['PROBLEM']['SELF_SUPERVISED'] = {}
        biapy_config['PROBLEM']['SELF_SUPERVISED']['RESIZING_FACTOR'] = int(get_text(self.ui.ssl_resizing_factor_input))
        biapy_config['PROBLEM']['SELF_SUPERVISED']['NOISE'] = float(get_text(self.ui.ssl_noise_input))

    # Dataset
    biapy_config['DATA'] = {}
    if get_text(self.ui.check_gen_input) == "Yes":
        biapy_config['DATA']['CHECK_GENERATORS'] = True

    biapy_config['DATA']['PATCH_SIZE'] = get_text(self.ui.patch_size_input)
    if get_text(self.ui.extract_random_patch_input) == "Yes":
        biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = True
        if get_text(self.ui.sem_seg_random_patch_prob_map_input) == "Yes":
            biapy_config['DATA']['PROBABILITY_MAP'] = True
            biapy_config['DATA']['W_FOREGROUND'] = float(get_text(self.ui.sem_seg_random_patch_fore_weights_input))
            biapy_config['DATA']['W_BACKGROUND'] = float(get_text(self.ui.sem_seg_random_patch_back_weights_input)) 
    else:
        biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = False

    if get_text(self.ui.reflect_to_complete_shape_input) == "Yes":
        biapy_config['DATA']['REFLECT_TO_COMPLETE_SHAPE'] = True

    if get_text(self.ui.normalization_type_input) == "custom":
        biapy_config['DATA']['NORMALIZATION'] = {}
        biapy_config['DATA']['NORMALIZATION']['TYPE'] = 'custom'
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_MEAN'] = float(get_text(self.ui.custom_mean_input)) 
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_STD'] = float(get_text(self.ui.custom_std_input)) 

    # Train
    if get_text(self.ui.enable_train_input) == "Yes":
        biapy_config['DATA']['TRAIN'] = {}

        # biapy_config['DATA']['TRAIN']['CHECK_DATA'] = True
        
        biapy_config['DATA']['TRAIN']['IN_MEMORY'] = True if get_text(self.ui.train_in_memory_comboBox) == "Yes" else False
        biapy_config['DATA']['TRAIN']['PATH'] = get_text(self.ui.train_data_input)
        if self.cfg.settings['selected_workflow'] not in [4,6,7]:
            biapy_config['DATA']['TRAIN']['GT_PATH'] = get_text(self.ui.train_data_gt_input)
        if int(get_text(self.ui.replicate_data_input)) != 0:
            biapy_config['DATA']['TRAIN']['REPLICATE'] = int(get_text(self.ui.replicate_data_input))
        biapy_config['DATA']['TRAIN']['OVERLAP'] = get_text(self.ui.train_overlap_input)
        biapy_config['DATA']['TRAIN']['PADDING'] = get_text(self.ui.train_padding_input)
        if get_text(self.ui.train_resolution_input) != "(1,1,1)" and get_text(self.ui.train_resolution_input) != "(1,1)":
            biapy_config['DATA']['TRAIN']['RESOLUTION'] = get_text(self.ui.train_resolution_input)
        
        if self.cfg.settings['selected_workflow'] == 0 and int(get_text(self.ui.sem_seg_minimum_fore_percentage_input)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(self.ui.sem_seg_minimum_fore_percentage_input))
        if self.cfg.settings['selected_workflow'] == 1 and int(get_text(self.ui.inst_seg_minimum_fore_percentage_input)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(self.ui.inst_seg_minimum_fore_percentage_input))
        if self.cfg.settings['selected_workflow'] == 2 and int(get_text(self.ui.det_minimum_fore_percentage_input)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(self.ui.det_minimum_fore_percentage_input))
        
        # Validation
        biapy_config['DATA']['VAL'] = {}

        if get_text(self.ui.validation_type_comboBox) == "Extract from train (split training)":
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
            biapy_config['DATA']['VAL']['SPLIT_TRAIN'] = float(get_text(self.ui.percentage_validation_input))
            biapy_config['DATA']['VAL']['RANDOM'] = True if get_text(self.ui.random_val_input) == "Yes" else False 
        elif get_text(self.ui.validation_type_comboBox) == "Extract from train (cross validation)":
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
            biapy_config['DATA']['VAL']['CROSS_VAL'] = True
            biapy_config['DATA']['VAL']['CROSS_VAL_NFOLD'] = int(get_text(self.ui.cross_validation_nfolds_input))
            biapy_config['DATA']['VAL']['CROSS_VAL_FOLD'] = int(get_text(self.ui.cross_validation_fold_input))
            biapy_config['DATA']['VAL']['RANDOM'] = True if get_text(self.ui.random_val_input) == "Yes" else False 
        # Not extracted from train (path needed)
        else:
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = False
            biapy_config['DATA']['VAL']['IN_MEMORY'] = True if get_text(self.ui.val_in_memory_comboBox) == "Yes" else False 
            biapy_config['DATA']['VAL']['PATH'] = get_text(self.ui.validation_data_input)
            if self.cfg.settings['selected_workflow'] not in [4,6,7]:
                biapy_config['DATA']['VAL']['GT_PATH'] = get_text(self.ui.validation_data_gt_input)
            biapy_config['DATA']['VAL']['OVERLAP'] = get_text(self.ui.validation_overlap_input)
            biapy_config['DATA']['VAL']['PADDING'] = get_text(self.ui.validation_padding_input)

        biapy_config['DATA']['VAL']['RESOLUTION'] = get_text(self.ui.validation_resolution_input)

    # Test
    if get_text(self.ui.enable_test_input) == "Yes":
        biapy_config['DATA']['TEST'] = {}
        # biapy_config['DATA']['TEST']['CHECK_DATA'] = True
        if get_text(self.ui.test_data_in_memory_input) == "Yes":
            biapy_config['DATA']['TEST']['IN_MEMORY'] = True
        else:
            biapy_config['DATA']['TEST']['IN_MEMORY'] = False
        if get_text(self.ui.use_val_as_test_input) == "Yes" and\
            get_text(self.ui.validation_type_comboBox) == "Extract from train (cross validation)":
            biapy_config['DATA']['TEST']['USE_VAL_AS_TEST'] = True
        else:
            if get_text(self.ui.test_exists_gt_input) == "Yes":
                biapy_config['DATA']['TEST']['LOAD_GT'] = True
                if self.cfg.settings['selected_workflow'] not in [4,6,7]:
                    biapy_config['DATA']['TEST']['GT_PATH'] = get_text(self.ui.test_data_gt_input)
            else:
                biapy_config['DATA']['TEST']['LOAD_GT'] = False
            biapy_config['DATA']['TEST']['PATH'] = get_text(self.ui.test_data_input)
            
        biapy_config['DATA']['TEST']['OVERLAP'] = get_text(self.ui.test_overlap_input)
        biapy_config['DATA']['TEST']['PADDING'] = get_text(self.ui.test_padding_input)
        if get_text(self.ui.test_median_padding_input) == "Yes":
            biapy_config['DATA']['TEST']['MEDIAN_PADDING'] = True 
        biapy_config['DATA']['TEST']['RESOLUTION'] = get_text(self.ui.test_resolution_input)
        if get_text(self.ui.test_argmax_input) == "Yes":
            biapy_config['DATA']['TEST']['ARGMAX_TO_OUTPUT'] = True


    # Data augmentation (DA)
    biapy_config['AUGMENTOR'] = {}
    if get_text(self.ui.da_enable_input) == "Yes":
        biapy_config['AUGMENTOR']['ENABLE'] = True  
        biapy_config['AUGMENTOR']['DA_PROB'] = float(get_text(self.ui.da_prob_input))
        biapy_config['AUGMENTOR']['AUG_SAMPLES'] = True if get_text(self.ui.da_check_input) == "Yes" else False 
        biapy_config['AUGMENTOR']['DRAW_GRID'] = True if get_text(self.ui.da_draw_grid_input) == "Yes" else False 
        if int(get_text(self.ui.da_num_samples_check_input)) != 10:
            biapy_config['AUGMENTOR']['AUG_NUM_SAMPLES'] = int(get_text(self.ui.da_num_samples_check_input))
        biapy_config['AUGMENTOR']['SHUFFLE_TRAIN_DATA_EACH_EPOCH'] = True if get_text(self.ui.da_shuffle_train_input) == "Yes" else False 
        biapy_config['AUGMENTOR']['SHUFFLE_VAL_DATA_EACH_EPOCH'] = True if get_text(self.ui.da_shuffle_val_input) == "Yes" else False 
        if get_text(self.ui.da_rot90_input) == "Yes":
            biapy_config['AUGMENTOR']['ROT90'] = True 
        if get_text(self.ui.da_random_rot_input) == "Yes":
            biapy_config['AUGMENTOR']['RANDOM_ROT'] = True  
            biapy_config['AUGMENTOR']['RANDOM_ROT_RANGE'] = get_text(self.ui.da_random_rot_range_input)
        if get_text(self.ui.da_shear_input) == "Yes":
            biapy_config['AUGMENTOR']['SHEAR'] = True  
            biapy_config['AUGMENTOR']['SHEAR_RANGE'] = get_text(self.ui.da_shear_range_input)
        if get_text(self.ui.da_zoom_input) == "Yes":
            biapy_config['AUGMENTOR']['ZOOM'] = True  
            biapy_config['AUGMENTOR']['ZOOM_RANGE'] = get_text(self.ui.da_zoom_range_input)
        if get_text(self.ui.da_shift_input) == "Yes":
            biapy_config['AUGMENTOR']['SHIFT'] = True 
            biapy_config['AUGMENTOR']['SHIFT_RANGE'] = get_text(self.ui.da_shift_range_input)
        if get_text(self.ui.da_shift_input) == "Yes" or get_text(self.ui.da_zoom_input) == "Yes" or\
            get_text(self.ui.da_shear_input) == "Yes" or get_text(self.ui.da_random_rot_input) == "Yes":
            biapy_config['AUGMENTOR']['AFFINE_MODE'] = get_text(self.ui.da_affine_mode_input)
        if get_text(self.ui.da_vertical_flip_input) == "Yes":
            biapy_config['AUGMENTOR']['VFLIP'] = True 
        if get_text(self.ui.da_horizontal_flip_input) == "Yes":
            biapy_config['AUGMENTOR']['HFLIP'] = True 
        if get_text(self.ui.da_z_flip_input) == "Yes":
            biapy_config['AUGMENTOR']['ZFLIP'] = True 
        if get_text(self.ui.da_elastic_input) == "Yes":
            biapy_config['AUGMENTOR']['ELASTIC'] = True 
            biapy_config['AUGMENTOR']['E_ALPHA'] = get_text(self.ui.da_elastic_alpha_input)
            biapy_config['AUGMENTOR']['E_SIGMA'] = int(get_text(self.ui.da_elastic_sigma_input))
            biapy_config['AUGMENTOR']['E_MODE'] = get_text(self.ui.da_elastic_mode_input)
        if get_text(self.ui.da_gaussian_blur_input) == "Yes":
            biapy_config['AUGMENTOR']['G_BLUR'] = True 
            biapy_config['AUGMENTOR']['G_SIGMA'] = get_text(self.ui.da_gaussian_sigma_input)
        if get_text(self.ui.da_median_blur_input) == "Yes":
            biapy_config['AUGMENTOR']['MEDIAN_BLUR'] = True 
            biapy_config['AUGMENTOR']['MB_KERNEL'] = get_text(self.ui.da_median_blur_k_size_input)
        if get_text(self.ui.da_motion_blur_input) == "Yes":
            biapy_config['AUGMENTOR']['MOTION_BLUR'] = True 
            biapy_config['AUGMENTOR']['MOTB_K_RANGE'] = get_text(self.ui.da_motion_blur_k_size_input)
        if get_text(self.ui.da_gamma_contrast_input) == "Yes":
            biapy_config['AUGMENTOR']['GAMMA_CONTRAST'] = True
            biapy_config['AUGMENTOR']['GC_GAMMA'] = get_text(self.ui.da_gamma_contrast_range_input)
        if get_text(self.ui.da_brightness_input) == "Yes":
            biapy_config['AUGMENTOR']['BRIGHTNESS'] = True
            biapy_config['AUGMENTOR']['BRIGHTNESS_FACTOR'] = get_text(self.ui.da_brightness_factor_range_input)
            biapy_config['AUGMENTOR']['BRIGHTNESS_MODE'] = get_text(self.ui.da_brightness_mode_input)
        if get_text(self.ui.da_contrast_input) == "Yes":
            biapy_config['AUGMENTOR']['CONTRAST'] = True
            biapy_config['AUGMENTOR']['CONTRAST_FACTOR'] = get_text(self.ui.da_contrast_factor)
            biapy_config['AUGMENTOR']['CONTRAST_MODE'] = get_text(self.ui.da_contrast_mode_input)
        if get_text(self.ui.da_brightness_em_input) == "Yes":
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM'] = True
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM_FACTOR'] = get_text(self.ui.da_brightness_em_factor_input)
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM_MODE'] = get_text(self.ui.da_brightness_em_mode_input)
        if get_text(self.ui.da_contrast_em_input) == "Yes":
            biapy_config['AUGMENTOR']['CONTRAST_EM'] = True
            biapy_config['AUGMENTOR']['CONTRAST_EM_FACTOR'] = get_text(self.ui.da_contrast_em_factor_input)
            biapy_config['AUGMENTOR']['CONTRAST_EM_MODE'] = get_text(self.ui.da_contrast_em_mode_input)
        if get_text(self.ui.da_dropout_input) == "Yes":
            biapy_config['AUGMENTOR']['DROPOUT'] = True
            biapy_config['AUGMENTOR']['DROP_RANGE'] = get_text(self.ui.da_dropout_range_input)
        if get_text(self.ui.da_cutout_input) == "Yes":
            biapy_config['AUGMENTOR']['CUTOUT'] = True
            biapy_config['AUGMENTOR']['COUT_NB_ITERATIONS'] = get_text(self.ui.da_cutout_number_iterations_input)
            biapy_config['AUGMENTOR']['COUT_SIZE'] = get_text(self.ui.da_cutout_size_input)
            biapy_config['AUGMENTOR']['COUT_CVAL'] = float(get_text(self.ui.da_cuout_cval_input))
            biapy_config['AUGMENTOR']['COUT_APPLY_TO_MASK'] = True if get_text(self.ui.da_cutout_to_mask_input) == "Yes" else False 
        if get_text(self.ui.da_cutblur_input) == "Yes":
            biapy_config['AUGMENTOR']['CUTBLUR'] = True
            biapy_config['AUGMENTOR']['CBLUR_SIZE'] = get_text(self.ui.da_cutblur_size_range_input)
            biapy_config['AUGMENTOR']['CBLUR_DOWN_RANGE'] = get_text(self.ui.da_cutblut_down_range_input)
            biapy_config['AUGMENTOR']['CBLUR_INSIDE'] = True if get_text(self.ui.da_cutblur_inside_input) == "Yes" else False 
        if get_text(self.ui.da_cutmix_input) == "Yes":
            biapy_config['AUGMENTOR']['CUTMIX'] = True
            biapy_config['AUGMENTOR']['CMIX_SIZE'] = get_text(self.ui.da_cutmix_size_range_input)
        if get_text(self.ui.da_cutnoise_input) == "Yes":
            biapy_config['AUGMENTOR']['CUTNOISE'] = True
            biapy_config['AUGMENTOR']['CNOISE_SCALE'] = get_text(self.ui.da_cutnoise_scale_range_input)
            biapy_config['AUGMENTOR']['CNOISE_NB_ITERATIONS'] = get_text(self.ui.da_cutnoise_number_iter_input)
            biapy_config['AUGMENTOR']['CNOISE_SIZE'] = get_text(self.ui.da_cutnoise_size_range_input)
        if get_text(self.ui.da_misaligment_input) == "Yes":
            biapy_config['AUGMENTOR']['MISALIGNMENT'] = True
            biapy_config['AUGMENTOR']['MS_DISPLACEMENT'] = int(get_text(self.ui.da_misaligment_displacement_input))
            biapy_config['AUGMENTOR']['MS_ROTATE_RATIO'] = float(get_text(self.ui.da_misaligment_rotate_ratio_input))
        if get_text(self.ui.da_missing_sections_input) == "Yes":
            biapy_config['AUGMENTOR']['MISSING_SECTIONS'] = True
            biapy_config['AUGMENTOR']['MISSP_ITERATIONS'] = get_text(self.ui.da_missing_sections_iteration_range_input)
        if get_text(self.ui.da_grayscale_input) == "Yes":
            biapy_config['AUGMENTOR']['GRAYSCALE'] = True
        if get_text(self.ui.da_channel_shuffle_input) == "Yes":
            biapy_config['AUGMENTOR']['CHANNEL_SHUFFLE'] = True
        if get_text(self.ui.da_gridmask_input) == "Yes":
            biapy_config['AUGMENTOR']['GRIDMASK'] = True
            biapy_config['AUGMENTOR']['GRID_RATIO'] = float(get_text(self.ui.da_grid_ratio_input))
            biapy_config['AUGMENTOR']['GRID_D_RANGE'] = get_text(self.ui.da_grid_d_range_input)
            biapy_config['AUGMENTOR']['GRID_ROTATE'] = float(get_text(self.ui.da_grid_rotate_input))
            biapy_config['AUGMENTOR']['GRID_INVERT'] = True if get_text(self.ui.da_grid_invert_input) == "Yes" else False 
        if get_text(self.ui.da_gaussian_noise_input) == "Yes":
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE'] = True
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_MEAN'] = float(get_text(self.ui.da_gaussian_noise_mean_input))
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_VAR'] = float(get_text(self.ui.da_gaussian_noise_var_input))
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR'] = True if get_text(self.ui.da_gaussian_noise_use_input_img_input) == "Yes" else False 
        if get_text(self.ui.da_poisson_noise_input) == "Yes":
            biapy_config['AUGMENTOR']['POISSON_NOISE'] = True
        if get_text(self.ui.da_salt_input) == "Yes":
            biapy_config['AUGMENTOR']['SALT'] = True
            biapy_config['AUGMENTOR']['SALT_AMOUNT'] = float(get_text(self.ui.da_salt_amount_input))
        if get_text(self.ui.da_pepper_input) == "Yes":
            biapy_config['AUGMENTOR']['PEPPER'] = True
            biapy_config['AUGMENTOR']['PEPPER_AMOUNT'] = float(get_text(self.ui.da_pepper_amount_input))
        if get_text(self.ui.da_salt_pepper_input) == "Yes":
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER'] = True
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER_AMOUNT'] = float(get_text(self.ui.da_salt_pepper_amount_input))
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER_PROP'] = float(get_text(self.ui.da_salt_pepper_prop_input))
    else:
        biapy_config['AUGMENTOR']['ENABLE'] = False

    # Model definition
    biapy_config['MODEL'] = {}
    biapy_config['MODEL']['ARCHITECTURE'] = get_text(self.ui.model_input)
    if get_text(self.ui.model_input) in ['unet', 'resunet', 'seunet', 'attention_unet']:
        biapy_config['MODEL']['FEATURE_MAPS'] = ast.literal_eval(get_text(self.ui.feature_maps_input))
        if get_text(self.ui.spatial_dropout_input) == "Yes":
            biapy_config['MODEL']['SPATIAL_DROPOUT'] = True  
        biapy_config['MODEL']['DROPOUT_VALUES'] = ast.literal_eval(get_text(self.ui.dropout_input)) 
        biapy_config['MODEL']['BATCH_NORMALIZATION'] = True if get_text(self.ui.batch_normalization_input) == "Yes" else False 
        if get_text(self.ui.kernel_init_input) != "he_normal":
            biapy_config['MODEL']['KERNEL_INIT'] = get_text(self.ui.kernel_init_input)
        if int(get_text(self.ui.kernel_size_input)) != 3:
            biapy_config['MODEL']['KERNEL_SIZE'] = int(get_text(self.ui.kernel_size_input))
        if get_text(self.ui.upsample_layer_input) != "convtranspose":
            biapy_config['MODEL']['UPSAMPLE_LAYER'] = get_text(self.ui.upsample_layer_input) 
        if get_text(self.ui.activation_input) != 'elu':
            biapy_config['MODEL']['ACTIVATION'] = get_text(self.ui.activation_input)
        if get_text(self.ui.last_activation_input) != 'sigmoid':
            biapy_config['MODEL']['LAST_ACTIVATION'] = get_text(self.ui.last_activation_input)
        biapy_config['MODEL']['N_CLASSES'] = int(get_text(self.ui.number_of_classes_input))
        biapy_config['MODEL']['Z_DOWN'] = ast.literal_eval(get_text(self.ui.z_down_input)) 
    elif get_text(self.ui.model_input) == "tiramisu":
        biapy_config['MODEL']['TIRAMISU_DEPTH'] = int(get_text(self.ui.tiramisu_depth_input))
        biapy_config['MODEL']['FEATURE_MAPS'] = int(get_text(self.ui.tiramisu_feature_maps_input))
        biapy_config['MODEL']['DROPOUT_VALUES'] = float(get_text(self.ui.tiramisu_dropout_input))
    elif get_text(self.ui.model_input) == "unetr":
        biapy_config['MODEL']['UNETR_TOKEN_SIZE'] = int(get_text(self.ui.unetr_token_size_input))
        biapy_config['MODEL']['UNETR_EMBED_DIM'] = int(get_text(self.ui.unetr_embed_dims_input))
        biapy_config['MODEL']['UNETR_DEPTH'] = int(get_text(self.ui.unetr_depth_input))
        biapy_config['MODEL']['UNETR_MLP_HIDDEN_UNITS'] = ast.literal_eval(get_text(self.ui.unetr_mlp_hidden_units_input))
        biapy_config['MODEL']['UNETR_NUM_HEADS'] = int(get_text(self.ui.unetr_num_heads_input))
        biapy_config['MODEL']['UNETR_VIT_HIDD_MULT'] = int(get_text(self.ui.unetr_vit_hidden_multiple_input)) 

    if get_text(self.ui.checkpoint_load_input) == "Yes":
        biapy_config['MODEL']['LOAD_CHECKPOINT'] = True 
        biapy_config['PATHS'] = {}
        if get_text(self.ui.checkpoint_file_path_input) != "":
            biapy_config['PATHS']['CHECKPOINT_FILE'] = get_text(self.ui.checkpoint_file_path_input)

    # Loss (in detection only)
    if self.cfg.settings['selected_workflow'] == 2:
        biapy_config['LOSS'] = {}
        biapy_config['LOSS']['TYPE'] = get_text(self.ui.det_loss_type_input)

    # Training phase
    biapy_config['TRAIN'] = {}
    if get_text(self.ui.enable_train_input) == "Yes":
        biapy_config['TRAIN']['ENABLE'] = True 
        biapy_config['TRAIN']['OPTIMIZER'] = get_text(self.ui.optimizer_input)
        biapy_config['TRAIN']['LR'] = float(get_text(self.ui.learning_rate_input))
        biapy_config['TRAIN']['BATCH_SIZE'] = int(get_text(self.ui.batch_size_input))
        biapy_config['TRAIN']['EPOCHS'] = int(get_text(self.ui.number_of_epochs_input)) 
        biapy_config['TRAIN']['PATIENCE'] = int(get_text(self.ui.patience_input))

        # LR Scheduler
        if get_text(self.ui.lr_schel_input) != "":
            biapy_config['TRAIN']['LR_SCHEDULER'] = {}
            biapy_config['TRAIN']['LR_SCHEDULER']['NAME'] = get_text(self.ui.lr_schel_input) 
            if get_text(self.ui.lr_schel_input) in ["warmupcosine","reduceonplateau"]: 
                biapy_config['TRAIN']['LR_SCHEDULER']['MIN_LR'] = float(get_text(self.ui.lr_schel_min_lr_input)) 
            if get_text(self.ui.lr_schel_input) == "reduceonplateau": 
                biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_FACTOR'] = float(get_text(self.ui.lr_schel_reduce_on_plat_factor_input)) 
                biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_PATIENCE'] = int(get_text(self.ui.lr_schel_reduce_on_plat_patience_input))
            if get_text(self.ui.lr_schel_input) == "warmupcosine":  
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_LR'] = float(get_text(self.ui.lr_schel_warmupcosine_lr_input))
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_EPOCHS'] = int(get_text(self.ui.lr_schel_warmupcosine_epochs_input))
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_HOLD_EPOCHS'] = int(get_text(self.ui.lr_schel_warmupcosine_hold_epochs_input))

        # Callbacks
        if get_text(self.ui.early_stopping_input) != 'val_loss':
            biapy_config['TRAIN']['EARLYSTOPPING_MONITOR'] = get_text(self.ui.early_stopping_input) 
        if get_text(self.ui.checkpoint_monitor_input) != 'val_loss':
            biapy_config['TRAIN']['CHECKPOINT_MONITOR'] = get_text(self.ui.checkpoint_monitor_input)
        if get_text(self.ui.profiler_input) == "Yes": 
            biapy_config['TRAIN']['PROFILER'] = True 
            biapy_config['TRAIN']['PROFILER_BATCH_RANGE'] = get_text(self.ui.profiler_batch_range_input)
    else:
        biapy_config['TRAIN']['ENABLE'] = False 

    # Test
    biapy_config['TEST'] = {}
    if get_text(self.ui.enable_test_input) == "Yes":    
        biapy_config['TEST']['ENABLE'] = True  
        biapy_config['TEST']['REDUCE_MEMORY'] = True if get_text(self.ui.test_reduce_memory_input) == "Yes" else False 
        biapy_config['TEST']['VERBOSE'] = True if get_text(self.ui.test_verbose_input) == "Yes" else False 
        biapy_config['TEST']['AUGMENTATION'] = True if get_text(self.ui.test_tta_input) == "Yes" else False
        if get_text(self.ui.test_evaluate_input) == "Yes" :
            biapy_config['TEST']['EVALUATE'] = True 
        if get_text(self.ui.test_2d_as_3d_stack_input) == "Yes" and get_text(self.ui.dimensions_comboBox) == "2D":
            biapy_config['TEST']['ANALIZE_2D_IMGS_AS_3D_STACK'] = True

        biapy_config['TEST']['STATS'] = {}
        biapy_config['TEST']['STATS']['PER_PATCH'] = True if get_text(self.ui.test_per_patch_input) == "Yes" else False 
        biapy_config['TEST']['STATS']['MERGE_PATCHES'] = True if get_text(self.ui.test_merge_patches_input) == "Yes" else False 
        if get_text(self.ui.test_full_image_input) == "Yes" and get_text(self.ui.dimensions_comboBox) == "2D":
            biapy_config['TEST']['STATS']['FULL_IMG'] = True 

        ### Instance segmentation
        if self.cfg.settings['selected_workflow'] == 1:
            biapy_config['TEST']['MATCHING_STATS'] = True if get_text(self.ui.inst_seg_matching_stats_input) == "Yes" else False 
            biapy_config['TEST']['MATCHING_STATS_THS'] = ast.literal_eval(get_text(self.ui.inst_seg_matching_stats_ths_input)) 
            if get_text(self.ui.inst_seg_matching_stats_colores_img_ths_input) != "[0.3]":
                biapy_config['TEST']['MATCHING_STATS_THS_COLORED_IMG'] = ast.literal_eval(get_text(self.ui.inst_seg_matching_stats_colores_img_ths_input))
            # biapy_config['TEST']['MATCHING_SEGCOMPARE'] = False 

        ### Detection
        elif self.cfg.settings['selected_workflow'] == 2:
            biapy_config['TEST']['DET_LOCAL_MAX_COORDS'] = True if get_text(self.ui.det_local_max_coords_input) == "Yes" else False 
            biapy_config['TEST']['DET_MIN_TH_TO_BE_PEAK'] = ast.literal_eval(get_text(self.ui.det_min_th_to_be_peak_input))
            biapy_config['TEST']['DET_TOLERANCE'] = ast.literal_eval(get_text(self.ui.det_tolerance_input))

        # Post-processing
        biapy_config['TEST']['POST_PROCESSING'] = {}
        ### Semantic segmentation
        if self.cfg.settings['selected_workflow'] == 0:
            if get_text(self.ui.sem_seg_yz_filtering_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(self.ui.sem_seg_yz_filtering_size_input))
            if get_text(self.ui.sem_seg_z_filtering_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(self.ui.sem_seg_z_filtering_size_input))
        ### Instance segmentation
        elif self.cfg.settings['selected_workflow'] == 1:
            if get_text(self.ui.inst_seg_yz_filtering_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(self.ui.inst_seg_yz_filtering_size_input))
            if get_text(self.ui.inst_seg_z_filtering_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(self.ui.inst_seg_z_filtering_size_input))
            if float(get_text(self.ui.inst_seg_circularity_filtering_input)) != -1:
                biapy_config['TEST']['POST_PROCESSING']['WATERSHED_CIRCULARITY'] = float(get_text(self.ui.inst_seg_circularity_filtering_input))
            if get_text(self.ui.inst_seg_data_channels_input) in ["BC", "BCM"] and get_text(self.ui.inst_seg_voronoi_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_ON_MASK'] = True 
            if get_text(self.ui.inst_seg_data_channels_input) == "BP":
                if int(get_text(self.ui.inst_seg_repare_large_blobs_input)) != -1:
                    biapy_config['TEST']['POST_PROCESSING']['REPARE_LARGE_BLOBS_SIZE'] = int(get_text(self.ui.inst_seg_repare_large_blobs_input))
                if get_text(self.ui.inst_seg_remove_close_points_input) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = ast.literal_eval(get_text(self.ui.inst_seg_remove_close_points_radius_input))
        ### Detection
        elif self.cfg.settings['selected_workflow'] == 2:
            if get_text(self.ui.det_yz_filtering_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(self.ui.det_yz_filtering_size_input))
            if get_text(self.ui.det_z_filtering_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(self.ui.det_z_filtering_size_input))
            if get_text(self.ui.det_remove_close_points_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = float(get_text(self.ui.det_remove_close_points_radius_input))
            if get_text(self.ui.det_watershed_input) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED'] = True
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_FIRST_DILATION'] = ast.literal_eval(get_text(self.ui.det_watershed_first_dilation_input) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_CLASSES'] = ast.literal_eval(get_text(self.ui.det_watershed_donuts_classes_input) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_PATCH'] = ast.literal_eval(get_text(self.ui.det_watershed_donuts_patch_input) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER'] = int(get_text(self.ui.det_watershed_donuts_nucleus_diam_input)) 
        if get_text(self.ui.test_apply_bin_mask_input) == "Yes":
            biapy_config['TEST']['POST_PROCESSING']['APPLY_MASK'] = True   

        if not biapy_config['TEST']['POST_PROCESSING']:
            del biapy_config['TEST']['POST_PROCESSING']
    else:
        biapy_config['TEST']['ENABLE'] = False

    # Checking the directory
    if self.cfg.settings['yaml_config_file_path'] == "":
        self.error_exec("YAML file path must be defined", "yaml_config_file_path")
        return True
    if not os.path.exists(self.cfg.settings['yaml_config_file_path']):
        self.error_exec("The directory '{}' does not exist. That folder was selected to store the YAML file"\
            .format(self.cfg.settings['yaml_config_file_path']), "yaml_config_file_path")
        return True

    # Checking YAML file name
    self.cfg.settings['yaml_config_filename'] = get_text(self.ui.goptions_yaml_name_input)
    if self.cfg.settings['yaml_config_filename'] == "":
        self.error_exec("The YAML filename must be defined", "goptions_yaml_name_input")
        return True
    if not self.cfg.settings['yaml_config_filename'].endswith(".yaml") and not self.cfg.settings['yaml_config_filename'].endswith(".yml"):
        self.error_exec("The YAML filename must have .yaml or .yml extension. You should change it to: {}"\
            .format(self.cfg.settings['yaml_config_filename']+".yaml"), "goptions_yaml_name_input")
        return True

    # Writing YAML file
    print("Creating YAML file") 
    with open(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']), 'w') as outfile:
        yaml.dump(biapy_config, outfile, default_flow_style=False)

    # Update GUI with the new YAML file path
    self.ui.select_yaml_name_label.setText(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']))

    # Load configuration
    load_yaml_config(self, False)
    
    # Advise user where the YAML file has been saved 
    message = "{}".format(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']))
    self.dialog_exec(message)
        
    return False

def load_yaml_config(self, checks=True):
    if checks:
        if self.cfg.settings['yaml_config_filename'] == "":
            self.error_exec("A YAML file must be selected", "select_yaml_name_label")
            return False
        yaml_file = get_text(self.ui.select_yaml_name_label)
        if not os.path.exists(yaml_file):
            self.error_exec("The YAML file does not exist!", "select_yaml_name_label")
            return False
        if not str(yaml_file).endswith(".yaml") and not str(yaml_file).endswith(".yml"):
            self.error_exec("The YAML filename must have .yaml or .yml extension", "select_yaml_name_label")
            return False
    self.cfg.settings['biapy_cfg'] = Config("/home/","jobname")
    
    errors = ""
    try:
        self.cfg.settings['biapy_cfg']._C.merge_from_file(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']))
        self.cfg.settings['biapy_cfg'] = self.cfg.settings['biapy_cfg'].get_cfg_defaults()
        check_configuration(self.cfg.settings['biapy_cfg'])
        
    except Exception as errors:   
        errors = str(errors)
        self.ui.check_yaml_file_errors_label.setText(errors)
        self.ui.check_yaml_file_errors_frame.setStyleSheet("border: 2px solid red;")    
    else:
        self.ui.check_yaml_file_errors_label.setText("No errors found in the YAML file")
        self.ui.check_yaml_file_errors_frame.setStyleSheet("")
        return True