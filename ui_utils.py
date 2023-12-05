import os 
import sys
import traceback
import docker
import ast 
import GPUtil
import yaml
import queue
from pathlib import PurePath, Path, PureWindowsPath

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QUrl, QObject, QThread
from PySide2.QtWidgets import *

import settings
from biapy_config import Config
from biapy_check_configuration import check_configuration

def examine(main_window, save_in_obj_tag=None, is_file=True):
    """ 
    Find an item in disk. Can be a file or a directory.  

    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    save_in_obj_tag : str
        Name of the widget to set the item's name into. 

    is_file : bool, optional
        Whether the item to find is a file or a directory.
    """
    if not is_file:
        out = QFileDialog.getExistingDirectory(main_window, 'Select a directory')
    else:
        out = QFileDialog.getOpenFileName()[0]

    if out == "": return # If no file was selected 

    if save_in_obj_tag is not None:
        getattr(main_window.ui, save_in_obj_tag).setText(os.path.normpath(out))
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

def mark_syntax_error(main_window, gui_widget_name, validator_type=["empty"]):
    """ 
    Functionality for the advanced option button (Down/UP arrows in GUI). 

    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    gui_widget_name : str
        Name of the button that triggers the function. 

    validator_type : List of str
        Constraints that ``gui_widget_name`` needs to satisfy in order to not have an 
        error. Options avaiable: ['empty', 'exists']. 'empty' means that the value can 
        not be empty, i.e. '' being an string, and 'exists' means that its value 
        represents a path and it needs to exist.
    """
    # Check constraints 
    error = False
    for v in validator_type:
        if v == "empty" and get_text(getattr(main_window.ui, gui_widget_name)) == "":
            error = True
        elif v == "exists" and not os.path.exists(get_text(getattr(main_window.ui, gui_widget_name))):
            error = True
        
    # Tell the user if there was an error
    if error:
        getattr(main_window.ui, gui_widget_name).setStyleSheet("border: 2px solid red;")
    else:
        getattr(main_window.ui, gui_widget_name).setStyleSheet("")

        out = get_text(getattr(main_window.ui, gui_widget_name))
        if gui_widget_name == "goptions_browse_yaml_path_input":
            main_window.cfg.settings['yaml_config_file_path'] = out
        elif gui_widget_name == "select_yaml_name_label":
            out_write = os.path.basename(out)
            main_window.cfg.settings['yaml_config_filename'] = out_write
            main_window.cfg.settings['yaml_config_file_path'] = os.path.dirname(out)
            main_window.ui.job_name_input.setPlainText(os.path.splitext(out_write)[0])

            # Reset the check
            main_window.ui.check_yaml_file_errors_label.setText("")
            main_window.ui.check_yaml_file_errors_frame.setStyleSheet("") 
        elif gui_widget_name == "output_folder_input":
            main_window.cfg.settings['output_folder'] = out 

def expand_hide_advanced_options(main_window, advanced_options_bn_tag, advanced_options_frame_tag):
    """
    Functionality for the advanced option button (Down/UP arrows in GUI). 

    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    advanced_options_bn_tag : str
        Name of the button that triggers the function. 

    advanced_options_frame_tag : str
        Name of the frame to show/hide.
    """
    expand = not getattr(main_window.ui, advanced_options_frame_tag).isVisible()
    getattr(main_window.ui, advanced_options_bn_tag).setIcon(main_window.cfg.settings['advanced_frame_images'][0] if expand else main_window.cfg.settings['advanced_frame_images'][1])
    getattr(main_window.ui, advanced_options_frame_tag).setVisible(expand)

def resource_path(relative_path):
    """ 
    Gets absolute path to resource. Needed for Pyinstaller so the resources are found in every OS.
    
    Parameters
    ----------
    relative_path : str
        Relative path of an item.
    
    Returns
    -------
    path : str
        Absolute path of the item. 
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def change_page(main_window, buttonName, to_page):
    """
    Move between pages.
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    buttonName : str
        Name of the button that triggers the movement. 

    to_page : int
        Number of the page moving to.
    """
    for each in main_window.ui.frame_bottom_west.findChildren(QFrame):
        if "biapy" not in each.objectName() or "frame_run_biapy" == each.objectName():
            each.setStyleSheet("background:rgb(64,144,253)")

    # Use global page_number to move as the user selected continue button
    if to_page == -1:
        move = True
        # if page_number != 1:
        #     move = UIFunction.check_input(main_window, page_number)
        # Do not move until the errors are corrected 
        if not move: return

        if buttonName == "up":
            main_window.cfg.settings['page_number'] += 1
        else:
            main_window.cfg.settings['page_number'] -= 1
        to_page = main_window.cfg.settings['page_number']

    if buttonName=='bn_home' or (buttonName=='down' and to_page == 0):
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_home)
        main_window.ui.frame_home.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 0

    elif buttonName=='bn_workflow' or ('bn_' not in buttonName and to_page == 1):
        main_window.ui.continue_bn.setText("Continue")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.workflow_selection_page)
        main_window.ui.frame_workflow.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 1
        adjust_window_progress(main_window)

    elif buttonName=='bn_goptions' or ('bn_' not in buttonName and to_page == 2):
        main_window.ui.continue_bn.setText("Continue")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.goptions_page)
        main_window.ui.frame_goptions.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 2
        adjust_window_progress(main_window)

    elif buttonName=='bn_train' or ('bn_' not in buttonName and to_page == 3):
        main_window.ui.continue_bn.setText("Continue")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.train_page)
        main_window.ui.frame_train.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 3
        adjust_window_progress(main_window)

    elif buttonName=='bn_test' or ('bn_' not in buttonName and to_page == 4):
        main_window.ui.continue_bn.setText("Create configuration file")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.test_page)
        main_window.ui.frame_test.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 4
        adjust_window_progress(main_window)

    elif buttonName=='bn_run_biapy' or ('bn_' not in buttonName and to_page == 5):            
        error = False
        created = True
        if ('bn_' not in buttonName and to_page == 5):
            error, created = create_yaml_file(main_window)
        # If there is an error do not make the movement, as the error dialog will redirect the user to the 
        # field that raises the error 
        if not error and created: 
            main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_run_biapy)
            main_window.ui.frame_run_biapy.setStyleSheet("background:rgb(255,255,255)") 
            main_window.cfg.settings['page_number'] = 5
        if not created:
            main_window.cfg.settings['page_number'] -= 1    
    move_between_workflows(main_window, to_page)   

def adjust_window_progress(main_window):
    """
    Changes new workflow creation progress visual clues. Currently, the blue dots in the bottom part of the GUI.  
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    main_window.ui.window1_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 1 else main_window.cfg.settings['dot_images'][1])
    main_window.ui.window2_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 2 else main_window.cfg.settings['dot_images'][1])
    main_window.ui.window3_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 3 else main_window.cfg.settings['dot_images'][1])
    main_window.ui.window4_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 4 else main_window.cfg.settings['dot_images'][1])

