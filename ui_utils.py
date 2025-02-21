import os 
import errno
import sys
import traceback
import docker
import ast 
import GPUtil
import yaml
import queue
import subprocess
import re
import pooch
import json 
import numpy as np
import certifi
import ssl
from pathlib import PurePath, Path, PureWindowsPath
from packaging.version import Version
from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections.abc

from PySide6 import QtCore
from PySide6.QtCore import QObject, QThread
from PySide6.QtWidgets import *
from PySide6.QtGui import QBrush, QColor

from biapy.biapy_config import Config
from biapy.biapy_check_configuration import check_configuration, check_torchvision_available_models, convert_old_model_cfg_to_current_version
from biapy.biapy_aux_functions import check_bmz_model_compatibility, check_images, check_csv_files, check_classification_images, check_model_restrictions


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

    if out == "": return out # If no file was selected 

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

    return out 

def wizard_path_changed(main_window, save_in_obj_tag=None, is_file=True):
    # Reset path check
    if examine(main_window, save_in_obj_tag, is_file) != "":
        # Reset again colors and checks so the user must check again the folder
        key = next(iter(main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(main_window.cfg.settings['wizard_question_index']+1)]))
        if f"CHECKED {key}" in main_window.cfg.settings["wizard_answers"]:
            main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] = -1
            set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>")
            index = main_window.cfg.settings['wizard_from_question_index_to_toc'][main_window.cfg.settings['wizard_question_index']]        
            main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(0,0,0))

def check_data_from_path(main_window):
    """
    Check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
    and Torchvision.
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    if main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] == -1:
        main_window.dialog_exec("Please select first a folder to check", reason="error")
    else:
        main_window.yes_no_exec("This process may take a while as all images will be checked one by one. Are you sure you want to proceed?")
        if main_window.yes_no.answer:

            def set_folder_checked(data_constraints, key, sample_info):
                main_window.logger.info(f"Data {key} checked!")
                if "data_constraints" not in main_window.cfg.settings["wizard_answers"]:
                    main_window.cfg.settings["wizard_answers"]["data_constraints"] = data_constraints
                else:
                    main_window.cfg.settings["wizard_answers"]["data_constraints"] = update_dict(
                        main_window.cfg.settings["wizard_answers"]["data_constraints"],
                        data_constraints
                    )
                main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] = 1
                set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#04aa6d'>Data checked!</span>")

                if "sample_info" not in main_window.cfg.settings["wizard_answers"]:
                    main_window.cfg.settings["wizard_answers"]["sample_info"] = {}
                main_window.cfg.settings["wizard_answers"]["sample_info"][sample_info['dir_name']] = sample_info

            main_window.logger.info("Checking data from path")
            dir_name = next(iter(main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(main_window.cfg.settings['wizard_question_index']+1)]))
            main_window.thread_spin = QThread()
            main_window.worker_spin = check_data_from_path_engine(main_window, dir_name)
            main_window.worker_spin.moveToThread(main_window.thread_spin)
            main_window.thread_spin.started.connect(main_window.worker_spin.run)
        
            # Set up signals
            main_window.worker_spin.state_signal.connect(main_window.loading_phase)
            main_window.worker_spin.update_var_signal.connect(main_window.update_variable_in_GUI)
            main_window.worker_spin.error_signal.connect(main_window.dialog_exec)
            main_window.worker_spin.add_model_card_signal.connect(main_window.add_model_card)
            main_window.worker_spin.report_path_check_result.connect(set_folder_checked)
            main_window.worker_spin.finished_signal.connect(main_window.thread_spin.quit)
            main_window.worker_spin.finished_signal.connect(main_window.worker_spin.deleteLater)
            main_window.thread_spin.finished.connect(main_window.thread_spin.deleteLater)

            # Start thread 
            main_window.thread_spin.start()       
            
class check_data_from_path_engine(QObject):
    # Signal to indicate the state of the process 
    state_signal = QtCore.Signal(int)

    # Signal to update variables in GUI
    update_var_signal = QtCore.Signal(str,str)

    # Signal to indicate the main thread that there was an error
    error_signal = QtCore.Signal(str, str)

    # Signal to send a message to the user about the result of model checking
    add_model_card_signal = QtCore.Signal(int, dict)

    # Signal to send a message to the user about the result of model checking
    report_path_check_result = QtCore.Signal(dict, str, dict)

    # Signal to indicate the main thread that the worker has finished 
    finished_signal = QtCore.Signal()

    def __init__(self, main_window, dir_name):
        """
        Class to check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
        and Torchvision.

        Parameters 
        ----------
        main_window : QMainWindow
            Main window of the application. 
        """
        super(check_data_from_path_engine, self).__init__()
        self.main_window =  main_window
        self.dir_name = dir_name

    def run(self):
        """
        Checks possible model available in BioImage Model Zoo and Torchivision for the workflow specified by Wizards form. 
        
        Parameters
        ----------
        main_window : QMainWindow
            Main window of the application.
        """
        try:
            self.state_signal.emit(0)

            self.main_window.cfg.settings["wizard_question_answered_index"]
            self.main_window.cfg.settings['wizard_question_index']
            folder = self.main_window.cfg.settings["wizard_question_answered_index"][self.main_window.cfg.settings['wizard_question_index']]
            if self.main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"] == -1:
                self.error_signal.emit(f"You need to answer 'Workflow' question before checking the data.", "inform_user")
            elif self.main_window.cfg.settings["wizard_answers"]["PROBLEM.NDIM"] == -1:
                self.error_signal.emit("You need to answer 'Dimensions' question before checking the data.", "inform_user")
            else:
                workflow = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"]
                ndim = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.NDIM"]
                key = next(iter(self.main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(self.main_window.cfg.settings['wizard_question_index']+1)]))
                is_3d = (ndim=="3D")
                if workflow == "SEMANTIC_SEG":
                    mask_type = "semantic_mask" if ("GT_PATH" in key) else ""
                    error, error_message, data_constraints, sample_info = check_images(
                        folder, is_mask=("GT_PATH" in key), mask_type=mask_type, 
                        is_3d=is_3d, dir_name=self.dir_name)
                elif workflow == "INSTANCE_SEG": 
                    mask_type = "instance_mask" if ("GT_PATH" in key) else ""
                    error, error_message, data_constraints, sample_info = check_images(folder, is_mask=("GT_PATH" in key), 
                        mask_type=mask_type, is_3d=is_3d, dir_name=self.dir_name)
                elif workflow == "DETECTION":
                    if "GT_PATH" not in key: 
                        error, error_message, data_constraints, sample_info = check_images(folder, is_3d=is_3d, dir_name=self.dir_name)
                    else:
                        error, error_message, data_constraints, sample_info = check_csv_files(folder, is_3d=is_3d, dir_name=self.dir_name) 
                elif workflow == "CLASSIFICATION": 
                    error, error_message, data_constraints, sample_info = check_classification_images(folder, is_3d=is_3d, dir_name=self.dir_name)
                elif workflow in ["DENOISING", "SUPER_RESOLUTION", "SELF_SUPERVISED", "IMAGE_TO_IMAGE"]:   
                    error, error_message, data_constraints, sample_info = check_images(folder, is_3d=is_3d, dir_name=self.dir_name)
                
                self.main_window.logger.info(f"data_constraints: {data_constraints}")
                if error:
                    self.main_window.logger.info(f"Error: {error}")
                    self.main_window.logger.info(f"Message: {error_message}")
                    self.error_signal.emit(f"Following error found when checking the folder: \n{error_message}", "error")
                else:
                    self.report_path_check_result.emit(data_constraints, key, sample_info)
        except:
            exc = traceback.format_exc()
            self.main_window.logger.error(exc)
            self.error_signal.emit(f"Error checking the data:\n{exc}", "unexpected_error")
            self.state_signal.emit(1)
            self.finished_signal.emit() 
        
        self.state_signal.emit(1)
        self.finished_signal.emit()

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

        out = get_text(getattr(main_window.ui, gui_widget_name), strip=False)
        if gui_widget_name == "goptions_browse_yaml_path_input":
            main_window.cfg.settings['yaml_config_file_path'] = out
        elif gui_widget_name == "select_yaml_name_label":
            out_write = os.path.basename(out)
            main_window.cfg.settings['yaml_config_filename'] = out_write
            main_window.cfg.settings['yaml_config_file_path'] = os.path.dirname(out)

            if get_text(main_window.ui.job_name_input) == "":
                main_window.ui.job_name_input.setPlainText(os.path.splitext(out_write)[0])

            # Reset the check
            main_window.ui.check_yaml_file_errors_label.setText("")
            main_window.ui.check_yaml_file_errors_frame.setStyleSheet("") 
        elif gui_widget_name == "output_folder_input":
            main_window.cfg.settings['output_folder'] = out 

        if gui_widget_name in ["job_name_input", "output_folder_input"]:
            path = get_text(main_window.ui.output_folder_input)
            if path != "":
                main_window.cfg.settings['job_real_output_path'] = os.path.join(path, get_text(main_window.ui.job_name_input))
                m = "Job results folder: <strong>{}</strong>".format(main_window.cfg.settings['job_real_output_path'])
                main_window.ui.output_final_directory_label.setText(m)

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

    elif buttonName=='bn_wizard' or (buttonName=='down' and to_page == 1):
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_wizard)
        main_window.ui.frame_wizard.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 1

    elif buttonName=='bn_workflow' or ('bn_' not in buttonName and to_page == 2):
        main_window.ui.continue_bn.setText("Continue")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.workflow_selection_page)
        main_window.ui.frame_workflow.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 2
        adjust_window_progress(main_window)

    elif buttonName=='bn_goptions' or ('bn_' not in buttonName and to_page == 3):
        main_window.ui.continue_bn.setText("Continue")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.goptions_page)
        main_window.ui.frame_goptions.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 3
        adjust_window_progress(main_window)

    elif buttonName=='bn_train' or ('bn_' not in buttonName and to_page == 4):
        main_window.ui.continue_bn.setText("Continue")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.train_page)
        main_window.ui.frame_train.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 4
        adjust_window_progress(main_window)

    elif buttonName=='bn_test' or ('bn_' not in buttonName and to_page == 5):
        main_window.ui.continue_bn.setText("Create configuration file")
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_create_yaml)
        main_window.ui.stackedWidget_create_yaml_frame.setCurrentWidget(main_window.ui.test_page)
        main_window.ui.frame_test.setStyleSheet("background:rgb(255,255,255)") 
        main_window.cfg.settings['page_number'] = 5
        adjust_window_progress(main_window)

    elif buttonName=='bn_run_biapy' or ('bn_' not in buttonName and to_page == 6):            
        error = False
        created = True
        if ('bn_' not in buttonName and to_page == 6):
            error, created = create_yaml_file(main_window)
        # If there is an error do not make the movement, as the error dialog will redirect the user to the 
        # field that raises the error 
        if not error and created: 
            main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_run_biapy)
            main_window.ui.frame_run_biapy.setStyleSheet("background:rgb(255,255,255)") 
            main_window.cfg.settings['page_number'] = 6
        if not created:
            main_window.cfg.settings['page_number'] -= 1    
    move_between_workflows(main_window, to_page)   

def eval_wizard_answer(main_window):
    """
    Stores the answer given for the current question and mark it to advice the user.
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    if main_window.allow_change_wizard_question_answer:
        mark_as_answered = False
        
        # Remember current answer
        if main_window.ui.wizard_question_answer_frame.isVisible():
            changed_answer = False
            if main_window.ui.wizard_question_answer.currentIndex() != -1:
                mark_as_answered = True    
                if main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] != main_window.ui.wizard_question_answer.currentIndex():
                    main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] = main_window.ui.wizard_question_answer.currentIndex()
                    changed_answer = True 

                for key, values in main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(main_window.cfg.settings['wizard_question_index']+1)].items():
                    main_window.cfg.settings["wizard_answers"][key] = values[main_window.ui.wizard_question_answer.currentIndex()]
        elif main_window.ui.wizard_path_input_frame.isVisible():
            te = get_text(main_window.ui.wizard_path_input)
            if te != "":
                key = next(iter(main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(main_window.cfg.settings['wizard_question_index']+1)]))
                main_window.cfg.settings["wizard_answers"][key] = te
                main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] = te    
                set_text(main_window.ui.wizard_path_input, te)

                # Check if the data was checked 
                if main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] == -1:
                    mark_as_answered = False
                else:
                    mark_as_answered = True

        if mark_as_answered:    
            # Mark section as answered in TOC
            index = main_window.cfg.settings['wizard_from_question_index_to_toc'][main_window.cfg.settings['wizard_question_index']]        
            main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(64,144,253))

        # Check the questions that need to hide/appear
        for question in main_window.cfg.settings["wizard_question_condition"]:
            make_visible = True
            set_default_value = True 
            
            # AND conditions
            if len(main_window.cfg.settings["wizard_question_condition"][question]["and_cond"]) > 0:
                for cond in main_window.cfg.settings["wizard_question_condition"][question]["and_cond"]:
                    if main_window.cfg.settings["wizard_answers"][cond[0]] != -1:
                        set_default_value = False
                        if main_window.cfg.settings["wizard_answers"][cond[0]] != cond[1]:
                            make_visible = False
                            break
                    else:
                        make_visible = False
                        break

            if make_visible:
                # OR conditions
                if len(main_window.cfg.settings["wizard_question_condition"][question]["or_cond"]) > 0:
                    for cond in main_window.cfg.settings["wizard_question_condition"][question]["or_cond"]:
                        if main_window.cfg.settings["wizard_answers"][cond[0]] != -1:
                            set_default_value = False
                            if main_window.cfg.settings["wizard_answers"][cond[0]] not in cond[1]:
                                make_visible = False
                                break
                        else:
                            make_visible = False
                            break

            if not set_default_value:
                question_number = int(question.replace("Q",""))-1
                if make_visible:
                    if not main_window.cfg.settings["wizard_question_visible"][question_number]:
                        main_window.cfg.settings['wizard_question_visible'][question_number] = True
                        index_in_toc = main_window.cfg.settings['wizard_from_question_index_to_toc'][question_number]
                        main_window.ui.wizard_treeView.setRowHidden(index_in_toc[1], main_window.wizard_toc_model.index(index_in_toc[0],0), False)
                else:
                    if main_window.cfg.settings["wizard_question_visible"][question_number]:
                        main_window.cfg.settings['wizard_question_visible'][question_number] = False
                        index_in_toc = main_window.cfg.settings['wizard_from_question_index_to_toc'][question_number]
                        main_window.ui.wizard_treeView.setRowHidden(index_in_toc[1], main_window.wizard_toc_model.index(index_in_toc[0],0), True)

        # Reset data checks if dimensionality or workflow changed, as the data check is different 
        if main_window.ui.wizard_question_answer_frame.isVisible() and changed_answer:
            main_window.pretrained_model_need_to_check = None
            key = next(iter(main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(main_window.cfg.settings['wizard_question_index']+1)]))
            if "PROBLEM.NDIM" == key or "PROBLEM.TYPE" == key:
                for key, val in main_window.cfg.settings["wizard_answers"].items():
                    if "CHECKED" in key: 
                        main_window.cfg.settings["wizard_answers"][key] = -1

                for i in range(main_window.cfg.settings["wizard_number_of_questions"]):
                    if main_window.cfg.settings['wizard_possible_answers'][i][0] == "PATH":
                        index = main_window.cfg.settings['wizard_from_question_index_to_toc'][i]        
                        main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(0,0,0))
                    elif main_window.cfg.settings['wizard_possible_answers'][i][0] in ["MODEL_BIAPY", "MODEL_OTHERS"]:
                        index = main_window.cfg.settings['wizard_from_question_index_to_toc'][i]        
                        main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(0,0,0))
                        main_window.cfg.settings["wizard_question_answered_index"][i] = -1

def change_wizard_page(main_window, val, based_on_toc=False, added_val=0):
    """
    Changes wizard page.

    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    val : int
        Number of question to move to. If ``based_on_toc`` is provided it needs to be calculated internally.

    based_on_toc : bool, optional
        If the call was triggered from QTreeView that represents the TOC. It advices the function that needs to 
        recalculated ``val`` value according to the selected index in TOC.
    
    added_val : bool, optional
        The value to be added to ``val`` in order to calculate where to continue: next or previous question.
    """
    if based_on_toc:
        if main_window.not_allow_change_question:
            return
        index = main_window.ui.wizard_treeView.selectionModel().selectedIndexes()
        if len(index) == 0:
            return 
        if len(index) > 1:
            raise ValueError(f"Found internal error in indexes: {index}. Contact BiaPy team!")
        index = index[0]
        if index.parent().row() != -1: 
            val = main_window.cfg.settings['wizard_from_toc_to_question_index'][index.parent().row()][index.row()]

    eval_wizard_answer(main_window)

    # Calculate valid next/previous question
    if not based_on_toc:
        if added_val > 0:
            val += 1
            for i in range(val,len(main_window.cfg.settings['wizard_question_visible'])):
                if main_window.cfg.settings['wizard_question_visible'][i]:
                    val = i
                    break 
        if added_val < 0:
            val -= 1
            for i in range(val,0,-1):
                if main_window.cfg.settings['wizard_question_visible'][i]:
                    val = i
                    break 
    
    # Go to the first view of the wizard
    last_shown = len(main_window.cfg.settings['wizard_question_visible']) - main_window.cfg.settings['wizard_question_visible'][::-1].index(True) -1
    if val == -1 and main_window.cfg.settings['wizard_question_index'] == 0:
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.wizard_start_page)
    elif val == last_shown+1:
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.summary_page)

        # Only visualice those questions that were answered and visible
        for i in range(len(main_window.cfg.settings["wizard_questions"])):
            if main_window.cfg.settings['wizard_question_visible'][i] and \
               main_window.cfg.settings["wizard_question_answered_index"][i] != -1:
                main_window.question_cards[i][f"summary_question_frame_{i}"].setVisible(True)
                set_text(main_window.question_cards[i][f"summary_question_text{i}"], main_window.cfg.settings['wizard_questions'][i])
                if isinstance(main_window.cfg.settings["wizard_question_answered_index"][i], str):
                    set_text(main_window.question_cards[i][f"summary_question_text_answer_{i}"], 
                        main_window.cfg.settings["wizard_question_answered_index"][i])
                else:
                    set_text(main_window.question_cards[i][f"summary_question_text_answer_{i}"], 
                        str(main_window.cfg.settings['wizard_possible_answers'][i][main_window.cfg.settings["wizard_question_answered_index"][i]]))
            else:
                main_window.question_cards[i][f"summary_question_frame_{i}"].setVisible(False)
        
        # Visualice the yaml_file name 
        set_text(main_window.ui.wizard_config_file_label, os.path.join(get_text(main_window.ui.wizard_browse_yaml_path_input), get_text(main_window.ui.wizard_yaml_name_input)))
    else:
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.questionary_page)

        main_window.cfg.settings['wizard_question_index'] = val
        main_window.cfg.settings['wizard_question_index'] = max(0,main_window.cfg.settings['wizard_question_index'])
        main_window.cfg.settings['wizard_question_index'] = min(
            len(main_window.cfg.settings['wizard_from_question_index_to_toc'])-1, 
            main_window.cfg.settings['wizard_question_index']
        )

        prepare_question(main_window)

    # Change TOC index
    if not based_on_toc:
        index_in_toc = main_window.cfg.settings['wizard_from_question_index_to_toc'][main_window.cfg.settings['wizard_question_index']]
        index = main_window.wizard_toc_model.item(index_in_toc[0]).child(index_in_toc[1])
        if index is not None:
            # As wizard_treeView is triggered when changing it's index we use this flag to block change_wizard_page functionality, 
            # as it has been done already
            main_window.not_allow_change_question = True
            
            main_window.ui.wizard_treeView.setCurrentIndex(index.index())

            # Activate again possible triggers of wizard_treeView
            main_window.not_allow_change_question = False

