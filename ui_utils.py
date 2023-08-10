import os 
import sys
import traceback
import docker
import ast 
import GPUtil
import yaml

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import *

import settings
from biapy_config import Config
from biapy_check_configuration import check_configuration

def examine(main_window, save_in_obj_tag=None, is_file=True):
    if not is_file:
        out = QFileDialog.getExistingDirectory(main_window, 'Select a directory')
    else:
        out = QFileDialog.getOpenFileName()[0]

    if out == "": return # If no file was selected 

    if save_in_obj_tag is not None:
        getattr(main_window.ui, save_in_obj_tag).setText(out)
        if save_in_obj_tag == "DATA__TRAIN__PATH__INPUT":
            main_window.cfg.settings['train_data_input_path'] = out 
        elif save_in_obj_tag == "DATA__TRAIN__GT_PATH__INPUT":
            main_window.cfg.settings['train_data_gt_input_path'] = out 
        elif save_in_obj_tag == "DATA__VAL__PATH__INPUT":
            main_window.cfg.settings['validation_data_input_path'] = out 
        elif save_in_obj_tag == "DATA__VAL__GT_PATH__INPUT":
            main_window.cfg.settings['validation_data_gt_input_path'] = out 
        elif save_in_obj_tag == "DATA__TEST__PATH__INPUT":
            main_window.cfg.settings['test_data_input_path'] = out 
        elif save_in_obj_tag == "DATA__TEST__GT_PATH__INPUT":
            main_window.cfg.settings['test_data_gt_input_path'] = out  

def combobox_hide_visible_action(main_window, combobox, frames_dict, frames_dict_values_to_set=None, frames_to_hide_if_empty=None):
    """
    frames_dict : Dict of list of (str and tuples)
        A list that is composed by three different parts: 1) the name of the widget; 2) a sequence of str until the first tuple; 
        and 3) a sequence of tuples. So the widget (1) is visible all the conditions must be True. Each definition is as follows: 
        1) Widget that will be modified when the combobox changed; 2) sequence of str that the combobox need to have; 3) Other 
        conditions. For instance, if the tuple is ("widgetA", ["valueA", "valueB"]) means that the widget called "widgetA" needs to 
        have a value between ["valueA, "valueB"]. When conditions (2) and (3) are True the widget (1) is set to visible. 
    """
    cbox_value = str(getattr(main_window.ui, combobox).currentText())
    for key in frames_dict:
        visible_values = frames_dict[key]
        if not isinstance(visible_values, list):
            visible_values = [visible_values]

        all_conditions = []
        if main_window.cfg.settings['selected_workflow'] in [3,5,6]:
            if '_gt_' in key:
                all_conditions.append(False)
            else:
                for visible_condition in visible_values:
                    if not isinstance(visible_condition, tuple):
                        if cbox_value == visible_condition:
                            all_conditions.append(True)
                    else:
                        if len(all_conditions) == 0:
                            all_conditions.append(False)
                            break
                        if get_text(getattr(main_window.ui, visible_condition[0])) in visible_condition[1]:
                            all_conditions.append(True)
                        else:
                            all_conditions.append(False)
                            break
        else:
            for visible_condition in visible_values:
                if not isinstance(visible_condition, tuple):
                    if cbox_value == visible_condition:
                        all_conditions.append(True)
                else:
                    if len(all_conditions) == 0:
                        all_conditions.append(False)
                        break
                    if get_text(getattr(main_window.ui, visible_condition[0])) in visible_condition[1]:
                        all_conditions.append(True)
                    else:
                        all_conditions.append(False)
                        break
        if len(all_conditions) == 0: all_conditions.append(False)
        vis = True if all(all_conditions) else False
        getattr(main_window.ui, key).setVisible(vis)

    if frames_dict_values_to_set is not None:
        for key in frames_dict_values_to_set:
            getattr(main_window.ui, key).setCurrentText(frames_dict_values_to_set[key]) 

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
        models = self.cfg.settings['semantic_models_real_names']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_semantic_seg_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_semantic_seg_page)
        # Train page
        self.ui.train_gt_label.setText("Input label folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input label folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input label folder")
        self.ui.test_exists_gt_label.setText("Do you have test labels?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
    # Instance seg
    elif self.cfg.settings['selected_workflow'] == 1:
        jobname = "my_instance_segmentation"
        models = self.cfg.settings['instance_models_real_names']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_instance_seg_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_instance_seg_page)
        # Train page
        self.ui.train_gt_label.setText("Input label folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input label folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input label folder")
        self.ui.test_exists_gt_label.setText("Do you have test labels?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
    # Detection
    elif self.cfg.settings['selected_workflow'] == 2:
        jobname = "my_detection"
        models = self.cfg.settings['detection_models_real_names']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_detection_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_detection_page)
        # Train page
        self.ui.train_gt_label.setText("Input CSV folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input CSV folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input CSV folder")
        self.ui.test_exists_gt_label.setText("Do you have CSV files for test data?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
    # Denoising
    elif self.cfg.settings['selected_workflow'] == 3:
        jobname = "my_denoising"
        models = self.cfg.settings['denoising_models_real_names']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_denoising_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_denoising_page)
        # Train page
        self.ui.train_gt_label.setVisible(False)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(False)
        self.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.test_exists_gt_label.setVisible(False)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(False)
    # Super resolution
    elif self.cfg.settings['selected_workflow'] == 4:
        jobname = "my_super_resolution"
        if get_text(self.ui.PROBLEM__NDIM__INPUT) == "2D":
            models = self.cfg.settings['sr_2d_models_real_names']
        else:
            models = self.cfg.settings['sr_3d_models_real_names']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_sr_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_sr_page)
        # Train page
        self.ui.train_gt_label.setText("Input high-resolution image folder")
        self.ui.train_gt_label.setVisible(True)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        self.ui.train_data_gt_input_browse_bn.setVisible(True)
        self.ui.validation_data_gt_label.setText("Input high-resolution image folder")
        # Test page
        self.ui.test_data_gt_label.setText("Input high-resolution image folder")
        self.ui.test_exists_gt_label.setText("Do you have high-resolution test data?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
    # Self-supevised learning
    elif self.cfg.settings['selected_workflow'] == 5:
        jobname = "my_self_supervised_learning"
        models = self.cfg.settings['ssl_models_real_names']
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_ssl_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_ssl_page)
        # Train page
        self.ui.train_gt_label.setVisible(False)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(False)
        self.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.test_exists_gt_label.setVisible(False)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(False)
    # Classification
    elif self.cfg.settings['selected_workflow'] == 6:
        jobname = "my_classification"
        models = self.cfg.settings['classification_models_real_names']
        goptions_tab_widget_visible = True
        self.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.train_workflow_specific_tab_classification_page)
        self.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(self.ui.test_workflow_specific_tab_classification_page)
        # Train page
        self.ui.train_gt_label.setVisible(False)
        self.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(False)
        self.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        self.ui.test_data_gt_label.setVisible(False)
        self.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        self.ui.test_data_gt_input_browse_bn.setVisible(False)
        self.ui.test_exists_gt_label.setText("Is the test separated in classes?")
        self.ui.test_exists_gt_label.setVisible(True)
        self.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)

    actual_name = get_text(self.ui.job_name_input)
    if actual_name in ["", "my_semantic_segmentation", "my_instance_segmentation", "my_detection", "my_denoising", \
        "my_super_resolution", "my_self_supervised_learning", "my_classification"]:
        if to_page == 5:
            self.ui.job_name_input.setPlainText(jobname)

    # General options page
    if to_page == 2:
        self.ui.goptions_advanced_options_scrollarea.setVisible(False)

    # Train page
    self.ui.MODEL__ARCHITECTURE__INPUT.clear()
    self.ui.MODEL__ARCHITECTURE__INPUT.addItems(models)

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
        self.ui.docker_frame.setStyleSheet("#docker_frame { border: 3px solid green; border-radius: 25px;}")
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