def move_between_workflows(main_window, to_page, dims=None):
    """
    Changes GUI variables and options according to the workflow and page selected. 
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.

    to_page : int
        Number of the page moving to. 

    dims : str, optional
        Image dimension choosen. E.g. ``2D`` or ``3D``.
    """
    # Semantic seg
    if main_window.cfg.settings['selected_workflow'] == 0:
        jobname = "my_semantic_segmentation"
        models = main_window.cfg.settings['semantic_models_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_semantic_seg_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_semantic_seg_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input label folder")
        main_window.ui.train_gt_label.setVisible(True)
        main_window.ui.train_gt_info.setVisible(True)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(True)
        main_window.ui.validation_data_gt_label.setText("Input label folder")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input label folder")
        main_window.ui.test_exists_gt_label.setText("Do you have test labels?")
        main_window.ui.test_exists_gt_label.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)
    # Instance seg
    elif main_window.cfg.settings['selected_workflow'] == 1:
        jobname = "my_instance_segmentation"
        models = main_window.cfg.settings['instance_models_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_instance_seg_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_instance_seg_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input label folder")
        main_window.ui.train_gt_label.setVisible(True)
        main_window.ui.train_gt_info.setVisible(True)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(True)
        main_window.ui.validation_data_gt_label.setText("Input label folder")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input label folder")
        main_window.ui.test_exists_gt_label.setText("Do you have test labels?")
        main_window.ui.test_exists_gt_label.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)
    # Detection
    elif main_window.cfg.settings['selected_workflow'] == 2:
        jobname = "my_detection"
        models = main_window.cfg.settings['detection_models_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_detection_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_detection_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input CSV folder")
        main_window.ui.train_gt_label.setVisible(True)
        main_window.ui.train_gt_info.setVisible(True)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(True)
        main_window.ui.validation_data_gt_label.setText("Input CSV folder")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input CSV folder")
        main_window.ui.test_exists_gt_label.setText("Do you have CSV files for test data?")
        main_window.ui.test_exists_gt_label.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)
    # Denoising
    elif main_window.cfg.settings['selected_workflow'] == 3:
        jobname = "my_denoising"
        models = main_window.cfg.settings['denoising_models_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_denoising_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_denoising_page)
        # Train page
        main_window.ui.train_gt_label.setVisible(False)
        main_window.ui.train_gt_info.setVisible(True)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(False)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        main_window.ui.test_data_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INFO.setVisible(False)
        main_window.ui.test_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.test_exists_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(False)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)
    # Super resolution
    elif main_window.cfg.settings['selected_workflow'] == 4:
        jobname = "my_super_resolution"
        if dims is None:
            if get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "2D":
                models = main_window.cfg.settings['sr_2d_models_real_names']
            else:
                models = main_window.cfg.settings['sr_3d_models_real_names']
        else:
            if dims == "2D":
                models = main_window.cfg.settings['sr_2d_models_real_names']
            else:
                models = main_window.cfg.settings['sr_3d_models_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_sr_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_sr_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input high-resolution image folder")
        main_window.ui.train_gt_label.setVisible(True)
        main_window.ui.train_gt_info.setVisible(True)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(True)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(True)
        main_window.ui.validation_data_gt_label.setText("Input high-resolution image folder")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input high-resolution image folder")
        main_window.ui.test_exists_gt_label.setText("Do you have high-resolution test data?")
        main_window.ui.test_exists_gt_label.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)
    # Self-supevised learning
    elif main_window.cfg.settings['selected_workflow'] == 5:
        jobname = "my_self_supervised_learning"
        models = main_window.cfg.settings['ssl_models_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_ssl_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_ssl_page)
        # Train page
        main_window.ui.train_gt_label.setVisible(False)
        main_window.ui.train_gt_info.setVisible(False)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(False)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        main_window.ui.test_data_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INFO.setVisible(False)
        main_window.ui.test_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.test_exists_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(False)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)
    # Classification
    elif main_window.cfg.settings['selected_workflow'] == 6:
        jobname = "my_classification"
        models = main_window.cfg.settings['classification_models_real_names']
        goptions_tab_widget_visible = True
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_classification_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_classification_page)
        # Train page
        main_window.ui.train_gt_label.setVisible(False)
        main_window.ui.train_gt_info.setVisible(False)
        main_window.ui.DATA__TRAIN__GT_PATH__INPUT.setVisible(False)
        main_window.ui.train_data_gt_input_browse_bn.setVisible(False)
        # Test page
        main_window.ui.test_data_gt_label.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INPUT.setVisible(False)
        main_window.ui.DATA__TEST__GT_PATH__INFO.setVisible(False)
        main_window.ui.test_data_gt_input_browse_bn.setVisible(False)
        main_window.ui.test_exists_gt_label.setText("Is the test separated in classes?")
        main_window.ui.test_exists_gt_label.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INPUT.setVisible(True)
        main_window.ui.DATA__TEST__LOAD_GT__INFO.setVisible(True)

    actual_name = get_text(main_window.ui.job_name_input)
    if actual_name in ["", "my_semantic_segmentation", "my_instance_segmentation", "my_detection", "my_denoising", \
        "my_super_resolution", "my_self_supervised_learning", "my_classification"]:
        if to_page == 5:
            main_window.ui.job_name_input.setPlainText(jobname)

    # General options page
    if to_page == 2:
        main_window.ui.goptions_advanced_options_scrollarea.setVisible(False)

    # Train page
    if main_window.last_selected_workflow != main_window.cfg.settings['selected_workflow']:
        main_window.last_selected_workflow = main_window.cfg.settings['selected_workflow']
        main_window.ui.MODEL__ARCHITECTURE__INPUT.clear()
        main_window.ui.MODEL__ARCHITECTURE__INPUT.addItems(models)