def prepare_question(main_window):
    """
    Prepare current question.
    """
    # Change question
    set_text(
        main_window.ui.wizard_question, 
        main_window.cfg.settings['wizard_questions'][
            main_window.cfg.settings['wizard_question_index']
            ]
        )
    set_text(
        main_window.ui.wizard_question_label, 
        "Question {}".format(main_window.cfg.settings['wizard_question_index']+1)
        )
    
    # Set bottom part of the question. Depeding on the question type different things must be done
    if main_window.cfg.settings['wizard_possible_answers'][main_window.cfg.settings['wizard_question_index']][0] == "PATH":
        main_window.ui.wizard_path_input_frame.setVisible(True)
        main_window.ui.wizard_question_answer_frame.setVisible(False)
        main_window.ui.wizard_model_input_frame.setVisible(False)

        # Remember the answer if the question was previously answered
        if main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] != -1:
            set_text(main_window.ui.wizard_path_input, main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']])
            key = next(iter(main_window.cfg.settings["wizard_variable_to_map"]["Q"+str(main_window.cfg.settings['wizard_question_index']+1)]))
            if main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] == -1:
                set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>")
            else:
                set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#04aa6d'>Data checked!</span>")
        else:
            set_text(main_window.ui.wizard_path_input, "")
            set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>")

    elif main_window.cfg.settings['wizard_possible_answers'][main_window.cfg.settings['wizard_question_index']][0] in ["MODEL_BIAPY", "MODEL_OTHERS"]:
        main_window.ui.wizard_path_input_frame.setVisible(False)
        main_window.ui.wizard_question_answer_frame.setVisible(False)
        main_window.ui.wizard_model_input_frame.setVisible(True)

        if main_window.cfg.settings['wizard_possible_answers'][main_window.cfg.settings['wizard_question_index']][0] == "MODEL_BIAPY":
            main_window.ui.wizard_model_check_bn.setVisible(False)
            main_window.ui.wizard_model_browse_bn.setVisible(True)
        else: # "MODEL_OTHERS"
            main_window.ui.wizard_model_check_bn.setVisible(True)
            main_window.ui.wizard_model_browse_bn.setVisible(False)
            
        # Remember the answer if the question was previously answered
        if main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] != -1:
            set_text(main_window.ui.wizard_model_input, main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']])
        else:
            set_text(main_window.ui.wizard_model_input, "")
    else:
        main_window.ui.wizard_path_input_frame.setVisible(False)
        main_window.ui.wizard_question_answer_frame.setVisible(True)
        main_window.ui.wizard_model_input_frame.setVisible(False)

        # Prevent eval_wizard_answer functionality during wizard_question_answer's currentIndexChanged trigger. It triggers a few times 
        # when clearing and inserting new data 
        main_window.allow_change_wizard_question_answer = False

        # Prepare combobox with the answers of the new question
        main_window.ui.wizard_question_answer.clear()
        for ans in main_window.cfg.settings['wizard_possible_answers'][
                main_window.cfg.settings['wizard_question_index']
                ]:
            main_window.ui.wizard_question_answer.addItem(ans)
        
        # Remember the answer if the question was previously answered
        if main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']] != -1:
            main_window.ui.wizard_question_answer.setCurrentIndex(main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings['wizard_question_index']])
        else:
            main_window.ui.wizard_question_answer.setCurrentIndex(-1)

        # Enable eval_wizard_answer calls again
        main_window.allow_change_wizard_question_answer = True
    

def clear_answers(main_window, ask_user=True):
    """
    Clear all answers. 

    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.

    ask_user : bool, optional  
        Whether to ask the user before proceed. 
    """
    continue_clearing = True
    if ask_user:
        main_window.yes_no_exec("Are you sure you want to clear all answers?")
        if not main_window.yes_no.answer:
            continue_clearing = False 

    if continue_clearing:
        main_window.cfg.settings["wizard_question_answered_index"] = [-1,]*main_window.cfg.settings["wizard_number_of_questions"] 

        # Reset TOC colors
        for i in range(main_window.wizard_toc_model.rowCount()):
            main_window.wizard_toc_model.item(i).setForeground(QColor(0,0,0))
            for j in range(main_window.wizard_toc_model.item(i).rowCount()):
                main_window.wizard_toc_model.item(i).child(j).setForeground(QColor(0,0,0))
        
        # Rewrite all keys
        main_window.cfg.settings["wizard_answers"] = main_window.cfg.settings["original_wizard_answers"].copy()

        main_window.cfg.settings['wizard_question_index'] = 0

def have_internet(main_window, timeout=3):
    try:
        urlopen('https://biapyx.github.io', timeout=timeout, context=ssl.create_default_context(cafile=certifi.where()))
        return True
    except Exception:
        exc = traceback.format_exc()
        main_window.logger.error(exc)
        return False
    
def check_models_from_other_sources(main_window, from_wizard=True):
    """
    Check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
    and Torchvision.
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.

    from_wizard : bool, optional  
        Whether this function was called through the Wizard or not. 
    """
    if main_window.pretrained_model_need_to_check is not None:
        main_window.external_model_list_built(main_window.pretrained_model_need_to_check)
        return
    
    if not from_wizard:
        main_window.yes_no_exec("This process needs internet connection and may take a while. Do you want to proceed?")
        if not main_window.yes_no.answer:
            return

    if not have_internet(main_window):
        main_window.dialog_exec("There is no internet connection. Check aborted!", reason="error")
        return 

    main_window.thread_spin = QThread()
    main_window.worker_spin = check_models_from_other_sources_engine(main_window, from_wizard)
    main_window.worker_spin.moveToThread(main_window.thread_spin)
    main_window.thread_spin.started.connect(main_window.worker_spin.run)
   
    # Set up signals
    main_window.worker_spin.state_signal.connect(main_window.loading_phase)
    main_window.worker_spin.update_var_signal.connect(main_window.update_variable_in_GUI)
    main_window.worker_spin.error_signal.connect(main_window.dialog_exec)
    main_window.worker_spin.add_model_card_signal.connect(main_window.add_model_card)
    main_window.worker_spin.report_yaml_model_check_result.connect(main_window.external_model_list_built)
    main_window.worker_spin.finished_signal.connect(main_window.thread_spin.quit)
    main_window.worker_spin.finished_signal.connect(main_window.worker_spin.deleteLater)
    main_window.thread_spin.finished.connect(main_window.thread_spin.deleteLater)

    # Start thread 
    main_window.thread_spin.start()       
    
        
class check_models_from_other_sources_engine(QObject):
    # Signal to indicate the state of the process 
    state_signal = QtCore.Signal(int)

    # Signal to update variables in GUI
    update_var_signal = QtCore.Signal(str,str)

    # Signal to indicate the main thread that there was an error
    error_signal = QtCore.Signal(str, str)

    # Signal to send a message to the user about the result of model checking
    add_model_card_signal = QtCore.Signal(int, dict, bool)

    # Signal to send a message to the user about the result of model checking
    report_yaml_model_check_result = QtCore.Signal(int)

    # Signal to indicate the main thread that the worker has finished 
    finished_signal = QtCore.Signal()

    def __init__(self, main_window, from_wizard):
        """
        Class to check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
        and Torchvision.

        Parameters 
        ----------
        main_window : QMainWindow
            Main window of the application. 
        """
        super(check_models_from_other_sources_engine, self).__init__()
        self.main_window =  main_window
        # self.COLLECTION_URL = "https://raw.githubusercontent.com/bioimage-io/collection-bioimage-io/gh-pages/collection.json"
        self.COLLECTION_URL = "https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/collection.json"
        self.from_wizard = from_wizard

    def run(self):
        """
        Checks possible model available in BioImage Model Zoo and Torchivision for the workflow specified by Wizards form. 
        """
        ## Functionality copied from BiaPy commit: 0ed2222869300316839af7202ce1d55761c6eb88 (3.5.1) - (check_bmz_args function)
        self.state_signal.emit(0)
        model_name = ""
        try:
            # Checking BMZ model compatibility using the available model list provided by BMZ
            collection_path = Path(pooch.retrieve(self.COLLECTION_URL, known_hash=None))
            with collection_path.open() as f:
                collection = json.load(f)

            # Collect all the models in BMZs
            model_urls = [entry["rdf_source"] for entry in collection["collection"] if entry["type"] == "model"]

            # Check each model compatibility
            model_rdfs = []
            model_count = 0
            for mu in model_urls:
                with open(Path(pooch.retrieve(mu, known_hash=None)), 'rt', encoding='utf8') as stream:
                    model_rdfs.append(yaml.safe_load(stream))
                    model_name = model_rdfs[-1]['name']
                    self.main_window.logger.info("Checking entry: {}".format(model_name))
                    
                    if self.from_wizard:
                        problem_type = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"]
                        problem_ndim = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.NDIM"]
                    else:
                        problem_type = self.main_window.cfg.settings["workflow_key_names"][self.main_window.cfg.settings['selected_workflow']]
                        problem_ndim = get_text(self.main_window.ui.PROBLEM__NDIM__INPUT)

                    workflow_specs = {}
                    workflow_specs["workflow_type"] = problem_type
                    workflow_specs["ndim"] = problem_ndim
                    workflow_specs["nclasses"] = "all"

                    _, error, em = check_bmz_model_compatibility(model_rdfs[-1], workflow_specs=workflow_specs)

                    if not error:
                        self.main_window.logger.info("Compatible model")
                        # Creating BMZ model object
                        # model = load_description(model_rdfs[-1]['config']['bioimageio']['nickname'])
                        # abs url: model.covers[0].absolute() (covers[0] is RelativeFilePath)
                        biapy_imposed_vars = check_model_restrictions(model_rdfs[-1], workflow_specs=workflow_specs)
                        doi = "/".join(model_rdfs[-1]['id'].split("/")[:2])
                        # Extract nickname and its icon
                        if 'nickname' in model_rdfs[-1]['config']['bioimageio']:
                            nickname = model_rdfs[-1]['config']['bioimageio']['nickname']
                            nickname_icon = model_rdfs[-1]['config']['bioimageio']['nickname_icon']
                        elif 'id' in model_rdfs[-1]['config']['bioimageio']:
                            nickname = model_rdfs[-1]['config']['bioimageio']['id']
                            nickname_icon = model_rdfs[-1]['config']['bioimageio']['id_emoji']
                        else:
                            nickname = doi
                            nickname_icon = doi
                        cover_url = "https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/"+nickname+"/"+str(model_rdfs[-1]["version"])+"/files/"+model_rdfs[-1]['covers'][0]
                        model_info = {
                            'name': model_name,
                            'source': "BioImage Model Zoo",
                            'description': model_rdfs[-1]['description'],
                            'nickname': nickname,
                            'nickname_icon': nickname_icon,
                            'id': doi,
                            'covers': cover_url,
                            'url': f"https://bioimage.io/#/?id={doi}",
                            'imposed_vars': biapy_imposed_vars,
                        }
                        self.add_model_card_signal.emit(model_count, model_info, self.from_wizard)

                        model_count += 1
                    else:
                        self.main_window.logger.info("Not compatible model")
                        self.main_window.logger.info(f"Error message: {em}")
            
            self.main_window.logger.info("Finish checking BMZ model . . .")

            # Check Torchvision models 
            models, model_restrictions_description, model_restrictions = check_torchvision_available_models(
                problem_type, 
                problem_ndim
            )
            for m, res, res_cmd in zip(models, model_restrictions_description, model_restrictions):
                self.main_window.logger.info(f"Creating model card for: {m} . . .")
                model_info = {
                    'name': m,
                    'nickname': m,
                    'source': "Torchvision",
                    'description': "Loaded with its default weights (normally on ImageNet data). More info in the link below",
                    'url': "https://pytorch.org/vision/main/models.html",
                    'restrictions': res,
                    'imposed_vars': res_cmd,
                }
                self.add_model_card_signal.emit(model_count, model_info, self.from_wizard)
                model_count += 1

        except:
            exc = traceback.format_exc()
            self.main_window.logger.error(exc)
            self.error_signal.emit(f"Error found when checking {model_name} model:\n{exc}", "unexpected_error")
            self.state_signal.emit(1)
            self.finished_signal.emit()
            return     

        self.report_yaml_model_check_result.emit(model_count)
        self.state_signal.emit(1)
        self.finished_signal.emit()