def set_text(obj, s):
    if isinstance(obj, QComboBox):
        index = obj.findText(s)
        if index >= 0:
            obj.setCurrentIndex(index)
        else:
            return "{} couldn't be loaded in {}".format(s,obj)
    elif isinstance(obj, QLineEdit):
        obj.setText(s)
    else: #QTextBrowser
        obj.setText(s)

def create_yaml_file(self):        
    biapy_config = {}

    # System
    biapy_config['SYSTEM'] = {}
    
    cpus = get_text(self.ui.SYSTEM__NUM_CPUS__INPUT)
    cpus = -1 if cpus == "All" else int(cpus)
    biapy_config['SYSTEM']['NUM_CPUS'] = cpus

    # Problem specification
    workflow_names_yaml = ['SEMANTIC_SEG', 'INSTANCE_SEG', 'DETECTION', 'DENOISING', 'SUPER_RESOLUTION', 
        'SELF_SUPERVISED', 'CLASSIFICATION']
    biapy_config['PROBLEM'] = {}
    biapy_config['PROBLEM']['TYPE'] = workflow_names_yaml[self.cfg.settings['selected_workflow']]
    biapy_config['PROBLEM']['NDIM'] = get_text(self.ui.PROBLEM__NDIM__INPUT)

    ### INSTANCE_SEG
    if self.cfg.settings['selected_workflow'] == 1:
        biapy_config['PROBLEM']['INSTANCE_SEG'] = {}
        
        # Transcribe problem representation
        problem_channels = 'BC'
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours":
            problem_channels = 'BC'
        elif get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Central points":
            problem_channels = 'BP'
        elif get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Distance map":
            problem_channels = 'BD'
        elif get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours + Foreground mask":
            problem_channels = 'BCM'
        elif get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours + Distance map":
            problem_channels = 'BCD'
        elif get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours + Distance map with background (experimental)":
            problem_channels = 'BCDv2'
        elif get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Distance map with background (experimental)":
            problem_channels = 'BDv2'
        else: # Distance map with background (experimental)
            problem_channels = 'Dv2'
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNELS'] = problem_channels
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNEL_WEIGHTS'] = get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS_WEIGHTS__INPUT) 
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT) != "thick":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CONTOUR_MODE'] = get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT)
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHECK_MW'] = get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT)
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_TYPE'] = get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT)
        if 'B' in problem_channels:
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_BINARY_MASK'] = float(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT))
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_FOREGROUND'] = float(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT))
        if 'C' in problem_channels:
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_CONTOUR'] = float(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT))
        if 'D' in problem_channels:    
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_DISTANCE'] = float(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT))
        if 'P' in problem_channels: 
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_POINTS'] = float(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT))
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_BEFORE_MW'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_BEFORE'] = int(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT))
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_AFTER_MW__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_AFTER_MW'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_AFTER'] = int(get_text(self.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_AFTER__INPUT))
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_SEQUENCE__INPUT) != "[]":
            biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_SEQUENCE'] = ast.literal_eval(get_text(self.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_SEQUENCE__INPUT) )
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT) != "[]":
            biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_RADIUS'] =  ast.literal_eval(get_text(self.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT))
        if get_text(self.ui.PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['ERODE_AND_DILATE_FOREGROUND'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_EROSION_RADIUS'] = int(get_text(self.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT))
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_DILATION_RADIUS'] = int(get_text(self.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT))

        # biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_OPTIMIZE_THS'] = False
        # biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHECK_MW'] = True
        
    ### DETECTION
    elif self.cfg.settings['selected_workflow'] == 2:
        biapy_config['PROBLEM']['DETECTION'] = {}
        biapy_config['PROBLEM']['DETECTION']['CENTRAL_POINT_DILATION'] = int(get_text(self.ui.PROBLEM__DETECTION__CENTRAL_POINT_DILATION__INPUT))
        biapy_config['PROBLEM']['DETECTION']['CHECK_POINTS_CREATED'] = True if get_text(self.ui.PROBLEM__DETECTION__CHECK_POINTS_CREATED__INPUT) == "Yes" else False
        if get_text(self.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INPUT) == "Yes" and get_text(self.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT) == "Yes":
            biapy_config['PROBLEM']['DETECTION']['DATA_CHECK_MW'] = True

    ### DENOISING
    elif self.cfg.settings['selected_workflow'] == 3:
        biapy_config['PROBLEM']['DENOISING'] = {}
        biapy_config['PROBLEM']['DENOISING']['N2V_PERC_PIX'] = float(get_text(self.ui.PROBLEM__DENOISING__N2V_PERC_PIX__INPUT))
        biapy_config['PROBLEM']['DENOISING']['N2V_MANIPULATOR'] = get_text(self.ui.PROBLEM__DENOISING__N2V_MANIPULATOR__INPUT)
        biapy_config['PROBLEM']['DENOISING']['N2V_NEIGHBORHOOD_RADIUS'] = int(get_text(self.ui.PROBLEM__DENOISING__N2V_NEIGHBORHOOD_RADIUS__INPUT))
        biapy_config['PROBLEM']['DENOISING']['N2V_STRUCTMASK'] = True if get_text(self.ui.PROBLEM__DENOISING__N2V_STRUCTMASK__INPUT) == "Yes" else False

    ### SUPER_RESOLUTION
    elif self.cfg.settings['selected_workflow'] == 4:
        biapy_config['PROBLEM']['SUPER_RESOLUTION'] = {}
        biapy_config['PROBLEM']['SUPER_RESOLUTION']['UPSCALING'] = int(get_text(self.ui.PROBLEM__SUPER_RESOLUTION__UPSCALING__INPUT))

    ### SELF_SUPERVISED
    elif self.cfg.settings['selected_workflow'] == 5:
        biapy_config['PROBLEM']['SELF_SUPERVISED'] = {}
        biapy_config['PROBLEM']['SELF_SUPERVISED']['PRETEXT_TASK'] = get_text(self.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT)
        if get_text(self.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT) == "crappify":
            biapy_config['PROBLEM']['SELF_SUPERVISED']['RESIZING_FACTOR'] = int(get_text(self.ui.PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INPUT))
            biapy_config['PROBLEM']['SELF_SUPERVISED']['NOISE'] = float(get_text(self.ui.PROBLEM__SELF_SUPERVISED__NOISE__INPUT))

    # Dataset
    biapy_config['DATA'] = {}
    if get_text(self.ui.DATA__CHECK_GENERATORS__INPUT) == "Yes":
        biapy_config['DATA']['CHECK_GENERATORS'] = True

    biapy_config['DATA']['PATCH_SIZE'] = get_text(self.ui.DATA__PATCH_SIZE__INPUT)
    if get_text(self.ui.DATA__EXTRACT_RANDOM_PATCH__INPUT) == "Yes":
        biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = True
        if get_text(self.ui.DATA__PROBABILITY_MAP__INPUT) == "Yes":
            biapy_config['DATA']['PROBABILITY_MAP'] = True
            biapy_config['DATA']['W_FOREGROUND'] = float(get_text(self.ui.DATA__W_FOREGROUND__INPUT))
            biapy_config['DATA']['W_BACKGROUND'] = float(get_text(self.ui.DATA__W_BACKGROUND__INPUT)) 
    else:
        biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = False

    if get_text(self.ui.DATA__REFLECT_TO_COMPLETE_SHAPE__INPUT) == "Yes":
        biapy_config['DATA']['REFLECT_TO_COMPLETE_SHAPE'] = True

    if get_text(self.ui.DATA__NORMALIZATION__TYPE__INPUT) == "custom":
        biapy_config['DATA']['NORMALIZATION'] = {}
        biapy_config['DATA']['NORMALIZATION']['TYPE'] = 'custom'
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_MEAN'] = float(get_text(self.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT)) 
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_STD'] = float(get_text(self.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT)) 

    # Train
    if get_text(self.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TRAIN'] = {}

        if self.cfg.settings['selected_workflow'] == 0 and get_text(self.ui.DATA__TRAIN__CHECK_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TRAIN']['CHECK_DATA'] = True
        
        biapy_config['DATA']['TRAIN']['IN_MEMORY'] = True if get_text(self.ui.DATA__TRAIN__IN_MEMORY__INPUT) == "Yes" else False
        biapy_config['DATA']['TRAIN']['PATH'] = get_text(self.ui.DATA__TRAIN__PATH__INPUT)
        if self.cfg.settings['selected_workflow'] not in [4,6,7]:
            biapy_config['DATA']['TRAIN']['GT_PATH'] = get_text(self.ui.DATA__TRAIN__GT_PATH__INPUT)
        if int(get_text(self.ui.DATA__TRAIN__REPLICATE__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['REPLICATE'] = int(get_text(self.ui.DATA__TRAIN__REPLICATE__INPUT))
        biapy_config['DATA']['TRAIN']['OVERLAP'] = get_text(self.ui.DATA__TRAIN__OVERLAP__INPUT)
        biapy_config['DATA']['TRAIN']['PADDING'] = get_text(self.ui.DATA__TRAIN__PADDING__INPUT)
        if get_text(self.ui.DATA__TRAIN__RESOLUTION__INPUT) != "(1,1,1)" and get_text(self.ui.DATA__TRAIN__RESOLUTION__INPUT) != "(1,1)":
            biapy_config['DATA']['TRAIN']['RESOLUTION'] = get_text(self.ui.DATA__TRAIN__RESOLUTION__INPUT)
        
        if self.cfg.settings['selected_workflow'] == 0 and int(get_text(self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__SEM_SEG__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__SEM_SEG__INPUT))
        if self.cfg.settings['selected_workflow'] == 1 and int(get_text(self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__INST_SEG__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__INST_SEG__INPUT))
        if self.cfg.settings['selected_workflow'] == 2 and int(get_text(self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__DET__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(self.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__DET__INPUT))
        
        # Validation
        biapy_config['DATA']['VAL'] = {}

        if get_text(self.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (split training)":
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
            biapy_config['DATA']['VAL']['SPLIT_TRAIN'] = float(get_text(self.ui.DATA__VAL__SPLIT_TRAIN__INPUT))
            biapy_config['DATA']['VAL']['RANDOM'] = True if get_text(self.ui.DATA__VAL__RANDOM__INPUT) == "Yes" else False 
        elif get_text(self.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (cross validation)":
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
            biapy_config['DATA']['VAL']['CROSS_VAL'] = True
            biapy_config['DATA']['VAL']['CROSS_VAL_NFOLD'] = int(get_text(self.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT))
            biapy_config['DATA']['VAL']['CROSS_VAL_FOLD'] = int(get_text(self.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT))
            biapy_config['DATA']['VAL']['RANDOM'] = True if get_text(self.ui.DATA__VAL__RANDOM__INPUT) == "Yes" else False 
        # Not extracted from train (path needed)
        else:
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = False
            biapy_config['DATA']['VAL']['IN_MEMORY'] = True if get_text(self.ui.DATA__VAL__IN_MEMORY__INPUT) == "Yes" else False 
            biapy_config['DATA']['VAL']['PATH'] = get_text(self.ui.DATA__VAL__PATH__INPUT)
            if self.cfg.settings['selected_workflow'] not in [4,6,7]:
                biapy_config['DATA']['VAL']['GT_PATH'] = get_text(self.ui.DATA__VAL__GT_PATH__INPUT)
            biapy_config['DATA']['VAL']['OVERLAP'] = get_text(self.ui.DATA__VAL__OVERLAP__INPUT)
            biapy_config['DATA']['VAL']['PADDING'] = get_text(self.ui.DATA__VAL__PADDING__INPUT)

        biapy_config['DATA']['VAL']['RESOLUTION'] = get_text(self.ui.DATA__VAL__RESOLUTION__INPUT)

    # Test
    if get_text(self.ui.TEST__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TEST'] = {}
        if self.cfg.settings['selected_workflow'] == 0 and get_text(self.ui.DATA__TEST__CHECK_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['CHECK_DATA'] = True
        if get_text(self.ui.DATA__TEST__IN_MEMORY__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['IN_MEMORY'] = True
        else:
            biapy_config['DATA']['TEST']['IN_MEMORY'] = False
        if get_text(self.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT) == "Yes" and\
            get_text(self.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (cross validation)":
            biapy_config['DATA']['TEST']['USE_VAL_AS_TEST'] = True
        else:
            if get_text(self.ui.DATA__TEST__LOAD_GT__INPUT) == "Yes":
                biapy_config['DATA']['TEST']['LOAD_GT'] = True
                if self.cfg.settings['selected_workflow'] not in [4,6,7]:
                    biapy_config['DATA']['TEST']['GT_PATH'] = get_text(self.ui.DATA__TEST__GT_PATH__INPUT)
            else:
                biapy_config['DATA']['TEST']['LOAD_GT'] = False
            biapy_config['DATA']['TEST']['PATH'] = get_text(self.ui.DATA__TEST__PATH__INPUT)
            
        biapy_config['DATA']['TEST']['OVERLAP'] = get_text(self.ui.DATA__TEST__OVERLAP__INPUT)
        biapy_config['DATA']['TEST']['PADDING'] = get_text(self.ui.DATA__TEST__PADDING__INPUT)
        if get_text(self.ui.DATA__TEST__MEDIAN_PADDING__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['MEDIAN_PADDING'] = True 
        biapy_config['DATA']['TEST']['RESOLUTION'] = get_text(self.ui.DATA__TEST__RESOLUTION__INPUT)
        if get_text(self.ui.DATA__TEST__ARGMAX_TO_OUTPUT__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['ARGMAX_TO_OUTPUT'] = True


    # Data augmentation (DA)
    biapy_config['AUGMENTOR'] = {}
    if get_text(self.ui.AUGMENTOR__ENABLE__INPUT) == "Yes":
        biapy_config['AUGMENTOR']['ENABLE'] = True  
        biapy_config['AUGMENTOR']['DA_PROB'] = float(get_text(self.ui.AUGMENTOR__DA_PROB__INPUT))
        biapy_config['AUGMENTOR']['AUG_SAMPLES'] = True if get_text(self.ui.AUGMENTOR__AUG_SAMPLES__INPUT) == "Yes" else False 
        biapy_config['AUGMENTOR']['DRAW_GRID'] = True if get_text(self.ui.AUGMENTOR__DRAW_GRID__INPUT) == "Yes" else False 
        if int(get_text(self.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT)) != 10:
            biapy_config['AUGMENTOR']['AUG_NUM_SAMPLES'] = int(get_text(self.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT))
        biapy_config['AUGMENTOR']['SHUFFLE_TRAIN_DATA_EACH_EPOCH'] = True if get_text(self.ui.AUGMENTOR__SHUFFLE_TRAIN_DATA_EACH_EPOCH__INPUT) == "Yes" else False 
        biapy_config['AUGMENTOR']['SHUFFLE_VAL_DATA_EACH_EPOCH'] = True if get_text(self.ui.AUGMENTOR__SHUFFLE_VAL_DATA_EACH_EPOCH__INPUT) == "Yes" else False 
        if get_text(self.ui.AUGMENTOR__ROT90__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ROT90'] = True 
        if get_text(self.ui.AUGMENTOR__RANDOM_ROT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['RANDOM_ROT'] = True  
            biapy_config['AUGMENTOR']['RANDOM_ROT_RANGE'] = get_text(self.ui.AUGMENTOR__RANDOM_ROT_RANGE__INPUT)
        if get_text(self.ui.AUGMENTOR__SHEAR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SHEAR'] = True  
            biapy_config['AUGMENTOR']['SHEAR_RANGE'] = get_text(self.ui.AUGMENTOR__SHEAR_RANGE__INPUT)
        if get_text(self.ui.AUGMENTOR__ZOOM__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ZOOM'] = True  
            biapy_config['AUGMENTOR']['ZOOM_RANGE'] = get_text(self.ui.AUGMENTOR__ZOOM_RANGE__INPUT)
        if get_text(self.ui.AUGMENTOR__SHIFT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SHIFT'] = True 
            biapy_config['AUGMENTOR']['SHIFT_RANGE'] = get_text(self.ui.AUGMENTOR__SHIFT_RANGE__INPUT)
        if get_text(self.ui.AUGMENTOR__SHIFT__INPUT) == "Yes" or get_text(self.ui.AUGMENTOR__ZOOM__INPUT) == "Yes" or\
            get_text(self.ui.AUGMENTOR__SHEAR__INPUT) == "Yes" or get_text(self.ui.AUGMENTOR__RANDOM_ROT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['AFFINE_MODE'] = get_text(self.ui.AUGMENTOR__AFFINE_MODE__INPUT)
        if get_text(self.ui.AUGMENTOR__VFLIP__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['VFLIP'] = True 
        if get_text(self.ui.AUGMENTOR__HFLIP__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['HFLIP'] = True 
        if get_text(self.ui.AUGMENTOR__ZFLIP__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ZFLIP'] = True 
        if get_text(self.ui.AUGMENTOR__ELASTIC__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ELASTIC'] = True 
            biapy_config['AUGMENTOR']['E_ALPHA'] = get_text(self.ui.AUGMENTOR__E_ALPHA__INPUT)
            biapy_config['AUGMENTOR']['E_SIGMA'] = int(get_text(self.ui.AUGMENTOR__E_SIGMA__INPUT))
            biapy_config['AUGMENTOR']['E_MODE'] = get_text(self.ui.AUGMENTOR__E_MODE__INPUT)
        if get_text(self.ui.AUGMENTOR__G_BLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['G_BLUR'] = True 
            biapy_config['AUGMENTOR']['G_SIGMA'] = get_text(self.ui.AUGMENTOR__G_SIGMA__INPUT)
        if get_text(self.ui.AUGMENTOR__MEDIAN_BLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MEDIAN_BLUR'] = True 
            biapy_config['AUGMENTOR']['MB_KERNEL'] = get_text(self.ui.AUGMENTOR__MB_KERNEL__INPUT)
        if get_text(self.ui.AUGMENTOR__MOTION_BLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MOTION_BLUR'] = True 
            biapy_config['AUGMENTOR']['MOTB_K_RANGE'] = get_text(self.ui.AUGMENTOR__MOTB_K_RANGE__INPUT)
        if get_text(self.ui.AUGMENTOR__GAMMA_CONTRAST__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GAMMA_CONTRAST'] = True
            biapy_config['AUGMENTOR']['GC_GAMMA'] = get_text(self.ui.AUGMENTOR__GC_GAMMA__INPUT)
        if get_text(self.ui.AUGMENTOR__BRIGHTNESS__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['BRIGHTNESS'] = True
            biapy_config['AUGMENTOR']['BRIGHTNESS_FACTOR'] = get_text(self.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['BRIGHTNESS_MODE'] = get_text(self.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT)
        if get_text(self.ui.AUGMENTOR__CONTRAST__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CONTRAST'] = True
            biapy_config['AUGMENTOR']['CONTRAST_FACTOR'] = get_text(self.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['CONTRAST_MODE'] = get_text(self.ui.AUGMENTOR__CONTRAST_MODE__INPUT)
        if get_text(self.ui.AUGMENTOR__BRIGHTNESS_EM__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM'] = True
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM_FACTOR'] = get_text(self.ui.AUGMENTOR__BRIGHTNESS_EM_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM_MODE'] = get_text(self.ui.AUGMENTOR__BRIGHTNESS_EM_MODE__INPUT)
        if get_text(self.ui.AUGMENTOR__CONTRAST_EM__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CONTRAST_EM'] = True
            biapy_config['AUGMENTOR']['CONTRAST_EM_FACTOR'] = get_text(self.ui.AUGMENTOR__CONTRAST_EM_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['CONTRAST_EM_MODE'] = get_text(self.ui.AUGMENTOR__CONTRAST_EM_MODE__INPUT)
        if get_text(self.ui.AUGMENTOR__DROPOUT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['DROPOUT'] = True
            biapy_config['AUGMENTOR']['DROP_RANGE'] = get_text(self.ui.AUGMENTOR__DROP_RANGE__INPUT)
        if get_text(self.ui.AUGMENTOR__CUTOUT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTOUT'] = True
            biapy_config['AUGMENTOR']['COUT_NB_ITERATIONS'] = get_text(self.ui.AUGMENTOR__COUT_NB_ITERATIONS__INPUT)
            biapy_config['AUGMENTOR']['COUT_SIZE'] = get_text(self.ui.AUGMENTOR__COUT_SIZE__INPUT)
            biapy_config['AUGMENTOR']['COUT_CVAL'] = float(get_text(self.ui.AUGMENTOR__COUT_CVAL__INPUT))
            biapy_config['AUGMENTOR']['COUT_APPLY_TO_MASK'] = True if get_text(self.ui.AUGMENTOR__COUT_APPLY_TO_MASK__INPUT) == "Yes" else False 
        if get_text(self.ui.AUGMENTOR__CUTBLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTBLUR'] = True
            biapy_config['AUGMENTOR']['CBLUR_SIZE'] = get_text(self.ui.AUGMENTOR__CBLUR_SIZE__INPUT)
            biapy_config['AUGMENTOR']['CBLUR_DOWN_RANGE'] = get_text(self.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INPUT)
            biapy_config['AUGMENTOR']['CBLUR_INSIDE'] = True if get_text(self.ui.AUGMENTOR__CBLUR_INSIDE__INPUT) == "Yes" else False 
        if get_text(self.ui.AUGMENTOR__CUTMIX__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTMIX'] = True
            biapy_config['AUGMENTOR']['CMIX_SIZE'] = get_text(self.ui.AUGMENTOR__CMIX_SIZE__INPUT)
        if get_text(self.ui.AUGMENTOR__CUTNOISE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTNOISE'] = True
            biapy_config['AUGMENTOR']['CNOISE_SCALE'] = get_text(self.ui.AUGMENTOR__CNOISE_SCALE__INPUT)
            biapy_config['AUGMENTOR']['CNOISE_NB_ITERATIONS'] = get_text(self.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT)
            biapy_config['AUGMENTOR']['CNOISE_SIZE'] = get_text(self.ui.AUGMENTOR__CNOISE_SIZE__INPUT)
        if get_text(self.ui.AUGMENTOR__MISALIGNMENT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MISALIGNMENT'] = True
            biapy_config['AUGMENTOR']['MS_DISPLACEMENT'] = int(get_text(self.ui.AUGMENTOR__MS_DISPLACEMENT__INPUT))
            biapy_config['AUGMENTOR']['MS_ROTATE_RATIO'] = float(get_text(self.ui.AUGMENTOR__MS_ROTATE_RATIO__INPUT))
        if get_text(self.ui.AUGMENTOR__MISSING_SECTIONS__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MISSING_SECTIONS'] = True
            biapy_config['AUGMENTOR']['MISSP_ITERATIONS'] = get_text(self.ui.AUGMENTOR__MISSP_ITERATIONS__INPUT)
        if get_text(self.ui.AUGMENTOR__GRAYSCALE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GRAYSCALE'] = True
        if get_text(self.ui.AUGMENTOR__CHANNEL_SHUFFLE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CHANNEL_SHUFFLE'] = True
        if get_text(self.ui.AUGMENTOR__GRIDMASK__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GRIDMASK'] = True
            biapy_config['AUGMENTOR']['GRID_RATIO'] = float(get_text(self.ui.AUGMENTOR__GRID_RATIO__INPUT))
            biapy_config['AUGMENTOR']['GRID_D_RANGE'] = get_text(self.ui.AUGMENTOR__GRID_D_RANGE__INPUT)
            biapy_config['AUGMENTOR']['GRID_ROTATE'] = float(get_text(self.ui.AUGMENTOR__GRID_ROTATE__INPUT))
            biapy_config['AUGMENTOR']['GRID_INVERT'] = True if get_text(self.ui.AUGMENTOR__GRID_INVERT__INPUT) == "Yes" else False 
        if get_text(self.ui.AUGMENTOR__GAUSSIAN_NOISE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE'] = True
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_MEAN'] = float(get_text(self.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT))
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_VAR'] = float(get_text(self.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT))
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR'] = True if get_text(self.ui.AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT) == "Yes" else False 
        if get_text(self.ui.AUGMENTOR__POISSON_NOISE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['POISSON_NOISE'] = True
        if get_text(self.ui.AUGMENTOR__SALT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SALT'] = True
            biapy_config['AUGMENTOR']['SALT_AMOUNT'] = float(get_text(self.ui.AUGMENTOR__SALT_AMOUNT__INPUT))
        if get_text(self.ui.AUGMENTOR__PEPPER__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['PEPPER'] = True
            biapy_config['AUGMENTOR']['PEPPER_AMOUNT'] = float(get_text(self.ui.AUGMENTOR__PEPPER_AMOUNT__INPUT))
        if get_text(self.ui.AUGMENTOR__SALT_AND_PEPPER__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER'] = True
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER_AMOUNT'] = float(get_text(self.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT))
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER_PROP'] = float(get_text(self.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT))
    else:
        biapy_config['AUGMENTOR']['ENABLE'] = False

    # Model definition
    biapy_config['MODEL'] = {}
    model_name = self.cfg.translate_model_names(get_text(self.ui.MODEL__ARCHITECTURE__INPUT), get_text(self.ui.PROBLEM__NDIM__INPUT))
    biapy_config['MODEL']['ARCHITECTURE'] = model_name
    if model_name in ['unet', 'resunet', 'seunet', 'attention_unet']:
        biapy_config['MODEL']['FEATURE_MAPS'] = ast.literal_eval(get_text(self.ui.MODEL__FEATURE_MAPS__INPUT))
        if get_text(self.ui.MODEL__SPATIAL_DROPOUT__INPUT) == "Yes":
            biapy_config['MODEL']['SPATIAL_DROPOUT'] = True  
        biapy_config['MODEL']['DROPOUT_VALUES'] = ast.literal_eval(get_text(self.ui.MODEL__DROPOUT_VALUES__INPUT)) 
        biapy_config['MODEL']['BATCH_NORMALIZATION'] = True if get_text(self.ui.MODEL__BATCH_NORMALIZATION__INPUT) == "Yes" else False 
        if get_text(self.ui.MODEL__KERNEL_INIT__INPUT) != "he_normal":
            biapy_config['MODEL']['KERNEL_INIT'] = get_text(self.ui.MODEL__KERNEL_INIT__INPUT)
        if int(get_text(self.ui.MODEL__KERNEL_SIZE__INPUT)) != 3:
            biapy_config['MODEL']['KERNEL_SIZE'] = int(get_text(self.ui.MODEL__KERNEL_SIZE__INPUT))
        if get_text(self.ui.MODEL__UPSAMPLE_LAYER__INPUT) != "convtranspose":
            biapy_config['MODEL']['UPSAMPLE_LAYER'] = get_text(self.ui.MODEL__UPSAMPLE_LAYER__INPUT) 
        if get_text(self.ui.MODEL__ACTIVATION__INPUT) != 'elu':
            biapy_config['MODEL']['ACTIVATION'] = get_text(self.ui.MODEL__ACTIVATION__INPUT)
        if get_text(self.ui.MODEL__LAST_ACTIVATION__INPUT) != 'sigmoid':
            biapy_config['MODEL']['LAST_ACTIVATION'] = get_text(self.ui.MODEL__LAST_ACTIVATION__INPUT)
        biapy_config['MODEL']['N_CLASSES'] = int(get_text(self.ui.MODEL__N_CLASSES__INPUT))
        biapy_config['MODEL']['Z_DOWN'] = ast.literal_eval(get_text(self.ui.MODEL__Z_DOWN__INPUT)) 
        if self.cfg.settings['selected_workflow'] == 4 and get_text(self.ui.PROBLEM__NDIM__INPUT) == "3D": # SR
            r = "pre" if get_text(self.ui.MODEL__UNET_SR_UPSAMPLE_POSITION__INPUT) == "Before model" else "post"
            biapy_config['MODEL']['UNET_SR_UPSAMPLE_POSITION'] = r
            
    elif model_name == "tiramisu":
        biapy_config['MODEL']['TIRAMISU_DEPTH'] = int(get_text(self.ui.MODEL__TIRAMISU_DEPTH__INPUT))
        biapy_config['MODEL']['FEATURE_MAPS'] = int(get_text(self.ui.MODEL__TIRAMISU_FEATURE_MAPS__INPUT))
        biapy_config['MODEL']['DROPOUT_VALUES'] = float(get_text(self.ui.MODEL__TIRAMISU_DROPOUT_VALUES__INPUT))
    elif model_name in ["unetr", "mae", "ViT"]:
        biapy_config['MODEL']['VIT_TOKEN_SIZE'] = int(get_text(self.ui.MODEL__VIT_TOKEN_SIZE__INPUT))
        biapy_config['MODEL']['VIT_HIDDEN_SIZE'] = int(get_text(self.ui.MODEL__VIT_HIDDEN_SIZE__INPUT))
        biapy_config['MODEL']['VIT_NUM_LAYERS'] = int(get_text(self.ui.MODEL__VIT_NUM_LAYERS__INPUT))
        biapy_config['MODEL']['VIT_MLP_DIMS'] = get_text(self.ui.MODEL__VIT_MLP_DIMS__INPUT)
        biapy_config['MODEL']['VIT_NUM_HEADS'] = int(get_text(self.ui.MODEL__VIT_NUM_HEADS__INPUT))

        # UNETR
        if model_name in "unetr":
            biapy_config['MODEL']['UNETR_VIT_HIDD_MULT'] = int(get_text(self.ui.MODEL__UNETR_VIT_HIDD_MULT__INPUT)) 
            biapy_config['MODEL']['UNETR_VIT_NUM_FILTERS'] = int(get_text(self.ui.MODEL__UNETR_VIT_NUM_FILTERS__INPUT)) 
            biapy_config['MODEL']['UNETR_DEC_ACTIVATION'] = get_text(self.ui.MODEL__UNETR_DEC_ACTIVATION__INPUT)
            biapy_config['MODEL']['UNETR_DEC_KERNEL_INIT'] = get_text(self.ui.MODEL__UNETR_DEC_KERNEL_INIT__INPUT)

    if get_text(self.ui.MODEL__LOAD_CHECKPOINT__INPUT) == "Yes":
        biapy_config['MODEL']['LOAD_CHECKPOINT'] = True 
        biapy_config['PATHS'] = {}
        if get_text(self.ui.PATHS__CHECKPOINT_FILE__INPUT) != "":
            biapy_config['PATHS']['CHECKPOINT_FILE'] = get_text(self.ui.PATHS__CHECKPOINT_FILE__INPUT)
    
    if get_text(self.ui.MODEL__MAKE_PLOT__INPUT) == "Yes":
        biapy_config['MODEL']['MAKE_PLOT'] = True

    # Loss (in detection only)
    if self.cfg.settings['selected_workflow'] == 2:
        biapy_config['LOSS'] = {}
        biapy_config['LOSS']['TYPE'] = get_text(self.ui.LOSS__TYPE__INPUT)

    # Training phase
    biapy_config['TRAIN'] = {}
    if get_text(self.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['TRAIN']['ENABLE'] = True 
        biapy_config['TRAIN']['OPTIMIZER'] = get_text(self.ui.TRAIN__OPTIMIZER__INPUT)
        biapy_config['TRAIN']['LR'] = float(get_text(self.ui.TRAIN__LR__INPUT))
        if biapy_config['TRAIN']['OPTIMIZER'] == "ADAMW":
            biapy_config['TRAIN']['W_DECAY'] = float(get_text(self.ui.TRAIN__W_DECAY__INPUT))
        biapy_config['TRAIN']['BATCH_SIZE'] = int(get_text(self.ui.TRAIN__BATCH_SIZE__INPUT))
        biapy_config['TRAIN']['EPOCHS'] = int(get_text(self.ui.TRAIN__EPOCHS__INPUT)) 
        biapy_config['TRAIN']['PATIENCE'] = int(get_text(self.ui.TRAIN__PATIENCE__INPUT))

        # LR Scheduler
        if get_text(self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) != "":
            biapy_config['TRAIN']['LR_SCHEDULER'] = {}
            biapy_config['TRAIN']['LR_SCHEDULER']['NAME'] = get_text(self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) 
            if get_text(self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) in ["warmupcosine","reduceonplateau"]: 
                biapy_config['TRAIN']['LR_SCHEDULER']['MIN_LR'] = float(get_text(self.ui.TRAIN__LR_SCHEDULER__MIN_LR__INPUT)) 
            if get_text(self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) == "reduceonplateau": 
                biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_FACTOR'] = float(get_text(self.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT)) 
                biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_PATIENCE'] = int(get_text(self.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT))
            if get_text(self.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) == "warmupcosine":  
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_LR'] = float(get_text(self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_LR__INPUT))
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_EPOCHS'] = int(get_text(self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT))
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_HOLD_EPOCHS'] = int(get_text(self.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_HOLD_EPOCHS__INPUT))

        # Callbacks
        if get_text(self.ui.TRAIN__EARLYSTOPPING_MONITOR__INPUT) != 'val_loss':
            biapy_config['TRAIN']['EARLYSTOPPING_MONITOR'] = get_text(self.ui.TRAIN__EARLYSTOPPING_MONITOR__INPUT) 
        if get_text(self.ui.TRAIN__CHECKPOINT_MONITOR__INPUT) != 'val_loss':
            biapy_config['TRAIN']['CHECKPOINT_MONITOR'] = get_text(self.ui.TRAIN__CHECKPOINT_MONITOR__INPUT)
        if get_text(self.ui.TRAIN__PROFILER__INPUT) == "Yes": 
            biapy_config['TRAIN']['PROFILER'] = True 
            biapy_config['TRAIN']['PROFILER_BATCH_RANGE'] = get_text(self.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT)
    else:
        biapy_config['TRAIN']['ENABLE'] = False 

    # Test
    biapy_config['TEST'] = {}
    if get_text(self.ui.TEST__ENABLE__INPUT) == "Yes":    
        biapy_config['TEST']['ENABLE'] = True  
        biapy_config['TEST']['REDUCE_MEMORY'] = True if get_text(self.ui.TEST__REDUCE_MEMORY__INPUT) == "Yes" else False 
        biapy_config['TEST']['VERBOSE'] = True if get_text(self.ui.TEST__VERBOSE__INPUT) == "Yes" else False 
        biapy_config['TEST']['AUGMENTATION'] = True if get_text(self.ui.TEST__AUGMENTATION__INPUT) == "Yes" else False
        if get_text(self.ui.TEST__EVALUATE__INPUT) == "Yes" :
            biapy_config['TEST']['EVALUATE'] = True 
        if get_text(self.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT) == "Yes" and get_text(self.ui.PROBLEM__NDIM__INPUT) == "2D":
            biapy_config['TEST']['ANALIZE_2D_IMGS_AS_3D_STACK'] = True

        biapy_config['TEST']['STATS'] = {}
        biapy_config['TEST']['STATS']['PER_PATCH'] = True if get_text(self.ui.TEST__STATS__PER_PATCH__INPUT) == "Yes" else False 
        biapy_config['TEST']['STATS']['MERGE_PATCHES'] = True if get_text(self.ui.TEST__STATS__MERGE_PATCHES__INPUT) == "Yes" else False 
        if get_text(self.ui.TEST__STATS__FULL_IMG__INPUT) == "Yes" and get_text(self.ui.PROBLEM__NDIM__INPUT) == "2D":
            biapy_config['TEST']['STATS']['FULL_IMG'] = True 

        ### Instance segmentation
        if self.cfg.settings['selected_workflow'] == 1:
            biapy_config['TEST']['MATCHING_STATS'] = True if get_text(self.ui.TEST__MATCHING_STATS__INPUT) == "Yes" else False 
            biapy_config['TEST']['MATCHING_STATS_THS'] = ast.literal_eval(get_text(self.ui.TEST__MATCHING_STATS_THS__INPUT)) 
            if get_text(self.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT) != "[0.3]":
                biapy_config['TEST']['MATCHING_STATS_THS_COLORED_IMG'] = ast.literal_eval(get_text(self.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT))
            # biapy_config['TEST']['MATCHING_SEGCOMPARE'] = False 

        ### Detection
        elif self.cfg.settings['selected_workflow'] == 2:
            biapy_config['TEST']['DET_LOCAL_MAX_COORDS'] = True if get_text(self.ui.TEST__DET_LOCAL_MAX_COORDS__INPUT) == "Yes" else False 
            biapy_config['TEST']['DET_MIN_TH_TO_BE_PEAK'] = ast.literal_eval(get_text(self.ui.TEST__DET_MIN_TH_TO_BE_PEAK__INPUT))
            biapy_config['TEST']['DET_TOLERANCE'] = ast.literal_eval(get_text(self.ui.TEST__DET_TOLERANCE__INPUT))

        # Post-processing
        biapy_config['TEST']['POST_PROCESSING'] = {}
        ### Semantic segmentation
        if self.cfg.settings['selected_workflow'] == 0:
            if get_text(self.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__SEM_SEG__INPUT))
            if get_text(self.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__SEM_SEG__INPUT))
        ### Instance segmentation
        elif self.cfg.settings['selected_workflow'] == 1:
            if get_text(self.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INST_SEG__INPUT))
            if get_text(self.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__INST_SEG__INPUT))
            if float(get_text(self.ui.TEST__POST_PROCESSING__WATERSHED_CIRCULARITY__INST_SEG__INPUT)) != -1:
                biapy_config['TEST']['POST_PROCESSING']['WATERSHED_CIRCULARITY'] = float(get_text(self.ui.TEST__POST_PROCESSING__WATERSHED_CIRCULARITY__INST_SEG__INPUT))
            if problem_channels in ["BC", "BCM"] and get_text(self.ui.TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_ON_MASK'] = True 
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_TH'] = float(get_text(self.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT))
                
            if problem_channels == "BP":
                if int(get_text(self.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT)) != -1:
                    biapy_config['TEST']['POST_PROCESSING']['REPARE_LARGE_BLOBS_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT))
                if get_text(self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = ast.literal_eval(get_text(self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT))
        ### Detection
        elif self.cfg.settings['selected_workflow'] == 2:
            if get_text(self.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__DET__INPUT))
            if get_text(self.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(self.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__DET__INPUT))
            if float(get_text(self.ui.TEST__POST_PROCESSING__WATERSHED_CIRCULARITY__DET__INPUT)) != -1:
                biapy_config['TEST']['POST_PROCESSING']['WATERSHED_CIRCULARITY'] = float(get_text(self.ui.TEST__POST_PROCESSING__WATERSHED_CIRCULARITY__DET__INPUT))
            if get_text(self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = float(get_text(self.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT))
            if get_text(self.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED'] = True
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_FIRST_DILATION'] = ast.literal_eval(get_text(self.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_CLASSES'] = ast.literal_eval(get_text(self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_PATCH'] = ast.literal_eval(get_text(self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER'] = int(get_text(self.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT)) 
        if get_text(self.ui.TEST__POST_PROCESSING__APPLY_MASK__INPUT) == "Yes":
            biapy_config['TEST']['POST_PROCESSING']['APPLY_MASK'] = True

        if not biapy_config['TEST']['POST_PROCESSING']:
            del biapy_config['TEST']['POST_PROCESSING']
    else:
        biapy_config['TEST']['ENABLE'] = False

    # Checking the directory
    if self.cfg.settings['yaml_config_file_path'] == "":
        self.dialog_exec("Configuration file path must be defined", "yaml_config_file_path")
        return True
    if not os.path.exists(self.cfg.settings['yaml_config_file_path']):
        self.dialog_exec("The directory '{}' does not exist. That folder was selected to store the configuration file"\
            .format(self.cfg.settings['yaml_config_file_path']), "yaml_config_file_path")
        return True

    # Checking YAML file name
    self.cfg.settings['yaml_config_filename'] = get_text(self.ui.goptions_yaml_name_input)
    if self.cfg.settings['yaml_config_filename'] == "":
        self.dialog_exec("The configuration filename must be defined", "goptions_yaml_name_input")
        return True
    if not self.cfg.settings['yaml_config_filename'].endswith(".yaml") and not self.cfg.settings['yaml_config_filename'].endswith(".yml"):
        self.dialog_exec("The configuration filename must have .yaml or .yml extension. You should change it to: {}"\
            .format(self.cfg.settings['yaml_config_filename']+".yaml"), "goptions_yaml_name_input")
        return True

    # Writing YAML file
    replace = True
    if os.path.exists(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename'])):
        self.yes_no_exec("The file '{}' already exists. Do you want to overwrite it?".format(self.cfg.settings['yaml_config_filename']))
        replace = True if self.yes_no.answer else False
        
    if replace:
        print("Creating YAML file") 
        with open(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']), 'w') as outfile:
            yaml.dump(biapy_config, outfile, default_flow_style=False)

    # Update GUI with the new YAML file path
    self.ui.select_yaml_name_label.setText(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']))

    # Load configuration
    load_yaml_config(self, False)
    
    if replace:
        # Advise user where the YAML file has been saved 
        message = "{}".format(os.path.join(self.cfg.settings['yaml_config_file_path'], self.cfg.settings['yaml_config_filename']))
        self.dialog_exec(message, reason="inform_user")
            
    return False

def load_yaml_config(self, checks=True, advise_user=False):
    if checks:
        if self.cfg.settings['yaml_config_filename'] == "":
            self.dialog_exec("A configuration file must be selected", "select_yaml_name_label")
            return False
        yaml_file = get_text(self.ui.select_yaml_name_label)
        if not os.path.exists(yaml_file):
            self.dialog_exec("The configuration file does not exist!", "select_yaml_name_label")
            return False
        if not str(yaml_file).endswith(".yaml") and not str(yaml_file).endswith(".yml"):
            self.dialog_exec("The configuration filename must have .yaml or .yml extension", "select_yaml_name_label")
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
        if advise_user:
            self.dialog_exec("Configuration file checked and some errors were found. "
            "Please correct them before proceeding.", reason="error")
    else:
        self.ui.check_yaml_file_errors_label.setText("No errors found in the configuration file")
        self.ui.check_yaml_file_errors_frame.setStyleSheet("")
        if advise_user:
            self.dialog_exec("Configuration file checked and no errors found.", reason="inform_user")
            
        return True

def load_yaml_to_GUI(self):
    """

    """
    # Load YAML file
    yaml_file = QFileDialog.getOpenFileName()[0]
    if yaml_file == "": return # If no file was selected 
    with open(yaml_file, "r") as stream:
        try:
            loaded_cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print(loaded_cfg)

    # Load configuration file and check possible errors
    tmp_cfg = Config("/home/","jobname")
    errors = ""
    try:
        tmp_cfg._C.merge_from_file(yaml_file)
        tmp_cfg = tmp_cfg.get_cfg_defaults()
        check_configuration(tmp_cfg, check_data_paths=False)
    except Exception as errors:  
        errors = str(errors) 
        print(errors) 
        self.dialog_exec(errors, "load_yaml_error")
    else:
        
        # Find the workflow
        workflow_str = ""
        try:
            work_dim = loaded_cfg['PROBLEM']['NDIM']
        except:
            work_dim = "2D"
        try:
            work_id = loaded_cfg['PROBLEM']['TYPE']
        except: 
            work_id = "SEMANTIC_SEG"
            workflow_str = "SEM_SEG"
        if work_id == "SEMANTIC_SEG":
            self.cfg.settings['selected_workflow'] = 0
            workflow_str = "SEM_SEG"
        elif work_id == "INSTANCE_SEG":
            self.cfg.settings['selected_workflow'] = 1
            workflow_str = "INST_SEG"
        elif work_id == "DETECTION":
            self.cfg.settings['selected_workflow'] = 2
            workflow_str = "DET"
        elif work_id == "DENOISING":
            self.cfg.settings['selected_workflow'] = 3
        elif work_id == "SUPER_RESOLUTION":
            self.cfg.settings['selected_workflow'] = 4
        elif work_id == "SELF_SUPERVISED":
            self.cfg.settings['selected_workflow'] = 5
        else: # CLASSIFICATION
            self.cfg.settings['selected_workflow'] = 6
        move_between_pages(self, self.cfg.settings['selected_workflow'])

        # Go over configuration file
        errors, variables_set = analyze_dict(self, loaded_cfg, work_dim, "")
        print("Variables updated: ")
        for i, k in enumerate(variables_set.keys()):
            print("{}. {}: {}".format(i+1, k, variables_set[k]))
        print("Errors: ")
        for i in range(len(errors)):
            print("{}. : {}".format(i+1, errors[i]))

        # Message for the user
        if len(errors) == 0:
            self.dialog_exec("Configuration file succesfully loaded! You will "\
                "be redirected to the workflow page so you can modify the configuration.", "inform_user_and_go")
            self.cfg.settings['yaml_config_file_path'] = os.path.dirname(yaml_file)
            self.ui.goptions_browse_yaml_path_input.setText(os.path.dirname(yaml_file))
            self.ui.goptions_yaml_name_input.setText(os.path.basename(yaml_file))
        else:
            self.dialog_exec(errors, "load_yaml_ok_but_errors")

def analyze_dict(self, d, workflow_str, work_dim, s=""):
    errors = []
    variables_set = {}
    for k, v in d.items():
        if isinstance(v, dict):
            err, _vars = analyze_dict(self,v,workflow_str,work_dim,s+k if s == "" else s+"__"+k)
            if err is not None: 
                errors +=err
                variables_set.update(_vars)
        else:
            widget_name = s+"__"+k+"__INPUT"
            other_widgets_to_set = []
            other_widgets_values_to_set = []
            set_var = True 
            
            # Boolean cases 
            if isinstance(v, bool) and v:
                v = "Yes" 
            elif isinstance(v, bool) and not v:
                v = "No"

            # Special cases
            if widget_name == "DATA__VAL__FROM_TRAIN__INPUT":
                set_var = False
            elif widget_name == "SYSTEM__NUM_CPUS__INPUT":
                v = "All" if v == -1 else v
            elif widget_name == "PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT":
                if v == 'BC':
                    v = "Binary mask + Contours"
                elif v == 'BP':
                    v = "Binary mask + Central points"
                elif v == 'BD':
                    v = "Binary mask + Distance map"
                elif v == 'BCM':
                    v = "Binary mask + Contours + Foreground mask"
                elif v == 'BCD':
                    v = "Binary mask + Contours + Distance map"
                elif v == 'BCDv2':
                    v = "Binary mask + Contours + Distance map with background (experimental)"
                elif v == 'BDv2':
                    v = "Binary mask + Distance map with background (experimental)"
                else: 
                    v = "Distance map with background (experimental)"
            elif widget_name == "PROBLEM__TYPE__INPUT":
                set_var = False
            elif widget_name == "DATA__VAL__SPLIT_TRAIN__INPUT":
                other_widgets_to_set.append("DATA__VAL__TYPE__INPUT")
                other_widgets_values_to_set.append("Extract from train (split training)")
            elif widget_name == "DATA__VAL__CROSS_VAL__INPUT":
                other_widgets_to_set.append("DATA__VAL__TYPE__INPUT")
                other_widgets_values_to_set.append("Extract from train (cross validation)")
            elif widget_name == "MODEL__ARCHITECTURE__INPUT":    
                v = self.cfg.translate_model_names(v, work_dim, inv=True)
            elif widget_name == "MODEL__UNET_SR_UPSAMPLE_POSITION__INPUT":
                v = "Before model" if v == "pre" else "After model"
            elif widget_name == "DATA__TRAIN__MINIMUM_FOREGROUND_PER__INPUT":
                widget_name = "DATA__TRAIN__MINIMUM_FOREGROUND_PER__{}__INPUT".format(workflow_str)
            elif widget_name == "TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INPUT":
                widget_name = "TEST__POST_PROCESSING__YZ_FILTERING_SIZE__{}__INPUT".format(workflow_str)
            elif widget_name == "TEST__POST_PROCESSING__Z_FILTERING_SIZE__INPUT":
                widget_name = "TEST__POST_PROCESSING__Z_FILTERING_SIZE__{}__INPUT".format(workflow_str)
            elif widget_name == "TEST__POST_PROCESSING__Z_FILTERING_SIZE__INPUT":
                widget_name = "TEST__POST_PROCESSING__WATERSHED_CIRCULARITY__{}__INPUT".format(workflow_str)
            elif widget_name == "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INPUT":
                widget_name = "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__{}__INPUT".format(workflow_str)

            # Set variable values
            if set_var: 
                all_widgets_to_set = [widget_name]
                all_widgets_to_set_values = [v]

                all_widgets_to_set += other_widgets_to_set
                all_widgets_to_set_values += other_widgets_values_to_set

                for x, y in zip(all_widgets_to_set, all_widgets_to_set_values):
                    if hasattr(self.ui, x):
                        err = set_text(getattr(self.ui, x), str(y))
                    else:
                        err = "{} widget does not exist".format(x)
                    if err is not None:
                        errors.append(err)
                    else:
                        variables_set[widget_name] = y
                        print("Setting {} : {} ({})".format(widget_name, y, k))
                    
    return errors, variables_set