def oninit_checks(main_window):
    """
    Initial checks of the GUI. Specifically, Docker installation and GPU are checked.  
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    # Docker check
    try:
        docker_client = docker.from_env()
        main_window.cfg.settings['docker_found'] = True
    except:
        main_window.cfg.settings['docker_found'] = False
        print(traceback.format_exc())
    if main_window.cfg.settings['docker_found']:
        main_window.ui.docker_status_label.setText("<br>Docker installation found")
        main_window.cfg.settings['biapy_container_ready'] = True
        main_window.ui.docker_head_label.setText("Docker dependency")

        main_window.ui.docker_frame.setStyleSheet("#docker_frame { border: 3px solid green; border-radius: 25px;}\n#docker_frame:disabled {border: 3px solid rgb(169,169,169);}")
    else:
        main_window.ui.docker_status_label.setText("Docker installation not found. Follow the \
                <a href=\"https://biapy.readthedocs.io/en/latest/get_started/installation.html#docker-installation/\">documentation</a> to install it.")
        main_window.ui.docker_head_label.setText("Docker dependency error")
        main_window.ui.docker_frame.setStyleSheet("#docker_frame { border: 3px solid red; border-radius: 25px;}\n#docker_frame:disabled {border: 3px solid rgb(169,169,169);}")

    # GPU check
    try:
        main_window.cfg.settings['GPUs'] = GPUtil.getGPUs()

        # Find the container that
        pos = -1
        if len(main_window.cfg.settings['GPUs']) > 0:
            driver_version = float(".".join(main_window.cfg.settings['GPUs'][0].driver.split('.')[:2]))
            for i in range(len(main_window.cfg.settings['NVIDIA_driver_list'])):
                pos = i
                if driver_version < main_window.cfg.settings['NVIDIA_driver_list'][i]:
                    break

        main_window.cfg.settings['biapy_container_name'] = \
            main_window.cfg.settings['biapy_container_basename'] + ":latest-"+str(main_window.cfg.settings['CUDA_version'][pos])
        main_window.cfg.settings['biapy_container_size'] = main_window.cfg.settings['biapy_container_sizes'][pos]
        print(f"Using {main_window.cfg.settings['biapy_container_name']} container")

    except Exception as gpu_check_error:
        main_window.cfg.settings['GPUs'] = []
        print(f"ERROR during driver check: {gpu_check_error}")

    if len(main_window.cfg.settings['GPUs']) > 0:
        if len(main_window.cfg.settings['GPUs']) == 1:
            main_window.ui.gpu_status_label.setText("1 NVIDIA GPU card found")
        else:
            main_window.ui.gpu_status_label.setText("{} NVIDIA GPU cards found".format(len(main_window.cfg.settings['GPUs'])))
        main_window.ui.gpu_head_label.setText("GPU dependency")
        main_window.ui.gpu_frame.setStyleSheet("#gpu_frame { border: 3px solid green; border-radius: 25px;}\n#gpu_frame:disabled {border: 3px solid rgb(169,169,169);}")
    else:
        main_window.ui.gpu_status_label.setText("No NVIDIA GPU card was found. BiaPy will run on the CPU, which is much slower!")
        main_window.ui.gpu_head_label.setText("GPU dependency error")
        main_window.ui.gpu_frame.setStyleSheet("#gpu_frame { border: 3px solid red; border-radius: 25px;}\n#gpu_frame:disabled {border: 3px solid rgb(169,169,169);}")


def get_text(gui_widget):
    """
    Gets the value of the input widget. 
    
    Parameters
    ----------
    gui_widget : QWidget
        Widget to get the value from. 
    """
    if isinstance(gui_widget, QComboBox):
        return gui_widget.currentText()
    elif isinstance(gui_widget, QLineEdit):
        return gui_widget.text()
    else: #QTextBrowser
        return gui_widget.toPlainText()

def set_text(gui_widget, new_value):
    """
    Sets a new value to the input widget. 
    
    Parameters
    ----------
    gui_widget : QWidget
        Widget to change the value to. 

    new_value : str
        Value to set. 
    """  
    if isinstance(gui_widget, QComboBox):
        index = gui_widget.findText(new_value)
        if index >= 0:
            gui_widget.setCurrentIndex(index)
        else:
            return "{} couldn't be loaded in {}".format(new_value,gui_widget.objectName())
    elif isinstance(gui_widget, QLineEdit):
        if "PATH" in gui_widget.objectName():
            gui_widget.setText(os.path.normpath(new_value))
        else:
            gui_widget.setText(new_value)
    else: #QTextBrowser
        gui_widget.setText(new_value)

def create_yaml_file(main_window): 
    """
    Create a new YAML configuration file with the variables from GUI. 
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.

    Returns
    -------
    errors : bool
        True if there was an error during the config file creation.

    created : bool
        True if the YAML file was finally created.
    """       
    biapy_config = {}

    # System
    biapy_config['SYSTEM'] = {}
    
    cpus = get_text(main_window.ui.SYSTEM__NUM_CPUS__INPUT)
    cpus = -1 if cpus == "All" else int(cpus)
    biapy_config['SYSTEM']['NUM_CPUS'] = cpus
    biapy_config['SYSTEM']['SEED'] = int(get_text(main_window.ui.SYSTEM__SEED__INPUT))

    # Problem specification
    workflow_names_yaml = ['SEMANTIC_SEG', 'INSTANCE_SEG', 'DETECTION', 'DENOISING', 'SUPER_RESOLUTION', 
        'SELF_SUPERVISED', 'CLASSIFICATION']
    biapy_config['PROBLEM'] = {}
    biapy_config['PROBLEM']['TYPE'] = workflow_names_yaml[main_window.cfg.settings['selected_workflow']]
    biapy_config['PROBLEM']['NDIM'] = get_text(main_window.ui.PROBLEM__NDIM__INPUT)
    
    ### SEMANTIC_SEG
    if main_window.cfg.settings['selected_workflow'] == 0:
        biapy_config['PROBLEM']['SEMANTIC_SEG'] = {}
        if get_text(main_window.ui.PROBLEM__SEMANTIC_SEG__IGNORE_CLASS_ID__INPUT) != 0:
            biapy_config['PROBLEM']['SEMANTIC_SEG']['IGNORE_CLASS_ID'] = get_text(main_window.ui.PROBLEM__SEMANTIC_SEG__IGNORE_CLASS_ID__INPUT)

    ### INSTANCE_SEG
    elif main_window.cfg.settings['selected_workflow'] == 1:
        biapy_config['PROBLEM']['INSTANCE_SEG'] = {}
        
        # Transcribe problem representation
        problem_channels = 'BC'
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours":
            problem_channels = 'BC'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Central points":
            problem_channels = 'BP'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Distance map":
            problem_channels = 'BD'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours + Foreground mask":
            problem_channels = 'BCM'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours + Distance map":
            problem_channels = 'BCD'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Contours + Distance map with background (experimental)":
            problem_channels = 'BCDv2'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Binary mask + Distance map with background (experimental)":
            problem_channels = 'BDv2'
        else: # Distance map with background (experimental)
            problem_channels = 'Dv2'
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNELS'] = problem_channels
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNEL_WEIGHTS__INPUT) != (1,1):
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHANNEL_WEIGHTS'] = get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNEL_WEIGHTS__INPUT) 
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT) != "thick":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CONTOUR_MODE'] = get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CONTOUR_MODE__INPUT)
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHECK_MW__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_CHECK_MW'] = True 
        biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_TYPE'] = get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_TYPE__INPUT)
        if 'B' in problem_channels:
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_BINARY_MASK'] = float(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_BINARY_MASK__INPUT))
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_FOREGROUND'] = float(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_FOREGROUND__INPUT))
        if 'C' in problem_channels:
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_CONTOUR'] = float(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_CONTOUR__INPUT))
        if 'D' in problem_channels:    
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_DISTANCE'] = float(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_DISTANCE__INPUT))
            if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DISTANCE_CHANNEL_MASK__INPUT) == "Yes":
                biapy_config['PROBLEM']['INSTANCE_SEG']['DISTANCE_CHANNEL_MASK'] = True
        if 'P' in problem_channels: 
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_POINTS'] = float(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_MW_TH_POINTS__INPUT))
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_BEFORE_MW__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_BEFORE_MW'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_REMOVE_SMALL_OBJ_BEFORE'] = int(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_REMOVE_SMALL_OBJ_BEFORE__INPUT))
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_SEQUENCE__INPUT) != "[]":
            biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_SEQUENCE'] = ast.literal_eval(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_SEQUENCE__INPUT) )
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT) != "[]":
            biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_RADIUS'] =  ast.literal_eval(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT))
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['ERODE_AND_DILATE_FOREGROUND'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_EROSION_RADIUS'] = int(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT))
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_DILATION_RADIUS'] = int(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT))

    ### DETECTION
    elif main_window.cfg.settings['selected_workflow'] == 2:
        biapy_config['PROBLEM']['DETECTION'] = {}
        biapy_config['PROBLEM']['DETECTION']['CENTRAL_POINT_DILATION'] = int(get_text(main_window.ui.PROBLEM__DETECTION__CENTRAL_POINT_DILATION__INPUT))
        biapy_config['PROBLEM']['DETECTION']['CHECK_POINTS_CREATED'] = True if get_text(main_window.ui.PROBLEM__DETECTION__CHECK_POINTS_CREATED__INPUT) == "Yes" else False
        if get_text(main_window.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INPUT) == "Yes" and get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT) == "Yes":
            biapy_config['PROBLEM']['DETECTION']['DATA_CHECK_MW'] = True

    ### DENOISING
    elif main_window.cfg.settings['selected_workflow'] == 3:
        biapy_config['PROBLEM']['DENOISING'] = {}
        biapy_config['PROBLEM']['DENOISING']['N2V_PERC_PIX'] = float(get_text(main_window.ui.PROBLEM__DENOISING__N2V_PERC_PIX__INPUT))
        biapy_config['PROBLEM']['DENOISING']['N2V_MANIPULATOR'] = get_text(main_window.ui.PROBLEM__DENOISING__N2V_MANIPULATOR__INPUT)
        biapy_config['PROBLEM']['DENOISING']['N2V_NEIGHBORHOOD_RADIUS'] = int(get_text(main_window.ui.PROBLEM__DENOISING__N2V_NEIGHBORHOOD_RADIUS__INPUT))
        biapy_config['PROBLEM']['DENOISING']['N2V_STRUCTMASK'] = True if get_text(main_window.ui.PROBLEM__DENOISING__N2V_STRUCTMASK__INPUT) == "Yes" else False

    ### SUPER_RESOLUTION
    elif main_window.cfg.settings['selected_workflow'] == 4:
        biapy_config['PROBLEM']['SUPER_RESOLUTION'] = {}
        biapy_config['PROBLEM']['SUPER_RESOLUTION']['UPSCALING'] = int(get_text(main_window.ui.PROBLEM__SUPER_RESOLUTION__UPSCALING__INPUT))

    ### SELF_SUPERVISED
    elif main_window.cfg.settings['selected_workflow'] == 5:
        biapy_config['PROBLEM']['SELF_SUPERVISED'] = {}
        biapy_config['PROBLEM']['SELF_SUPERVISED']['PRETEXT_TASK'] = get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT)
        if get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT) == "crappify":
            biapy_config['PROBLEM']['SELF_SUPERVISED']['RESIZING_FACTOR'] = int(get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INPUT))
            biapy_config['PROBLEM']['SELF_SUPERVISED']['NOISE'] = float(get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__NOISE__INPUT))

    # Dataset
    biapy_config['DATA'] = {}
    if get_text(main_window.ui.DATA__CHECK_GENERATORS__INPUT) == "Yes":
        biapy_config['DATA']['CHECK_GENERATORS'] = True

    biapy_config['DATA']['PATCH_SIZE'] = get_text(main_window.ui.DATA__PATCH_SIZE__INPUT)
    if get_text(main_window.ui.DATA__EXTRACT_RANDOM_PATCH__INPUT) == "Yes":
        biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = True
        if get_text(main_window.ui.DATA__PROBABILITY_MAP__INPUT) == "Yes":
            biapy_config['DATA']['PROBABILITY_MAP'] = True
            biapy_config['DATA']['W_FOREGROUND'] = float(get_text(main_window.ui.DATA__W_FOREGROUND__INPUT))
            biapy_config['DATA']['W_BACKGROUND'] = float(get_text(main_window.ui.DATA__W_BACKGROUND__INPUT)) 
    else:
        biapy_config['DATA']['EXTRACT_RANDOM_PATCH'] = False

    if get_text(main_window.ui.DATA__REFLECT_TO_COMPLETE_SHAPE__INPUT) == "Yes":
        biapy_config['DATA']['REFLECT_TO_COMPLETE_SHAPE'] = True

    if get_text(main_window.ui.DATA__NORMALIZATION__TYPE__INPUT) == "custom":
        biapy_config['DATA']['NORMALIZATION'] = {}
        biapy_config['DATA']['NORMALIZATION']['TYPE'] = 'custom'
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_MEAN'] = float(get_text(main_window.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT)) 
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_STD'] = float(get_text(main_window.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT)) 

    # Train
    if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TRAIN'] = {}

        if main_window.cfg.settings['selected_workflow'] == 0 and get_text(main_window.ui.DATA__TRAIN__CHECK_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TRAIN']['CHECK_DATA'] = True
        
        biapy_config['DATA']['TRAIN']['IN_MEMORY'] = True if get_text(main_window.ui.DATA__TRAIN__IN_MEMORY__INPUT) == "Yes" else False
        biapy_config['DATA']['TRAIN']['PATH'] = get_text(main_window.ui.DATA__TRAIN__PATH__INPUT)
        if main_window.cfg.settings['selected_workflow'] not in [5,6,7]:
            biapy_config['DATA']['TRAIN']['GT_PATH'] = get_text(main_window.ui.DATA__TRAIN__GT_PATH__INPUT)
        if int(get_text(main_window.ui.DATA__TRAIN__REPLICATE__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['REPLICATE'] = int(get_text(main_window.ui.DATA__TRAIN__REPLICATE__INPUT))
        biapy_config['DATA']['TRAIN']['OVERLAP'] = get_text(main_window.ui.DATA__TRAIN__OVERLAP__INPUT)
        biapy_config['DATA']['TRAIN']['PADDING'] = get_text(main_window.ui.DATA__TRAIN__PADDING__INPUT)
        if get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT) != "(1,1,1)" and get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT) != "(1,1)":
            biapy_config['DATA']['TRAIN']['RESOLUTION'] = get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT)
        
        if main_window.cfg.settings['selected_workflow'] == 0 and int(get_text(main_window.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__SEM_SEG__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(main_window.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__SEM_SEG__INPUT))
        if main_window.cfg.settings['selected_workflow'] == 1 and int(get_text(main_window.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__INST_SEG__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(main_window.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__INST_SEG__INPUT))
        if main_window.cfg.settings['selected_workflow'] == 2 and int(get_text(main_window.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__DET__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['MINIMUM_FOREGROUND_PER'] = int(get_text(main_window.ui.DATA__TRAIN__MINIMUM_FOREGROUND_PER__DET__INPUT))
        
        # Validation
        biapy_config['DATA']['VAL'] = {}

        if get_text(main_window.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (split training)":
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
            biapy_config['DATA']['VAL']['SPLIT_TRAIN'] = float(get_text(main_window.ui.DATA__VAL__SPLIT_TRAIN__INPUT))
            biapy_config['DATA']['VAL']['RANDOM'] = True if get_text(main_window.ui.DATA__VAL__RANDOM__INPUT) == "Yes" else False 
        elif get_text(main_window.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (cross validation)":
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = True
            biapy_config['DATA']['VAL']['CROSS_VAL'] = True
            biapy_config['DATA']['VAL']['CROSS_VAL_NFOLD'] = int(get_text(main_window.ui.DATA__VAL__CROSS_VAL_NFOLD__INPUT))
            biapy_config['DATA']['VAL']['CROSS_VAL_FOLD'] = int(get_text(main_window.ui.DATA__VAL__CROSS_VAL_FOLD__INPUT))
            biapy_config['DATA']['VAL']['RANDOM'] = True if get_text(main_window.ui.DATA__VAL__RANDOM__INPUT) == "Yes" else False 
        # Not extracted from train (path needed)
        else:
            biapy_config['DATA']['VAL']['FROM_TRAIN'] = False
            biapy_config['DATA']['VAL']['IN_MEMORY'] = True if get_text(main_window.ui.DATA__VAL__IN_MEMORY__INPUT) == "Yes" else False 
            biapy_config['DATA']['VAL']['PATH'] = get_text(main_window.ui.DATA__VAL__PATH__INPUT)
            if main_window.cfg.settings['selected_workflow'] not in [5,6,7]:
                biapy_config['DATA']['VAL']['GT_PATH'] = get_text(main_window.ui.DATA__VAL__GT_PATH__INPUT)
            biapy_config['DATA']['VAL']['OVERLAP'] = get_text(main_window.ui.DATA__VAL__OVERLAP__INPUT)
            biapy_config['DATA']['VAL']['PADDING'] = get_text(main_window.ui.DATA__VAL__PADDING__INPUT)

        biapy_config['DATA']['VAL']['RESOLUTION'] = get_text(main_window.ui.DATA__VAL__RESOLUTION__INPUT)

    # Test
    if get_text(main_window.ui.TEST__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TEST'] = {}
        if main_window.cfg.settings['selected_workflow'] == 0 and get_text(main_window.ui.DATA__TEST__CHECK_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['CHECK_DATA'] = True
        if get_text(main_window.ui.DATA__TEST__IN_MEMORY__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['IN_MEMORY'] = True
        else:
            biapy_config['DATA']['TEST']['IN_MEMORY'] = False
        if get_text(main_window.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT) == "Yes" and\
            get_text(main_window.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (cross validation)":
            biapy_config['DATA']['TEST']['USE_VAL_AS_TEST'] = True
        else:
            if get_text(main_window.ui.DATA__TEST__LOAD_GT__INPUT) == "Yes":
                biapy_config['DATA']['TEST']['LOAD_GT'] = True
                if main_window.cfg.settings['selected_workflow'] not in [5,6,7]:
                    biapy_config['DATA']['TEST']['GT_PATH'] = get_text(main_window.ui.DATA__TEST__GT_PATH__INPUT)
            else:
                biapy_config['DATA']['TEST']['LOAD_GT'] = False
            biapy_config['DATA']['TEST']['PATH'] = get_text(main_window.ui.DATA__TEST__PATH__INPUT)
            
        biapy_config['DATA']['TEST']['OVERLAP'] = get_text(main_window.ui.DATA__TEST__OVERLAP__INPUT)
        biapy_config['DATA']['TEST']['PADDING'] = get_text(main_window.ui.DATA__TEST__PADDING__INPUT)
        if get_text(main_window.ui.DATA__TEST__MEDIAN_PADDING__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['MEDIAN_PADDING'] = True 
        biapy_config['DATA']['TEST']['RESOLUTION'] = get_text(main_window.ui.DATA__TEST__RESOLUTION__INPUT)
        if get_text(main_window.ui.DATA__TEST__ARGMAX_TO_OUTPUT__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['ARGMAX_TO_OUTPUT'] = True

    # Data augmentation (DA)
    biapy_config['AUGMENTOR'] = {}
    if get_text(main_window.ui.AUGMENTOR__ENABLE__INPUT) == "Yes":
        biapy_config['AUGMENTOR']['ENABLE'] = True  
        biapy_config['AUGMENTOR']['DA_PROB'] = float(get_text(main_window.ui.AUGMENTOR__DA_PROB__INPUT))
        biapy_config['AUGMENTOR']['AUG_SAMPLES'] = True if get_text(main_window.ui.AUGMENTOR__AUG_SAMPLES__INPUT) == "Yes" else False
        if get_text(main_window.ui.AUGMENTOR__DRAW_GRID__INPUT) == "False": 
            biapy_config['AUGMENTOR']['DRAW_GRID'] = False
        if int(get_text(main_window.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT)) != 10:
            biapy_config['AUGMENTOR']['AUG_NUM_SAMPLES'] = int(get_text(main_window.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT))
        biapy_config['AUGMENTOR']['SHUFFLE_TRAIN_DATA_EACH_EPOCH'] = True if get_text(main_window.ui.AUGMENTOR__SHUFFLE_TRAIN_DATA_EACH_EPOCH__INPUT) == "Yes" else False 
        biapy_config['AUGMENTOR']['SHUFFLE_VAL_DATA_EACH_EPOCH'] = True if get_text(main_window.ui.AUGMENTOR__SHUFFLE_VAL_DATA_EACH_EPOCH__INPUT) == "Yes" else False 
        if get_text(main_window.ui.AUGMENTOR__ROT90__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ROT90'] = True 
        if get_text(main_window.ui.AUGMENTOR__RANDOM_ROT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['RANDOM_ROT'] = True  
            biapy_config['AUGMENTOR']['RANDOM_ROT_RANGE'] = get_text(main_window.ui.AUGMENTOR__RANDOM_ROT_RANGE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__SHEAR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SHEAR'] = True  
            biapy_config['AUGMENTOR']['SHEAR_RANGE'] = get_text(main_window.ui.AUGMENTOR__SHEAR_RANGE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__ZOOM__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ZOOM'] = True  
            biapy_config['AUGMENTOR']['ZOOM_RANGE'] = get_text(main_window.ui.AUGMENTOR__ZOOM_RANGE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__SHIFT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SHIFT'] = True 
            biapy_config['AUGMENTOR']['SHIFT_RANGE'] = get_text(main_window.ui.AUGMENTOR__SHIFT_RANGE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__SHIFT__INPUT) == "Yes" or get_text(main_window.ui.AUGMENTOR__ZOOM__INPUT) == "Yes" or\
            get_text(main_window.ui.AUGMENTOR__SHEAR__INPUT) == "Yes" or get_text(main_window.ui.AUGMENTOR__RANDOM_ROT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['AFFINE_MODE'] = get_text(main_window.ui.AUGMENTOR__AFFINE_MODE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__VFLIP__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['VFLIP'] = True 
        if get_text(main_window.ui.AUGMENTOR__HFLIP__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['HFLIP'] = True 
        if get_text(main_window.ui.AUGMENTOR__ZFLIP__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ZFLIP'] = True 
        if get_text(main_window.ui.AUGMENTOR__ELASTIC__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ELASTIC'] = True 
            biapy_config['AUGMENTOR']['E_ALPHA'] = get_text(main_window.ui.AUGMENTOR__E_ALPHA__INPUT)
            biapy_config['AUGMENTOR']['E_SIGMA'] = int(get_text(main_window.ui.AUGMENTOR__E_SIGMA__INPUT))
            biapy_config['AUGMENTOR']['E_MODE'] = get_text(main_window.ui.AUGMENTOR__E_MODE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__G_BLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['G_BLUR'] = True 
            biapy_config['AUGMENTOR']['G_SIGMA'] = get_text(main_window.ui.AUGMENTOR__G_SIGMA__INPUT)
        if get_text(main_window.ui.AUGMENTOR__MEDIAN_BLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MEDIAN_BLUR'] = True 
            biapy_config['AUGMENTOR']['MB_KERNEL'] = get_text(main_window.ui.AUGMENTOR__MB_KERNEL__INPUT)
        if get_text(main_window.ui.AUGMENTOR__MOTION_BLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MOTION_BLUR'] = True 
            biapy_config['AUGMENTOR']['MOTB_K_RANGE'] = get_text(main_window.ui.AUGMENTOR__MOTB_K_RANGE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__GAMMA_CONTRAST__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GAMMA_CONTRAST'] = True
            biapy_config['AUGMENTOR']['GC_GAMMA'] = get_text(main_window.ui.AUGMENTOR__GC_GAMMA__INPUT)
        if get_text(main_window.ui.AUGMENTOR__BRIGHTNESS__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['BRIGHTNESS'] = True
            biapy_config['AUGMENTOR']['BRIGHTNESS_FACTOR'] = get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['BRIGHTNESS_MODE'] = get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__CONTRAST__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CONTRAST'] = True
            biapy_config['AUGMENTOR']['CONTRAST_FACTOR'] = get_text(main_window.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['CONTRAST_MODE'] = get_text(main_window.ui.AUGMENTOR__CONTRAST_MODE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_EM__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM'] = True
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM_FACTOR'] = get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_EM_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['BRIGHTNESS_EM_MODE'] = get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_EM_MODE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__CONTRAST_EM__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CONTRAST_EM'] = True
            biapy_config['AUGMENTOR']['CONTRAST_EM_FACTOR'] = get_text(main_window.ui.AUGMENTOR__CONTRAST_EM_FACTOR__INPUT)
            biapy_config['AUGMENTOR']['CONTRAST_EM_MODE'] = get_text(main_window.ui.AUGMENTOR__CONTRAST_EM_MODE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__DROPOUT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['DROPOUT'] = True
            biapy_config['AUGMENTOR']['DROP_RANGE'] = get_text(main_window.ui.AUGMENTOR__DROP_RANGE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__CUTOUT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTOUT'] = True
            biapy_config['AUGMENTOR']['COUT_NB_ITERATIONS'] = get_text(main_window.ui.AUGMENTOR__COUT_NB_ITERATIONS__INPUT)
            biapy_config['AUGMENTOR']['COUT_SIZE'] = get_text(main_window.ui.AUGMENTOR__COUT_SIZE__INPUT)
            biapy_config['AUGMENTOR']['COUT_CVAL'] = float(get_text(main_window.ui.AUGMENTOR__COUT_CVAL__INPUT))
            biapy_config['AUGMENTOR']['COUT_APPLY_TO_MASK'] = True if get_text(main_window.ui.AUGMENTOR__COUT_APPLY_TO_MASK__INPUT) == "Yes" else False 
        if get_text(main_window.ui.AUGMENTOR__CUTBLUR__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTBLUR'] = True
            biapy_config['AUGMENTOR']['CBLUR_SIZE'] = get_text(main_window.ui.AUGMENTOR__CBLUR_SIZE__INPUT)
            biapy_config['AUGMENTOR']['CBLUR_DOWN_RANGE'] = get_text(main_window.ui.AUGMENTOR__CBLUR_DOWN_RANGE__INPUT)
            biapy_config['AUGMENTOR']['CBLUR_INSIDE'] = True if get_text(main_window.ui.AUGMENTOR__CBLUR_INSIDE__INPUT) == "Yes" else False 
        if get_text(main_window.ui.AUGMENTOR__CUTMIX__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTMIX'] = True
            biapy_config['AUGMENTOR']['CMIX_SIZE'] = get_text(main_window.ui.AUGMENTOR__CMIX_SIZE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__CUTNOISE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CUTNOISE'] = True
            biapy_config['AUGMENTOR']['CNOISE_SCALE'] = get_text(main_window.ui.AUGMENTOR__CNOISE_SCALE__INPUT)
            biapy_config['AUGMENTOR']['CNOISE_NB_ITERATIONS'] = get_text(main_window.ui.AUGMENTOR__CNOISE_NB_ITERATIONS__INPUT)
            biapy_config['AUGMENTOR']['CNOISE_SIZE'] = get_text(main_window.ui.AUGMENTOR__CNOISE_SIZE__INPUT)
        if get_text(main_window.ui.AUGMENTOR__MISALIGNMENT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MISALIGNMENT'] = True
            biapy_config['AUGMENTOR']['MS_DISPLACEMENT'] = int(get_text(main_window.ui.AUGMENTOR__MS_DISPLACEMENT__INPUT))
            biapy_config['AUGMENTOR']['MS_ROTATE_RATIO'] = float(get_text(main_window.ui.AUGMENTOR__MS_ROTATE_RATIO__INPUT))
        if get_text(main_window.ui.AUGMENTOR__MISSING_SECTIONS__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['MISSING_SECTIONS'] = True
            biapy_config['AUGMENTOR']['MISSP_ITERATIONS'] = get_text(main_window.ui.AUGMENTOR__MISSP_ITERATIONS__INPUT)
        if get_text(main_window.ui.AUGMENTOR__GRAYSCALE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GRAYSCALE'] = True
        if get_text(main_window.ui.AUGMENTOR__CHANNEL_SHUFFLE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['CHANNEL_SHUFFLE'] = True
        if get_text(main_window.ui.AUGMENTOR__GRIDMASK__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GRIDMASK'] = True
            biapy_config['AUGMENTOR']['GRID_RATIO'] = float(get_text(main_window.ui.AUGMENTOR__GRID_RATIO__INPUT))
            biapy_config['AUGMENTOR']['GRID_D_RANGE'] = get_text(main_window.ui.AUGMENTOR__GRID_D_RANGE__INPUT)
            biapy_config['AUGMENTOR']['GRID_ROTATE'] = float(get_text(main_window.ui.AUGMENTOR__GRID_ROTATE__INPUT))
            biapy_config['AUGMENTOR']['GRID_INVERT'] = True if get_text(main_window.ui.AUGMENTOR__GRID_INVERT__INPUT) == "Yes" else False 
        if get_text(main_window.ui.AUGMENTOR__GAUSSIAN_NOISE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE'] = True
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_MEAN'] = float(get_text(main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_MEAN__INPUT))
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_VAR'] = float(get_text(main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_VAR__INPUT))
            biapy_config['AUGMENTOR']['GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR'] = True if get_text(main_window.ui.AUGMENTOR__GAUSSIAN_NOISE_USE_INPUT_IMG_MEAN_AND_VAR__INPUT) == "Yes" else False 
        if get_text(main_window.ui.AUGMENTOR__POISSON_NOISE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['POISSON_NOISE'] = True
        if get_text(main_window.ui.AUGMENTOR__SALT__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SALT'] = True
            biapy_config['AUGMENTOR']['SALT_AMOUNT'] = float(get_text(main_window.ui.AUGMENTOR__SALT_AMOUNT__INPUT))
        if get_text(main_window.ui.AUGMENTOR__PEPPER__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['PEPPER'] = True
            biapy_config['AUGMENTOR']['PEPPER_AMOUNT'] = float(get_text(main_window.ui.AUGMENTOR__PEPPER_AMOUNT__INPUT))
        if get_text(main_window.ui.AUGMENTOR__SALT_AND_PEPPER__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER'] = True
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER_AMOUNT'] = float(get_text(main_window.ui.AUGMENTOR__SALT_AND_PEPPER_AMOUNT__INPUT))
            biapy_config['AUGMENTOR']['SALT_AND_PEPPER_PROP'] = float(get_text(main_window.ui.AUGMENTOR__SALT_AND_PEPPER_PROP__INPUT))
    else:
        biapy_config['AUGMENTOR']['ENABLE'] = False

    # Model definition
    biapy_config['MODEL'] = {}
    model_name = main_window.cfg.translate_model_names(get_text(main_window.ui.MODEL__ARCHITECTURE__INPUT), get_text(main_window.ui.PROBLEM__NDIM__INPUT))
    biapy_config['MODEL']['ARCHITECTURE'] = model_name
    if model_name in ['unet', 'resunet', 'resunet++', 'seunet', 'attention_unet']:
        biapy_config['MODEL']['FEATURE_MAPS'] = ast.literal_eval(get_text(main_window.ui.MODEL__FEATURE_MAPS__INPUT))
        biapy_config['MODEL']['DROPOUT_VALUES'] = ast.literal_eval(get_text(main_window.ui.MODEL__DROPOUT_VALUES__INPUT)) 
        if get_text(main_window.ui.MODEL__BATCH_NORMALIZATION__INPUT) == "No":
            biapy_config['MODEL']['BATCH_NORMALIZATION'] = False 
        if int(get_text(main_window.ui.MODEL__KERNEL_SIZE__INPUT)) != 3:
            biapy_config['MODEL']['KERNEL_SIZE'] = int(get_text(main_window.ui.MODEL__KERNEL_SIZE__INPUT))
        if get_text(main_window.ui.MODEL__UPSAMPLE_LAYER__INPUT) != "convtranspose":
            biapy_config['MODEL']['UPSAMPLE_LAYER'] = get_text(main_window.ui.MODEL__UPSAMPLE_LAYER__INPUT) 
        if get_text(main_window.ui.MODEL__ACTIVATION__INPUT) != 'elu':
            biapy_config['MODEL']['ACTIVATION'] = get_text(main_window.ui.MODEL__ACTIVATION__INPUT)
        if get_text(main_window.ui.MODEL__LAST_ACTIVATION__INPUT) != 'sigmoid':
            biapy_config['MODEL']['LAST_ACTIVATION'] = get_text(main_window.ui.MODEL__LAST_ACTIVATION__INPUT)
        if int(get_text(main_window.ui.MODEL__N_CLASSES__INPUT)) != 2:
            biapy_config['MODEL']['N_CLASSES'] = int(get_text(main_window.ui.MODEL__N_CLASSES__INPUT))
        biapy_config['MODEL']['Z_DOWN'] = ast.literal_eval(get_text(main_window.ui.MODEL__Z_DOWN__INPUT)) 
        if main_window.cfg.settings['selected_workflow'] == 4 and get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "3D": # SR
            r = "pre" if get_text(main_window.ui.MODEL__UNET_SR_UPSAMPLE_POSITION__INPUT) == "Before model" else "post"
            biapy_config['MODEL']['UNET_SR_UPSAMPLE_POSITION'] = r
    elif model_name in ["unetr", "mae", "ViT"]:
        biapy_config['MODEL']['VIT_TOKEN_SIZE'] = int(get_text(main_window.ui.MODEL__VIT_TOKEN_SIZE__INPUT))
        biapy_config['MODEL']['VIT_EMBED_DIM'] = int(get_text(main_window.ui.MODEL__VIT_EMBED_DIM__INPUT))
        biapy_config['MODEL']['VIT_NUM_LAYERS'] = int(get_text(main_window.ui.MODEL__VIT_NUM_LAYERS__INPUT))
        biapy_config['MODEL']['VIT_MLP_RATIO'] = get_text(main_window.ui.MODEL__VIT_MLP_RATIO__INPUT)
        biapy_config['MODEL']['VIT_NUM_HEADS'] = int(get_text(main_window.ui.MODEL__VIT_NUM_HEADS__INPUT))
        biapy_config['MODEL']['VIT_NORM_EPS'] = get_text(main_window.ui.MODEL__VIT_NORM_EPS__INPUT)

        # UNETR
        if model_name in "unetr":
            biapy_config['MODEL']['UNETR_VIT_HIDD_MULT'] = int(get_text(main_window.ui.MODEL__UNETR_VIT_HIDD_MULT__INPUT)) 
            biapy_config['MODEL']['UNETR_VIT_NUM_FILTERS'] = int(get_text(main_window.ui.MODEL__UNETR_VIT_NUM_FILTERS__INPUT)) 
            biapy_config['MODEL']['UNETR_DEC_ACTIVATION'] = get_text(main_window.ui.MODEL__UNETR_DEC_ACTIVATION__INPUT)
        
        # MAE
        if model_name in "mae":
            biapy_config['MODEL']['MAE_MASK_RATIO_SIZE'] = int(get_text(main_window.ui.MODEL__MAE_MASK_RATIO__INPUT)) 
            biapy_config['MODEL']['MAE_DEC_HIDDEN_SIZE'] = int(get_text(main_window.ui.MODEL__MAE_DEC_HIDDEN_SIZE__INPUT)) 
            biapy_config['MODEL']['MAE_DEC_NUM_LAYERS'] = int(get_text(main_window.ui.MODEL__MAE_DEC_NUM_LAYERS__INPUT)) 
            biapy_config['MODEL']['MAE_DEC_NUM_HEADS'] = get_text(main_window.ui.MODEL__MAE_DEC_NUM_HEADS__INPUT)
            biapy_config['MODEL']['MAE_DEC_MLP_DIMS'] = get_text(main_window.ui.MODEL__MAE_DEC_MLP_DIMS__INPUT)

    if get_text(main_window.ui.MODEL__LOAD_CHECKPOINT__INPUT) == "Yes":
        biapy_config['MODEL']['LOAD_CHECKPOINT'] = True 
        biapy_config['PATHS'] = {}
        if get_text(main_window.ui.PATHS__CHECKPOINT_FILE__INPUT) != "":
            biapy_config['PATHS']['CHECKPOINT_FILE'] = get_text(main_window.ui.PATHS__CHECKPOINT_FILE__INPUT)
        if get_text(main_window.ui.MODEL__SAVE_CKPT_FREQ__INPUT) != -1:
            biapy_config['MODEL']['SAVE_CKPT_FREQ'] = int(get_text(main_window.ui.MODEL__SAVE_CKPT_FREQ__INPUT))
        if get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_EPOCH__INPUT) != "best_on_val":
            biapy_config['MODEL']['LOAD_CHECKPOINT_EPOCH'] = get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_EPOCH__INPUT)
        if get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_ONLY_WEIGHTS__INPUT) != "Yes":
            biapy_config['MODEL']['LOAD_CHECKPOINT_ONLY_WEIGHTS'] = get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_ONLY_WEIGHTS__INPUT)

    # Loss (in detection only)
    if main_window.cfg.settings['selected_workflow'] == 2:
        biapy_config['LOSS'] = {}
        biapy_config['LOSS']['TYPE'] = get_text(main_window.ui.LOSS__TYPE__INPUT)

    # Training phase
    biapy_config['TRAIN'] = {}
    if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['TRAIN']['ENABLE'] = True 
        biapy_config['TRAIN']['OPTIMIZER'] = get_text(main_window.ui.TRAIN__OPTIMIZER__INPUT)
        biapy_config['TRAIN']['LR'] = float(get_text(main_window.ui.TRAIN__LR__INPUT))
        if biapy_config['TRAIN']['OPTIMIZER'] == "ADAMW":
            biapy_config['TRAIN']['W_DECAY'] = float(get_text(main_window.ui.TRAIN__W_DECAY__INPUT))
        biapy_config['TRAIN']['BATCH_SIZE'] = int(get_text(main_window.ui.TRAIN__BATCH_SIZE__INPUT))
        biapy_config['TRAIN']['EPOCHS'] = int(get_text(main_window.ui.TRAIN__EPOCHS__INPUT)) 
        if get_text(main_window.ui.TRAIN__ACCUM_ITER__INPUT) != 1:
            biapy_config['TRAIN']['ACCUM_ITER'] = int(get_text(main_window.ui.TRAIN__ACCUM_ITER__INPUT)) 
        biapy_config['TRAIN']['PATIENCE'] = int(get_text(main_window.ui.TRAIN__PATIENCE__INPUT))

        # LR Scheduler
        if get_text(main_window.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) != "":
            biapy_config['TRAIN']['LR_SCHEDULER'] = {}
            biapy_config['TRAIN']['LR_SCHEDULER']['NAME'] = get_text(main_window.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) 
            if get_text(main_window.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) in ["warmupcosine","reduceonplateau"]: 
                biapy_config['TRAIN']['LR_SCHEDULER']['MIN_LR'] = float(get_text(main_window.ui.TRAIN__LR_SCHEDULER__MIN_LR__INPUT)) 
            if get_text(main_window.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) == "reduceonplateau": 
                biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_FACTOR'] = float(get_text(main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_FACTOR__INPUT)) 
                biapy_config['TRAIN']['LR_SCHEDULER']['REDUCEONPLATEAU_PATIENCE'] = int(get_text(main_window.ui.TRAIN__LR_SCHEDULER__REDUCEONPLATEAU_PATIENCE__INPUT))
            if get_text(main_window.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) == "warmupcosine":  
                biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_EPOCHS'] = int(get_text(main_window.ui.TRAIN__LR_SCHEDULER__WARMUP_COSINE_DECAY_EPOCHS__INPUT))

        # Callbacks
        # if get_text(main_window.ui.TRAIN__PROFILER__INPUT) == "Yes": 
        #     biapy_config['TRAIN']['PROFILER'] = True 
        #     biapy_config['TRAIN']['PROFILER_BATCH_RANGE'] = get_text(main_window.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT)
    else:
        biapy_config['TRAIN']['ENABLE'] = False 

    # Test
    biapy_config['TEST'] = {}
    if get_text(main_window.ui.TEST__ENABLE__INPUT) == "Yes":    
        biapy_config['TEST']['ENABLE'] = True  
        if get_text(main_window.ui.TEST__REDUCE_MEMORY__INPUT) == "Yes":
            biapy_config['TEST']['REDUCE_MEMORY'] = True
        biapy_config['TEST']['VERBOSE'] = True if get_text(main_window.ui.TEST__VERBOSE__INPUT) == "Yes" else False
        if get_text(main_window.ui.TEST__AUGMENTATION__INPUT) == "Yes":
            biapy_config['TEST']['AUGMENTATION'] = True 
        if get_text(main_window.ui.TEST__EVALUATE__INPUT) == "Yes" :
            biapy_config['TEST']['EVALUATE'] = True 
        if get_text(main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT) == "Yes" and get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "2D":
            biapy_config['TEST']['ANALIZE_2D_IMGS_AS_3D_STACK'] = True

        biapy_config['TEST']['STATS'] = {}
        biapy_config['TEST']['STATS']['PER_PATCH'] = True if get_text(main_window.ui.TEST__STATS__PER_PATCH__INPUT) == "Yes" else False 
        biapy_config['TEST']['STATS']['MERGE_PATCHES'] = True if get_text(main_window.ui.TEST__STATS__MERGE_PATCHES__INPUT) == "Yes" else False 
        if get_text(main_window.ui.TEST__STATS__FULL_IMG__INPUT) == "Yes" and get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "2D":
            biapy_config['TEST']['STATS']['FULL_IMG'] = True 

        if get_text(main_window.ui.TEST__BY_CHUNKS__ENABLE__INPUT) == "Yes":
            biapy_config['TEST']['BY_CHUNKS'] = {}
            biapy_config['TEST']['BY_CHUNKS']['ENABLE'] = True
            biapy_config['TEST']['BY_CHUNKS']['FORMAT'] = get_text(main_window.ui.TEST__BY_CHUNKS__FORMAT__INPUT)
            if get_text(main_window.ui.TEST__BY_CHUNKS__SAVE_OUT_TIF__INPUT) == "Yes":
                biapy_config['TEST']['BY_CHUNKS']['SAVE_OUT_TIF'] = True  
            biapy_config['TEST']['BY_CHUNKS']['FLUSH_EACH'] = get_text(main_window.ui.TEST__BY_CHUNKS__FLUSH_EACH__INPUT)
            if get_text(main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__ENABLE__INPUT) == "Yes":
                biapy_config['TEST']['BY_CHUNKS']['WORKFLOW_PROCESS'] = {}
                biapy_config['TEST']['BY_CHUNKS']['WORKFLOW_PROCESS']['ENABLE'] = True
                biapy_config['TEST']['BY_CHUNKS']['WORKFLOW_PROCESS']['TYPE'] = get_text(main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INPUT)

        ### Instance segmentation
        if main_window.cfg.settings['selected_workflow'] == 1:
            biapy_config['TEST']['MATCHING_STATS'] = True if get_text(main_window.ui.TEST__MATCHING_STATS__INPUT) == "Yes" else False 
            biapy_config['TEST']['MATCHING_STATS_THS'] = ast.literal_eval(get_text(main_window.ui.TEST__MATCHING_STATS_THS__INPUT)) 
            if get_text(main_window.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT) != "[0.3]":
                biapy_config['TEST']['MATCHING_STATS_THS_COLORED_IMG'] = ast.literal_eval(get_text(main_window.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT))

        ### Detection
        elif main_window.cfg.settings['selected_workflow'] == 2:
            biapy_config['TEST']['DET_POINT_CREATION_FUNCTION'] = get_text(main_window.ui.TEST__DET_POINT_CREATION_FUNCTION__INPUT)
            biapy_config['TEST']['DET_MIN_TH_TO_BE_PEAK'] = ast.literal_eval(get_text(main_window.ui.TEST__DET_MIN_TH_TO_BE_PEAK__INPUT))
            biapy_config['TEST']['DET_TOLERANCE'] = ast.literal_eval(get_text(main_window.ui.TEST__DET_TOLERANCE__INPUT))
            if get_text(main_window.ui.TEST__DET_POINT_CREATION_FUNCTION__INPUT) == "blob_log":
                biapy_config['TEST']['DET_BLOB_LOG_MIN_SIGMA'] = int(get_text(main_window.ui.TEST__DET_BLOB_LOG_MIN_SIGMA__INPUT))    
                biapy_config['TEST']['DET_BLOB_LOG_MAX_SIGMA'] = int(get_text(main_window.ui.TEST__DET_BLOB_LOG_MAX_SIGMA__INPUT)) 
                biapy_config['TEST']['DET_BLOB_LOG_NUM_SIGMA'] = int(get_text(main_window.ui.TEST__DET_BLOB_LOG_NUM_SIGMA__INPUT)) 

        # Post-processing
        biapy_config['TEST']['POST_PROCESSING'] = {}
        ### Semantic segmentation
        if main_window.cfg.settings['selected_workflow'] == 0:
            if get_text(main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__SEM_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__SEM_SEG__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__SEM_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__SEM_SEG__INPUT))
        ### Instance segmentation
        elif main_window.cfg.settings['selected_workflow'] == 1:
            if get_text(main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__INST_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INST_SEG__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__INST_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__INST_SEG__INPUT))
            if problem_channels in ["BC", "BCM"] and get_text(main_window.ui.TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_ON_MASK'] = True 
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_TH'] = float(get_text(main_window.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES__INST_SEG__INPUT) != "[]":
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_BY_PROPERTIES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES__INST_SEG__INPUT) ) 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_BY_PROPERTIES_VALUES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_VALUES__INST_SEG__INPUT) ) 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_BY_PROPERTIES_SIGN'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_SIGN__INST_SEG__INPUT) ) 
            if problem_channels == "BP":
                if int(get_text(main_window.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT)) != -1:
                    biapy_config['TEST']['POST_PROCESSING']['REPARE_LARGE_BLOBS_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT))
                if get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT))
        ### Detection
        elif main_window.cfg.settings['selected_workflow'] == 2:
            if get_text(main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['YZ_FILTERING_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__YZ_FILTERING_SIZE__DET__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__Z_FILTERING__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING'] = True 
                biapy_config['TEST']['POST_PROCESSING']['Z_FILTERING_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__Z_FILTERING_SIZE__DET__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = float(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED'] = True
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_FIRST_DILATION'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_CLASSES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_PATCH'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT) )
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT)) 
            if get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES__DET__INPUT) != "[]":
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_BY_PROPERTIES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES__DET__INPUT) ) 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_BY_PROPERTIES_VALUES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_VALUES__DET__INPUT) ) 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_BY_PROPERTIES_SIGN'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_SIGN__DET__INPUT) ) 
        if get_text(main_window.ui.TEST__POST_PROCESSING__APPLY_MASK__INPUT) == "Yes":
            biapy_config['TEST']['POST_PROCESSING']['APPLY_MASK'] = True
        if get_text(main_window.ui.TEST__POST_PROCESSING__CLEAR_BORDER__INPUT) == "Yes":
            biapy_config['TEST']['POST_PROCESSING']['CLEAR_BORDER'] = True

        if not biapy_config['TEST']['POST_PROCESSING']:
            del biapy_config['TEST']['POST_PROCESSING']
    else:
        biapy_config['TEST']['ENABLE'] = False

    # Checking the directory
    if main_window.cfg.settings['yaml_config_file_path'] == "":
        main_window.dialog_exec("Configuration file path must be defined", "yaml_config_file_path")
        return True, False
    if not os.path.exists(main_window.cfg.settings['yaml_config_file_path']):
        main_window.dialog_exec("The directory '{}' where the configuration file is going to be saves does not exist."
            .format(main_window.cfg.settings['yaml_config_file_path']), "yaml_config_file_path")
        return True, False

    # Checking YAML file name
    main_window.cfg.settings['yaml_config_filename'] = get_text(main_window.ui.goptions_yaml_name_input)
    if main_window.cfg.settings['yaml_config_filename'] == "":
        main_window.dialog_exec("The configuration filename must be defined", "goptions_yaml_name_input")
        return True, False
    if not main_window.cfg.settings['yaml_config_filename'].endswith(".yaml") and not main_window.cfg.settings['yaml_config_filename'].endswith(".yml"):
        main_window.cfg.settings['yaml_config_filename'] = main_window.cfg.settings['yaml_config_filename']+".yaml"
        set_text(main_window.ui.goptions_yaml_name_input, main_window.cfg.settings['yaml_config_filename'])

    # Writing YAML file
    replace = True
    if os.path.exists(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename'])):
        main_window.yes_no_exec("The file '{}' already exists. Do you want to overwrite it?".format(main_window.cfg.settings['yaml_config_filename']))
        replace = True if main_window.yes_no.answer else False
        
    if replace:
        print("Creating YAML file") 
        with open(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename']), 'w') as outfile:
            yaml.dump(biapy_config, outfile, default_flow_style=False)

    # Reset the check 
    main_window.ui.check_yaml_file_errors_label.setText("")
    main_window.ui.check_yaml_file_errors_frame.setStyleSheet("") 
    
    # Update GUI with the new YAML file path
    main_window.ui.select_yaml_name_label.setText(os.path.normpath(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename'])))
    
    if replace:
        # Advise user where the YAML file has been saved 
        message = "Configuration file created:\n{}".format(os.path.normpath(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename'])))
        main_window.dialog_exec(message, reason="inform_user")
            
    return False, replace

def load_yaml_config(main_window, advise_user=False):
    """
    Load YAML configuration file and check its consistency. This function should be called before running BiaPy's
    container or while checking YAMl file consistency button. 
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    advise_user : bool, optional
        Whether to advice the user with a dialog window with the errors.
    """

    # Check GUI variables 
    if main_window.cfg.settings['yaml_config_filename'] == "":
        main_window.dialog_exec("A configuration file must be selected", "select_yaml_name_label")
        return False
    yaml_file = get_text(main_window.ui.select_yaml_name_label)
    if not os.path.exists(yaml_file):
        main_window.dialog_exec("The configuration file '{}' does not exist!".format(yaml_file), "select_yaml_name_label")
        return False
    if not str(yaml_file).endswith(".yaml") and not str(yaml_file).endswith(".yml"):
        main_window.dialog_exec("The configuration filename '{}' must have .yaml or .yml extension".format(yaml_file), 
            "select_yaml_name_label")
        return False

    ofolder = main_window.cfg.settings['output_folder'] if main_window.cfg.settings['output_folder'] != "" else str(Path.home())
    jobname = get_text(main_window.ui.job_name_input) if get_text(main_window.ui.job_name_input) != "" else "jobname"
    ofolder = os.path.join(ofolder, jobname+"_1")
    main_window.cfg.settings['biapy_cfg'] = Config(ofolder, jobname)
    
    # Merge loaded configuration with the YACS defaults to see if everything is correct or not 
    errors = ""
    try:
        main_window.cfg.settings['biapy_cfg']._C.merge_from_file(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename']))
        main_window.cfg.settings['biapy_cfg'] = main_window.cfg.settings['biapy_cfg'].get_cfg_defaults()
        check_configuration(main_window.cfg.settings['biapy_cfg'])
        
    except Exception as errors:   
        errors = str(errors)
        main_window.ui.check_yaml_file_errors_label.setText(errors)
        main_window.ui.check_yaml_file_errors_frame.setStyleSheet("border: 2px solid red;")    
        if advise_user:
            main_window.dialog_exec("Configuration file checked and some errors were found. "
            "Please correct them before proceeding.", reason="error")
    else:
        main_window.ui.check_yaml_file_errors_label.setText("No errors found in the configuration file")
        main_window.ui.check_yaml_file_errors_frame.setStyleSheet("border: 2px solid green;") 
        if advise_user:
            main_window.dialog_exec("Configuration file checked and no errors found.", reason="inform_user")
            
        return True

def load_yaml_to_GUI(main_window):
    """
    Load YAML configuration file and update the GUI accordingly. It starts a new thead for doing 
    so while the main thread will be running a the spin window.
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    # Load YAML file
    yaml_file = QFileDialog.getOpenFileName()[0]
    if yaml_file == "": return # If no file was selected 
    
    main_window.thread_queue = queue.Queue()
    main_window.thread_spin = QThread()
    main_window.worker_spin = load_yaml_to_GUI_engine(main_window, yaml_file, main_window.thread_queue)
    main_window.worker_spin.moveToThread(main_window.thread_spin)
    main_window.thread_spin.started.connect(main_window.worker_spin.run)
   
    # Set up signals
    main_window.worker_spin.state_signal.connect(main_window.loading_phase)
    main_window.worker_spin.update_var_signal.connect(main_window.update_variable_in_GUI)
    main_window.worker_spin.error_signal.connect(main_window.dialog_exec)
    main_window.worker_spin.report_yaml_load_result.connect(main_window.report_yaml_load)
    main_window.worker_spin.finished_signal.connect(main_window.thread_spin.quit)
    main_window.worker_spin.finished_signal.connect(main_window.worker_spin.deleteLater)
    main_window.thread_spin.finished.connect(main_window.thread_spin.deleteLater)

    # Start thread 
    main_window.thread_spin.start()       