def export_wizard_summary(main_window):
    """
    Create a yaml configuration file for the questions of the wizard. 
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    main_window.logger.info("Preparing the function to export the wizard's summary")

    # Check if there are not answered questions
    finished = True
    finished_data_checks = True
    for i in range(len(main_window.cfg.settings['wizard_question_visible'])):
        if main_window.cfg.settings['wizard_question_visible'][i] and \
            main_window.cfg.settings["wizard_question_answered_index"][i] == -1:
            finished = False
            break
            
        if main_window.cfg.settings['wizard_possible_answers'][i][0] == "PATH":
            key = next(iter(main_window.cfg.settings["wizard_variable_to_map"][f"Q{(i+1)}"].keys()))
            phase = "TRAIN" if "TRAIN" in key else "TEST"
            if (
                main_window.cfg.settings["wizard_answers"][f"{phase}.ENABLE"] 
                and f"CHECKED {key}" in main_window.cfg.settings["wizard_answers"] 
                and main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] == -1
                and not (
                    "GT_PATH" in key 
                    and main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"] in ["DENOISING", "CLASSIFICATION", "SELF_SUPERVISED"]
                )
                and not (
                    "GT_PATH" in key 
                    and phase == "TEST"
                    and not main_window.cfg.settings["wizard_answers"]["DATA.TEST.LOAD_GT"]
                )
            ):
                finished_data_checks = False

    # Check if the data folder was checked 
    if not finished:
        main_window.dialog_exec("There are still some questions not answered. Please go back and do "
            "it before continue.", "inform_user")
    elif not finished_data_checks:
        main_window.dialog_exec("Please check the data in training/test paths selected in order to prevent future errors.", "inform_user")
    else:  
        main_window.yes_no_exec("Do you want to finish wizard and create the configuration based on your answers?")
        if not main_window.yes_no.answer:
            return 
        
        biapy_cfg = main_window.cfg.settings["wizard_answers"].copy()
        biapy_cfg["data_constraints"] = main_window.cfg.settings["wizard_answers"]["data_constraints"].copy()
        biapy_cfg["sample_info"] = main_window.cfg.settings["wizard_answers"]["sample_info"].copy()
        if "model_restrictions" in biapy_cfg:
            biapy_cfg["model_restrictions"] = main_window.cfg.settings["wizard_answers"]["model_restrictions"].copy()
        sample_info = biapy_cfg["sample_info"]
        del biapy_cfg["sample_info"]

        # Check class compatibility between model and data 
        data_imposed_classes = 2 if "MODEL.N_CLASSES" not in biapy_cfg["data_constraints"] else biapy_cfg["data_constraints"]["MODEL.N_CLASSES"]
        if "model_restrictions" in biapy_cfg and "MODEL.N_CLASSES" in biapy_cfg["model_restrictions"]:
            model_imposed_classes = max(2, biapy_cfg["model_restrictions"]["MODEL.N_CLASSES"])
        else:
            model_imposed_classes = data_imposed_classes
        if data_imposed_classes != model_imposed_classes:
            main_window.dialog_exec(f"Incompatibility found: data provided seems to have {data_imposed_classes} classes whereas "
                f"the pretrained model is prepared to work with {model_imposed_classes} classes. Please select another pretrained model.", reason="error")
            return

        # Special variables that need to be processed
        # Constraints imposed by the model. Patch size will be determined by the model
        if "model_restrictions" in biapy_cfg:
            for key, value in biapy_cfg["model_restrictions"].items():
                biapy_cfg[key] = value
            del biapy_cfg["DATA.PATCH_SIZE_Z"]
            del biapy_cfg["DATA.PATCH_SIZE_XY"]
            del biapy_cfg["model_restrictions"]
        else:
            patch_size = ()
            if biapy_cfg["DATA.PATCH_SIZE_Z"] != -1:
                patch_size = (biapy_cfg["DATA.PATCH_SIZE_Z"],)
            del biapy_cfg["DATA.PATCH_SIZE_Z"]

            if biapy_cfg["DATA.PATCH_SIZE_XY"] == -1:
                patch_size = (-1,)
            else:
                patch_size += biapy_cfg["DATA.PATCH_SIZE_XY"]
            patch_size += (biapy_cfg["data_constraints"]["DATA.PATCH_SIZE_C"],)
            del biapy_cfg["DATA.PATCH_SIZE_XY"]
            biapy_cfg["DATA.PATCH_SIZE"] = patch_size

        # Channel compatibility
        model_channels = biapy_cfg["DATA.PATCH_SIZE"][-1]
        data_channels = biapy_cfg["data_constraints"]["DATA.PATCH_SIZE_C"]
        if data_channels != model_channels:
            main_window.dialog_exec(f"Incompatibility found: data provided seems to have {data_channels} channels whereas "
                f"the pretrained model expects {model_channels} channels. Please select another pretrained model.", reason="error")
            return
        del biapy_cfg["data_constraints"]["DATA.PATCH_SIZE_C"]

        # Check number of samples between provided paths 
        for phase in ["TRAIN","TEST"]:
            if biapy_cfg[f"{phase}.ENABLE"]:
                if f"DATA.{phase}.GT_PATH" in biapy_cfg["data_constraints"]:
                    if biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH"] != biapy_cfg["data_constraints"][f"DATA.{phase}.PATH"]:
                        m = "Incompatibility found: number of raw images and ground truth mismatch. Each raw image must "\
                            "have a ground truth image. Please check both directories:\n"\
                            "    - {} items found in {}\n"\
                            "    - {} items found in {}\n".format(
                                biapy_cfg["data_constraints"][f"DATA.{phase}.PATH"],
                                biapy_cfg["data_constraints"][f"DATA.{phase}.PATH_path"],
                                biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH"],
                                biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH_path"]
                                )
                        main_window.dialog_exec(m, reason="error")
                        return

                    if (
                        f"DATA.{phase}.PATH_path_shapes" in biapy_cfg["data_constraints"] 
                        and f"DATA.{phase}.GT_PATH_path_shapes" in biapy_cfg["data_constraints"]
                    ):
                        y_upscaling = -1
                        for x, y in zip(
                            biapy_cfg["data_constraints"][f"DATA.{phase}.PATH_path_shapes"], 
                            biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH_path_shapes"]
                        ):
                            if y_upscaling == -1 and biapy_cfg["PROBLEM.TYPE"] == "SUPER_RESOLUTION":
                                y_upscaling = []
                                for i in range(len(x[:-1])):
                                    div = y[i] / x[i]
                                    if div % 1 != 0:
                                        main_window.dialog_exec("Raw images and their corresponding targets seem to not have an integer division. "
                                            "Remember that in super-resolution workflow an upsampled version of the raw images are expected as target. "
                                            "For instance, if raw image shape is 512x512 the expected target image shape need to be 1024x1024 in a x2 "
                                            "upsampling. Here we found {} and {} shapes for raw images and target respectively. Check the data to "
                                            "proceed.".format(x,y), reason="error")
                                        return
                                    else:
                                        y_upscaling.append(int(div))
                                y_upscaling = tuple(y_upscaling)
                                biapy_cfg["PROBLEM.SUPER_RESOLUTION.UPSCALING"] = y_upscaling

                            if biapy_cfg["PROBLEM.TYPE"] == "SUPER_RESOLUTION":
                                if biapy_cfg["PROBLEM.NDIM"] == "3D":
                                    expected_y_shape = (
                                        x[0] * y_upscaling[0],
                                        x[1] * y_upscaling[1],
                                        x[2] * y_upscaling[2],
                                        x[3],
                                    )
                                else:
                                    expected_y_shape = (
                                        x[0] * y_upscaling[0],
                                        x[1] * y_upscaling[1],
                                        x[2],
                                    )
                            else:
                                expected_y_shape = x
                                
                            if y[:-1] != expected_y_shape[:-1]:
                                main_window.dialog_exec("Raw images and their corresponding targets seem to not match in shape. "
                                    "Expected {} and {}. Found {} and {} for raw images and target respectively"\
                                    .format(x[:-1],expected_y_shape[:-1],x[:-1],y[:-1]), reason="error")
                                return    

                if f"DATA.{phase}.PATH_path_shapes" in biapy_cfg["data_constraints"]:
                    del biapy_cfg["data_constraints"][f"DATA.{phase}.PATH_path_shapes"]
                if f"DATA.{phase}.GT_PATH_path_shapes" in biapy_cfg["data_constraints"]:
                    del biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH_path_shapes"]
                if f"DATA.{phase}.PATH" in biapy_cfg["data_constraints"]:    
                    del biapy_cfg["data_constraints"][f"DATA.{phase}.PATH"]
                if f"DATA.{phase}.PATH_path" in biapy_cfg["data_constraints"]:    
                    del biapy_cfg["data_constraints"][f"DATA.{phase}.PATH_path"]
                if f"DATA.{phase}.GT_PATH" in biapy_cfg["data_constraints"]:
                    del biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH"]
                if f"DATA.{phase}.GT_PATH_path" in biapy_cfg["data_constraints"]:
                    del biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH_path"]

        # Set the rest of the variables found by checking the data 
        for key, value in biapy_cfg["data_constraints"].items():
            biapy_cfg[key] = value
        del biapy_cfg["data_constraints"]

        # Remove control values 
        keys_to_remove = [x for x in biapy_cfg.keys() if "CHECKED " in x]
        for k in keys_to_remove:
            del biapy_cfg[k]

        # Generate config from answers 
        out_config = {}
        for key, value in biapy_cfg.items():
            if value != -1:
                if isinstance(key, str):
                    create_dict_from_key(key, value, out_config)
                else:
                    raise ValueError(f"Error found in config: {key}. Contact BiaPy team!")
        out_config = set_default_config(
            out_config.copy(), 
            main_window.cfg.settings['GPUs'], 
            sample_info
            )

        yaml_file = os.path.join(get_text(main_window.ui.wizard_browse_yaml_path_input), get_text(main_window.ui.wizard_yaml_name_input))
        if not yaml_file.endswith(".yaml") and not yaml_file.endswith(".yml"):
            yaml_file +=".yaml"
        main_window.cfg.settings['yaml_config_filename'] = yaml_file 

        # Writing YAML file
        replace = True
        if os.path.exists(yaml_file):
            main_window.yes_no_exec("The file '{}' already exists. Do you want to overwrite it?".format(yaml_file))
            replace = True if main_window.yes_no.answer else False
        if replace:
            main_window.logger.info("Creating YAML file") 
            with open(yaml_file, 'w', encoding='utf8') as outfile:
                yaml.dump(out_config, outfile, default_flow_style=False)

        # Update GUI with the new YAML file path and resets the check 
        main_window.ui.select_yaml_name_label.setText(os.path.normpath(yaml_file))
        actual_name = get_text(main_window.ui.job_name_input)
        if actual_name in ["", "my_semantic_segmentation", "my_instance_segmentation", "my_detection", "my_denoising", \
            "my_super_resolution", "my_self_supervised_learning", "my_classification", "my_image_to_image"]:
            main_window.ui.job_name_input.setPlainText("my_"+ out_config["PROBLEM"]["TYPE"].lower())
        main_window.ui.check_yaml_file_errors_label.setText("")
        main_window.ui.check_yaml_file_errors_frame.setStyleSheet("") 

        if replace:
            # Advise user where the YAML file has been saved 
            message = "Configuration file created:\n{}".format(yaml_file)
            main_window.dialog_exec(message, reason="inform_user")
        
        change_page(main_window,'bn_run_biapy',99)
        
        # Resets wizard 
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.wizard_start_page)
        clear_answers(main_window, ask_user=False)

def set_default_config(cfg, gpu_info, sample_info):
    """
    Set default variables depending on the workflow.

    Parameters
    ----------
    cfg : dict
        Configuration.

    gpu_info : list of GPUtil.GPUtil.GPU
        Information of all GPUs found in the system.

    sample_info : dict of dict
        Information with training data. Expected keys are "DATA.TRAIN.PATH" and "DATA.TEST.PATH". For each item, another 
        dictionary is expected with the following keys:
            * 'total_samples': integer. Number of samples. 
            * 'crop_shape': tuple of int. Shape of the crops used to calculate the number of samples. E.g. (256, 256, 1).
            * 'dir_name': string. Directory processed.
    """
    ##################
    # GENERAL CONFIG #
    ##################
    # System 
    cfg["SYSTEM"] = {}
    cfg["SYSTEM"]["NUM_CPUS"] = -1
    cfg["SYSTEM"]["NUM_WORKERS"] = 3

    ########
    # DATA #
    ########
    cfg['DATA']['REFLECT_TO_COMPLETE_SHAPE'] = True
    if cfg['TRAIN']['ENABLE']:
        # Train data 
        cfg["DATA"]["TRAIN"]["IN_MEMORY"] = False
        # Validation data
        if "VAL" not in cfg['DATA']:
            cfg['DATA']['VAL'] = {}
        cfg['DATA']['VAL']['IN_MEMORY'] = False
        cfg["DATA"]["VAL"]["FROM_TRAIN"] = True
        cfg["DATA"]["VAL"]["SPLIT_TRAIN"] = 0.1
    
    if cfg['TEST']['ENABLE']:
        # Test data
        if "TEST" not in cfg['DATA']:
            cfg['DATA']['TEST'] = {}
        cfg["DATA"]["TEST"]["IN_MEMORY"] = False

        # Adjust test padding accordingly
        if cfg['DATA']['PATCH_SIZE'][0] != -1:
            cfg['DATA']['TEST']['PADDING'] = str(tuple([x//6 for x in cfg['DATA']['PATCH_SIZE'][:-1]]))

    # Normalization
    if "NORMALIZATION" not in cfg['DATA']:
        cfg['DATA']['NORMALIZATION'] = {}
    cfg['DATA']['NORMALIZATION']['TYPE'] = 'custom'
    cfg['DATA']['NORMALIZATION']['PERC_CLIP'] = True
    cfg['DATA']['NORMALIZATION']['PERC_LOWER'] = 0.1
    cfg['DATA']['NORMALIZATION']['PERC_UPPER'] = 99.9

    #######################
    # TRAINING PARAMETERS #
    #######################
    if cfg['TRAIN']['ENABLE']:
        cfg['TRAIN']['EPOCHS'] = 150
        cfg['TRAIN']['PATIENCE'] = 50
        cfg['TRAIN']['OPTIMIZER'] = "ADAMW"
        cfg['TRAIN']['LR'] = 1.E-4
        # Learning rate scheduler
        if "LR_SCHEDULER" not in cfg['TRAIN']:
            cfg['TRAIN']['LR_SCHEDULER'] = {}
        cfg['TRAIN']['LR_SCHEDULER']['NAME'] = 'warmupcosine'
        cfg['TRAIN']['LR_SCHEDULER']['MIN_LR'] = 1.E-5
        cfg['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_EPOCHS'] = 10
        if "LOSS" not in cfg:
            cfg['LOSS'] = {}
        cfg['LOSS']['CLASS_REBALANCE'] = True 

    #########
    # MODEL #
    #########
    # TODO: calculate BMZ/torchvision model size. Now a high number to ensure batch_size is set to 1 so it 
    # works always
    network_base_memory = 9999999  
    if cfg['MODEL']['SOURCE'] == "biapy":
        if cfg["PROBLEM"]["TYPE"] in [
            "SEMANTIC_SEG",
            "INSTANCE_SEG",
            "DETECTION",
            "DENOISING",
            "IMAGE_TO_IMAGE"
        ]:
            cfg["MODEL"]["ARCHITECTURE"] = "resunet"
            if cfg['PROBLEM']['NDIM'] == "3D":
                cfg["MODEL"]["Z_DOWN"] = [1, 1, 1, 1]
            network_base_memory = 400
        elif cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
            if cfg['PROBLEM']['NDIM'] == "3D":
                cfg["MODEL"]["ARCHITECTURE"] = "resunet"
                cfg["MODEL"]["Z_DOWN"] = [1, 1, 1, 1]
                network_base_memory = 400
            else:
                cfg["MODEL"]["ARCHITECTURE"] = "rcan"
                network_base_memory = 3500 
        elif cfg["PROBLEM"]["TYPE"] == "SELF_SUPERVISED":
            cfg["MODEL"]["ARCHITECTURE"] = "resunet"
            network_base_memory = 400
            if cfg['PROBLEM']['NDIM'] == "3D":
                cfg["MODEL"]["Z_DOWN"] = [1, 1, 1, 1]
        elif cfg["PROBLEM"]["TYPE"] == "CLASSIFICATION":
            cfg["MODEL"]["ARCHITECTURE"] = "vit" 
            network_base_memory = 2200 

    #####################
    # DATA AUGMENTATION #
    #####################
    if cfg['TRAIN']['ENABLE']:
        if "AUGMENTOR" not in cfg:
            cfg['AUGMENTOR'] = {}
        cfg['AUGMENTOR']["ENABLE"] = True
        cfg['AUGMENTOR']["AFFINE_MODE"] = 'reflect'
        cfg['AUGMENTOR']["VFLIP"] = True
        cfg['AUGMENTOR']["HFLIP"] = True
        if cfg['PROBLEM']['NDIM'] == "3D":
            cfg['AUGMENTOR']['ZFLIP'] = True
        
    ###################
    # TEST PARAMETERS #
    ###################
    if cfg['TEST']['ENABLE']:
        if 'FULL_IMG' not in cfg['TEST']:
            cfg['TEST']['FULL_IMG'] = False

    ############################
    # WORKFLOW SPECIFIC CONFIG #
    ############################
    max_batch_size_allowed = 16 if cfg['PROBLEM']['NDIM'] == "2D" else 4 
    data_channels = cfg["DATA"]["PATCH_SIZE"][-1]
    if cfg["PROBLEM"]["TYPE"] in [
            "SEMANTIC_SEG",
            "INSTANCE_SEG",
            "DETECTION",
            "IMAGE_TO_IMAGE"
        ]:
        if cfg['TRAIN']['ENABLE']:
            if 'AUGMENTOR' not in cfg:
                cfg['AUGMENTOR'] = {}
            cfg['AUGMENTOR']['BRIGHTNESS'] = True
            cfg['AUGMENTOR']['BRIGHTNESS_FACTOR'] = str((-0.1, 0.1))
            cfg['AUGMENTOR']['CONTRAST'] = True
            cfg['AUGMENTOR']['CONTRAST_FACTOR'] = str((-0.1, 0.1))
            cfg['AUGMENTOR']['ELASTIC'] = True
            cfg['AUGMENTOR']['ZOOM'] = True
            cfg['AUGMENTOR']['ZOOM_RANGE'] = str((0.9, 1.1))
            cfg['AUGMENTOR']['RANDOM_ROT'] = True

        if cfg['PROBLEM']['TYPE'] == 'INSTANCE_SEG':
            if "INSTANCE_SEG" not in cfg['PROBLEM']:
                cfg['PROBLEM']['INSTANCE_SEG'] = {}
            cfg['PROBLEM']['INSTANCE_SEG']['DATA_CHANNELS'] = 'BC'
            cfg['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_TYPE'] = "auto"

        elif cfg['PROBLEM']['TYPE'] == 'DETECTION':  
            if "DETECTION" not in cfg['PROBLEM']:
                cfg['PROBLEM']['DETECTION'] = {}
            cfg['PROBLEM']['DETECTION']['CHECK_POINTS_CREATED'] = False    
            if cfg['TEST']['ENABLE']:
                if "REMOVE_CLOSE_POINTS_RADIUS" not in cfg['TEST']['POST_PROCESSING']:
                    cfg['TEST']['POST_PROCESSING']["REMOVE_CLOSE_POINTS_RADIUS"] = 5
                cfg['TEST']['DET_TOLERANCE'] = int(0.8*cfg['TEST']['POST_PROCESSING']["REMOVE_CLOSE_POINTS_RADIUS"])
                cfg['TEST']['DET_MIN_TH_TO_BE_PEAK'] = 0.5 
                cfg['TEST']['POST_PROCESSING']["REMOVE_CLOSE_POINTS"] = True
    elif cfg["PROBLEM"]["TYPE"] == "DENOISING":
        if cfg['DATA']['PATCH_SIZE'][0] == -1:
            if cfg['PROBLEM']['NDIM'] == "2D":
                cfg['DATA']['PATCH_SIZE'] = (64,64)+(data_channels,)
            else:
                cfg['DATA']['PATCH_SIZE'] = (12,64,64)+(data_channels,)
            if cfg['TEST']['ENABLE']:
                cfg['DATA']['TEST']['PADDING'] = str(tuple([x//6 for x in cfg['DATA']['PATCH_SIZE'][:-1]]))

        # Config as Noise2Void default parameters
        if "DENOISING" not in cfg['PROBLEM']:
            cfg['PROBLEM']['DENOISING'] = {}
        cfg['PROBLEM']['DENOISING']['N2V_STRUCTMASK'] = True
        cfg['MODEL']['ARCHITECTURE'] = 'unet'
        cfg['MODEL']['FEATURE_MAPS'] = [32, 64, 96]
        if cfg['PROBLEM']['NDIM'] == "3D":
            cfg["MODEL"]["Z_DOWN"] = [1, 1]
        cfg['MODEL']['KERNEL_SIZE'] = 3
        cfg['MODEL']['UPSAMPLE_LAYER'] = "upsampling"
        cfg['MODEL']['DROPOUT_VALUES'] = [0, 0, 0]
        cfg['MODEL']['ACTIVATION'] = 'relu'
        cfg['MODEL']['LAST_ACTIVATION'] = 'linear'
        cfg['MODEL']['NORMALIZATION'] = 'bn'
        max_batch_size_allowed = 64
    elif cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
        if cfg['DATA']['PATCH_SIZE'][0] == -1:
            if cfg['PROBLEM']['NDIM'] == "2D":
                cfg['DATA']['PATCH_SIZE'] = (48,48)+(data_channels,)
            else:
                cfg['DATA']['PATCH_SIZE'] = (6,128,128)+(data_channels,)

            if cfg['TEST']['ENABLE']:
                cfg['DATA']['TEST']['PADDING'] = str(tuple([x//6 for x in cfg['DATA']['PATCH_SIZE'][:-1]]))

        # Force div normalization
        cfg['DATA']['NORMALIZATION']['TYPE'] = 'div'
        max_batch_size_allowed = 64
    elif cfg["PROBLEM"]["TYPE"] == "CLASSIFICATION":
        pass

    # Removing detection key added from the wizard if we are not in that workflow 
    if not cfg['TEST']['ENABLE'] or cfg['PROBLEM']['TYPE'] != 'DETECTION':  
        if 'POST_PROCESSING' in cfg['TEST'] and "REMOVE_CLOSE_POINTS_RADIUS" in cfg['TEST']['POST_PROCESSING']:
            del cfg['TEST']['POST_PROCESSING']["REMOVE_CLOSE_POINTS_RADIUS"]
            if len(cfg['TEST']['POST_PROCESSING']) == 0:
                del cfg['TEST']['POST_PROCESSING']

    # Calculate data channels 
    # cfg.PROBLEM.TYPE == "CLASSIFICATION" or "SELF_SUPERVISED" and PRETEXT_TASK == "masking". But as in the wizard there is no SSL
    # we reduce the if fo samples_each_time to this
    if cfg["PROBLEM"]["TYPE"] == "CLASSIFICATION":
        y_channels = 0
    else:
        if cfg["PROBLEM"]["TYPE"] in [
            "DENOISING",
            "SUPER_RESOLUTION",
            "IMAGE_TO_IMAGE"
        ]:
            y_channels = cfg['DATA']['PATCH_SIZE'][-1]   
        elif cfg["PROBLEM"]["TYPE"] == "INSTANCE_SEG":
            y_channels = 2 # As we are using a BC approach in the Wizard 
        else:
            y_channels = 1

    channels_per_sample = {
        "x": cfg['DATA']['PATCH_SIZE'][-1], 
        "y": y_channels, 
        }

    # Batch size calculation
    if cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
        y_upsampling = cfg["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"]
    else:
        y_upsampling = (1,1) if cfg['PROBLEM']['NDIM'] == "2D" else (1,1,1)
    # batch_size = batch_size_calculator(
    #     gpu_info=gpu_info, 
    #     sample_info=sample_info, 
    #     patch_size=cfg['DATA']['PATCH_SIZE'],
    #     channels_per_sample=channels_per_sample,
    #     network_base_memory=network_base_memory, 
    #     y_upsampling=y_upsampling,
    #     max_batch_size_allowed=max_batch_size_allowed,
    #     )
    batch_size = 1
    
    if cfg['TRAIN']['ENABLE']:
        cfg['TRAIN']['BATCH_SIZE'] = batch_size

    cfg['DATA']['PATCH_SIZE'] = str(cfg['DATA']['PATCH_SIZE'])
    if cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
        cfg["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"] = str(cfg["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"])
    return cfg 

def batch_size_calculator(
        gpu_info, 
        sample_info, 
        patch_size,
        channels_per_sample, 
        network_base_memory=400, 
        sample_size_reference=256, 
        sample_memory_reference=100,
        max_batch_size_allowed=32,
        y_upsampling=(1,1),
    ):
    """
    Calculate a reasonable value for the batch size measuring how much memory can consume a item returned by BiaPy generator 
    (i.e. __getitem__ function). It takes into account the GPUs available (taking the minimum memory among them), number
    of samples, memory of the network (``network_base_memory``) and a sample reference memory (``sample_size_reference`` and 
    ``sample_memory_reference``). The default settings of this variables takes as reference samples of (256,256,1), where each 
    sample is calculated to consume 100MB of memory (more or less).
    
    Parameters
    ----------
    gpu_info : list of GPUtil.GPUtil.GPU
        Information of all GPUs found in the system.

    sample_info : dict of dict
        Information with training data. Expected keys are "DATA.TRAIN.PATH" and "DATA.TEST.PATH". For each item, another 
        dictionary is expected with the following keys:
            * 'total_samples': integer. Number of samples. 
            * 'crop_shape': tuple of int. Shape of the crops used to calculate the number of samples during data check. 
              E.g. (256, 256, 1).
            * 'dir_name': string. Directory processed.

    patch_size : tuple of int
        Patch size selected in the wizard. 

    channels_per_sample : dict of int
        Information of the number of channels for X and Y data. The following keys are expected:
            * 'x': int. Channels for X data.
            * 'y': int. Channels for Y data.

    network_base_memory : int, optional
        Memory consumed by the deep learning model in MB. This needs to be previously measured. For instace, the default
        U-Net of BiaPy takes 400MB in the GPU.

    sample_size_reference : int, optional
        Size reference used to measure ``sample_memory_reference``.
    
    sample_memory_reference : int, optional
        Memory in MB that consume a sample of size ``sample_size_reference``. 

    max_batch_size_allowed : int, optional
        Maximum batch size to allow.

    y_upsampling : tuple of int, optional
        Upsampling to be done to the Y data. Should be always 1 but in super-resolution workflow. 
    """    
    # Calculate min memory between available GPUs
    min_mem_gpu = None
    for gpu in gpu_info:
        if min_mem_gpu is None:
            min_mem_gpu = gpu.memoryTotal
        else:
            min_mem_gpu = min(min_mem_gpu, gpu.memoryTotal)

    x_data_to_analize = sample_info["DATA.TRAIN.PATH"] if "DATA.TRAIN.PATH" in sample_info else sample_info["DATA.TEST.PATH"]        
    # Leave 20% of the memory to not overload it too much and ensure the batch size will always fit 
    if min_mem_gpu is not None:
        min_mem_gpu = min_mem_gpu*0.8

        # Calculate how much memory takes each X data comparing both, 1) selected patch size and and 2) the crop shape used for cropping 
        # the data an calculating the total number of samples, with the sample reference (composed by sample_size_reference and 
        # sample_memory_reference). 
        x_analisis_ref_ratio = x_data_to_analize['crop_shape'][1] / sample_size_reference 
        x_selected_patch_ref_ratio = (patch_size[1] / sample_size_reference)**2
        x_sample_memory_ratio = x_analisis_ref_ratio * x_selected_patch_ref_ratio * sample_memory_reference
        
        y_data_to_analize = None
        if "DATA.TRAIN.GT_PATH" in sample_info:
            y_data_to_analize = sample_info["DATA.TRAIN.GT_PATH"]
        elif "DATA.TEST.GT_PATH" in sample_info:
            y_data_to_analize = sample_info["DATA.TEST.GT_PATH"]

        if y_data_to_analize is not None:
            y_crop = y_data_to_analize['crop_shape'][1] * y_upsampling[1]
            # Patch size always square in wizard, that's why we use always y_data_to_analize['crop_shape'][1]
            y_analisis_ref_ratio = y_crop / sample_size_reference
            y_selected_patch_ref_ratio = (patch_size[1] / sample_size_reference)**2
            y_sample_memory_ratio = y_analisis_ref_ratio * y_selected_patch_ref_ratio * sample_memory_reference
        else:
            y_sample_memory_ratio = 0

        # How many "slices", i.e. z dimension and channels, to take into account
        x_data = channels_per_sample['x']
        y_data = channels_per_sample['y']
        if len(x_data_to_analize['crop_shape']) == 4: # Add Z dim if working in 3D
            x_data *= x_data_to_analize['crop_shape'][0]
            if y_data_to_analize is not None:
                y_data *= y_data_to_analize['crop_shape'][0] * y_upsampling[0]

        # This value will be close to the one being used during a __getitem__ of BiaPy generator
        item_memory_consumption = (x_sample_memory_ratio*x_data) + (y_sample_memory_ratio*y_data)

        # The network will hold more memory depending on the input_size. It's calculated to be like 210MB per each (256,256,1) sample
        # so we use here x_sample_memory_ratio as it was measure with sample_memory_reference=100MB by default
        approx_network_memory = network_base_memory + (2*x_sample_memory_ratio*x_data)
         
        if item_memory_consumption == 0: item_memory_consumption = 1
        approx_batch_size = (min_mem_gpu - approx_network_memory)//item_memory_consumption if item_memory_consumption > 0 else 1
    else:
        approx_batch_size = max_batch_size_allowed//2

    # Rough stimation on how many patches could be obtained using the actual patch size selected in the wizard 
    sample_data_factor = np.prod([x/y for x,y in zip(x_data_to_analize['crop_shape'],patch_size)])
    total_samples = x_data_to_analize['total_samples']*sample_data_factor
    
    batch_size = int(max(1,min(min(total_samples, approx_batch_size), max_batch_size_allowed)))   

    return batch_size

def adjust_window_progress(main_window):
    """
    Changes new workflow creation progress visual clues. Currently, the blue dots in the bottom part of the GUI.  
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    main_window.ui.window1_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 2 else main_window.cfg.settings['dot_images'][1])
    main_window.ui.window2_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 3 else main_window.cfg.settings['dot_images'][1])
    main_window.ui.window3_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 4 else main_window.cfg.settings['dot_images'][1])
    main_window.ui.window4_bn.setIcon(main_window.cfg.settings['dot_images'][0] if main_window.cfg.settings['page_number'] >= 5 else main_window.cfg.settings['dot_images'][1])

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
    workflow_key_name = main_window.cfg.settings["workflow_key_names"][main_window.cfg.settings['selected_workflow']]
    if workflow_key_name == "SEMANTIC_SEG":
        jobname = "my_semantic_segmentation"
        models = main_window.cfg.settings['semantic_models_real_names']
        losses = main_window.cfg.settings['semantic_losses_real_names']
        metrics = main_window.cfg.settings['semantic_metrics_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_semantic_seg_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_semantic_seg_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input label folder")
        main_window.ui.validation_data_gt_label.setText("Input label folder")
        main_window.ui.transformers_label.setText("UNETR")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input label folder")
        main_window.ui.test_exists_gt_label.setText("Do you have test labels?")
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("SEMANTIC_SEG")
    # Instance seg
    elif workflow_key_name == "INSTANCE_SEG":
        jobname = "my_instance_segmentation"
        models = main_window.cfg.settings['instance_models_real_names']
        losses = main_window.cfg.settings['instance_losses_real_names']
        metrics = main_window.cfg.settings['instance_metrics_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_instance_seg_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_instance_seg_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input label folder")
        main_window.ui.validation_data_gt_label.setText("Input label folder")
        main_window.ui.transformers_label.setText("UNETR")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input label folder")
        main_window.ui.test_exists_gt_label.setText("Do you have test labels?")
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("INSTANCE_SEG")
    # Detection
    elif workflow_key_name == "DETECTION":
        jobname = "my_detection"
        models = main_window.cfg.settings['detection_models_real_names']
        losses = main_window.cfg.settings['detection_losses_real_names']
        metrics = main_window.cfg.settings['detection_metrics_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_detection_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_detection_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input CSV folder")
        main_window.ui.validation_data_gt_label.setText("Input CSV folder")
        main_window.ui.transformers_label.setText("UNETR")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input CSV folder")
        main_window.ui.test_exists_gt_label.setText("Do you have CSV files for test data?")
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("DETECTION")
    # Denoising
    elif workflow_key_name == "DENOISING":
        jobname = "my_denoising"
        models = main_window.cfg.settings['denoising_models_real_names']
        losses = main_window.cfg.settings['denoising_losses_real_names']
        metrics = main_window.cfg.settings['denoising_metrics_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_denoising_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_denoising_page)
        # Train page
        main_window.ui.transformers_label.setText("UNETR")
        # Test page
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("DENOISING")
    # Super resolution
    elif workflow_key_name == "SUPER_RESOLUTION":
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
        losses = main_window.cfg.settings['sr_losses_real_names']
        metrics = main_window.cfg.settings['sr_metrics_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_sr_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_sr_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input high-resolution image folder")
        main_window.ui.validation_data_gt_label.setText("Input high-resolution image folder")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input high-resolution image folder")
        main_window.ui.test_exists_gt_label.setText("Do you have high-resolution test data?")
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("SUPER_RESOLUTION")
    # Self-supevised learning
    elif workflow_key_name == "SELF_SUPERVISED":
        jobname = "my_self_supervised_learning"
        models = main_window.cfg.settings['ssl_models_real_names']
        losses = main_window.cfg.settings['ssl_losses_real_names']
        metrics = main_window.cfg.settings['ssl_metrics_real_names']
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_ssl_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_ssl_page)
        # Train page
        main_window.ui.transformers_label.setText("MAE")
        # Test page
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("SELF_SUPERVISED")
    # Classification
    elif workflow_key_name == "CLASSIFICATION":
        jobname = "my_classification"
        models = main_window.cfg.settings['classification_models_real_names']
        losses = main_window.cfg.settings['classification_losses_real_names']
        metrics = main_window.cfg.settings['classification_metrics_real_names']
        goptions_tab_widget_visible = True
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_classification_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_classification_page)
        # Test page
        main_window.ui.test_exists_gt_label.setText("Is the test separated in classes?")
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("CLASSIFICATION")
    # Image to image
    elif workflow_key_name == "IMAGE_TO_IMAGE":
        jobname = "my_image_to_image"
        models = main_window.cfg.settings['i2i_models_real_names']
        losses = main_window.cfg.settings['i2i_losses_real_names']
        metrics = main_window.cfg.settings['i2i_metrics_real_names']
        goptions_tab_widget_visible = True
        main_window.ui.train_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.train_workflow_specific_tab_i2i_page)
        main_window.ui.test_workflow_specific_tab_stackedWidget.setCurrentWidget(main_window.ui.test_workflow_specific_tab_i2i_page)
        # Train page
        main_window.ui.train_gt_label.setText("Input target folder")
        main_window.ui.validation_data_gt_label.setText("Input target folder")
        main_window.ui.transformers_label.setText("UNETR")
        # Test page
        main_window.ui.test_data_gt_label.setText("Input target folder")
        main_window.ui.test_exists_gt_label.setText("Do you have target test data?")
        main_window.ui.WORKFLOW_SELECTED_LABEL.setText("IMAGE_TO_IMAGE")

    main_window.condition_db.combobox_hide_visible_action(main_window,
        ["test_exists_gt_label", "DATA__TEST__LOAD_GT__INPUT", "DATA__TEST__LOAD_GT__INFO", 
         "test_data_gt_label", "DATA__TEST__GT_PATH__INPUT", "DATA__TEST__GT_PATH__INFO", "test_data_gt_input_browse_bn",
         "train_gt_label", "train_gt_info", "DATA__TRAIN__GT_PATH__INPUT", "train_data_gt_input_browse_bn",
         "validation_data_gt_label", "validation_data_gt_info", "DATA__VAL__GT_PATH__INPUT", "val_data_gt_input_browse_bn"])

    actual_name = get_text(main_window.ui.job_name_input)
    if actual_name in ["", "my_semantic_segmentation", "my_instance_segmentation", "my_detection", "my_denoising", \
        "my_super_resolution", "my_self_supervised_learning", "my_classification", "my_image_to_image"]:
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
        main_window.ui.LOSS__TYPE__INPUT.clear()
        main_window.ui.LOSS__TYPE__INPUT.addItems(losses)


def start_wizard_questionary(main_window):
    """
    Starts questionary.
            
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    """
    if get_text(main_window.ui.wizard_browse_yaml_path_input) == "":
        main_window.dialog_exec("Configuration file path must be defined", "error")
        return
    elif get_text(main_window.ui.wizard_yaml_name_input) == "":
        main_window.dialog_exec("Configuration file name must be defined", "error")
        return
    
    main_window.ui.goptions_advanced_options_scrollarea.setVisible(False)
    main_window.ui.continue_bn.setText("Create configuration file")
    main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.questionary_page)

    prepare_question(main_window)

    # Change TOC index
    index_in_toc = main_window.cfg.settings['wizard_from_question_index_to_toc'][main_window.cfg.settings['wizard_question_index']]
    index = main_window.wizard_toc_model.item(index_in_toc[0]).child(index_in_toc[1])
    if index is not None:
        # As wizard_treeView is triggered when changing it's index we use this flag to block change_wizard_page functionality, 
        # as it has been done already
        main_window.not_allow_change_question = True
        
        main_window.ui.wizard_treeView.setCurrentIndex(index.index())

        # Activate again possible triggers of wizard_treeView
        main_window.not_allow_change_question = False
                
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
        main_window.docker_client = docker.from_env()
        main_window.cfg.settings['docker_found'] = True
    except:
        main_window.cfg.settings['docker_found'] = False
        main_window.logger.info("The following error is expected as Docker has not been found in the system:")
        main_window.logger.warning(traceback.format_exc())
        main_window.logger.info("Below this point the we expect no more errors!")
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
    main_window.cfg.settings['GPUs'] = []
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
        
        main_window.cfg.settings["CUDA_selected"] = str(main_window.cfg.settings['CUDA_version'][pos])
        main_window.cfg.settings['biapy_container_size'] = main_window.cfg.settings['biapy_container_sizes'][pos]

    except Exception as gpu_check_error:
        main_window.cfg.settings['GPUs'] = []
        main_window.logger.warning(f"ERROR during driver check: {gpu_check_error}")

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


def get_text(gui_widget, strip=True):
    """
    Gets the value of the input widget. 
    
    Parameters
    ----------
    gui_widget : QWidget
        Widget to get the value from. 
    """
    if isinstance(gui_widget, QComboBox):
        v = gui_widget.currentText()
    elif isinstance(gui_widget, QLineEdit) or isinstance(gui_widget, QLabel):
        v = gui_widget.text()
    else: #QTextBrowser
        v = gui_widget.toPlainText()
    if strip: v = v.strip()
    return v

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
    elif isinstance(gui_widget, QLineEdit) or isinstance(gui_widget, QLabel):
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

    biapy_config = {}

    # System
    biapy_config['SYSTEM'] = {}
    
    cpus = get_text(main_window.ui.SYSTEM__NUM_CPUS__INPUT)
    cpus = -1 if cpus == "All" else int(cpus)
    biapy_config['SYSTEM']['NUM_CPUS'] = cpus
    biapy_config['SYSTEM']['NUM_WORKERS'] = int(get_text(main_window.ui.SYSTEM__NUM_WORKERS__INPUT))
    biapy_config['SYSTEM']['SEED'] = int(get_text(main_window.ui.SYSTEM__SEED__INPUT))

    # Problem specification
    biapy_config['PROBLEM'] = {}
    biapy_config['PROBLEM']['TYPE'] = main_window.cfg.settings["workflow_key_names"][main_window.cfg.settings['selected_workflow']]
    biapy_config['PROBLEM']['NDIM'] = get_text(main_window.ui.PROBLEM__NDIM__INPUT)
    
    workflow_key_name = main_window.cfg.settings["workflow_key_names"][main_window.cfg.settings['selected_workflow']]
    ### SEMANTIC_SEG
    if workflow_key_name == "SEMANTIC_SEG":
        if int(get_text(main_window.ui.PROBLEM__SEMANTIC_SEG__IGNORE_CLASS_ID__INPUT)) != 0:
            biapy_config['PROBLEM']['SEMANTIC_SEG'] = {}
            biapy_config['PROBLEM']['SEMANTIC_SEG']['IGNORE_CLASS_ID'] = int(get_text(main_window.ui.PROBLEM__SEMANTIC_SEG__IGNORE_CLASS_ID__INPUT))

    ### INSTANCE_SEG
    elif workflow_key_name == "INSTANCE_SEG":
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
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Contours":
            problem_channels = 'C'
        elif get_text(main_window.ui.PROBLEM__INSTANCE_SEG__DATA_CHANNELS__INPUT) == "Affinities":
            problem_channels = 'A'
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
        if biapy_config['PROBLEM']['INSTANCE_SEG']['DATA_MW_TH_TYPE'] == "manual":
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
            try:
                biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_SEQUENCE'] = ast.literal_eval(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_SEQUENCE__INPUT) )
            except: 
                main_window.dialog_exec("There was an error with instance segmentation seed morph sequence field (PROBLEM.INSTANCE_SEG.SEED_MORPH_SEQUENCE). Please check its syntax!", reason="error")
                return True, False
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT) != "[]":
            try:
                biapy_config['PROBLEM']['INSTANCE_SEG']['SEED_MORPH_RADIUS'] =  ast.literal_eval(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__SEED_MORPH_RADIUS__INPUT))
            except:
                main_window.dialog_exec("There was an error with instance segmentation seed morph radius field (PROBLEM.INSTANCE_SEG.SEED_MORPH_RADIUS). Please check its syntax!", reason="error")
                return True, False
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__ERODE_AND_DILATE_FOREGROUND__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['ERODE_AND_DILATE_FOREGROUND'] = True
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_EROSION_RADIUS'] = int(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__FORE_EROSION_RADIUS__INPUT))
            biapy_config['PROBLEM']['INSTANCE_SEG']['FORE_DILATION_RADIUS'] = int(get_text(main_window.ui.PROBLEM__INSTANCE_SEG__FORE_DILATION_RADIUS__INPUT))
        if get_text(main_window.ui.PROBLEM__INSTANCE_SEG__WATERSHED_BY_2D_SLICES__INPUT) == "Yes":
            biapy_config['PROBLEM']['INSTANCE_SEG']['WATERSHED_BY_2D_SLICES'] = True

    ### DETECTION
    elif workflow_key_name == "DETECTION":
        biapy_config['PROBLEM']['DETECTION'] = {}
        try:
            biapy_config['PROBLEM']['DETECTION']['CENTRAL_POINT_DILATION'] = ast.literal_eval(get_text(main_window.ui.PROBLEM__DETECTION__CENTRAL_POINT_DILATION__INPUT))
        except: 
            main_window.dialog_exec("There was an error with detection central point dilation field (PROBLEM.DETECTION.CENTRAL_POINT_DILATION). Please check its syntax!", reason="error")
            return True, False
        biapy_config['PROBLEM']['DETECTION']['CHECK_POINTS_CREATED'] = True if get_text(main_window.ui.PROBLEM__DETECTION__CHECK_POINTS_CREATED__INPUT) == "Yes" else False
        if get_text(main_window.ui.PROBLEM__DETECTION__DATA_CHECK_MW__INPUT) == "Yes" and get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT) == "Yes":
            biapy_config['PROBLEM']['DETECTION']['DATA_CHECK_MW'] = True

    ### DENOISING
    elif workflow_key_name == "DENOISING":
        biapy_config['PROBLEM']['DENOISING'] = {}
        biapy_config['PROBLEM']['DENOISING']['N2V_PERC_PIX'] = float(get_text(main_window.ui.PROBLEM__DENOISING__N2V_PERC_PIX__INPUT))
        biapy_config['PROBLEM']['DENOISING']['N2V_MANIPULATOR'] = get_text(main_window.ui.PROBLEM__DENOISING__N2V_MANIPULATOR__INPUT)
        biapy_config['PROBLEM']['DENOISING']['N2V_NEIGHBORHOOD_RADIUS'] = int(get_text(main_window.ui.PROBLEM__DENOISING__N2V_NEIGHBORHOOD_RADIUS__INPUT))
        biapy_config['PROBLEM']['DENOISING']['N2V_STRUCTMASK'] = True if get_text(main_window.ui.PROBLEM__DENOISING__N2V_STRUCTMASK__INPUT) == "Yes" else False

    ### SUPER_RESOLUTION
    elif workflow_key_name == "SUPER_RESOLUTION":
        biapy_config['PROBLEM']['SUPER_RESOLUTION'] = {}
        biapy_config['PROBLEM']['SUPER_RESOLUTION']['UPSCALING'] = get_text(main_window.ui.PROBLEM__SUPER_RESOLUTION__UPSCALING__INPUT)

    ### SELF_SUPERVISED
    elif workflow_key_name == "SELF_SUPERVISED":
        biapy_config['PROBLEM']['SELF_SUPERVISED'] = {}
        biapy_config['PROBLEM']['SELF_SUPERVISED']['PRETEXT_TASK'] = get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT)
        if get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__PRETEXT_TASK__INPUT) == "crappify":
            biapy_config['PROBLEM']['SELF_SUPERVISED']['RESIZING_FACTOR'] = int(get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__RESIZING_FACTOR__INPUT))
            biapy_config['PROBLEM']['SELF_SUPERVISED']['NOISE'] = float(get_text(main_window.ui.PROBLEM__SELF_SUPERVISED__NOISE__INPUT))

    ### IMAGE_TO_IMAGE
    elif workflow_key_name == "IMAGE_TO_IMAGE":
        biapy_config['PROBLEM']['IMAGE_TO_IMAGE'] = {}
        biapy_config['PROBLEM']['IMAGE_TO_IMAGE']['MULTIPLE_RAW_ONE_TARGET_LOADER'] = True if get_text(main_window.ui.PROBLEM__IMAGE_TO_IMAGE__MULTIPLE_RAW_ONE_TARGET_LOADER__INPUT) == "Yes" else False

    # Dataset
    biapy_config['DATA'] = {}
    if get_text(main_window.ui.DATA__CHECK_GENERATORS__INPUT) == "Yes":
        biapy_config['DATA']['CHECK_GENERATORS'] = True

    if get_text(main_window.ui.DATA__FORCE_RGB__INPUT) == "Yes":
        biapy_config['DATA']['FORCE_RGB'] = True
    
    preprocess_done = False
    if get_text(main_window.ui.DATA__PREPROCESS__TRAIN__INPUT) == "Yes" or \
        get_text(main_window.ui.DATA__PREPROCESS__VAL__INPUT) == "Yes":
        preprocess_done = True
        biapy_config['DATA']['PREPROCESS'] = {}
        biapy_config['DATA']['PREPROCESS']['TRAIN'] = True if get_text(main_window.ui.DATA__PREPROCESS__TRAIN__INPUT) == "Yes" else False
        if biapy_config['DATA']['PREPROCESS']['TRAIN'] and get_text(main_window.ui.DATA__VAL__TYPE__INPUT) in ["Extract from train (cross validation)","Extract from train (split training)"]:
            biapy_config['DATA']['PREPROCESS']['VAL'] = True
        else:
            biapy_config['DATA']['PREPROCESS']['VAL'] = True if get_text(main_window.ui.DATA__PREPROCESS__VAL__INPUT) == "Yes" else False
        if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['PREPROCESS']['RESIZE'] = {}
            biapy_config['DATA']['PREPROCESS']['RESIZE']['ENABLE'] = True
            biapy_config['DATA']['PREPROCESS']['RESIZE']['OUTPUT_SHAPE'] = get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT)
            order = 1
            if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) == "Nearest-neighbor":
                order = 0
            elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) == "Bi-linear":
                order = 1
            elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) == "Bi-quadratic":
                order = 2
            elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) == "Bi-cubic":
                order = 3
            elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) == "Bi-quartic":
                order = 4
            elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__INPUT) == "Bi-quintic":
                order = 5
            biapy_config['DATA']['PREPROCESS']['RESIZE']['ORDER'] = order
            biapy_config['DATA']['PREPROCESS']['RESIZE']['MODE'] = get_text(main_window.ui.DATA__PREPROCESS__RESIZE__MODE__INPUT)
            biapy_config['DATA']['PREPROCESS']['RESIZE']['CVAL'] = float(get_text(main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__INPUT))
            biapy_config['DATA']['PREPROCESS']['RESIZE']['CLIP'] = True if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__INPUT) else False
            biapy_config['DATA']['PREPROCESS']['RESIZE']['PRESERVE_RANGE'] = True if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__INPUT) else False
            biapy_config['DATA']['PREPROCESS']['RESIZE']['ANTI_ALIASING'] = True if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__INPUT) else False
        
        if get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR'] = {}
            biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['ENABLE'] = True
            biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['SIGMA'] = int(get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__INPUT))
            biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['MODE'] = get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__INPUT)
            if get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INPUT) != "":
                biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['CHANNEL_AXIS'] = int(get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__INPUT))
        
        if get_text(main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['PREPROCESS']['MEDIAN_BLUR'] = {}
            biapy_config['DATA']['PREPROCESS']['MEDIAN_BLUR']['ENABLE'] = True
            try:
                biapy_config['DATA']['PREPROCESS']['MEDIAN_BLUR']['KERNEL_SIZE'] = ast.literal_eval(get_text(main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with preprocessing median blur kernel size field (DATA.PREPROCESS.MEDIAN_BLUR.KERNEL_SIZE). Please check its syntax!", reason="error")
                return True, False

        if get_text(main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['PREPROCESS']['MATCH_HISTOGRAM'] = {}
            biapy_config['DATA']['PREPROCESS']['MATCH_HISTOGRAM']['ENABLE'] = True
            biapy_config['DATA']['PREPROCESS']['MATCH_HISTOGRAM']['REFERENCE_PATH'] = get_text(main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__INPUT, strip=False)

        if get_text(main_window.ui.DATA__PREPROCESS__CLAHE__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['PREPROCESS']['CLAHE'] = {}
            biapy_config['DATA']['PREPROCESS']['CLAHE']['ENABLE'] = True
            if get_text(main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INPUT) != "":
                biapy_config['DATA']['PREPROCESS']['CLAHE']['KERNEL_SIZE'] = int(get_text(main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__INPUT))
            biapy_config['DATA']['PREPROCESS']['CLAHE']['CLIP_LIMIT'] = float(get_text(main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__INPUT))
        
        if get_text(main_window.ui.DATA__PREPROCESS__CANNY__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['PREPROCESS']['CANNY'] = {}
            biapy_config['DATA']['PREPROCESS']['CANNY']['ENABLE'] = True
            if get_text(main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INPUT) != "":
                biapy_config['DATA']['PREPROCESS']['CANNY']['LOW_THRESHOLD'] = float(get_text(main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__INPUT))
            if get_text(main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INPUT) != "":
                biapy_config['DATA']['PREPROCESS']['CANNY']['HIGH_THRESHOLD'] = float(get_text(main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__INPUT))
    
    # Extract preprocessing from the test fields
    if get_text(main_window.ui.DATA__PREPROCESS__TEST__INPUT) == "Yes":
        if not preprocess_done:
            biapy_config['DATA']['PREPROCESS'] = {}
        biapy_config['DATA']['PREPROCESS']['TEST'] = True if get_text(main_window.ui.DATA__PREPROCESS__TEST__INPUT) == "Yes" else False
        if not preprocess_done:
            if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__ENABLE__TEST__INPUT) == "Yes":
                biapy_config['DATA']['PREPROCESS']['RESIZE'] = {}
                biapy_config['DATA']['PREPROCESS']['RESIZE']['ENABLE'] = True
                biapy_config['DATA']['PREPROCESS']['RESIZE']['OUTPUT_SHAPE'] = get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT)
                order = 1
                if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) == "Nearest-neighbor":
                    order = 0
                elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) == "Bi-linear":
                    order = 1
                elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) == "Bi-quadratic":
                    order = 2
                elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) == "Bi-cubic":
                    order = 3
                elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) == "Bi-quartic":
                    order = 4
                elif get_text(main_window.ui.DATA__PREPROCESS__RESIZE__OUTPUT_SHAPE__TEST__INPUT) == "Bi-quintic":
                    order = 5
                biapy_config['DATA']['PREPROCESS']['RESIZE']['ORDER'] = order
                biapy_config['DATA']['PREPROCESS']['RESIZE']['MODE'] = get_text(main_window.ui.DATA__PREPROCESS__RESIZE__MODE__TEST__INPUT)
                biapy_config['DATA']['PREPROCESS']['RESIZE']['CVAL'] = float(get_text(main_window.ui.DATA__PREPROCESS__RESIZE__CVAL__TEST__INPUT))
                biapy_config['DATA']['PREPROCESS']['RESIZE']['CLIP'] = True if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__CLIP__TEST__INPUT) else False
                biapy_config['DATA']['PREPROCESS']['RESIZE']['PRESERVE_RANGE'] = True if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__PRESERVE_RANGE__TEST__INPUT) else False
                biapy_config['DATA']['PREPROCESS']['RESIZE']['ANTI_ALIASING'] = True if get_text(main_window.ui.DATA__PREPROCESS__RESIZE__ANTI_ALIASING__TEST__INPUT) else False
            
            if get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__ENABLE__TEST__INPUT) == "Yes":
                biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR'] = {}
                biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['ENABLE'] = True
                biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['SIGMA'] = int(get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__SIGMA__TEST__INPUT))
                biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['MODE'] = get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__MODE__TEST__INPUT)
                if get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INPUT) != "":
                    biapy_config['DATA']['PREPROCESS']['GAUSSIAN_BLUR']['CHANNEL_AXIS'] = int(get_text(main_window.ui.DATA__PREPROCESS__GAUSSIAN_BLUR__CHANNEL_AXIS__TEST__INPUT))
            
            if get_text(main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__ENABLE__TEST__INPUT) == "Yes":
                biapy_config['DATA']['PREPROCESS']['MEDIAN_BLUR'] = {}
                biapy_config['DATA']['PREPROCESS']['MEDIAN_BLUR']['ENABLE'] = True
                try:
                    biapy_config['DATA']['PREPROCESS']['MEDIAN_BLUR']['KERNEL_SIZE'] = ast.literal_eval(get_text(main_window.ui.DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INPUT))
                except: 
                    main_window.dialog_exec("There was an error with preprocessing median blur kernel size field (DATA.PREPROCESS.MEDIAN_BLUR.KERNEL_SIZE). Please check its syntax!", reason="error")
                    return True, False

            if get_text(main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__ENABLE__TEST__INPUT) == "Yes":
                biapy_config['DATA']['PREPROCESS']['MATCH_HISTOGRAM'] = {}
                biapy_config['DATA']['PREPROCESS']['MATCH_HISTOGRAM']['ENABLE'] = True
                biapy_config['DATA']['PREPROCESS']['MATCH_HISTOGRAM']['REFERENCE_PATH'] = get_text(main_window.ui.DATA__PREPROCESS__MATCH_HISTOGRAM__REFERENCE_PATH__TEST__INPUT, strip=False)

            if get_text(main_window.ui.DATA__PREPROCESS__CLAHE__ENABLE__TEST__INPUT) == "Yes":
                biapy_config['DATA']['PREPROCESS']['CLAHE'] = {}
                biapy_config['DATA']['PREPROCESS']['CLAHE']['ENABLE'] = True
                if get_text(main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INPUT) != "":
                    biapy_config['DATA']['PREPROCESS']['CLAHE']['KERNEL_SIZE'] = int(get_text(main_window.ui.DATA__PREPROCESS__CLAHE__KERNEL_SIZE__TEST__INPUT))
                biapy_config['DATA']['PREPROCESS']['CLAHE']['CLIP_LIMIT'] = float(get_text(main_window.ui.DATA__PREPROCESS__CLAHE__CLIP_LIMIT__TEST__INPUT))
            
            if get_text(main_window.ui.DATA__PREPROCESS__CANNY__ENABLE__TEST__INPUT) == "Yes":
                biapy_config['DATA']['PREPROCESS']['CANNY'] = {}
                biapy_config['DATA']['PREPROCESS']['CANNY']['ENABLE'] = True
                if get_text(main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INPUT) != "":
                    biapy_config['DATA']['PREPROCESS']['CANNY']['LOW_THRESHOLD'] = float(get_text(main_window.ui.DATA__PREPROCESS__CANNY__LOW_THRESHOLD__TEST__INPUT))
                if get_text(main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INPUT) != "":
                    biapy_config['DATA']['PREPROCESS']['CANNY']['HIGH_THRESHOLD'] = float(get_text(main_window.ui.DATA__PREPROCESS__CANNY__HIGH_THRESHOLD__TEST__INPUT))
            

    if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['PATCH_SIZE'] = get_text(main_window.ui.DATA__PATCH_SIZE__INPUT)
    else:
        biapy_config['DATA']['PATCH_SIZE'] = get_text(main_window.ui.DATA__PATCH_SIZE__TEST__INPUT)
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

    if get_text(main_window.ui.DATA__NORMALIZATION__PERC_CLIP__INPUT) == "Yes":
        biapy_config['DATA']['NORMALIZATION'] = {}
        biapy_config['DATA']['NORMALIZATION']['PERC_CLIP'] = True
        biapy_config['DATA']['NORMALIZATION']['PERC_LOWER'] = float(get_text(main_window.ui.DATA__NORMALIZATION__PERC_LOWER__INPUT)) 
        biapy_config['DATA']['NORMALIZATION']['PERC_UPPER'] = float(get_text(main_window.ui.DATA__NORMALIZATION__PERC_UPPER__INPUT)) 

    if get_text(main_window.ui.DATA__NORMALIZATION__TYPE__INPUT) == "custom":
        if 'NORMALIZATION' not in biapy_config['DATA']:
            biapy_config['DATA']['NORMALIZATION'] = {}
        biapy_config['DATA']['NORMALIZATION']['TYPE'] = 'custom'
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_MEAN'] = float(get_text(main_window.ui.DATA__NORMALIZATION__CUSTOM_MEAN__INPUT)) 
        biapy_config['DATA']['NORMALIZATION']['CUSTOM_STD'] = float(get_text(main_window.ui.DATA__NORMALIZATION__CUSTOM_STD__INPUT)) 
        
    # Train
    if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TRAIN'] = {}

        if workflow_key_name == "SEMANTIC_SEG" and get_text(main_window.ui.DATA__TRAIN__CHECK_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TRAIN']['CHECK_DATA'] = True
        
        biapy_config['DATA']['TRAIN']['IN_MEMORY'] = True if get_text(main_window.ui.DATA__TRAIN__IN_MEMORY__INPUT) == "Yes" else False
        biapy_config['DATA']['TRAIN']['PATH'] = get_text(main_window.ui.DATA__TRAIN__PATH__INPUT, strip=False)
        if workflow_key_name not in ["DENOISING","SELF_SUPERVISED","CLASSIFICATION"]:
            biapy_config['DATA']['TRAIN']['GT_PATH'] = get_text(main_window.ui.DATA__TRAIN__GT_PATH__INPUT, strip=False)
        if int(get_text(main_window.ui.DATA__TRAIN__REPLICATE__INPUT)) != 0:
            biapy_config['DATA']['TRAIN']['REPLICATE'] = int(get_text(main_window.ui.DATA__TRAIN__REPLICATE__INPUT))
        biapy_config['DATA']['TRAIN']['OVERLAP'] = get_text(main_window.ui.DATA__TRAIN__OVERLAP__INPUT)
        biapy_config['DATA']['TRAIN']['PADDING'] = get_text(main_window.ui.DATA__TRAIN__PADDING__INPUT)
        if get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT) != "(1,1,1)" and get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT) != "(1,1)":
            biapy_config['DATA']['TRAIN']['RESOLUTION'] = get_text(main_window.ui.DATA__TRAIN__RESOLUTION__INPUT)
        
        if get_text(main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TRAIN']['INPUT_ZARR_MULTIPLE_DATA'] = True
            biapy_config['DATA']['TRAIN']['INPUT_ZARR_MULTIPLE_DATA_RAW_PATH'] = get_text(main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT)
            biapy_config['DATA']['TRAIN']['INPUT_ZARR_MULTIPLE_DATA_GT_PATH'] = get_text(main_window.ui.DATA__TRAIN__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT)

        if get_text(main_window.ui.DATA__TRAIN__INPUT_IMG_AXES_ORDER__INPUT) != "TZCYX":
            biapy_config['DATA']['TRAIN']['INPUT_IMG_AXES_ORDER'] = get_text(main_window.ui.DATA__TRAIN__INPUT_IMG_AXES_ORDER__INPUT)

        if get_text(main_window.ui.DATA__TRAIN__INPUT_MASK_AXES_ORDER__INPUT) != "TZCYX":
            biapy_config['DATA']['TRAIN']['INPUT_MASK_AXES_ORDER'] = get_text(main_window.ui.DATA__TRAIN__INPUT_MASK_AXES_ORDER__INPUT)

        if get_text(main_window.ui.DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['TRAIN']['FILTER_SAMPLES'] = {}
            biapy_config['DATA']['TRAIN']['FILTER_SAMPLES']['ENABLE'] = True
            try:
                biapy_config['DATA']['TRAIN']['FILTER_SAMPLES']['PROPS'] = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with train data filter samples property array field (DATA.TRAIN.FILTER_SAMPLES.PROPS). Please check its syntax!", reason="error")
                return True, False
            try:
                biapy_config['DATA']['TRAIN']['FILTER_SAMPLES']['VALUES'] = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with train data filter samples values array field (DATA.TRAIN.FILTER_SAMPLES.VALUES). Please check its syntax!", reason="error")
                return True, False
            try:
                biapy_config['DATA']['TRAIN']['FILTER_SAMPLES']['SIGNS'] = ast.literal_eval(get_text(main_window.ui.DATA__TRAIN__FILTER_SAMPLES__ENABLE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with train data filter samples signs array field (DATA.TRAIN.FILTER_SAMPLES.SIGNS). Please check its syntax!", reason="error")
                return True, False

        # Validation
        biapy_config['DATA']['VAL'] = {}
        biapy_config['DATA']['VAL']['IN_MEMORY'] = True if get_text(main_window.ui.DATA__VAL__IN_MEMORY__INPUT) == "Yes" else False
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
            biapy_config['DATA']['VAL']['PATH'] = get_text(main_window.ui.DATA__VAL__PATH__INPUT, strip=False)
            if workflow_key_name not in ["DENOISING","SELF_SUPERVISED","CLASSIFICATION"]:
                biapy_config['DATA']['VAL']['GT_PATH'] = get_text(main_window.ui.DATA__VAL__GT_PATH__INPUT, strip=False)
            biapy_config['DATA']['VAL']['OVERLAP'] = get_text(main_window.ui.DATA__VAL__OVERLAP__INPUT)
            biapy_config['DATA']['VAL']['PADDING'] = get_text(main_window.ui.DATA__VAL__PADDING__INPUT)

        biapy_config['DATA']['VAL']['RESOLUTION'] = get_text(main_window.ui.DATA__VAL__RESOLUTION__INPUT)

        if get_text(main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA__INPUT) == "Yes":
            biapy_config['DATA']['VAL']['INPUT_ZARR_MULTIPLE_DATA'] = True
            biapy_config['DATA']['VAL']['INPUT_ZARR_MULTIPLE_DATA_RAW_PATH'] = get_text(main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT)
            biapy_config['DATA']['VAL']['INPUT_ZARR_MULTIPLE_DATA_GT_PATH'] = get_text(main_window.ui.DATA__VAL__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT)

        if get_text(main_window.ui.DATA__VAL__INPUT_IMG_AXES_ORDER__INPUT) != "TZCYX":
            biapy_config['DATA']['VAL']['INPUT_IMG_AXES_ORDER'] = get_text(main_window.ui.DATA__VAL__INPUT_IMG_AXES_ORDER__INPUT)

        if get_text(main_window.ui.DATA__VAL__INPUT_MASK_AXES_ORDER__INPUT) != "TZCYX":
            biapy_config['DATA']['VAL']['INPUT_MASK_AXES_ORDER'] = get_text(main_window.ui.DATA__VAL__INPUT_MASK_AXES_ORDER__INPUT)

        if get_text(main_window.ui.DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT) == "Yes":
            biapy_config['DATA']['VAL']['FILTER_SAMPLES'] = {}
            biapy_config['DATA']['VAL']['FILTER_SAMPLES']['ENABLE'] = True
            try:
                biapy_config['DATA']['VAL']['FILTER_SAMPLES']['PROPS'] = ast.literal_eval(get_text(main_window.ui.DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with train data filter samples prperty array field (DATA.TRAIN.FILTER_SAMPLES.PROPS). Please check its syntax!", reason="error")
                return True, False
            try:
                biapy_config['DATA']['VAL']['FILTER_SAMPLES']['VALUES'] = ast.literal_eval(get_text(main_window.ui.DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with train data filter samples values array field (DATA.TRAIN.FILTER_SAMPLES.VALUES). Please check its syntax!", reason="error")
                return True, False
            try:
                biapy_config['DATA']['VAL']['FILTER_SAMPLES']['SIGNS'] = ast.literal_eval(get_text(main_window.ui.DATA__VAL__FILTER_SAMPLES__ENABLE__INPUT))
            except: 
                main_window.dialog_exec("There was an error with train data filter samples signs array field (DATA.TRAIN.FILTER_SAMPLES.SIGNS). Please check its syntax!", reason="error")
                return True, False
            
        # Data augmentation (DA)
        biapy_config['AUGMENTOR'] = {}
        if get_text(main_window.ui.AUGMENTOR__ENABLE__INPUT) == "Yes":
            biapy_config['AUGMENTOR']['ENABLE'] = True  
            if float(get_text(main_window.ui.AUGMENTOR__DA_PROB__INPUT)) != 0.5:
                biapy_config['AUGMENTOR']['DA_PROB'] = float(get_text(main_window.ui.AUGMENTOR__DA_PROB__INPUT))
            biapy_config['AUGMENTOR']['AUG_SAMPLES'] = True if get_text(main_window.ui.AUGMENTOR__AUG_SAMPLES__INPUT) == "Yes" else False
            if get_text(main_window.ui.AUGMENTOR__DRAW_GRID__INPUT) == "No": 
                biapy_config['AUGMENTOR']['DRAW_GRID'] = False
            if int(get_text(main_window.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT)) != 10:
                biapy_config['AUGMENTOR']['AUG_NUM_SAMPLES'] = int(get_text(main_window.ui.AUGMENTOR__AUG_NUM_SAMPLES__INPUT))
            if get_text(main_window.ui.AUGMENTOR__SHUFFLE_TRAIN_DATA_EACH_EPOCH__INPUT) == "No":                
                biapy_config['AUGMENTOR']['SHUFFLE_TRAIN_DATA_EACH_EPOCH'] = False
            if get_text(main_window.ui.AUGMENTOR__SHUFFLE_VAL_DATA_EACH_EPOCH__INPUT) == "Yes":
                biapy_config['AUGMENTOR']['SHUFFLE_VAL_DATA_EACH_EPOCH'] = True
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
                if get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "3D" and get_text(main_window.ui.AUGMENTOR__ZOOM_IN_Z__INPUT) == "Yes":
                    biapy_config['AUGMENTOR']['ZOOM_IN_Z'] = True
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
            if get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "3D" and get_text(main_window.ui.AUGMENTOR__ZFLIP__INPUT) == "Yes":
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
                if get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT) != "3D":
                    biapy_config['AUGMENTOR']['BRIGHTNESS_MODE'] = get_text(main_window.ui.AUGMENTOR__BRIGHTNESS_MODE__INPUT)
            if get_text(main_window.ui.AUGMENTOR__CONTRAST__INPUT) == "Yes":
                biapy_config['AUGMENTOR']['CONTRAST'] = True
                biapy_config['AUGMENTOR']['CONTRAST_FACTOR'] = get_text(main_window.ui.AUGMENTOR__CONTRAST_FACTOR__INPUT)
                if get_text(main_window.ui.AUGMENTOR__CONTRAST_MODE__INPUT) != "3D":
                    biapy_config['AUGMENTOR']['CONTRAST_MODE'] = get_text(main_window.ui.AUGMENTOR__CONTRAST_MODE__INPUT)
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
            if get_text(main_window.ui.AUTOMATIC__AUG__INPUT) == "Manually":
                biapy_config['AUGMENTOR']['ENABLE'] = False
            else: # Automatically: configure default augmentations depending on the workflow 
                biapy_config['AUGMENTOR']['ENABLE'] = True

                # Basic DA
                biapy_config['AUGMENTOR']["AFFINE_MODE"] = 'reflect'
                biapy_config['AUGMENTOR']["VFLIP"] = True
                biapy_config['AUGMENTOR']["HFLIP"] = True
                if biapy_config['PROBLEM']['NDIM'] == "3D":
                    biapy_config['AUGMENTOR']['ZFLIP'] = True

                # Workflow specific DA
                if workflow_key_name in [
                    "SEMANTIC_SEG",
                    "INSTANCE_SEG",
                    "DETECTION",
                    "IMAGE_TO_IMAGE"
                ]:
                    biapy_config['AUGMENTOR']['BRIGHTNESS'] = True
                    biapy_config['AUGMENTOR']['BRIGHTNESS_FACTOR'] = str((-0.1, 0.1))
                    biapy_config['AUGMENTOR']['CONTRAST'] = True
                    biapy_config['AUGMENTOR']['CONTRAST_FACTOR'] = str((-0.1, 0.1))
                    biapy_config['AUGMENTOR']['ELASTIC'] = True
                    biapy_config['AUGMENTOR']['ZOOM'] = True
                    biapy_config['AUGMENTOR']['ZOOM_RANGE'] = str((0.9, 1.1))
                    biapy_config['AUGMENTOR']['RANDOM_ROT'] = True
                    biapy_config['AUGMENTOR']['RANDOM_ROT_RANGE'] = str((-180, 180))
            
    # Test
    if get_text(main_window.ui.TEST__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TEST'] = {}
        if workflow_key_name == "SEMANTIC_SEG" and get_text(main_window.ui.DATA__TEST__CHECK_DATA__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['CHECK_DATA'] = True
        biapy_config['DATA']['TEST']['IN_MEMORY'] = True if get_text(main_window.ui.DATA__TEST__IN_MEMORY__INPUT) == "Yes" else False
        if get_text(main_window.ui.DATA__TEST__USE_VAL_AS_TEST__INPUT) == "Yes" and\
            get_text(main_window.ui.DATA__VAL__TYPE__INPUT) == "Extract from train (cross validation)":
            biapy_config['DATA']['TEST']['USE_VAL_AS_TEST'] = True
        else:
            if get_text(main_window.ui.DATA__TEST__LOAD_GT__INPUT) == "Yes":
                biapy_config['DATA']['TEST']['LOAD_GT'] = True
                if workflow_key_name not in ["DENOISING","SELF_SUPERVISED","CLASSIFICATION"]:
                    biapy_config['DATA']['TEST']['GT_PATH'] = get_text(main_window.ui.DATA__TEST__GT_PATH__INPUT, strip=False)
            else:
                biapy_config['DATA']['TEST']['LOAD_GT'] = False
            biapy_config['DATA']['TEST']['PATH'] = get_text(main_window.ui.DATA__TEST__PATH__INPUT, strip=False)
            
        biapy_config['DATA']['TEST']['OVERLAP'] = get_text(main_window.ui.DATA__TEST__OVERLAP__INPUT)
        biapy_config['DATA']['TEST']['PADDING'] = get_text(main_window.ui.DATA__TEST__PADDING__INPUT)
        if get_text(main_window.ui.DATA__TEST__MEDIAN_PADDING__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['MEDIAN_PADDING'] = True 
        biapy_config['DATA']['TEST']['RESOLUTION'] = get_text(main_window.ui.DATA__TEST__RESOLUTION__INPUT)
        if get_text(main_window.ui.DATA__TEST__ARGMAX_TO_OUTPUT__INPUT) == "Yes":
            biapy_config['DATA']['TEST']['ARGMAX_TO_OUTPUT'] = True

    if get_text(main_window.ui.DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT) == "Yes":
        biapy_config['DATA']['TEST']['FILTER_SAMPLES'] = {}
        biapy_config['DATA']['TEST']['FILTER_SAMPLES']['ENABLE'] = True
        try:
            biapy_config['DATA']['TEST']['FILTER_SAMPLES']['PROPS'] = ast.literal_eval(get_text(main_window.ui.DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT))
        except: 
            main_window.dialog_exec("There was an error with train data filter samples properties array field (DATA.TRAIN.FILTER_SAMPLES.PROPS). Please check its syntax!", reason="error")
            return True, False
        try:
            biapy_config['DATA']['TEST']['FILTER_SAMPLES']['VALUES'] = ast.literal_eval(get_text(main_window.ui.DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT))
        except: 
            main_window.dialog_exec("There was an error with train data filter samples values array field (DATA.TRAIN.FILTER_SAMPLES.VALUES). Please check its syntax!", reason="error")
            return True, False
        try:
            biapy_config['DATA']['TEST']['FILTER_SAMPLES']['SIGNS'] = ast.literal_eval(get_text(main_window.ui.DATA__TEST__FILTER_SAMPLES__ENABLE__INPUT))
        except: 
            main_window.dialog_exec("There was an error with train data filter samples signs array field (DATA.TRAIN.FILTER_SAMPLES.SIGNS). Please check its syntax!", reason="error")
            return True, False

    # Model definition
    biapy_config['MODEL'] = {}
    if not (get_text(main_window.ui.LOAD_PRETRAINED_MODEL__INPUT) == "Yes" 
        and get_text(main_window.ui.MODEL__SOURCE__INPUT) != "I have a model trained with BiaPy"
    ):
        model_name = main_window.cfg.translate_model_names(get_text(main_window.ui.MODEL__ARCHITECTURE__INPUT), get_text(main_window.ui.PROBLEM__NDIM__INPUT))
        biapy_config['MODEL']['ARCHITECTURE'] = model_name
        if model_name in ['unet', 'resunet', 'resunet++', 'seunet', 'attention_unet']:
            try:
                biapy_config['MODEL']['FEATURE_MAPS'] = ast.literal_eval(get_text(main_window.ui.MODEL__FEATURE_MAPS__INPUT))
            except: 
                main_window.dialog_exec("There was an error in model's feature maps field (MODEL.FEATURE_MAPS). Please check its syntax!", reason="error")
                return True, False
            try:
                biapy_config['MODEL']['DROPOUT_VALUES'] = ast.literal_eval(get_text(main_window.ui.MODEL__DROPOUT_VALUES__INPUT)) 
            except: 
                main_window.dialog_exec("There was an error in model's dropout values field (MODEL.DROPOUT_VALUES). Please check its syntax!", reason="error")
                return True, False
            if get_text(main_window.ui.MODEL__NORMALIZATION__INPUT) != "bn":
                biapy_config['MODEL']['NORMALIZATION'] = get_text(main_window.ui.MODEL__NORMALIZATION__INPUT) 
            if int(get_text(main_window.ui.MODEL__KERNEL_SIZE__INPUT)) != 3:
                biapy_config['MODEL']['KERNEL_SIZE'] = int(get_text(main_window.ui.MODEL__KERNEL_SIZE__INPUT))
            if get_text(main_window.ui.MODEL__UPSAMPLE_LAYER__INPUT) != "convtranspose":
                biapy_config['MODEL']['UPSAMPLE_LAYER'] = get_text(main_window.ui.MODEL__UPSAMPLE_LAYER__INPUT) 
            if get_text(main_window.ui.MODEL__ACTIVATION__INPUT) != 'elu':
                biapy_config['MODEL']['ACTIVATION'] = get_text(main_window.ui.MODEL__ACTIVATION__INPUT)
            if get_text(main_window.ui.MODEL__LAST_ACTIVATION__INPUT) != 'sigmoid':
                biapy_config['MODEL']['LAST_ACTIVATION'] = get_text(main_window.ui.MODEL__LAST_ACTIVATION__INPUT)
            if get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "3D":
                try:
                    biapy_config['MODEL']['Z_DOWN'] = ast.literal_eval(get_text(main_window.ui.MODEL__Z_DOWN__INPUT)) 
                except: 
                    main_window.dialog_exec("There was an error in model's z axis downsampling  field (MODEL.Z_DOWN). Please check its syntax!", reason="error")
                    return True, False
            if get_text(main_window.ui.MODEL__ISOTROPY__INPUT) != "[True, True, True, True, True]":
                try:
                    biapy_config['MODEL']['ISOTROPY'] = ast.literal_eval(get_text(main_window.ui.MODEL__ISOTROPY__INPUT)) 
                except: 
                    main_window.dialog_exec("There was an error in model's isotropy field (MODEL.ISOTROPY). Please check its syntax!", reason="error")
                    return True, False
            if get_text(main_window.ui.MODEL__LAGER_IO__INPUT) == "Yes":
                biapy_config['MODEL']['LAGER_IO'] = True
            if workflow_key_name == "SUPER_RESOLUTION" and get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "3D": # SR
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
                biapy_config['MODEL']['UNETR_DEC_KERNEL_SIZE'] = int(get_text(main_window.ui.MODEL__UNETR_DEC_KERNEL_SIZE__INPUT))

            # MAE
            if model_name in "mae":
                biapy_config['MODEL']['MAE_MASK_TYPE'] = get_text(main_window.ui.MODEL__MAE_MASK_TYPE__INPUT)
                if get_text(main_window.ui.MODEL__MAE_MASK_TYPE__INPUT) == "random":
                    biapy_config['MODEL']['MAE_MASK_RATIO'] = float(get_text(main_window.ui.MODEL__MAE_MASK_RATIO__INPUT))
                biapy_config['MODEL']['MAE_DEC_HIDDEN_SIZE'] = int(get_text(main_window.ui.MODEL__MAE_DEC_HIDDEN_SIZE__INPUT)) 
                biapy_config['MODEL']['MAE_DEC_NUM_LAYERS'] = int(get_text(main_window.ui.MODEL__MAE_DEC_NUM_LAYERS__INPUT)) 
                biapy_config['MODEL']['MAE_DEC_NUM_HEADS'] = get_text(main_window.ui.MODEL__MAE_DEC_NUM_HEADS__INPUT)
                biapy_config['MODEL']['MAE_DEC_MLP_DIMS'] = get_text(main_window.ui.MODEL__MAE_DEC_MLP_DIMS__INPUT)

            # ConvNeXT 
            if model_name in "unext_v1":
                try:
                    biapy_config['MODEL']['CONVNEXT_LAYERS'] = ast.literal_eval(get_text(main_window.ui.MODEL__CONVNEXT_LAYERS__INPUT))
                except: 
                    main_window.dialog_exec("There was an error in model's convnext layers field (MODEL.CONVNEXT_LAYERS). Please check its syntax!", reason="error")
                    return True, False
                biapy_config['MODEL']['CONVNEXT_SD_PROB'] = float(get_text(main_window.ui.MODEL__CONVNEXT_SD_PROB__INPUT))
                biapy_config['MODEL']['CONVNEXT_LAYER_SCALE'] = float(get_text(main_window.ui.MODEL__CONVNEXT_LAYER_SCALE__INPUT))
                biapy_config['MODEL']['CONVNEXT_STEM_K_SIZE'] = int(get_text(main_window.ui.MODEL__CONVNEXT_STEM_K_SIZE__INPUT))

        if workflow_key_name in ["SEMANTIC_SEG","INSTANCE_SEG","DETECTION","CLASSIFICATION"]:
            classes = 2
            if workflow_key_name == "SEMANTIC_SEG" and int(get_text(main_window.ui.MODEL__N_CLASSES__INPUT)) != 2:
                classes = int(get_text(main_window.ui.MODEL__N_CLASSES__INPUT))
            elif workflow_key_name == "INSTANCE_SEG" and int(get_text(main_window.ui.MODEL__N_CLASSES__INST_SEG__INPUT)) != 2:
                classes = int(get_text(main_window.ui.MODEL__N_CLASSES__INST_SEG__INPUT))
            elif workflow_key_name == "DETECTION" and int(get_text(main_window.ui.MODEL__N_CLASSES__DET__INPUT)) != 2:
                classes = int(get_text(main_window.ui.MODEL__N_CLASSES__DET__INPUT))
            else: # CLASSIFICATION
                classes = int(get_text(main_window.ui.MODEL__N_CLASSES__CLS__INPUT))

            if classes == 1: 
                classes = 2
            biapy_config['MODEL']['N_CLASSES'] = classes
        
    if get_text(main_window.ui.LOAD_PRETRAINED_MODEL__INPUT) == "Yes":
        if get_text(main_window.ui.MODEL__SOURCE__INPUT) == "I have a model trained with BiaPy":
            biapy_config['MODEL']['LOAD_CHECKPOINT'] = True 
            biapy_config['MODEL']["SOURCE"] = "biapy"
            biapy_config['PATHS'] = {}
            if get_text(main_window.ui.PATHS__CHECKPOINT_FILE__INPUT) != "" and get_text(main_window.ui.PATHS__CHECKPOINT_FILE__INPUT) != "model_weights.pth":
                biapy_config['PATHS']['CHECKPOINT_FILE'] = get_text(main_window.ui.PATHS__CHECKPOINT_FILE__INPUT, strip=False)
            if int(get_text(main_window.ui.MODEL__SAVE_CKPT_FREQ__INPUT)) != -1:
                biapy_config['MODEL']['SAVE_CKPT_FREQ'] = int(get_text(main_window.ui.MODEL__SAVE_CKPT_FREQ__INPUT))
            if get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_EPOCH__INPUT) != "best_on_val":
                biapy_config['MODEL']['LOAD_CHECKPOINT_EPOCH'] = get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_EPOCH__INPUT)
            if get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_ONLY_WEIGHTS__INPUT) != "Yes":
                biapy_config['MODEL']['LOAD_CHECKPOINT_ONLY_WEIGHTS'] = get_text(main_window.ui.MODEL__LOAD_CHECKPOINT_ONLY_WEIGHTS__INPUT)
        else: # BMZ or Torchvision
            if get_text(main_window.ui.MODEL__BMZ__SOURCE_MODEL_ID__INPUT) != "":
                arr = get_text(main_window.ui.MODEL__BMZ__SOURCE_MODEL_ID__INPUT).split("(")
                model = arr[0].strip()
                if "BioImage Model Zoo" in arr[1]:
                    biapy_config['MODEL']["SOURCE"] = "bmz"
                    biapy_config['MODEL']['BMZ'] = {}
                    biapy_config['MODEL']['BMZ']['SOURCE_MODEL_ID'] = str(model)
                else:
                    biapy_config['MODEL']["SOURCE"] = "torchvision"
                    biapy_config['MODEL']['TORCHVISION_MODEL_NAME'] = str(model)
            else:
                main_window.dialog_exec("Please, select an external model by clicking on 'Check models' button in 'Generic options' window.", reason="error")
                return True, False
        
    # Set BMZ variables 
    if get_text(main_window.ui.MODEL__BMZ__EXPORT__ENABLE__INPUT) == "Yes":
        if "BMZ" not in biapy_config['MODEL']:
            biapy_config['MODEL']['BMZ'] = {}
        biapy_config['MODEL']['BMZ']["EXPORT"] = {}    
        biapy_config['MODEL']['BMZ']["EXPORT"]["ENABLE"] = True
        try:
            model_src = biapy_config['MODEL']['SOURCE']
        except: 
            model_src = "biapy"
        if model_src == "bmz" and get_text(main_window.ui.MODEL__BMZ__EXPORT__REUSE_BMZ_CONFIG__INPUT) == "Yes": 
            biapy_config['MODEL']['BMZ']["EXPORT"]["REUSE_BMZ_CONFIG"] = True 
        else:
            biapy_config['MODEL']['BMZ']["EXPORT"]["REUSE_BMZ_CONFIG"] = False
            biapy_config['MODEL']['BMZ']["EXPORT"]["MODEL_NAME"] = get_text(main_window.ui.MODEL__BMZ__EXPORT__MODEL_NAME__INPUT)
            biapy_config['MODEL']['BMZ']["EXPORT"]["DESCRIPTION"] = get_text(main_window.ui.MODEL__BMZ__EXPORT__DESCRIPTION__INPUT)
            biapy_config['MODEL']['BMZ']["EXPORT"]["LICENSE"] = get_text(main_window.ui.MODEL__BMZ__EXPORT__LICENSE__INPUT)
            biapy_config['MODEL']['BMZ']["EXPORT"]["MODEL_VERSION"] = get_text(main_window.ui.MODEL__BMZ__EXPORT__MODEL_VERSION__INPUT)
            if get_text(main_window.ui.MODEL_AUTOGENERATE_DOC_INPUT) == "No" and get_text(main_window.ui.MODEL__BMZ__EXPORT__DOCUMENTATION__INPUT) != "":
                biapy_config['MODEL']['BMZ']["EXPORT"]["DOCUMENTATION"] = get_text(main_window.ui.MODEL__BMZ__EXPORT__DOCUMENTATION__INPUT)                
            if get_text(main_window.ui.MODEL__BMZ__EXPORT__AUTHORS__INPUT) != "":
                try:
                    biapy_config['MODEL']['BMZ']["EXPORT"]["AUTHORS"] = ast.literal_eval(get_text(main_window.ui.MODEL__BMZ__EXPORT__AUTHORS__INPUT))
                except:
                    main_window.dialog_exec("There was an error with BMZ authors field (MODEL.BMZ.EXPORT.AUTHORS). Please check its syntax!", reason="error")
                    return True, False
            if get_text(main_window.ui.MODEL__BMZ__EXPORT__TAGS__INPUT) != "":
                try:
                    biapy_config['MODEL']['BMZ']["EXPORT"]["TAGS"] = ast.literal_eval(get_text(main_window.ui.MODEL__BMZ__EXPORT__TAGS__INPUT))
                except: 
                    main_window.dialog_exec("There was an error with BMZ tags field (MODEL.BMZ.EXPORT.TAGS). Please check its syntax!", reason="error")
                    return True, False
            if get_text(main_window.ui.MODEL__BMZ__EXPORT__CITE__INPUT) != "":
                try:
                    biapy_config['MODEL']['BMZ']["EXPORT"]["CITE"] = ast.literal_eval(get_text(main_window.ui.MODEL__BMZ__EXPORT__CITE__INPUT))
                except:
                    main_window.dialog_exec("There was an error with BMZ citation field (MODEL.BMZ.EXPORT.CITE). Please check its syntax!", reason="error")
                    return True, False
            if get_text(main_window.ui.MODEL__BMZ__EXPORT__DATASET_INFO__INPUT) != "":
                try:
                    biapy_config['MODEL']['BMZ']["EXPORT"]["DATASET_INFO"] = ast.literal_eval(get_text(main_window.ui.MODEL__BMZ__EXPORT__DATASET_INFO__INPUT))
                except:
                    main_window.dialog_exec("There was an error with BMZ citation field (MODEL.BMZ.EXPORT.DATASET_INFO). Please check its syntax!", reason="error")
                    return True, False

    # Loss
    loss_name = main_window.cfg.translate_names(get_text(main_window.ui.LOSS__TYPE__INPUT), key_str="losses")
    biapy_config['LOSS'] = {}
    biapy_config['LOSS']['TYPE'] = loss_name
    if biapy_config['LOSS']['TYPE'] == "W_CE_DICE":
        try:
            biapy_config['LOSS']['WEIGHTS'] = ast.literal_eval(get_text(main_window.ui.LOSS__WEIGHTS__INPUT)) 
        except:
            main_window.dialog_exec("There was an error with loss weights field (LOSS.WEIGHTS). Please check its syntax!", reason="error")
            return True, False
    biapy_config['LOSS']['CLASS_REBALANCE'] = True if get_text(main_window.ui.LOSS__CLASS_REBALANCE__INPUT) == "Yes" else False
    
    # Metrics 
    biapy_config['TRAIN'] = {}
    try:
        biapy_config['TRAIN']['METRICS'] = ast.literal_eval(get_text(main_window.ui.TRAIN__METRICS__INPUT))
    except:
        main_window.dialog_exec("There was an error with train metrics field (TRAIN.METRICS). Please check its syntax!", reason="error")
        return True, False

    # Training phase
    biapy_config['TRAIN'] = {}
    if get_text(main_window.ui.TRAIN__ENABLE__INPUT) == "Yes":
        biapy_config['TRAIN']['ENABLE'] = True 
        biapy_config['TRAIN']['OPTIMIZER'] = get_text(main_window.ui.TRAIN__OPTIMIZER__INPUT)
        biapy_config['TRAIN']['LR'] = float(get_text(main_window.ui.TRAIN__LR__INPUT))
        if biapy_config['TRAIN']['OPTIMIZER'] == "ADAMW":
            biapy_config['TRAIN']['W_DECAY'] = float(get_text(main_window.ui.TRAIN__W_DECAY__INPUT))
            biapy_config['TRAIN']['OPT_BETAS'] = get_text(main_window.ui.TRAIN__OPT_BETAS__INPUT)
        if get_text(main_window.ui.TRAIN__BATCH_SIZE__CALCULATION__INPUT) == "Yes":
            try:
                patch_size = ast.literal_eval(biapy_config['DATA']['PATCH_SIZE'])
            except:
                main_window.dialog_exec("There was an error with the patch size formating (DATA.PATCH_SIZE). Please check its syntax!", reason="error")
                return True, False
            
            network_base_memory = 4000 # High value here to prevent crash  
                                        
            if biapy_config["PROBLEM"]["TYPE"] == "CLASSIFICATION":
                y_channels = 0
            else:
                if biapy_config["PROBLEM"]["TYPE"] in [
                    "DENOISING",
                    "SUPER_RESOLUTION",
                    "IMAGE_TO_IMAGE"
                ]:
                    y_channels = patch_size[-1]   
                elif biapy_config["PROBLEM"]["TYPE"] == "INSTANCE_SEG":
                    y_channels = 2 # As we are using a BC approach in the Wizard 
                else:
                    y_channels = 1

            channels_per_sample = {
                "x": patch_size[-1], 
                "y": y_channels, 
                }
            
            if biapy_config["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
                y_upsampling = biapy_config["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"]
            else:
                y_upsampling = (1,1) if biapy_config['PROBLEM']['NDIM'] == "2D" else (1,1,1)
                
            try:
                total_samples = len(next(os.walk(biapy_config['DATA']['TRAIN']['PATH']))[2]) 
            except:
                total_samples = 1
            if biapy_config["PROBLEM"]["TYPE"] not in ["SUPER_RESOLUTION", "DENOISING"]:
                max_batch_size_allowed = 16 if biapy_config['PROBLEM']['NDIM'] == "2D" else 4   
            else:
                max_batch_size_allowed = 64

            if total_samples == 1:
                batch_size = 1
            else:    
                sample_info = {
                    "DATA.TRAIN.PATH": {
                        'total_samples': total_samples,
                        'crop_shape': patch_size,
                        'dir_name': biapy_config['DATA']['TRAIN']['PATH'],
                    }
                }
                try:
                    masking = (
                        biapy_config["PROBLEM"]["TYPE"] == "SELF_SUPERVISED" 
                        and biapy_config['PROBLEM']['SELF_SUPERVISED']['PRETEXT_TASK'] == "masking"
                        )
                except:
                    masking = False
                if (
                    biapy_config["PROBLEM"]["TYPE"] != "DENOISING" 
                    and not masking
                ):
                    try:
                        total_samples = len(next(os.walk(biapy_config['DATA']['TRAIN']['GT_PATH']))[2]) 
                    except:
                        total_samples = 1
                    sample_info["DATA.TRAIN.GT_PATH"] = {
                        'total_samples': total_samples,
                        'crop_shape': patch_size,
                        'dir_name': biapy_config['DATA']['TRAIN']['GT_PATH'],
                    }    
                batch_size = batch_size_calculator(
                    gpu_info=main_window.cfg.settings['GPUs'], 
                    sample_info=sample_info, 
                    patch_size=patch_size,
                    channels_per_sample=channels_per_sample,
                    network_base_memory=network_base_memory, 
                    y_upsampling=y_upsampling,
                    max_batch_size_allowed=max_batch_size_allowed,
                    )
            biapy_config['TRAIN']['BATCH_SIZE'] = batch_size
        else:
            biapy_config['TRAIN']['BATCH_SIZE'] = int(get_text(main_window.ui.TRAIN__BATCH_SIZE__INPUT))
        biapy_config['TRAIN']['EPOCHS'] = int(get_text(main_window.ui.TRAIN__EPOCHS__INPUT)) 
        if int(get_text(main_window.ui.TRAIN__ACCUM_ITER__INPUT)) != 1:
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

        # Set LR scheduler by default if default epochs and patience 
        if biapy_config['TRAIN']['EPOCHS'] == 150 and biapy_config['TRAIN']['PATIENCE'] == 50 and get_text(main_window.ui.TRAIN__LR_SCHEDULER__NAME__INPUT) == "":
            if "LR_SCHEDULER" not in biapy_config['TRAIN']:
                biapy_config['TRAIN']['LR_SCHEDULER'] = {}
            biapy_config['TRAIN']['LR_SCHEDULER']['NAME'] = 'warmupcosine'
            biapy_config['TRAIN']['LR_SCHEDULER']['MIN_LR'] = 1.E-5
            biapy_config['TRAIN']['LR_SCHEDULER']['WARMUP_COSINE_DECAY_EPOCHS'] = 10
            
        # Callbacks
        # if get_text(main_window.ui.TRAIN__PROFILER__INPUT) == "Yes": 
        #     biapy_config['TRAIN']['PROFILER'] = True 
        #     biapy_config['TRAIN']['PROFILER_BATCH_RANGE'] = get_text(main_window.ui.TRAIN__PROFILER_BATCH_RANGE__INPUT)
        
        if get_text(main_window.ui.TRAIN__VERBOSE__INPUT) == "Yes":
            biapy_config['TRAIN']['VERBOSE'] = True 
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
            biapy_config['TEST']['AUGMENTATION_MODE'] = get_text(main_window.ui.TEST__AUGMENTATION_MODE__INPUT) 
        if get_text(main_window.ui.TEST__REUSE_PREDICTIONS__INPUT) == "Yes" :
            biapy_config['TEST']['REUSE_PREDICTIONS'] = True 
        if get_text(main_window.ui.TEST__ANALIZE_2D_IMGS_AS_3D_STACK__INPUT) == "Yes" and get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "2D":
            biapy_config['TEST']['ANALIZE_2D_IMGS_AS_3D_STACK'] = True

        if get_text(main_window.ui.TEST__FULL_IMG__INPUT) == "Yes" and get_text(main_window.ui.PROBLEM__NDIM__INPUT) == "2D":
            biapy_config['TEST']['FULL_IMG'] = True 

        if get_text(main_window.ui.TEST__BY_CHUNKS__ENABLE__INPUT) == "Yes":
            biapy_config['TEST']['BY_CHUNKS'] = {}
            biapy_config['TEST']['BY_CHUNKS']['ENABLE'] = True
            biapy_config['TEST']['BY_CHUNKS']['FORMAT'] = get_text(main_window.ui.TEST__BY_CHUNKS__FORMAT__INPUT)
            if get_text(main_window.ui.TEST__BY_CHUNKS__SAVE_OUT_TIF__INPUT) == "Yes":
                biapy_config['TEST']['BY_CHUNKS']['SAVE_OUT_TIF'] = True  
            biapy_config['TEST']['BY_CHUNKS']['FLUSH_EACH'] = int(get_text(main_window.ui.TEST__BY_CHUNKS__FLUSH_EACH__INPUT))
            biapy_config['TEST']['BY_CHUNKS']['INPUT_IMG_AXES_ORDER'] = get_text(main_window.ui.TEST__BY_CHUNKS__INPUT_IMG_AXES_ORDER__INPUT)
            biapy_config['TEST']['BY_CHUNKS']['INPUT_MASK_AXES_ORDER'] = get_text(main_window.ui.TEST__BY_CHUNKS__INPUT_MASK_AXES_ORDER__INPUT)
            if get_text(main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA__INPUT) == "Yes":
                biapy_config['TEST']['BY_CHUNKS']['INPUT_ZARR_MULTIPLE_DATA'] = True
                biapy_config['TEST']['BY_CHUNKS']['INPUT_ZARR_MULTIPLE_DATA_RAW_PATH'] = get_text(main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_RAW_PATH__INPUT)
                biapy_config['TEST']['BY_CHUNKS']['INPUT_ZARR_MULTIPLE_DATA_GT_PATH'] = get_text(main_window.ui.TEST__BY_CHUNKS__INPUT_ZARR_MULTIPLE_DATA_GT_PATH__INPUT)
            if get_text(main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__ENABLE__INPUT) == "Yes":
                biapy_config['TEST']['BY_CHUNKS']['WORKFLOW_PROCESS'] = {}
                biapy_config['TEST']['BY_CHUNKS']['WORKFLOW_PROCESS']['ENABLE'] = True
                biapy_config['TEST']['BY_CHUNKS']['WORKFLOW_PROCESS']['TYPE'] = get_text(main_window.ui.TEST__BY_CHUNKS__WORKFLOW_PROCESS__TYPE__INPUT)

        ### Instance segmentation
        if workflow_key_name == "INSTANCE_SEG":
            biapy_config['TEST']['MATCHING_STATS'] = True if get_text(main_window.ui.TEST__MATCHING_STATS__INPUT) == "Yes" else False
            try: 
                biapy_config['TEST']['MATCHING_STATS_THS'] = ast.literal_eval(get_text(main_window.ui.TEST__MATCHING_STATS_THS__INPUT)) 
            except:
                main_window.dialog_exec("There was an error with test matching start thresholds field (TEST.MATCHING_STATS_THS). Please check its syntax!", reason="error")
                return True, False
            if get_text(main_window.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT) != "[0.3]":
                try:
                    biapy_config['TEST']['MATCHING_STATS_THS_COLORED_IMG'] = ast.literal_eval(get_text(main_window.ui.TEST__MATCHING_STATS_THS_COLORED_IMG__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test matching start thresholds colored image field (TEST.MATCHING_STATS_THS_COLORED_IMG). Please check its syntax!", reason="error")
                    return True, False

        ### Detection
        elif workflow_key_name == "DETECTION":
            biapy_config['TEST']['DET_POINT_CREATION_FUNCTION'] = get_text(main_window.ui.TEST__DET_POINT_CREATION_FUNCTION__INPUT)
            biapy_config['TEST']['DET_MIN_TH_TO_BE_PEAK'] = float(get_text(main_window.ui.TEST__DET_MIN_TH_TO_BE_PEAK__INPUT))
            biapy_config['TEST']['DET_EXCLUDE_BORDER'] = True if get_text(main_window.ui.TEST__DET_EXCLUDE_BORDER__INPUT) == "Yes" else False
            biapy_config['TEST']['DET_TOLERANCE'] = int(get_text(main_window.ui.TEST__DET_TOLERANCE__INPUT))
            if get_text(main_window.ui.TEST__DET_IGNORE_POINTS_OUTSIDE_BOX__INPUT) != "[]":
                try:
                    biapy_config['TEST']['DET_IGNORE_POINTS_OUTSIDE_BOX'] = ast.literal_eval(get_text(main_window.ui.TEST__DET_IGNORE_POINTS_OUTSIDE_BOX__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test detection ignore points outside box field (TEST.DET_IGNORE_POINTS_OUTSIDE_BOX). Please check its syntax!", reason="error")
                    return True, False
            if get_text(main_window.ui.TEST__DET_POINT_CREATION_FUNCTION__INPUT) == "blob_log":
                biapy_config['TEST']['DET_BLOB_LOG_MIN_SIGMA'] = int(get_text(main_window.ui.TEST__DET_BLOB_LOG_MIN_SIGMA__INPUT))    
                biapy_config['TEST']['DET_BLOB_LOG_MAX_SIGMA'] = int(get_text(main_window.ui.TEST__DET_BLOB_LOG_MAX_SIGMA__INPUT)) 
                biapy_config['TEST']['DET_BLOB_LOG_NUM_SIGMA'] = int(get_text(main_window.ui.TEST__DET_BLOB_LOG_NUM_SIGMA__INPUT)) 

        # Post-processing
        biapy_config['TEST']['POST_PROCESSING'] = {}
        ### Semantic segmentation
        if workflow_key_name == "SEMANTIC_SEG":
            if get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER__SEM_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER'] = True
                try:
                    biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER_AXIS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__SEM_SEG__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test post processing median filter axis field (TEST.POST_PROCESSING.MEDIAN_FILTER_AXIS). Please check its syntax!", reason="error")
                    return True, False
                try:
                    biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER_SIZE'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__SEM_SEG__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test post processing median filter size field (TEST.POST_PROCESSING.MEDIAN_FILTER_SIZE). Please check its syntax!", reason="error")
                    return True, False
        ### Instance segmentation
        elif workflow_key_name == "INSTANCE_SEG":
            if get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER__INST_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER'] = True
                try:
                    biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER_AXIS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INST_SEG__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test post processing median filter axis field (TEST.POST_PROCESSING.MEDIAN_FILTER_AXIS). Please check its syntax!", reason="error")
                    return True, False
                try:
                    biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER_SIZE'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__INST_SEG__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test post processing median filter size field (TEST.POST_PROCESSING.MEDIAN_FILTER_SIZE). Please check its syntax!", reason="error")
                    return True, False
            if problem_channels in ["BC", "BCM"] and get_text(main_window.ui.TEST__POST_PROCESSING__VORONOI_ON_MASK__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_ON_MASK'] = True 
                biapy_config['TEST']['POST_PROCESSING']['VORONOI_TH'] = float(get_text(main_window.ui.TEST__POST_PROCESSING__VORONOI_TH__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INST_SEG__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES'] = {}
                biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['ENABLE'] = True
                if get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INST_SEG__INPUT) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES'] = {}
                    biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['ENABLE'] = True
                    try:
                        biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['PROPS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INST_SEG__INPUT) ) 
                    except:
                        main_window.dialog_exec("There was an error with test post processing measure properties, removing my properties, in properties array field (TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.PROPS). Please check its syntax!", reason="error")
                        return True, False
                    try:
                        biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['VALUES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INST_SEG__INPUT) ) 
                    except:
                        main_window.dialog_exec("There was an error with test post processing measure properties, removing my properties, in values array field (TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.VALUES). Please check its syntax!", reason="error")
                        return True, False
                    try:
                        biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['SIGNS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INST_SEG__INPUT) ) 
                    except:
                        main_window.dialog_exec("There was an error with test post processing measure properties, removing my properties, in signs array field (TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.SIGNS). Please check its syntax!", reason="error")
                        return True, False
            if problem_channels == "BP":
                if int(get_text(main_window.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT)) != -1:
                    biapy_config['TEST']['POST_PROCESSING']['REPARE_LARGE_BLOBS_SIZE'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__REPARE_LARGE_BLOBS_SIZE__INPUT))
                if get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INST_SEG__INPUT) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                    biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INST_SEG__INPUT))
        ### Detection
        elif workflow_key_name == "DETECTION":
            if get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER'] = True
                try:
                    biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER_AXIS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__DET__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test post processing median filter axis field (TEST.POST_PROCESSING.MEDIAN_FILTER_AXIS). Please check its syntax!", reason="error")
                    return True, False
                try:
                    biapy_config['TEST']['POST_PROCESSING']['MEDIAN_FILTER_SIZE'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEDIAN_FILTER_SIZE__DET__INPUT))
                except:
                    main_window.dialog_exec("There was an error with test post processing median filter size field (TEST.POST_PROCESSING.MEDIAN_FILTER_SIZE). Please check its syntax!", reason="error")
                    return True, False

            if get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__DET__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS'] = True 
                biapy_config['TEST']['POST_PROCESSING']['REMOVE_CLOSE_POINTS_RADIUS'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__DET__INPUT))
            if get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED__INPUT) == "Yes":
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED'] = True
                try:
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_FIRST_DILATION'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_FIRST_DILATION__INPUT) )
                except:
                    main_window.dialog_exec("There was an error with test post processing detection watershed first dilation field (TEST.POST_PROCESSING.DET_WATERSHED_FIRST_DILATION). Please check its syntax!", reason="error")
                    return True, False
                try:
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_CLASSES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_CLASSES__INPUT) )
                except:
                    main_window.dialog_exec("There was an error with test post processing detection watershed donuts classes field (TEST.POST_PROCESSING.DET_WATERSHED_DONUTS_CLASSES). Please check its syntax!", reason="error")
                    return True, False
                try:
                    biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_PATCH'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_PATCH__INPUT) )
                except:
                    main_window.dialog_exec("There was an error with test post processing detection watershed donuts patch field (TEST.POST_PROCESSING.DET_WATERSHED_DONUTS_PATCH). Please check its syntax!", reason="error")
                    return True, False
                biapy_config['TEST']['POST_PROCESSING']['DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER'] = int(get_text(main_window.ui.TEST__POST_PROCESSING__DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER__INPUT)) 
                if get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__DET__INPUT) == "Yes":
                    biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES'] = {}
                    biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['ENABLE'] = True
                    if get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__DET__INPUT) == "Yes":
                        biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES'] = {}
                        biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['ENABLE'] = True
                        try:
                            biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['PROPS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__DET__INPUT) ) 
                        except:
                            main_window.dialog_exec("There was an error with test post processing measure properties, removing my properties, in properties array field (TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.PROPS). Please check its syntax!", reason="error")
                            return True, False
                        try:
                            biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['VALUES'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__DET__INPUT) ) 
                        except:
                            main_window.dialog_exec("There was an error with test post processing measure properties, removing my properties, in values array field (TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.VALUES). Please check its syntax!", reason="error")
                            return True, False
                        try:
                            biapy_config['TEST']['POST_PROCESSING']['MEASURE_PROPERTIES']['REMOVE_BY_PROPERTIES']['SIGNS'] = ast.literal_eval(get_text(main_window.ui.TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__DET__INPUT) ) 
                        except:
                            main_window.dialog_exec("There was an error with test post processing measure properties, removing my properties, in signs array field (TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.SIGNS). Please check its syntax!", reason="error")
                            return True, False
        if get_text(main_window.ui.TEST__POST_PROCESSING__APPLY_MASK__INPUT) == "Yes":
            biapy_config['TEST']['POST_PROCESSING']['APPLY_MASK'] = True
        if get_text(main_window.ui.TEST__POST_PROCESSING__CLEAR_BORDER__INPUT) == "Yes":
            biapy_config['TEST']['POST_PROCESSING']['CLEAR_BORDER'] = True

        if not biapy_config['TEST']['POST_PROCESSING']:
            del biapy_config['TEST']['POST_PROCESSING']
    else:
        biapy_config['TEST']['ENABLE'] = False

    # Imposed variables due to loaded pretrained model 
    if main_window.external_model_restrictions is not None:
        m=""
        for key, val in main_window.external_model_restrictions.items():
            if "PATCH_SIZE_C" in key:
                val = "PATCH_SIZE (channel)"
            m  += f"    - {key} : {val}\n"
        main_window.dialog_exec("The following variables will be set automatically as they are imposed by the pretrained model selected:\n"+m, 
            "inform_user")

        # Generate config from answers 
        model_restrictions = {}
        for key, value in main_window.external_model_restrictions.items():
            if value != -1:
                if isinstance(key, str):
                    if isinstance(value, tuple):
                        value = str(value)
                    create_dict_from_key(key, value, model_restrictions)
                else:
                    raise ValueError(f"Error found in config: {key}. Contact BiaPy team!")
        biapy_config = update_dict(biapy_config, model_restrictions)

    if not main_window.cfg.settings['yaml_config_filename'].endswith(".yaml") and not main_window.cfg.settings['yaml_config_filename'].endswith(".yml"):
        main_window.cfg.settings['yaml_config_filename'] = main_window.cfg.settings['yaml_config_filename']+".yaml"
        set_text(main_window.ui.goptions_yaml_name_input, main_window.cfg.settings['yaml_config_filename'])

    # Writing YAML file
    replace = True
    if os.path.exists(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename'])):
        main_window.yes_no_exec("The file '{}' already exists. Do you want to overwrite it?".format(main_window.cfg.settings['yaml_config_filename']))
        replace = True if main_window.yes_no.answer else False
        
    if replace:
        main_window.logger.info("Creating YAML file") 
        with open(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename']), 'w', encoding='utf8') as outfile:
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
    ofolder = os.path.join(ofolder, jobname)
    main_window.cfg.settings['biapy_cfg'] = Config(ofolder, jobname+"_1")

    # Create a temporal file with the configuration. In this process old key variables that the configuration file may have 
    # are automatically translated into the BiaPy version the GUI is running.
    with open(os.path.join(main_window.cfg.settings['yaml_config_file_path'], main_window.cfg.settings['yaml_config_filename']), "r", encoding='utf8') as stream:
        try:
            temp_cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            main_window.logger.error(exc)
            main_window.dialog_exec("There was a problem loading the .yaml config file", reason="error")
    temp_cfg = convert_old_model_cfg_to_current_version(temp_cfg)
    main_window.logger.info("Creating temporal input YAML file for converting possible old configuration") 
    tmp_cfg_file = os.path.join(main_window.log_info["log_dir"], "biapy_tmp.yaml")
    with open(tmp_cfg_file, 'w', encoding='utf8') as outfile:
        yaml.dump(temp_cfg, outfile, default_flow_style=False)

    # Merge loaded configuration with the YACS defaults to see if everything is correct or not 
    errors = ""
    try:
        main_window.cfg.settings['biapy_cfg']._C.merge_from_file(tmp_cfg_file)
        main_window.cfg.settings['biapy_cfg'] = main_window.cfg.settings['biapy_cfg'].get_cfg_defaults()
        check_configuration(main_window.cfg.settings['biapy_cfg'], jobname+"_1")
        
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
            "DATA__VAL__DETECTION_MASK_DIR__INPUT", "DATA__VAL__INSTANCE_CHANNELS_DIR__INPUT", 
            "DATA__VAL__INSTANCE_CHANNELS_MASK_DIR__INPUT", "DATA__VAL__SSL_SOURCE_DIR__INPUT", 
            "LOG__CHART_CREATION_FREQ__INPUT", "LOG__LOG_DIR__INPUT", "LOG__LOG_FILE_PREFIX__INPUT", 
            "LOG__TENSORBOARD_LOG_DIR__INPUT", "SYSTEM__NUM_GPUS__INPUT",

            # Handled with different names
            "MODEL__LOAD_CHECKPOINT__INPUT", "MODEL__SOURCE__INPUT", "MODEL__TORCHVISION_MODEL_NAME__INPUT",

            # Not used or decided to not insert in GUI
            "SYSTEM__PIN_MEM__INPUT", "TRAIN__CHECKPOINT_MONITOR__INPUT","DATA__VAL__DIST_EVAL__INPUT",
            "MODEL__VIT_MODEL__INPUT", "SYSTEM__DEVICE", "DATA__PREPROCESS__ZOOM", 
            "DATA__PREPROCESS__ZOOM__ENABLE", "DATA__PREPROCESS__ZOOM__ZOOM_FACTOR",
            "DATA__TRAIN__FILTER_SAMPLES__SIGNS", "DATA__FILTER_BY_IMAGE", "MODEL__LOAD_MODEL_FROM_CHECKPOINT__INPUT",
        ]
        
    def run(self):
        """
        Process of loading YAML file into GUI.
        """
        self.state_signal.emit(0)
        try:
            with open(self.yaml_file, "r", encoding='utf8') as stream:
                cfg_content = stream.read()
                tab_detected_mss = ""
                if '\t' in cfg_content:
                    tab_detected_mss = "WARNING: Tabs have been identified and substituted with two spaces. This error may be "+\
                        "attributed to this, so please eliminate them.\n"
                    cfg_content = cfg_content.replace('\t', '  ')
                try:
                    loaded_cfg = yaml.safe_load(cfg_content)
                except:
                    exc = traceback.format_exc()
                    self.main_window.logger.error(exc)
                    self.error_signal.emit(f"Error found reading YAML {self.yaml_file}.\nPlease check the file!", "unexpected_error")
                    self.state_signal.emit(1)
                    self.finished_signal.emit()
                    return 

            if loaded_cfg is None:
                self.error_signal.emit(f"The input config file seems to be empty", "error")
                self.state_signal.emit(1)
                self.finished_signal.emit()
                return  

            # Create a temporal file with the configuration. In this process old key variables that the configuration file may have 
            # are automatically translated into the BiaPy version the GUI is running.
            loaded_cfg = convert_old_model_cfg_to_current_version(loaded_cfg)
            self.main_window.logger.info("Creating temporal input YAML file for converting possible old configuration") 
            tmp_cfg_file = os.path.join(self.main_window.log_info["log_dir"], "biapy_tmp.yaml")
            with open(tmp_cfg_file, 'w', encoding='utf8') as outfile:
                yaml.dump(loaded_cfg, outfile, default_flow_style=False)

            self.main_window.logger.info(f"Loaded: {loaded_cfg}")

            # Load configuration file and check possible errors
            tmp_cfg = Config("/home/","jobname")
            errors = ""
            tmp_cfg._C.merge_from_file(tmp_cfg_file)
            tmp_cfg = tmp_cfg.get_cfg_defaults()
            check_configuration(tmp_cfg, get_text(self.main_window.ui.job_name_input), check_data_paths=False)
        
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
            elif work_id == "CLASSIFICATION":
                self.main_window.cfg.settings['selected_workflow'] = 6
            else: # IMAGE_TO_IMAGE
                self.main_window.cfg.settings['selected_workflow'] = 7
            move_between_workflows(self.main_window, self.main_window.cfg.settings['selected_workflow'], self.work_dim)
            
            # Preprocessing
            try:
                self.train_preprocessing = loaded_cfg['DATA']['PREPROCESS']['TRAIN']
            except:
                self.train_preprocessing = False
            try:
                self.val_preprocessing = loaded_cfg['DATA']['PREPROCESS']['VAL']
            except:
                self.val_preprocessing = False
            try:
                self.test_preprocessing = loaded_cfg['DATA']['PREPROCESS']['TEST']
            except:
                self.test_preprocessing = False

            # BiaPy pretrained model
            self.biapy_pretrained = (tmp_cfg['MODEL']['SOURCE'] == "biapy" and tmp_cfg['MODEL']['LOAD_CHECKPOINT'])

            # BMZ pretrained model
            self.bmz_pretrained = (tmp_cfg['MODEL']['SOURCE'] == "bmz" and tmp_cfg['MODEL']['BMZ']['SOURCE_MODEL_ID'] != "")

            # Torchvision pretrained model
            self.torchvision_pretrained = (tmp_cfg['MODEL']['SOURCE'] == "torchvision" and tmp_cfg['MODEL']['TORCHVISION_MODEL_NAME'] != "")
            
            # Go over configuration file
            errors, variables_set = self.analyze_dict(conf=loaded_cfg, sep="")
            
            self.main_window.logger.info("Variables updated: ")
            for i, k in enumerate(variables_set.keys()):
                self.main_window.logger.info("{}. {}: {}".format(i+1, k, variables_set[k]))
            if len(errors) > 0:
                self.main_window.logger.info("Errors: ")
                for i in range(len(errors)):
                    self.main_window.logger.info("{}. : {}".format(i+1, errors[i]))

            # Message for the user
            self.report_yaml_load_result.emit(errors, self.yaml_file)
        except:
            exc = traceback.format_exc()
            self.main_window.logger.error(exc)
            self.error_signal.emit(f"Error found loading YAML to the GUI:\n{exc}", "unexpected_error")
            self.state_signal.emit(1)
            self.finished_signal.emit()
        else:                 
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
                    variables_set = update_dict(variables_set,_vars)
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
                    elif v == 'C':
                        v = "Contours"
                    elif v == 'A':
                        v = "Affinities"
                    elif v == 'BCDv2':
                        v = "Binary mask + Contours + Distance map with background (experimental)"
                    elif v == 'BDv2':
                        v = "Binary mask + Distance map with background (experimental)"
                    else: 
                        v = "Distance map with background (experimental)"
                elif widget_name == "DATA__PREPROCESS__RESIZE__ORDER__INPUT":
                    if v == 0:
                        v = "Nearest-neighbor"
                    elif v == 1:
                        v = "Bi-linear"
                    elif v == 2:
                        v = "Bi-quadratic"
                    elif v == 3:
                        v = "Bi-cubic"
                    elif v == 4:
                        v = "Bi-quartic"
                    elif v == 5:
                        v = "Bi-quintic"
                    else:
                        v = "Bi-linear"
                elif widget_name == "DATA__PATCH_SIZE__INPUT":
                    other_widgets_to_set.append("DATA__PATCH_SIZE__TEST__INPUT")
                    other_widgets_values_to_set.append(v)
                    # Update test padding, as that is set to other value but (0,0) depending on the batch size through the GUI.
                    patch_size = ast.literal_eval(v)
                    padding = str(tuple([x//6 for x in patch_size[:-1]]))
                    other_widgets_to_set.append("DATA__TEST__PADDING__INPUT")
                    other_widgets_values_to_set.append(padding)
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
                elif widget_name == "LOSS__TYPE__INPUT":    
                    v = self.main_window.cfg.translate_names(v, "losses", inv=True)
                elif widget_name == "MODEL__UNET_SR_UPSAMPLE_POSITION__INPUT":
                    v = "Before model" if v == "pre" else "After model"              
                elif widget_name == "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__INPUT":
                    widget_name = "TEST__POST_PROCESSING__MEASURE_PROPERTIES__ENABLE__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__INPUT":
                    widget_name = "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__ENABLE__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__PROPS__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__INPUT":
                    widget_name = "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__VALUES__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__MEASURE_PROPERTIES__REMOVE_BY_PROPERTIES__SIGNS__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__REMOVE_CLOSE_POINTS_RADIUS__{}__INPUT".format(self.workflow_str)
                elif widget_name in ["MODEL__ACTIVATION__INPUT", "MODEL__UNETR_DEC_ACTIVATION__INPUT"]:
                    v = v.lower()
                elif widget_name == "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__TEST__INPUT":
                    widget_name = "DATA__PREPROCESS__MEDIAN_BLUR__KERNEL_SIZE__{}__INPUT".format(self.workflow_str)
                elif widget_name == "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__INPUT":
                    widget_name = "TEST__POST_PROCESSING__MEDIAN_FILTER_AXIS__{}__INPUT".format(self.workflow_str)
                elif widget_name == "MODEL__SOURCE__INPUT":
                    if self.biapy_pretrained: 
                        v = "I have a model trained with BiaPy" 
                        other_widgets_to_set.append("LOAD_PRETRAINED_MODEL__INPUT")
                        other_widgets_values_to_set.append("Yes") 
                    elif self.bmz_pretrained:
                        v = "I want to check other online sources"
                        other_widgets_to_set.append("LOAD_PRETRAINED_MODEL__INPUT")
                        other_widgets_values_to_set.append("Yes") 
                    elif self.torchvision_pretrained:
                        v = "I want to check other online sources"
                        other_widgets_to_set.append("LOAD_PRETRAINED_MODEL__INPUT")
                        other_widgets_values_to_set.append("Yes") 
                elif widget_name == "MODEL__LOAD_CHECKPOINT__INPUT":
                    if self.biapy_pretrained:
                        other_widgets_to_set.append("LOAD_PRETRAINED_MODEL__INPUT")
                        other_widgets_values_to_set.append("Yes") 
                elif widget_name == "MODEL__BMZ__SOURCE_MODEL_ID__INPUT":
                    if self.bmz_pretrained:
                        v += " (BioImage Model Zoo)"
                elif widget_name == "MODEL__TORCHVISION_MODEL_NAME__INPUT":
                    if self.torchvision_pretrained:
                        v += " (Torchvision)"
                    # Using same field as BMZ
                    other_widgets_to_set.append("MODEL__BMZ__SOURCE_MODEL_ID__INPUT")
                    other_widgets_values_to_set.append(v)                     
                elif widget_name == "MODEL__N_CLASSES__INPUT": 
                    other_widgets_to_set.append("MODEL__N_CLASSES__INST_SEG__INPUT")
                    other_widgets_values_to_set.append(v)    
                    other_widgets_to_set.append("MODEL__N_CLASSES__DET__INPUT")
                    other_widgets_values_to_set.append(v)    
                    other_widgets_to_set.append("MODEL__N_CLASSES__CLS__INPUT")
                    other_widgets_values_to_set.append(v)    

                if "DATA__PREPROCESS__" in widget_name and widget_name not in ["DATA__PREPROCESS__TRAIN__INPUT", \
                    "DATA__PREPROCESS__VAL__INPUT", "DATA__PREPROCESS__TEST__INPUT"]:
                    if self.train_preprocessing or self.val_preprocessing:
                        if self.test_preprocessing:
                            aux = widget_name if "__TEST" in widget_name else widget_name.replace("__INPUT", "__TEST__INPUT")
                            other_widgets_to_set.append(aux)
                            other_widgets_values_to_set.append(v)
                    else:
                        if self.test_preprocessing:
                            if "__TEST" not in widget_name:
                                widget_name = widget_name.replace("__INPUT", "__TEST__INPUT")

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
                            variables_set[x] = y
                            self.main_window.logger.info("Setting {} : {} ({})".format(x, y, k))
                        
        return errors, variables_set

def get_git_revision_short_hash(main_window) -> str:
    sha = None 
    vtag = None
    try:
        process = subprocess.Popen(["git", "ls-remote", main_window.cfg.settings['biapy_gui_github']], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        sha = re.split(r'\t+', stdout.decode('ascii'))[0]
        vtag = str(re.split(r'\t+', stdout.decode('ascii'))[-1]).replace("refs/tags/","").replace('^{}',"").replace('\n',"")   
    except Exception: 
        exc = traceback.format_exc()
        main_window.logger.error("There was an error getting BiaPy-GUI latest version (attempt 1)")
        main_window.logger.error(exc)

    try: 
        vtag = Version(vtag)
    except Exception:
        exc = traceback.format_exc()
        main_window.logger.error(f"There was an error converting the vtag into Version object. vtag is {vtag}")
        main_window.logger.error(exc) 

    if vtag is None:
        try:
            import requests
            response = requests.get("https://api.github.com/repos/BiaPyX/BiaPy-GUI/releases/latest")
            vtag = Version(response.json()["name"].split(' ')[-1])
        except Exception: 
            exc = traceback.format_exc()
            main_window.logger.error("There was an error getting BiaPy-GUI latest version (attempt 2)")
            main_window.logger.error(exc)

    if vtag is None:
        main_window.logger.info("Setting finally the version of the current GUI because other attempts failed. "
                                "Please, report this issue with BiaPy developers so they can fix it.")
        vtag = main_window.cfg.settings["biapy_gui_version"]

    return sha, vtag 
        
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

def create_dict_from_key(cfg_key, value, out_cfg):
    keys = cfg_key.split(".")
    if keys[0] not in out_cfg:
        out_cfg[keys[0]] = {}
    if len(keys) == 2:
        out_cfg[keys[0]][keys[1]] = value    
    else:
        create_dict_from_key(".".join(keys[1:]), value, out_cfg[keys[0]])  


# Extracted from: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
def is_path_exists_or_creatable(pathname: str) -> bool:
    '''
    `True` if the passed pathname is a valid pathname for the current OS _and_
    either currently exists or is hypothetically creatable; `False` otherwise.

    This function is guaranteed to _never_ raise exceptions.
    '''
    try:
        # To prevent "os" module calls from raising undesirable exceptions on
        # invalid pathnames, is_pathname_valid() is explicitly called first.
        return is_pathname_valid(pathname) and (
            os.path.exists(pathname) or is_path_creatable(pathname))
    # Report failure on non-fatal filesystem complaints (e.g., connection
    # timeouts, permissions issues) implying this path to be inaccessible. All
    # other exceptions are unrelated fatal issues and should not be caught here.
    except OSError:
        return False

# Extracted from: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
def is_path_creatable(pathname: str) -> bool:
    '''
    `True` if the current user has sufficient permissions to create the passed
    pathname; `False` otherwise.
    '''
    # Parent directory of the passed path. If empty, we substitute the current
    # working directory (CWD) instead.
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)

# Sadly, Python fails to provide the following magic number for us.
ERROR_INVALID_NAME = 123
'''
Windows-specific error code indicating an invalid pathname.

See Also
----------
https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
    Official listing of all such codes.
'''

# Extracted from: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
def is_pathname_valid(pathname: str) -> bool:
    '''
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    '''
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)   # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True
    # If any other exception was raised, this is an unrelated fatal issue
    # (e.g., a bug). Permit this exception to unwind the call stack.
    #
    # Did we mention this should be shipped with Python already?


def check_supported_container_versions(gui_version, logger):
    """
    Reads BiaPy's landing page, in the GUI history, to find the containers supported for this version of the GUI. 
    """
    compatible_versions = []
    try:
        # Read the page 
        response = urlopen('https://biapyx.github.io/GUI_versions/', context=ssl.create_default_context(cafile=certifi.where()))

        # Parse it 
        soup = BeautifulSoup(response.read(), from_encoding=response.headers.get_content_charset(), features="html.parser")
        find_version = soup.find_all(string=re.compile(str(gui_version)))
        if len(find_version) == 0:
            print("Version not found in landing page...")
        else:
            version_row = find_version[0].parent.parent
            container_table = version_row.find("table", attrs={"class": "styled-table_inside"})
            compatible_versions_td = container_table.find_all("td")
            for version in compatible_versions_td:
                for child in version.children:
                    if "v" in child.text:
                        try:
                            compatible_versions.append(Version(child.text))
                        except: 
                            pass    
        return compatible_versions
    except:
        exc = traceback.format_exc()
        logger.error(exc)
        return compatible_versions
    
def save_biapy_config(main_window, data, biapy_version=""): 
    """
    Save BiaPy configuration.
    
    Parameters
    ----------
    main_window : QMainWindow
        Main window of the application.
    
    data: dict
        Data dict to save.

    biapy_version : str, optional
        Data version to save if there is no one in the config file. 
    """    
    try:
        with open(main_window.log_info["config_file"], 'r') as file:
            old_data = json.load(file)
    except:
        old_data = {}
    old_data = update_dict(old_data, data)

    if biapy_version != "":
        if "GUI_VERSION" not in old_data:
            old_data["GUI_VERSION"] = biapy_version
        elif "GUI_VERSION" in old_data:
            try:
                file_version = Version(old_data["GUI_VERSION"])
                if file_version < biapy_version:
                    old_data["GUI_VERSION"] = biapy_version
            except:
                old_data["GUI_VERSION"] = biapy_version 

    with open(main_window.log_info["config_file"], "w") as outfile:
        json.dump(old_data, outfile, indent=4)

def update_dict(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d