class load_yaml_to_GUI_engine(QObject):
    # Signal to indicate the state of the process 
    state_signal = QtCore.Signal(int)

    # Signal to update variables in GUI
    update_var_signal = QtCore.Signal(str,str)

    # Signal to indicate the main thread that there was an error
    error_signal = QtCore.Signal(str, str)

    # Signal to send a message to the user about the result of loading the YAML file
    report_yaml_load_result = QtCore.Signal(str, str)

    # Signal to indicate the main thread that the worker has finished 
    finished_signal = QtCore.Signal()

    def __init__(self, main_window, yaml_file, thread_queue):
        """
        Class to load the YAML configuration file into the GUI. It is done in a separated thread and sends signals
        to the main thread, as this will be locked in the spin window. 

        Parameters 
        ----------
        main_window : QMainWindow
            Main window of the application. 

        yaml_file : str
            YAML configuration file path to load. 

        thread_queue : Queue
            Queue to pass information between main thread and this process. 
        """
        super(load_yaml_to_GUI_engine, self).__init__()
        self.main_window =  main_window
        self.yaml_file = yaml_file
        self.thread_queue = thread_queue
        self.white_list = [
            "DATA__VAL__CROSS_VAL__INPUT", "DATA__TEST__BINARY_MASKS__INPUT",
            "DATA__TEST__DETECTION_MASK_DIR__INPUT", "DATA__TEST__INSTANCE_CHANNELS_DIR__INPUT",
            "DATA__TEST__INSTANCE_CHANNELS_MASK_DIR__INPUT", "DATA__TEST__SSL_SOURCE_DIR__INPUT",
            "DATA__TRAIN__DETECTION_MASK_DIR__INPUT", "DATA__TRAIN__INSTANCE_CHANNELS_DIR__INPUT",
            "DATA__TRAIN__INSTANCE_CHANNELS_MASK_DIR__INPUT", "DATA__TRAIN__SSL_SOURCE_DIR__INPUT",
            "DATA__VAL__BINARY_MASKS__INPUT", "DATA__VAL__DETECTION_MASK_DIR__INPUT",
            "DATA__VAL__INSTANCE_CHANNELS_DIR__INPUT", "DATA__VAL__INSTANCE_CHANNELS_MASK_DIR__INPUT",
            "DATA__VAL__SSL_SOURCE_DIR__INPUT", "LOG__CHART_CREATION_FREQ__INPUT", "LOG__LOG_DIR__INPUT",
            "LOG__LOG_FILE_PREFIX__INPUT", "LOG__TENSORBOARD_LOG_DIR__INPUT", "SYSTEM__NUM_GPUS__INPUT",

            # Not used or decided to not insert in GUI
            "SYSTEM__PIN_MEM__INPUT", "TRAIN__CHECKPOINT_MONITOR__INPUT","DATA__VAL__DIST_EVAL__INPUT",
            "MODEL__VIT_MODEL__INPUT"
        ]
        
    def run(self):
        """
        Process of loading YAML file into GUI.
        """
        self.state_signal.emit(0)

        with open(self.yaml_file, "r") as stream:
            try:
                loaded_cfg = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                self.error_signal.emit(f"Following error found when loading configuration file: \n{exc}", "error")
                self.state_signal.emit(1)
                self.finished_signal.emit()
                return 
        if loaded_cfg is None:
            self.error_signal.emit(f"The input config file seems to be empty", "error")
            self.state_signal.emit(1)
            self.finished_signal.emit()
            return  
        print(f"Loaded: {loaded_cfg}")

        # Load configuration file and check possible errors
        tmp_cfg = Config("/home/","jobname")
        errors = ""
        try:
            tmp_cfg._C.merge_from_file(self.yaml_file)
            tmp_cfg = tmp_cfg.get_cfg_defaults()
            check_configuration(tmp_cfg, check_data_paths=False)
        except Exception as errors:  
            errors = str(errors) 
            print(errors) 
            self.error_signal.emit(errors, "load_yaml_error")
        else:
            
            # Find the workflow
            self.workflow_str = ""
            try:
                self.work_dim = loaded_cfg['PROBLEM']['NDIM']
            except:
                self.work_dim = "2D"
            try:
                work_id = loaded_cfg['PROBLEM']['TYPE']
            except: 
                work_id = "SEMANTIC_SEG"
                self.workflow_str = "SEM_SEG"
            if work_id == "SEMANTIC_SEG":
                self.main_window.cfg.settings['selected_workflow'] = 0
                self.workflow_str = "SEM_SEG"
            elif work_id == "INSTANCE_SEG":
                self.main_window.cfg.settings['selected_workflow'] = 1
                self.workflow_str = "INST_SEG"
            elif work_id == "DETECTION":
                self.main_window.cfg.settings['selected_workflow'] = 2
                self.workflow_str = "DET"
            elif work_id == "DENOISING":
                self.main_window.cfg.settings['selected_workflow'] = 3
            elif work_id == "SUPER_RESOLUTION":
                self.main_window.cfg.settings['selected_workflow'] = 4
            elif work_id == "SELF_SUPERVISED":
                self.main_window.cfg.settings['selected_workflow'] = 5
            else: # CLASSIFICATION
                self.main_window.cfg.settings['selected_workflow'] = 6
            move_between_workflows(self.main_window, self.main_window.cfg.settings['selected_workflow'], self.work_dim)

            # Go over configuration file
            errors, variables_set = self.analyze_dict(conf=loaded_cfg, sep="")
            print("Variables updated: ")
            for i, k in enumerate(variables_set.keys()):
                print("{}. {}: {}".format(i+1, k, variables_set[k]))
            if len(errors) > 0:
                print("Errors: ")
                for i in range(len(errors)):
                    print("{}. : {}".format(i+1, errors[i]))

            # Message for the user
            self.report_yaml_load_result.emit(errors, self.yaml_file)
            
        self.state_signal.emit(1)
        self.finished_signal.emit()

    def analyze_dict(self, conf, sep=""):
        """
        Analizes loaded YAML configuration recursively and sets GUI variables with the same name as found 
        variables.

        Parameters
        ----------
        conf : dict
            YAML configuration read.

        sep : str, optional
            Variable separator. It is going to be filled on each call, constructing the variable name to be set 
            in the GUI. 
        
        Returns
        -------
        errors : List of str
            List of errors loading the YAML file. 

        variables_set : dict
            Variables of the GUI to be set with their respective values.
        """
        errors = []
        variables_set = {}
        for k, v in conf.items():
            if isinstance(v, dict):
                err, _vars = self.analyze_dict(v,sep+k if sep == "" else sep+"__"+k)
                if err is not None: 
                    errors +=err
                    variables_set.update(_vars)
            else:
                widget_name = sep+"__"+k+"__INPUT"
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
                    v = self.main_window.cfg.translate_model_names(v, self.work_dim, inv=True)
                elif widget_name == "MODEL__UNET_SR_UPSAMPLE_POSITION__INPUT":
                    v = "Before model" if v == "pre" else "After model"
                elif widget_name == "DATA__TRAIN__MINIMUM_FOREGROUND_PER__INPUT":
                    widget_name = "DATA__TRAIN__MINIMUM_FOREGROUND_PER__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__YZ_FILTERING__INPUT":
                    widget_name = "TEST__POST_PROCESSING__YZ_FILTERING__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__YZ_FILTERING_SIZE__INPUT":
                    widget_name = "TEST__POST_PROCESSING__YZ_FILTERING_SIZE__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__Z_FILTERING__INPUT":
                    widget_name = "TEST__POST_PROCESSING__Z_FILTERING__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__Z_FILTERING_SIZE__INPUT":
                    widget_name = "TEST__POST_PROCESSING__Z_FILTERING_SIZE__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_VALUES__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_VALUES__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_SIGN__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_BY_PROPERTIES_SIGN__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__{}__INPUT".format(self.workflow_str)
                elif widget_name in ["MODEL__ACTIVATION__INPUT", "MODEL__UNETR_DEC_ACTIVATION__INPUT"]:
                    v = v.lower()

                # Set variable values
                if set_var: 
                    all_widgets_to_set = [widget_name]
                    all_widgets_to_set_values = [v]

                    all_widgets_to_set += other_widgets_to_set
                    all_widgets_to_set_values += other_widgets_values_to_set

                    for x, y in zip(all_widgets_to_set, all_widgets_to_set_values):
                        err = None
                        if hasattr(self.main_window.ui, x):
                            self.update_var_signal.emit(x, str(y))
                            err = self.thread_queue.get()
                        else:
                            if x not in self.white_list and not x.startswith("PATHS__"):
                                err = "{} widget does not exist".format(x)

                        if err is not None:
                            errors.append(err)
                        else:
                            variables_set[widget_name] = y
                            print("Setting {} : {} ({})".format(widget_name, y, k))
                        
        return errors, variables_set

def path_in_list(list, path):
    """
    Check whether the given path is in the list. It also checks if the path is relative 
    to another one present in the list. E.g. ``list=[/home/user/Downloads]`` and 
    ``path=/home/user/Downloads/examples`` will return ``True``. 

    Parameters
    ----------
    list : List of str
        List of paths to loop over finding ``path``.
    
    path : str
        Path to check if is inside ``list``.
    
    Returns
    -------
    bool : bool
        ``True``if ``path`` is contained in ``list`` or is relative to any of the paths there.
    """
    if path in list:
        return True
    else:
        for i in list:
            if PurePath(path).is_relative_to(PurePath(i)):
                return True
    return False

def path_to_linux(p, orig_os="win"):
    """
    Converts given path to Linux. 

    Parameters
    ----------
    p : str
        Path to convert.

    orig_os : str
        Origin of the path given. If it is 'win' the path will be converted to Linux. 

    Returns
    -------
    p : str
        Converted path to Linux.
    """
    if "win" in orig_os.lower():
        p = PureWindowsPath(p)
        p = os.path.join("/"+p.parts[0][0],*p.parts[1:]).replace('\\','/')
    return p 