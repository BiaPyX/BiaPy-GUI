from __future__ import annotations
import os
import errno
import sys
import traceback
import yaml
import queue
import subprocess
import re
import pooch
import json
import numpy as np
import certifi
import ssl
import tempfile
from pathlib import PurePath, Path, PureWindowsPath
from packaging.version import Version
from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections.abc
from logging import Logger
from typing import (
    Tuple,
    Dict,
    Optional,
    List,
)

from PySide6.QtCore import QObject, QThread, Signal, QRect, Qt
from PySide6.QtWidgets import QFileDialog, QComboBox, QLineEdit, QLabel, QWidget, QFrame, QStyle
from PySide6.QtGui import QColor

import main
from biapy.biapy_config import Config
from biapy.biapy_check_configuration import (
    check_configuration,
    check_torchvision_available_models,
    convert_old_model_cfg_to_current_version,
)
from biapy.biapy_aux_functions import (
    check_bmz_model_compatibility_in_GUI,
    check_images,
    check_csv_files,
    check_classification_images,
    check_model_restrictions,
)


def examine(main_window: main.MainWindow, save_in_obj_tag: Optional[str] = None, is_file: bool = True) -> str:
    """
    Find an item in disk. Can be a file or a directory.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    save_in_obj_tag : str
        Name of the widget to set the item's name into.

    is_file : bool, optional
        Whether the item to find is a file or a directory.
    """
    if not is_file:
        out = QFileDialog.getExistingDirectory(main_window, "Select a directory")
    else:
        out = QFileDialog.getOpenFileName()[0]

    if out == "":
        return out  # If no file was selected

    if save_in_obj_tag is not None:
        getattr(main_window.ui, save_in_obj_tag).setText(os.path.normpath(out))
        if save_in_obj_tag == "DATA__TRAIN__PATH__INPUT":
            main_window.cfg.settings["train_data_input_path"] = out
        elif save_in_obj_tag == "DATA__TRAIN__GT_PATH__INPUT":
            main_window.cfg.settings["train_data_gt_input_path"] = out
        elif save_in_obj_tag == "DATA__VAL__PATH__INPUT":
            main_window.cfg.settings["validation_data_input_path"] = out
        elif save_in_obj_tag == "DATA__VAL__GT_PATH__INPUT":
            main_window.cfg.settings["validation_data_gt_input_path"] = out
        elif save_in_obj_tag == "DATA__TEST__PATH__INPUT":
            main_window.cfg.settings["test_data_input_path"] = out
        elif save_in_obj_tag == "DATA__TEST__GT_PATH__INPUT":
            main_window.cfg.settings["test_data_gt_input_path"] = out

    return out


def wizard_path_changed(main_window: main.MainWindow, save_in_obj_tag: Optional[str] = None, is_file: bool = True):
    """
    Request a path for the user and advice the user that they need to check the paths again.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    save_in_obj_tag : str
        Name of the widget to set the item's name into.

    is_file : bool, optional
        Whether the item to find is a file or a directory.
    """

    # Reset path check
    if examine(main_window, save_in_obj_tag, is_file) != "":
        # Reset again colors and checks so the user must check again the folder
        key = next(
            iter(
                main_window.cfg.settings["wizard_variable_to_map"][
                    "Q" + str(main_window.cfg.settings["wizard_question_index"] + 1)
                ]
            )
        )
        if f"CHECKED {key}" in main_window.cfg.settings["wizard_answers"]:
            main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] = -1
            set_text(
                main_window.ui.wizard_data_checked_label,
                "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>",
            )
            index = main_window.cfg.settings["wizard_from_question_index_to_toc"][
                main_window.cfg.settings["wizard_question_index"]
            ]
            main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(0, 0, 0))


def check_data_from_path(main_window: main.MainWindow):
    """
    Checks available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
    and Torchvision.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.
    """
    if (
        main_window.cfg.settings["wizard_question_answered_index"][main_window.cfg.settings["wizard_question_index"]]
        == -1
    ):
        main_window.dialog_exec("Please select first a folder to check", reason="error")
    else:
        main_window.yes_no_exec(
            "This process may take a while as all images will be checked one by one. Are you sure you want to proceed?"
        )
        assert main_window.yes_no
        if main_window.yes_no.answer:

            def set_folder_checked(data_constraints, key, sample_info):
                main_window.logger.info(f"Data {key} checked!")
                if "data_constraints" not in main_window.cfg.settings["wizard_answers"]:
                    main_window.cfg.settings["wizard_answers"]["data_constraints"] = data_constraints
                else:
                    main_window.cfg.settings["wizard_answers"]["data_constraints"] = update_dict(
                        main_window.cfg.settings["wizard_answers"]["data_constraints"], data_constraints
                    )
                main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] = 1
                set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#04aa6d'>Data checked!</span>")

                if "sample_info" not in main_window.cfg.settings["wizard_answers"]:
                    main_window.cfg.settings["wizard_answers"]["sample_info"] = {}
                main_window.cfg.settings["wizard_answers"]["sample_info"][sample_info["dir_name"]] = sample_info

            main_window.logger.info("Checking data from path")
            dir_name = next(
                iter(
                    main_window.cfg.settings["wizard_variable_to_map"][
                        "Q" + str(main_window.cfg.settings["wizard_question_index"] + 1)
                    ]
                )
            )
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
    state_signal = Signal(int)

    # Signal to update variables in GUI
    update_var_signal = Signal(str, str)

    # Signal to indicate the main thread that there was an error
    error_signal = Signal(str, str)

    # Signal to send a message to the user about the result of model checking
    add_model_card_signal = Signal(int, dict)

    # Signal to send a message to the user about the result of model checking
    report_path_check_result = Signal(dict, str, dict)

    # Signal to indicate the main thread that the worker has finished
    finished_signal = Signal()

    def __init__(self, main_window, dir_name):
        """
        Class to check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
        and Torchvision.

        Parameters
        ----------
        main_window : MainWindow
            Main window of the application.
        """
        super(check_data_from_path_engine, self).__init__()
        self.main_window = main_window
        self.dir_name = dir_name

    def run(self):
        """
        Checks possible model available in BioImage Model Zoo and Torchivision for the workflow specified by Wizards form.

        Parameters
        ----------
        main_window : MainWindow
            Main window of the application.
        """
        try:
            self.state_signal.emit(0)

            self.main_window.cfg.settings["wizard_question_answered_index"]
            self.main_window.cfg.settings["wizard_question_index"]
            folder = self.main_window.cfg.settings["wizard_question_answered_index"][
                self.main_window.cfg.settings["wizard_question_index"]
            ]
            if self.main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"] == -1:
                self.error_signal.emit(
                    f"You need to answer 'Workflow' question before checking the data.", "inform_user"
                )
            elif self.main_window.cfg.settings["wizard_answers"]["PROBLEM.NDIM"] == -1:
                self.error_signal.emit(
                    "You need to answer 'Dimensions' question before checking the data.", "inform_user"
                )
            else:
                workflow = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"]
                ndim = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.NDIM"]
                key = next(
                    iter(
                        self.main_window.cfg.settings["wizard_variable_to_map"][
                            "Q" + str(self.main_window.cfg.settings["wizard_question_index"] + 1)
                        ]
                    )
                )
                is_3d = ndim == "3D"
                if workflow == "SEMANTIC_SEG":
                    mask_type = "semantic_mask" if ("GT_PATH" in key) else ""
                    error, error_message, data_constraints, sample_info = check_images(
                        folder, is_mask=("GT_PATH" in key), mask_type=mask_type, is_3d=is_3d, dir_name=self.dir_name
                    )
                elif workflow == "INSTANCE_SEG":
                    mask_type = "instance_mask" if ("GT_PATH" in key) else ""
                    error, error_message, data_constraints, sample_info = check_images(
                        folder, is_mask=("GT_PATH" in key), mask_type=mask_type, is_3d=is_3d, dir_name=self.dir_name
                    )
                elif workflow == "DETECTION":
                    if "GT_PATH" not in key:
                        error, error_message, data_constraints, sample_info = check_images(
                            folder, is_3d=is_3d, dir_name=self.dir_name
                        )
                    else:
                        error, error_message, data_constraints, sample_info = check_csv_files(
                            folder, is_3d=is_3d, dir_name=self.dir_name
                        )
                elif workflow == "CLASSIFICATION":
                    error, error_message, data_constraints, sample_info = check_classification_images(
                        folder, is_3d=is_3d, dir_name=self.dir_name
                    )
                elif workflow in ["DENOISING", "SUPER_RESOLUTION", "SELF_SUPERVISED", "IMAGE_TO_IMAGE"]:
                    error, error_message, data_constraints, sample_info = check_images(
                        folder, is_3d=is_3d, dir_name=self.dir_name
                    )

                self.main_window.logger.info(f"data_constraints: {data_constraints}")
                if error:
                    self.main_window.logger.info(f"Error: {error}")
                    self.main_window.logger.info(f"Message: {error_message}")
                    self.error_signal.emit(
                        f"Following error found when checking the folder: \n{error_message}", "error"
                    )
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


def mark_syntax_error(main_window: main.MainWindow, gui_widget_name: str, validator_type: List[str] = ["empty"]):
    """
    Functionality for the advanced option button (Down/UP arrows in GUI).

    Parameters
    ----------
    main_window : MainWindow
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
        if gui_widget_name == "select_yaml_name_label":
            out_write = os.path.basename(out)
            main_window.cfg.settings["yaml_config_filename"] = out_write
            main_window.cfg.settings["yaml_config_file_path"] = os.path.dirname(out)

            if get_text(main_window.ui.job_name_input) == "":
                main_window.ui.job_name_input.setPlainText(os.path.splitext(out_write)[0])
        elif gui_widget_name == "output_folder_input":
            main_window.cfg.settings["output_folder"] = out

        if gui_widget_name in ["job_name_input", "output_folder_input"]:
            path = get_text(main_window.ui.output_folder_input)
            if path != "":
                main_window.cfg.settings["job_real_output_path"] = os.path.join(
                    path, get_text(main_window.ui.job_name_input)
                )
                m = "Job results folder: <strong>{}</strong>".format(main_window.cfg.settings["job_real_output_path"])
                main_window.ui.output_final_directory_label.setText(m)

def resource_path(relative_path: str) -> str:
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


def change_page(main_window: main.MainWindow, buttonName: str, to_page: int):
    """
    Move between pages.

    Parameters
    ----------
    main_window : MainWindow
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
        if not move:
            return

        if buttonName == "up":
            main_window.cfg.settings["page_number"] += 1
        else:
            main_window.cfg.settings["page_number"] -= 1
        to_page = main_window.cfg.settings["page_number"]

    if buttonName == "bn_home" or (buttonName == "down" and to_page == 0):
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_home)
        main_window.ui.frame_home.setStyleSheet("background:rgb(255,255,255)")
        main_window.cfg.settings["page_number"] = 0

    elif buttonName == "bn_wizard" or (buttonName == "down" and to_page == 1):
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_wizard)
        main_window.ui.frame_wizard.setStyleSheet("background:rgb(255,255,255)")
        main_window.cfg.settings["page_number"] = 1

    elif buttonName == "bn_run_biapy" or ("bn_" not in buttonName and to_page == 6):
        main_window.ui.stackedWidget.setCurrentWidget(main_window.ui.page_run_biapy)
        main_window.ui.frame_run_biapy.setStyleSheet("background:rgb(255,255,255)")
        main_window.cfg.settings["page_number"] = 6


def eval_wizard_answer(main_window: main.MainWindow):
    """
    Stores the answer given for the current question and mark it to advice the user.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.
    """
    if main_window.allow_change_wizard_question_answer:
        mark_as_answered = False

        # Remember current answer
        if main_window.ui.wizard_question_answer_frame.isVisible():
            changed_answer = False
            if main_window.ui.wizard_question_answer.currentIndex() != -1:
                mark_as_answered = True
                if (
                    main_window.cfg.settings["wizard_question_answered_index"][
                        main_window.cfg.settings["wizard_question_index"]
                    ]
                    != main_window.ui.wizard_question_answer.currentIndex()
                ):
                    main_window.cfg.settings["wizard_question_answered_index"][
                        main_window.cfg.settings["wizard_question_index"]
                    ] = main_window.ui.wizard_question_answer.currentIndex()
                    changed_answer = True

                for key, values in main_window.cfg.settings["wizard_variable_to_map"][
                    "Q" + str(main_window.cfg.settings["wizard_question_index"] + 1)
                ].items():
                    main_window.cfg.settings["wizard_answers"][key] = values[
                        main_window.ui.wizard_question_answer.currentIndex()
                    ]
        elif main_window.ui.wizard_path_input_frame.isVisible():
            te = get_text(main_window.ui.wizard_path_input)
            if te != "":
                key = next(
                    iter(
                        main_window.cfg.settings["wizard_variable_to_map"][
                            "Q" + str(main_window.cfg.settings["wizard_question_index"] + 1)
                        ]
                    )
                )
                main_window.cfg.settings["wizard_answers"][key] = te
                main_window.cfg.settings["wizard_question_answered_index"][
                    main_window.cfg.settings["wizard_question_index"]
                ] = te
                set_text(main_window.ui.wizard_path_input, te)

                # Check if the data was checked
                if main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] == -1:
                    mark_as_answered = False
                else:
                    mark_as_answered = True

        if mark_as_answered:
            # Mark section as answered in TOC
            index = main_window.cfg.settings["wizard_from_question_index_to_toc"][
                main_window.cfg.settings["wizard_question_index"]
            ]
            main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(64, 144, 253))

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
                question_number = int(question.replace("Q", "")) - 1
                if make_visible:
                    if not main_window.cfg.settings["wizard_question_visible"][question_number]:
                        main_window.cfg.settings["wizard_question_visible"][question_number] = True
                        index_in_toc = main_window.cfg.settings["wizard_from_question_index_to_toc"][question_number]
                        main_window.ui.wizard_treeView.setRowHidden(
                            index_in_toc[1], main_window.wizard_toc_model.index(index_in_toc[0], 0), False
                        )
                else:
                    if main_window.cfg.settings["wizard_question_visible"][question_number]:
                        main_window.cfg.settings["wizard_question_visible"][question_number] = False
                        index_in_toc = main_window.cfg.settings["wizard_from_question_index_to_toc"][question_number]
                        main_window.ui.wizard_treeView.setRowHidden(
                            index_in_toc[1], main_window.wizard_toc_model.index(index_in_toc[0], 0), True
                        )

        # Reset data checks if dimensionality or workflow changed, as the data check is different
        if main_window.ui.wizard_question_answer_frame.isVisible() and changed_answer:
            main_window.pretrained_model_need_to_check = None
            key = next(
                iter(
                    main_window.cfg.settings["wizard_variable_to_map"][
                        "Q" + str(main_window.cfg.settings["wizard_question_index"] + 1)
                    ]
                )
            )
            if "PROBLEM.NDIM" == key or "PROBLEM.TYPE" == key:
                for key, val in main_window.cfg.settings["wizard_answers"].items():
                    if "CHECKED" in key:
                        main_window.cfg.settings["wizard_answers"][key] = -1

                for i in range(main_window.cfg.settings["wizard_number_of_questions"]):
                    if main_window.cfg.settings["wizard_possible_answers"][i][0] == "PATH":
                        index = main_window.cfg.settings["wizard_from_question_index_to_toc"][i]
                        main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(0, 0, 0))
                    elif main_window.cfg.settings["wizard_possible_answers"][i][0] in ["MODEL_BIAPY", "MODEL_OTHERS"]:
                        index = main_window.cfg.settings["wizard_from_question_index_to_toc"][i]
                        main_window.wizard_toc_model.item(index[0]).child(index[1]).setForeground(QColor(0, 0, 0))
                        main_window.cfg.settings["wizard_question_answered_index"][i] = -1


def change_wizard_page(main_window: main.MainWindow, val: int, based_on_toc: bool = False, added_val=0):
    """
    Changes wizard page.

    Parameters
    ----------
    main_window : MainWindow
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
            val = main_window.cfg.settings["wizard_from_toc_to_question_index"][index.parent().row()][index.row()]

    eval_wizard_answer(main_window)

    # Calculate valid next/previous question
    if not based_on_toc:
        if added_val > 0:
            val += 1
            for i in range(val, len(main_window.cfg.settings["wizard_question_visible"])):
                if main_window.cfg.settings["wizard_question_visible"][i]:
                    val = i
                    break
        if added_val < 0:
            val -= 1
            for i in range(val, 0, -1):
                if main_window.cfg.settings["wizard_question_visible"][i]:
                    val = i
                    break

    # Go to the first view of the wizard
    last_shown = (
        len(main_window.cfg.settings["wizard_question_visible"])
        - main_window.cfg.settings["wizard_question_visible"][::-1].index(True)
        - 1
    )
    if val == -1 and main_window.cfg.settings["wizard_question_index"] == 0:
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.wizard_start_page)
    elif val == last_shown + 1:
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.summary_page)

        # Only visualice those questions that were answered and visible
        for i in range(len(main_window.cfg.settings["wizard_questions"])):
            if (
                main_window.cfg.settings["wizard_question_visible"][i]
                and main_window.cfg.settings["wizard_question_answered_index"][i] != -1
            ):
                main_window.question_cards[i][f"summary_question_frame_{i}"].setVisible(True)
                set_text(
                    main_window.question_cards[i][f"summary_question_text{i}"],
                    main_window.cfg.settings["wizard_questions"][i],
                )
                if isinstance(main_window.cfg.settings["wizard_question_answered_index"][i], str):
                    set_text(
                        main_window.question_cards[i][f"summary_question_text_answer_{i}"],
                        main_window.cfg.settings["wizard_question_answered_index"][i],
                    )
                else:
                    set_text(
                        main_window.question_cards[i][f"summary_question_text_answer_{i}"],
                        str(
                            main_window.cfg.settings["wizard_possible_answers"][i][
                                main_window.cfg.settings["wizard_question_answered_index"][i]
                            ]
                        ),
                    )
            else:
                main_window.question_cards[i][f"summary_question_frame_{i}"].setVisible(False)

        # Visualice the yaml_file name
        set_text(
            main_window.ui.wizard_config_file_label,
            os.path.join(
                get_text(main_window.ui.wizard_browse_yaml_path_input), get_text(main_window.ui.wizard_yaml_name_input)
            ),
        )
    else:
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.questionary_page)

        main_window.cfg.settings["wizard_question_index"] = val
        main_window.cfg.settings["wizard_question_index"] = max(0, main_window.cfg.settings["wizard_question_index"])
        main_window.cfg.settings["wizard_question_index"] = min(
            len(main_window.cfg.settings["wizard_from_question_index_to_toc"]) - 1,
            main_window.cfg.settings["wizard_question_index"],
        )

        prepare_question(main_window)

    # Change TOC index
    if not based_on_toc:
        index_in_toc = main_window.cfg.settings["wizard_from_question_index_to_toc"][
            main_window.cfg.settings["wizard_question_index"]
        ]
        index = main_window.wizard_toc_model.item(index_in_toc[0]).child(index_in_toc[1])
        if index is not None:
            # As wizard_treeView is triggered when changing it's index we use this flag to block change_wizard_page functionality,
            # as it has been done already
            main_window.not_allow_change_question = True

            main_window.ui.wizard_treeView.setCurrentIndex(index.index())

            # Activate again possible triggers of wizard_treeView
            main_window.not_allow_change_question = False


def prepare_question(main_window: main.MainWindow):
    """
    Prepare current question.
    """
    # Change question
    set_text(
        main_window.ui.wizard_question,
        main_window.cfg.settings["wizard_questions"][main_window.cfg.settings["wizard_question_index"]],
    )
    set_text(
        main_window.ui.wizard_question_label,
        "Question {}".format(main_window.cfg.settings["wizard_question_index"] + 1),
    )

    # Set bottom part of the question. Depeding on the question type different things must be done
    if (
        main_window.cfg.settings["wizard_possible_answers"][main_window.cfg.settings["wizard_question_index"]][0]
        == "PATH"
    ):
        main_window.ui.wizard_path_input_frame.setVisible(True)
        main_window.ui.wizard_question_answer_frame.setVisible(False)
        main_window.ui.wizard_model_input_frame.setVisible(False)

        # Remember the answer if the question was previously answered
        if (
            main_window.cfg.settings["wizard_question_answered_index"][
                main_window.cfg.settings["wizard_question_index"]
            ]
            != -1
        ):
            set_text(
                main_window.ui.wizard_path_input,
                main_window.cfg.settings["wizard_question_answered_index"][
                    main_window.cfg.settings["wizard_question_index"]
                ],
            )
            key = next(
                iter(
                    main_window.cfg.settings["wizard_variable_to_map"][
                        "Q" + str(main_window.cfg.settings["wizard_question_index"] + 1)
                    ]
                )
            )
            if main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] == -1:
                set_text(
                    main_window.ui.wizard_data_checked_label,
                    "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>",
                )
            else:
                set_text(main_window.ui.wizard_data_checked_label, "<span style='color:#04aa6d'>Data checked!</span>")
        else:
            set_text(main_window.ui.wizard_path_input, "")
            set_text(
                main_window.ui.wizard_data_checked_label,
                "<span style='color:#ff3300'><span style='font-size:16pt;'>&larr;</span> Data not checked yet!</span>",
            )

    elif main_window.cfg.settings["wizard_possible_answers"][main_window.cfg.settings["wizard_question_index"]][0] in [
        "MODEL_BIAPY",
        "MODEL_OTHERS",
    ]:
        main_window.ui.wizard_path_input_frame.setVisible(False)
        main_window.ui.wizard_question_answer_frame.setVisible(False)
        main_window.ui.wizard_model_input_frame.setVisible(True)

        if (
            main_window.cfg.settings["wizard_possible_answers"][main_window.cfg.settings["wizard_question_index"]][0]
            == "MODEL_BIAPY"
        ):
            main_window.ui.wizard_model_check_bn.setVisible(False)
            main_window.ui.wizard_model_browse_bn.setVisible(True)
        else:  # "MODEL_OTHERS"
            main_window.ui.wizard_model_check_bn.setVisible(True)
            main_window.ui.wizard_model_browse_bn.setVisible(False)

        # Remember the answer if the question was previously answered
        if (
            main_window.cfg.settings["wizard_question_answered_index"][
                main_window.cfg.settings["wizard_question_index"]
            ]
            != -1
        ):
            set_text(
                main_window.ui.wizard_model_input,
                main_window.cfg.settings["wizard_question_answered_index"][
                    main_window.cfg.settings["wizard_question_index"]
                ],
            )
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
        for ans in main_window.cfg.settings["wizard_possible_answers"][
            main_window.cfg.settings["wizard_question_index"]
        ]:
            main_window.ui.wizard_question_answer.addItem(ans)

        # Remember the answer if the question was previously answered
        if (
            main_window.cfg.settings["wizard_question_answered_index"][
                main_window.cfg.settings["wizard_question_index"]
            ]
            != -1
        ):
            main_window.ui.wizard_question_answer.setCurrentIndex(
                main_window.cfg.settings["wizard_question_answered_index"][
                    main_window.cfg.settings["wizard_question_index"]
                ]
            )
        else:
            main_window.ui.wizard_question_answer.setCurrentIndex(-1)

        # Enable eval_wizard_answer calls again
        main_window.allow_change_wizard_question_answer = True


def clear_answers(main_window: main.MainWindow, ask_user: bool = True):
    """
    Clear all answers.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    ask_user : bool, optional
        Whether to ask the user before proceed.
    """
    continue_clearing = True
    if ask_user:
        main_window.yes_no_exec("Are you sure you want to clear all answers?")
        assert main_window.yes_no
        if not main_window.yes_no.answer:
            continue_clearing = False

    if continue_clearing:
        main_window.cfg.settings["wizard_question_answered_index"] = [
            -1,
        ] * main_window.cfg.settings["wizard_number_of_questions"]

        # Reset TOC colors
        for i in range(main_window.wizard_toc_model.rowCount()):
            main_window.wizard_toc_model.item(i).setForeground(QColor(0, 0, 0))
            for j in range(main_window.wizard_toc_model.item(i).rowCount()):
                main_window.wizard_toc_model.item(i).child(j).setForeground(QColor(0, 0, 0))

        # Rewrite all keys
        main_window.cfg.settings["wizard_answers"] = main_window.cfg.settings["original_wizard_answers"].copy()

        main_window.cfg.settings["wizard_question_index"] = 0


def have_internet(main_window: main.MainWindow, timeout: int = 3) -> bool:
    """
    Checks whether there is internet connection or not.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    timeout : int, optional
        Timeout seconds to wait.
    """
    try:
        urlopen("https://biapyx.github.io", timeout=timeout, context=ssl.create_default_context(cafile=certifi.where()))
        return True
    except Exception:
        exc = traceback.format_exc()
        main_window.logger.error(exc)
        return False


def check_models_from_other_sources(main_window: main.MainWindow, from_wizard: bool = True):
    """
    Check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
    and Torchvision.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    from_wizard : bool, optional
        Whether this function was called through the Wizard or not.
    """
    if main_window.pretrained_model_need_to_check is not None:
        main_window.external_model_list_built(main_window.pretrained_model_need_to_check)
        return

    if not from_wizard:
        main_window.yes_no_exec("This process needs internet connection and may take a while. Do you want to proceed?")
        assert main_window.yes_no
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
    state_signal = Signal(int)

    # Signal to update variables in GUI
    update_var_signal = Signal(str, str)

    # Signal to indicate the main thread that there was an error
    error_signal = Signal(str, str)

    # Signal to send a message to the user about the result of model checking
    add_model_card_signal = Signal(int, dict, bool)

    # Signal to send a message to the user about the result of model checking
    report_yaml_model_check_result = Signal(int)

    # Signal to indicate the main thread that the worker has finished
    finished_signal = Signal()

    def __init__(self, main_window, from_wizard):
        """
        Class to check available model compatible with BiaPy from external sources such as BioImage Model Zoo (BMZ)
        and Torchvision.

        Parameters
        ----------
        main_window : MainWindow
            Main window of the application.
        """
        super(check_models_from_other_sources_engine, self).__init__()
        self.main_window = main_window
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

        if self.from_wizard:
            problem_type = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"]
            problem_ndim = self.main_window.cfg.settings["wizard_answers"]["PROBLEM.NDIM"]
        else:
            problem_type = self.main_window.cfg.settings["workflow_key_names"][
                self.main_window.cfg.settings["selected_workflow"]
            ]
            problem_ndim = get_text(self.main_window.ui.PROBLEM__NDIM__INPUT)
        workflow_specs = {}
        workflow_specs["workflow_type"] = problem_type
        workflow_specs["ndim"] = problem_ndim
        workflow_specs["nclasses"] = "all"
        biapy_version_to_compare = self.main_window.cfg.settings["biapy_code_version"]
        try:
            # Checking BMZ model compatibility using the available model list provided by BMZ
            collection_path = Path(pooch.retrieve(self.COLLECTION_URL, known_hash=None))
            with collection_path.open() as f:
                collection = json.load(f)

            # Collect all the models in BMZs
            model_urls = [entry["rdf_source"] for entry in collection["collection"] if entry["type"] == "model"]

            # Check each model compatibility
            model_count = 0
            for mu in model_urls:
                splited_url = mu.split("/")
                model_name = splited_url[-4]
                model_version = splited_url[-3]
                self.main_window.logger.info("Checking entry: {}".format(model_name))
                
                # Try to decice a better value for the version to compare, as maybe the CI has not run yet 
                if model_name == "affable-shark":
                    previous_biapy_version_to_compare = ""
                    try:
                        affable_shark_file = f"https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/affable-shark/{model_version}/compatibility/biapy_{str(biapy_version_to_compare)}.json"
                        _ = Path(pooch.retrieve(affable_shark_file, known_hash=None))
                    except: 
                        # Seems that the CI was not passed yet so we try to check the compatibility with the last BiaPy release                        
                        if biapy_version_to_compare.micro-1 >= 0:
                            previous_release = int(biapy_version_to_compare.micro-1)
                            previous_biapy_version_to_compare = ".".join(str(biapy_version_to_compare).split(".")[:-1]+[str(previous_release),])
                        try:
                            affable_shark_file = f"https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/affable-shark/{model_version}/compatibility/biapy_{str(previous_biapy_version_to_compare)}.json"
                            _ = Path(pooch.retrieve(affable_shark_file, known_hash=None))
                        except: 
                            pass
                    if previous_biapy_version_to_compare != "":
                        biapy_version_to_compare = previous_biapy_version_to_compare
                    
                compatible, model_rdf = check_bmz_model_compatibility_in_GUI(
                    model_rdf_file=mu,
                    model_name=model_name, 
                    model_version=model_version,
                    biapy_version=str(biapy_version_to_compare),
                    workflow_specs=workflow_specs, 
                    logger=self.main_window.logger
                )

                if compatible:
                    assert model_rdf
                    self.main_window.logger.info("Compatible model")
                    # Creating BMZ model object
                    # model = load_description(model_rdf['config']['bioimageio']['nickname'])
                    # abs url: model.covers[0].absolute() (covers[0] is RelativeFilePath)
                    biapy_imposed_vars = check_model_restrictions(model_rdf, workflow_specs=workflow_specs)
                    doi = "/".join(model_rdf["id"].split("/")[:2])
                    # Extract nickname and its icon
                    if "nickname" in model_rdf["config"]["bioimageio"]:
                        nickname = model_rdf["config"]["bioimageio"]["nickname"]
                        nickname_icon = model_rdf["config"]["bioimageio"]["nickname_icon"]
                    elif "id" in model_rdf["config"]["bioimageio"]:
                        nickname = model_rdf["config"]["bioimageio"]["id"]
                        nickname_icon = model_rdf["config"]["bioimageio"]["id_emoji"]
                    else:
                        nickname = doi
                        nickname_icon = doi
                    cover_url = (
                        "https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/"
                        + nickname
                        + "/"
                        + str(model_rdf["version"])
                        + "/files/"
                        + model_rdf["covers"][0]
                    )
                    model_info = {
                        "name": model_name,
                        "source": "BioImage Model Zoo",
                        "description": model_rdf["description"],
                        "nickname": nickname,
                        "nickname_icon": nickname_icon,
                        "id": doi,
                        "covers": cover_url,
                        "url": f"https://bioimage.io/#/?id={doi}",
                        "imposed_vars": biapy_imposed_vars,
                    }
                    self.add_model_card_signal.emit(model_count, model_info, self.from_wizard)

                    model_count += 1
                else:
                    self.main_window.logger.info("Not compatible model")

            self.main_window.logger.info("Finish checking BMZ model . . .")

            # Check Torchvision models
            models, model_restrictions_description, model_restrictions = check_torchvision_available_models(
                problem_type, problem_ndim
            )
            for m, res, res_cmd in zip(models, model_restrictions_description, model_restrictions):
                self.main_window.logger.info(f"Creating model card for: {m} . . .")
                model_info = {
                    "name": m,
                    "nickname": m,
                    "source": "Torchvision",
                    "description": "Loaded with its default weights (normally on ImageNet data). More info in the link below",
                    "url": "https://pytorch.org/vision/main/models.html",
                    "restrictions": res,
                    "imposed_vars": res_cmd,
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


def export_wizard_summary(main_window: main.MainWindow):
    """
    Create a yaml configuration file for the questions of the wizard.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.
    """
    main_window.logger.info("Preparing the function to export the wizard's summary")

    # Check if there are not answered questions
    finished = True
    finished_data_checks = True
    for i in range(len(main_window.cfg.settings["wizard_question_visible"])):
        if (
            main_window.cfg.settings["wizard_question_visible"][i]
            and main_window.cfg.settings["wizard_question_answered_index"][i] == -1
        ):
            finished = False
            break

        if main_window.cfg.settings["wizard_possible_answers"][i][0] == "PATH":
            key = next(iter(main_window.cfg.settings["wizard_variable_to_map"][f"Q{(i+1)}"].keys()))
            phase = "TRAIN" if "TRAIN" in key else "TEST"
            if (
                main_window.cfg.settings["wizard_answers"][f"{phase}.ENABLE"]
                and f"CHECKED {key}" in main_window.cfg.settings["wizard_answers"]
                and main_window.cfg.settings["wizard_answers"][f"CHECKED {key}"] == -1
                and not (
                    "GT_PATH" in key
                    and main_window.cfg.settings["wizard_answers"]["PROBLEM.TYPE"]
                    in ["DENOISING", "CLASSIFICATION", "SELF_SUPERVISED"]
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
        main_window.dialog_exec(
            "There are still some questions not answered. Please go back and do " "it before continue.", "inform_user"
        )
    elif not finished_data_checks:
        main_window.dialog_exec(
            "Please check the data in training/test paths selected in order to prevent future errors.", "inform_user"
        )
    else:
        main_window.yes_no_exec("Do you want to finish wizard and create the configuration based on your answers?")
        assert main_window.yes_no
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
        data_imposed_classes = (
            2
            if "MODEL.N_CLASSES" not in biapy_cfg["data_constraints"]
            else biapy_cfg["data_constraints"]["MODEL.N_CLASSES"]
        )
        if "model_restrictions" in biapy_cfg and "MODEL.N_CLASSES" in biapy_cfg["model_restrictions"]:
            model_imposed_classes = max(2, biapy_cfg["model_restrictions"]["MODEL.N_CLASSES"])
        else:
            model_imposed_classes = data_imposed_classes
        if data_imposed_classes != model_imposed_classes:
            main_window.dialog_exec(
                f"Incompatibility found: data provided seems to have {data_imposed_classes} classes whereas "
                f"the pretrained model is prepared to work with {model_imposed_classes} classes. Please select another pretrained model.",
                reason="error",
            )
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
            main_window.dialog_exec(
                f"Incompatibility found: data provided seems to have {data_channels} channels whereas "
                f"the pretrained model expects {model_channels} channels. Please select another pretrained model.",
                reason="error",
            )
            return
        del biapy_cfg["data_constraints"]["DATA.PATCH_SIZE_C"]

        # Check number of samples between provided paths
        for phase in ["TRAIN", "TEST"]:
            if biapy_cfg[f"{phase}.ENABLE"]:
                if f"DATA.{phase}.GT_PATH" in biapy_cfg["data_constraints"]:
                    if (
                        biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH"]
                        != biapy_cfg["data_constraints"][f"DATA.{phase}.PATH"]
                    ):
                        m = (
                            "Incompatibility found: number of raw images and ground truth mismatch. Each raw image must "
                            "have a ground truth image. Please check both directories:\n"
                            "    - {} items found in {}\n"
                            "    - {} items found in {}\n".format(
                                biapy_cfg["data_constraints"][f"DATA.{phase}.PATH"],
                                biapy_cfg["data_constraints"][f"DATA.{phase}.PATH_path"],
                                biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH"],
                                biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH_path"],
                            )
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
                            biapy_cfg["data_constraints"][f"DATA.{phase}.GT_PATH_path_shapes"],
                        ):
                            if y_upscaling == -1 and biapy_cfg["PROBLEM.TYPE"] == "SUPER_RESOLUTION":
                                y_upscaling = []
                                for i in range(len(x[:-1])):
                                    div = y[i] / x[i]
                                    if div % 1 != 0:
                                        main_window.dialog_exec(
                                            "Raw images and their corresponding targets seem to not have an integer division. "
                                            "Remember that in super-resolution workflow an upsampled version of the raw images are expected as target. "
                                            "For instance, if raw image shape is 512x512 the expected target image shape need to be 1024x1024 in a x2 "
                                            "upsampling. Here we found {} and {} shapes for raw images and target respectively. Check the data to "
                                            "proceed.".format(x, y),
                                            reason="error",
                                        )
                                        return
                                    else:
                                        y_upscaling.append(int(div))
                                y_upscaling = tuple(y_upscaling)
                                biapy_cfg["PROBLEM.SUPER_RESOLUTION.UPSCALING"] = y_upscaling

                            if biapy_cfg["PROBLEM.TYPE"] == "SUPER_RESOLUTION":
                                assert y_upscaling is not None and isinstance(y_upscaling, list)
                                if biapy_cfg["PROBLEM.NDIM"] == "3D":
                                    assert len(y_upscaling) == 3
                                    expected_y_shape = (
                                        x[0] * y_upscaling[0],
                                        x[1] * y_upscaling[1],
                                        x[2] * y_upscaling[2],
                                        x[3],
                                    )
                                else:
                                    assert len(y_upscaling) == 2
                                    expected_y_shape = (
                                        x[0] * y_upscaling[0],
                                        x[1] * y_upscaling[1],
                                        x[2],
                                    )
                            else:
                                expected_y_shape = x

                            if y[:-1] != expected_y_shape[:-1]:
                                main_window.dialog_exec(
                                    "Raw images and their corresponding targets seem to not match in shape. "
                                    "Expected {} and {}. Found {} and {} for raw images and target respectively".format(
                                        x[:-1], expected_y_shape[:-1], x[:-1], y[:-1]
                                    ),
                                    reason="error",
                                )
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
        out_config = set_default_config(out_config.copy(), main_window.cfg.settings["GPUs"], sample_info)

        yaml_file = os.path.join(
            get_text(main_window.ui.wizard_browse_yaml_path_input), get_text(main_window.ui.wizard_yaml_name_input)
        )
        if not yaml_file.endswith(".yaml") and not yaml_file.endswith(".yml"):
            yaml_file += ".yaml"
        main_window.cfg.settings["yaml_config_filename"] = yaml_file

        # Writing YAML file
        replace = True
        if os.path.exists(yaml_file):
            main_window.yes_no_exec("The file '{}' already exists. Do you want to overwrite it?".format(yaml_file))
            replace = True if main_window.yes_no.answer else False
        if replace:
            main_window.logger.info("Creating YAML file")
            with open(yaml_file, "w", encoding="utf8") as outfile:
                yaml.dump(out_config, outfile, default_flow_style=False)

        # Update GUI with the new YAML file path and resets the check
        main_window.ui.select_yaml_name_label.setText(os.path.normpath(yaml_file))
        actual_name = get_text(main_window.ui.job_name_input)
        if actual_name in [
            "",
            "my_semantic_segmentation",
            "my_instance_segmentation",
            "my_detection",
            "my_denoising",
            "my_super_resolution",
            "my_self_supervised_learning",
            "my_classification",
            "my_image_to_image",
        ]:
            main_window.ui.job_name_input.setPlainText("my_" + out_config["PROBLEM"]["TYPE"].lower())

        if replace:
            # Advise user where the YAML file has been saved
            message = "Configuration file created:\n{}".format(yaml_file)
            main_window.dialog_exec(message, reason="inform_user")

        change_page(main_window, "bn_run_biapy", 99)

        # Resets wizard
        main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.wizard_start_page)
        clear_answers(main_window, ask_user=False)


def set_default_config(
    cfg: Dict,
    gpu_info: List,
    sample_info: Dict,
) -> Dict:
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

    if "PROBLEM" not in cfg:
        cfg["PROBLEM"] = {}
        cfg["PROBLEM"]["TYPE"] = "SEMANTIC_SEG"
        cfg["PROBLEM"]["NDIM"] = "2D"

    ########
    # DATA #
    ########
    if "DATA" not in cfg:
        cfg["DATA"] = {}
    cfg["DATA"]["REFLECT_TO_COMPLETE_SHAPE"] = True

    if "TRAIN" not in cfg:
        cfg["TRAIN"] = {}
    if cfg["TRAIN"]["ENABLE"]:
        # Train data
        if "TRAIN" not in cfg["DATA"]:
            cfg["DATA"]["TRAIN"] = {}
        cfg["DATA"]["TRAIN"]["IN_MEMORY"] = False
        # Validation data
        if "VAL" not in cfg["DATA"]:
            cfg["DATA"]["VAL"] = {}
        cfg["DATA"]["VAL"]["IN_MEMORY"] = False
        cfg["DATA"]["VAL"]["FROM_TRAIN"] = True
        cfg["DATA"]["VAL"]["SPLIT_TRAIN"] = 0.1

    if "TEST" not in cfg:
        cfg["TEST"] = {}
    if cfg["TEST"]["ENABLE"]:
        # Test data
        if "TEST" not in cfg["DATA"]:
            cfg["DATA"]["TEST"] = {}
        cfg["DATA"]["TEST"]["IN_MEMORY"] = False

        # Adjust test padding accordingly
        if cfg["DATA"]["PATCH_SIZE"][0] != -1:
            cfg["DATA"]["TEST"]["PADDING"] = str(tuple([x // 6 for x in cfg["DATA"]["PATCH_SIZE"][:-1]]))

        if "FULL_IMG" not in cfg["TEST"]:
            cfg["TEST"]["FULL_IMG"] = False

    # Normalization
    if "NORMALIZATION" not in cfg["DATA"]:
        cfg["DATA"]["NORMALIZATION"] = {}
    cfg["DATA"]["NORMALIZATION"]["TYPE"] = "zero_mean_unit_variance"
    cfg["DATA"]["NORMALIZATION"]["PERC_CLIP"] = {}
    cfg["DATA"]["NORMALIZATION"]["PERC_CLIP"]["ENABLE"] = True
    cfg["DATA"]["NORMALIZATION"]["PERC_CLIP"]["LOWER_PERC"] = 0.2
    cfg["DATA"]["NORMALIZATION"]["PERC_CLIP"]["UPPER_PERC"] = 99.8

    #######################
    # TRAINING PARAMETERS #
    #######################
    if cfg["TRAIN"]["ENABLE"]:
        cfg["TRAIN"]["EPOCHS"] = 150
        cfg["TRAIN"]["PATIENCE"] = 50
        cfg["TRAIN"]["OPTIMIZER"] = "ADAMW"
        cfg["TRAIN"]["LR"] = 1.0e-4
        # Learning rate scheduler
        if "LR_SCHEDULER" not in cfg["TRAIN"]:
            cfg["TRAIN"]["LR_SCHEDULER"] = {}
        cfg["TRAIN"]["LR_SCHEDULER"]["NAME"] = "warmupcosine"
        cfg["TRAIN"]["LR_SCHEDULER"]["MIN_LR"] = 1.0e-5
        cfg["TRAIN"]["LR_SCHEDULER"]["WARMUP_COSINE_DECAY_EPOCHS"] = 10
        if "LOSS" not in cfg:
            cfg["LOSS"] = {}
        cfg["LOSS"]["CLASS_REBALANCE"] = True

    #########
    # MODEL #
    #########
    # TODO: calculate BMZ/torchvision model size. Now a high number to ensure batch_size is set to 1 so it
    # works always
    network_base_memory = 9999999
    if "MODEL" not in cfg:
        cfg["MODEL"] = {}
    if "SOURCE" not in cfg["MODEL"]:
        cfg["MODEL"]["SOURCE"] = "biapy"
    if cfg["MODEL"]["SOURCE"] == "biapy":
        if cfg["PROBLEM"]["TYPE"] in ["SEMANTIC_SEG", "INSTANCE_SEG", "DETECTION", "DENOISING", "IMAGE_TO_IMAGE"]:
            cfg["MODEL"]["ARCHITECTURE"] = "resunet"
            if cfg["PROBLEM"]["NDIM"] == "3D":
                cfg["MODEL"]["Z_DOWN"] = [1, 1, 1, 1]
            network_base_memory = 400
        elif cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
            if cfg["PROBLEM"]["NDIM"] == "3D":
                cfg["MODEL"]["ARCHITECTURE"] = "resunet"
                cfg["MODEL"]["Z_DOWN"] = [1, 1, 1, 1]
                network_base_memory = 400
            else:
                cfg["MODEL"]["ARCHITECTURE"] = "rcan"
                network_base_memory = 3500
        elif cfg["PROBLEM"]["TYPE"] == "SELF_SUPERVISED":
            cfg["MODEL"]["ARCHITECTURE"] = "resunet"
            network_base_memory = 400
            if cfg["PROBLEM"]["NDIM"] == "3D":
                cfg["MODEL"]["Z_DOWN"] = [1, 1, 1, 1]
        elif cfg["PROBLEM"]["TYPE"] == "CLASSIFICATION":
            cfg["MODEL"]["ARCHITECTURE"] = "vit"
            network_base_memory = 2200

    #####################
    # DATA AUGMENTATION #
    #####################
    if cfg["TRAIN"]["ENABLE"]:
        if "AUGMENTOR" not in cfg:
            cfg["AUGMENTOR"] = {}
        cfg["AUGMENTOR"]["ENABLE"] = True
        cfg["AUGMENTOR"]["AFFINE_MODE"] = "reflect"
        cfg["AUGMENTOR"]["VFLIP"] = True
        cfg["AUGMENTOR"]["HFLIP"] = True
        if cfg["PROBLEM"]["NDIM"] == "3D":
            cfg["AUGMENTOR"]["ZFLIP"] = True

    ############################
    # WORKFLOW SPECIFIC CONFIG #
    ############################
    max_batch_size_allowed = 16 if cfg["PROBLEM"]["NDIM"] == "2D" else 4
    data_channels = cfg["DATA"]["PATCH_SIZE"][-1]
    if cfg["PROBLEM"]["TYPE"] in ["SEMANTIC_SEG", "INSTANCE_SEG", "DETECTION", "IMAGE_TO_IMAGE"]:
        if cfg["TRAIN"]["ENABLE"]:
            cfg["AUGMENTOR"]["BRIGHTNESS"] = True
            cfg["AUGMENTOR"]["BRIGHTNESS_FACTOR"] = str((-0.1, 0.1))
            cfg["AUGMENTOR"]["CONTRAST"] = True
            cfg["AUGMENTOR"]["CONTRAST_FACTOR"] = str((-0.1, 0.1))
            cfg["AUGMENTOR"]["ELASTIC"] = True
            cfg["AUGMENTOR"]["ZOOM"] = True
            cfg["AUGMENTOR"]["ZOOM_RANGE"] = str((0.9, 1.1))
            cfg["AUGMENTOR"]["RANDOM_ROT"] = True

        if cfg["PROBLEM"]["TYPE"] == "INSTANCE_SEG":
            if "INSTANCE_SEG" not in cfg["PROBLEM"]:
                cfg["PROBLEM"]["INSTANCE_SEG"] = {}
            cfg["PROBLEM"]["INSTANCE_SEG"]["DATA_CHANNELS"] = "BC"
            cfg["PROBLEM"]["INSTANCE_SEG"]["DATA_MW_TH_TYPE"] = "auto"

        elif cfg["PROBLEM"]["TYPE"] == "DETECTION":
            if "DETECTION" not in cfg["PROBLEM"]:
                cfg["PROBLEM"]["DETECTION"] = {}
            cfg["PROBLEM"]["DETECTION"]["CHECK_POINTS_CREATED"] = False
            if cfg["TEST"]["ENABLE"]:
                if "POST_PROCESSING" not in cfg["TEST"]:
                    cfg["TEST"]["POST_PROCESSING"] = {}
                if "REMOVE_CLOSE_POINTS_RADIUS" not in cfg["TEST"]["POST_PROCESSING"]:
                    cfg["TEST"]["POST_PROCESSING"]["REMOVE_CLOSE_POINTS_RADIUS"] = 5
                cfg["TEST"]["DET_TOLERANCE"] = int(0.8 * cfg["TEST"]["POST_PROCESSING"]["REMOVE_CLOSE_POINTS_RADIUS"])
                cfg["TEST"]["DET_MIN_TH_TO_BE_PEAK"] = 0.5
                cfg["TEST"]["POST_PROCESSING"]["REMOVE_CLOSE_POINTS"] = True
    elif cfg["PROBLEM"]["TYPE"] == "DENOISING":
        if cfg["DATA"]["PATCH_SIZE"][0] == -1:
            if cfg["PROBLEM"]["NDIM"] == "2D":
                cfg["DATA"]["PATCH_SIZE"] = (64, 64) + (data_channels,)
            else:
                cfg["DATA"]["PATCH_SIZE"] = (12, 64, 64) + (data_channels,)
            if cfg["TEST"]["ENABLE"]:
                cfg["DATA"]["TEST"]["PADDING"] = str(tuple([x // 6 for x in cfg["DATA"]["PATCH_SIZE"][:-1]]))

        # Config as Noise2Void default parameters
        if "DENOISING" not in cfg["PROBLEM"]:
            cfg["PROBLEM"]["DENOISING"] = {}
        cfg["PROBLEM"]["DENOISING"]["N2V_STRUCTMASK"] = True
        cfg["MODEL"]["ARCHITECTURE"] = "unet"
        cfg["MODEL"]["FEATURE_MAPS"] = [32, 64, 96]
        if cfg["PROBLEM"]["NDIM"] == "3D":
            cfg["MODEL"]["Z_DOWN"] = [1, 1]
        cfg["MODEL"]["KERNEL_SIZE"] = 3
        cfg["MODEL"]["UPSAMPLE_LAYER"] = "upsampling"
        cfg["MODEL"]["DROPOUT_VALUES"] = [0, 0, 0]
        cfg["MODEL"]["ACTIVATION"] = "relu"
        cfg["MODEL"]["LAST_ACTIVATION"] = "linear"
        cfg["MODEL"]["NORMALIZATION"] = "bn"
        max_batch_size_allowed = 64
    elif cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
        if cfg["DATA"]["PATCH_SIZE"][0] == -1:
            if cfg["PROBLEM"]["NDIM"] == "2D":
                cfg["DATA"]["PATCH_SIZE"] = (48, 48) + (data_channels,)
            else:
                cfg["DATA"]["PATCH_SIZE"] = (6, 128, 128) + (data_channels,)

            if cfg["TEST"]["ENABLE"]:
                cfg["DATA"]["TEST"]["PADDING"] = str(tuple([x // 6 for x in cfg["DATA"]["PATCH_SIZE"][:-1]]))

        # Force div normalization
        cfg["DATA"]["NORMALIZATION"]["TYPE"] = "scale_range"
        max_batch_size_allowed = 64
    elif cfg["PROBLEM"]["TYPE"] == "CLASSIFICATION":
        pass

    # Removing detection key added from the wizard if we are not in that workflow
    if not cfg["TEST"]["ENABLE"] or cfg["PROBLEM"]["TYPE"] != "DETECTION":
        if "POST_PROCESSING" in cfg["TEST"] and "REMOVE_CLOSE_POINTS_RADIUS" in cfg["TEST"]["POST_PROCESSING"]:
            del cfg["TEST"]["POST_PROCESSING"]["REMOVE_CLOSE_POINTS_RADIUS"]
            if len(cfg["TEST"]["POST_PROCESSING"]) == 0:
                del cfg["TEST"]["POST_PROCESSING"]

    # Calculate data channels
    # cfg.PROBLEM.TYPE == "CLASSIFICATION" or "SELF_SUPERVISED" and PRETEXT_TASK == "masking". But as in the wizard there is no SSL
    # we reduce the if fo samples_each_time to this
    if cfg["PROBLEM"]["TYPE"] == "CLASSIFICATION":
        y_channels = 0
    else:
        if cfg["PROBLEM"]["TYPE"] in ["DENOISING", "SUPER_RESOLUTION", "IMAGE_TO_IMAGE"]:
            y_channels = cfg["DATA"]["PATCH_SIZE"][-1]
        elif cfg["PROBLEM"]["TYPE"] == "INSTANCE_SEG":
            y_channels = 2  # As we are using a BC approach in the Wizard
        else:
            y_channels = 1

    channels_per_sample = {
        "x": cfg["DATA"]["PATCH_SIZE"][-1],
        "y": y_channels,
    }

    # Batch size calculation
    if cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
        y_upsampling = cfg["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"]
    else:
        y_upsampling = (1, 1) if cfg["PROBLEM"]["NDIM"] == "2D" else (1, 1, 1)
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

    if cfg["TRAIN"]["ENABLE"]:
        cfg["TRAIN"]["BATCH_SIZE"] = batch_size

    cfg["DATA"]["PATCH_SIZE"] = str(cfg["DATA"]["PATCH_SIZE"])
    if cfg["PROBLEM"]["TYPE"] == "SUPER_RESOLUTION":
        cfg["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"] = str(cfg["PROBLEM"]["SUPER_RESOLUTION"]["UPSCALING"])
    return cfg


def batch_size_calculator(
    gpu_info: List,
    sample_info: Dict,
    patch_size: Tuple[int, ...],
    channels_per_sample: Dict,
    network_base_memory: int = 400,
    sample_size_reference: int = 256,
    sample_memory_reference: int = 100,
    max_batch_size_allowed: int = 32,
    y_upsampling: Tuple[int, ...] = (1, 1),
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

    Returns
    -------
    batch_size : int
        Optimum batch size to use.
    """
    # Calculate min memory between available GPUs
    min_mem_gpu = None
    for gpu in gpu_info:
        if min_mem_gpu is None:
            min_mem_gpu = gpu.memoryTotal
        else:
            min_mem_gpu = min(min_mem_gpu, gpu.memoryTotal)

    x_data_to_analize = (
        sample_info["DATA.TRAIN.PATH"] if "DATA.TRAIN.PATH" in sample_info else sample_info["DATA.TEST.PATH"]
    )
    # Leave 20% of the memory to not overload it too much and ensure the batch size will always fit
    if min_mem_gpu is not None:
        min_mem_gpu = min_mem_gpu * 0.8

        # Calculate how much memory takes each X data comparing both, 1) selected patch size and and 2) the crop shape used for cropping
        # the data an calculating the total number of samples, with the sample reference (composed by sample_size_reference and
        # sample_memory_reference).
        x_analisis_ref_ratio = x_data_to_analize["crop_shape"][1] / sample_size_reference
        x_selected_patch_ref_ratio = (patch_size[1] / sample_size_reference) ** 2
        x_sample_memory_ratio = x_analisis_ref_ratio * x_selected_patch_ref_ratio * sample_memory_reference

        y_data_to_analize = None
        if "DATA.TRAIN.GT_PATH" in sample_info:
            y_data_to_analize = sample_info["DATA.TRAIN.GT_PATH"]
        elif "DATA.TEST.GT_PATH" in sample_info:
            y_data_to_analize = sample_info["DATA.TEST.GT_PATH"]

        if y_data_to_analize is not None:
            y_crop = y_data_to_analize["crop_shape"][1] * y_upsampling[1]
            # Patch size always square in wizard, that's why we use always y_data_to_analize['crop_shape'][1]
            y_analisis_ref_ratio = y_crop / sample_size_reference
            y_selected_patch_ref_ratio = (patch_size[1] / sample_size_reference) ** 2
            y_sample_memory_ratio = y_analisis_ref_ratio * y_selected_patch_ref_ratio * sample_memory_reference
        else:
            y_sample_memory_ratio = 0

        # How many "slices", i.e. z dimension and channels, to take into account
        x_data = channels_per_sample["x"]
        y_data = channels_per_sample["y"]
        if len(x_data_to_analize["crop_shape"]) == 4:  # Add Z dim if working in 3D
            x_data *= x_data_to_analize["crop_shape"][0]
            if y_data_to_analize is not None:
                y_data *= y_data_to_analize["crop_shape"][0] * y_upsampling[0]

        # This value will be close to the one being used during a __getitem__ of BiaPy generator
        item_memory_consumption = (x_sample_memory_ratio * x_data) + (y_sample_memory_ratio * y_data)

        # The network will hold more memory depending on the input_size. It's calculated to be like 210MB per each (256,256,1) sample
        # so we use here x_sample_memory_ratio as it was measure with sample_memory_reference=100MB by default
        approx_network_memory = network_base_memory + (2 * x_sample_memory_ratio * x_data)

        if item_memory_consumption == 0:
            item_memory_consumption = 1
        approx_batch_size = (
            (min_mem_gpu - approx_network_memory) // item_memory_consumption if item_memory_consumption > 0 else 1
        )
    else:
        approx_batch_size = max_batch_size_allowed // 2

    # Rough stimation on how many patches could be obtained using the actual patch size selected in the wizard
    sample_data_factor = np.prod([x / y for x, y in zip(x_data_to_analize["crop_shape"], patch_size)])
    total_samples = x_data_to_analize["total_samples"] * sample_data_factor

    batch_size = int(max(1, min(min(total_samples, approx_batch_size), max_batch_size_allowed)))

    return batch_size


def adjust_window_progress(main_window: main.MainWindow):
    """
    Changes new workflow creation progress visual clues. Currently, the blue dots in the bottom part of the GUI.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.
    """
    main_window.ui.window1_bn.setIcon(
        main_window.cfg.settings["dot_images"][0]
        if main_window.cfg.settings["page_number"] >= 2
        else main_window.cfg.settings["dot_images"][1]
    )
    main_window.ui.window2_bn.setIcon(
        main_window.cfg.settings["dot_images"][0]
        if main_window.cfg.settings["page_number"] >= 3
        else main_window.cfg.settings["dot_images"][1]
    )
    main_window.ui.window3_bn.setIcon(
        main_window.cfg.settings["dot_images"][0]
        if main_window.cfg.settings["page_number"] >= 4
        else main_window.cfg.settings["dot_images"][1]
    )
    main_window.ui.window4_bn.setIcon(
        main_window.cfg.settings["dot_images"][0]
        if main_window.cfg.settings["page_number"] >= 5
        else main_window.cfg.settings["dot_images"][1]
    )

def start_wizard_questionary(main_window: main.MainWindow):
    """
    Starts questionary.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.
    """
    if get_text(main_window.ui.wizard_browse_yaml_path_input) == "":
        main_window.dialog_exec("Configuration file path must be defined", "error")
        return
    elif get_text(main_window.ui.wizard_yaml_name_input) == "":
        main_window.dialog_exec("Configuration file name must be defined", "error")
        return

    main_window.ui.wizard_main_frame.setCurrentWidget(main_window.ui.questionary_page)

    prepare_question(main_window)

    # Change TOC index
    index_in_toc = main_window.cfg.settings["wizard_from_question_index_to_toc"][
        main_window.cfg.settings["wizard_question_index"]
    ]
    index = main_window.wizard_toc_model.item(index_in_toc[0]).child(index_in_toc[1])
    if index is not None:
        # As wizard_treeView is triggered when changing it's index we use this flag to block change_wizard_page functionality,
        # as it has been done already
        main_window.not_allow_change_question = True

        main_window.ui.wizard_treeView.setCurrentIndex(index.index())

        # Activate again possible triggers of wizard_treeView
        main_window.not_allow_change_question = False

def get_text(gui_widget: QWidget, strip: bool = True) -> str:
    """
    Gets the value of the input widget.

    Parameters
    ----------
    gui_widget : QWidget
        Widget to get the value from.

    strip : bool, optional
        Whether to strip or not the text.

    Returns
    -------
    v: str
        Text of ``gui_widget``.
    """
    if isinstance(gui_widget, QComboBox):
        v = gui_widget.currentText()
    elif isinstance(gui_widget, QLineEdit) or isinstance(gui_widget, QLabel):
        v = gui_widget.text()
    else:  # QTextBrowser
        v = gui_widget.toPlainText()
    if strip:
        v = v.strip()
    return v


def set_text(
    gui_widget: QWidget,
    new_value: str,
):
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
            return "{} couldn't be loaded in {}".format(new_value, gui_widget.objectName())
    elif isinstance(gui_widget, QLineEdit) or isinstance(gui_widget, QLabel):
        if "PATH" in gui_widget.objectName():
            gui_widget.setText(os.path.normpath(new_value))
        else:
            gui_widget.setText(new_value)
    else:  # QTextBrowser
        gui_widget.setText(new_value)


def load_yaml_config(main_window: main.MainWindow) -> Optional[bool]:
    """
    Load YAML configuration file and check its consistency. This function should be called before running BiaPy's
    container or while checking YAMl file consistency button.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    Returns
    -------
    bool : bool, optional
        Whether the yaml configuration was loaded successfully or not.
    """

    # Check GUI variables
    if main_window.cfg.settings["yaml_config_filename"] == "":
        main_window.dialog_exec("A configuration file must be selected", "select_yaml_name_label")
        return False
    yaml_file = get_text(main_window.ui.select_yaml_name_label)
    if not os.path.exists(yaml_file):
        main_window.dialog_exec(
            "The configuration file '{}' does not exist!".format(yaml_file), "select_yaml_name_label"
        )
        return False
    if not str(yaml_file).endswith(".yaml") and not str(yaml_file).endswith(".yml"):
        main_window.dialog_exec(
            "The configuration filename '{}' must have .yaml or .yml extension".format(yaml_file),
            "select_yaml_name_label",
        )
        return False

    ofolder = (
        main_window.cfg.settings["output_folder"]
        if main_window.cfg.settings["output_folder"] != ""
        else str(Path.home())
    )
    jobname = get_text(main_window.ui.job_name_input) if get_text(main_window.ui.job_name_input) != "" else "jobname"
    ofolder = os.path.join(ofolder, jobname)
    main_window.cfg.settings["biapy_cfg"] = Config(ofolder, jobname + "_1")

    # Create a temporal file with the configuration. In this process old key variables that the configuration file may have
    # are automatically translated into the BiaPy version the GUI is running.
    with open(
        os.path.join(
            main_window.cfg.settings["yaml_config_file_path"], main_window.cfg.settings["yaml_config_filename"]
        ),
        "r",
        encoding="utf8",
    ) as stream:
        try:
            temp_cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            main_window.logger.error(exc)
            main_window.dialog_exec("There was a problem loading the .yaml config file", reason="error")
    temp_cfg = convert_old_model_cfg_to_current_version(temp_cfg)
    main_window.logger.info("Creating temporal input YAML file for converting possible old configuration")
    tmp_cfg_file = os.path.join(main_window.log_info["log_dir"], "biapy_tmp.yaml")
    with open(tmp_cfg_file, "w", encoding="utf8") as outfile:
        yaml.dump(temp_cfg, outfile, default_flow_style=False)

    # Merge loaded configuration with the YACS defaults to see if everything is correct or not
    errors = ""
    try:
        main_window.cfg.settings["biapy_cfg"]._C.merge_from_file(tmp_cfg_file)
        main_window.cfg.settings["biapy_cfg"] = main_window.cfg.settings["biapy_cfg"].get_cfg_defaults()
        check_configuration(main_window.cfg.settings["biapy_cfg"], jobname + "_1")

    except Exception as errors:
        errors = str(errors)
        main_window.dialog_exec(
            f"Configuration file checked and some errors were found:\n{errors}\nPlease correct them before proceeding.",
            reason="error",
        )
    else:
        main_window.dialog_exec("Configuration file checked and no errors found.", reason="inform_user")
        return True


def load_yaml_to_GUI(main_window: main.MainWindow):
    """
    Load YAML configuration file and update the GUI accordingly. It starts a new thead for doing
    so while the main thread will be running a the spin window.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.
    """
    # Load YAML file
    yaml_file = QFileDialog.getOpenFileName()[0]
    if yaml_file == "":
        return  # If no file was selected

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
    state_signal = Signal(int)

    # Signal to update variables in GUI
    update_var_signal = Signal(str, str)

    # Signal to indicate the main thread that there was an error
    error_signal = Signal(str, str)

    # Signal to send a message to the user about the result of loading the YAML file
    report_yaml_load_result = Signal(str, str)

    # Signal to indicate the main thread that the worker has finished
    finished_signal = Signal()

    def __init__(self, main_window: main.MainWindow, yaml_file: str, thread_queue: queue.Queue):
        """
        Class to load the YAML configuration file into the GUI. It is done in a separated thread and sends signals
        to the main thread, as this will be locked in the spin window.

        Parameters
        ----------
        main_window : MainWindow
            Main window of the application.

        yaml_file : str
            YAML configuration file path to load.

        thread_queue : Queue
            Queue to pass information between main thread and this process.
        """
        super(load_yaml_to_GUI_engine, self).__init__()
        self.main_window = main_window
        self.yaml_file = yaml_file
        self.thread_queue = thread_queue

    def run(self):
        """
        Process of loading YAML file into GUI.
        """
        self.state_signal.emit(0)
        try:
            with open(self.yaml_file, "r", encoding="utf8") as stream:
                cfg_content = stream.read()
                if "\t" in cfg_content:
                    cfg_content = cfg_content.replace("\t", "  ")
                try:
                    loaded_cfg = yaml.safe_load(cfg_content)
                except:
                    exc = traceback.format_exc()
                    self.main_window.logger.error(exc)
                    self.error_signal.emit(
                        f"Error found reading YAML {self.yaml_file}.\nPlease check the file!", "unexpected_error"
                    )
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
            with open(tmp_cfg_file, "w", encoding="utf8") as outfile:
                yaml.dump(loaded_cfg, outfile, default_flow_style=False)

            self.main_window.logger.info(f"Loaded: {loaded_cfg}")

            # Load configuration file and check possible errors
            tmp_cfg = Config("/home/", "jobname")
            errors = ""
            tmp_cfg._C.merge_from_file(tmp_cfg_file)
            tmp_cfg = tmp_cfg.get_cfg_defaults()
            check_configuration(tmp_cfg, get_text(self.main_window.ui.job_name_input), check_data_paths=False)

            self.vars_to_set = [
                "SYSTEM__NUM_CPUS__INPUT",
                "DATA__TRAIN__PATH__INPUT",
                "DATA__TRAIN__GT_PATH__INPUT",
                "DATA__VAL__PATH__INPUT",
                "DATA__VAL__GT_PATH__INPUT",
                "DATA__TEST__PATH__INPUT",
                "DATA__TEST__GT_PATH__INPUT",
            ]

            # Go over configuration file
            errors, variables_set = self.analyze_dict(conf=loaded_cfg, sep="")

            self.main_window.logger.info("Variables updated: ")
            for i, k in enumerate(variables_set.keys()):
                self.main_window.logger.info("{}. {}: {}".format(i + 1, k, variables_set[k]))
            if len(errors) > 0:
                self.main_window.logger.info("Errors: ")
                for i in range(len(errors)):
                    self.main_window.logger.info("{}. : {}".format(i + 1, errors[i]))

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

    def analyze_dict(self, conf: Dict, sep: str = "") -> Tuple[List[str], Dict]:
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
                err, _vars = self.analyze_dict(v, sep + k if sep == "" else sep + "__" + k)
                if err is not None:
                    errors += err
                    variables_set = update_dict(variables_set, _vars)
            else:
                widget_name = sep + "__" + k + "__INPUT"
                set_var = True

                if widget_name not in self.vars_to_set:
                    set_var = False

                # Special cases
                if widget_name == "SYSTEM__NUM_CPUS__INPUT":
                    v = "All" if v == -1 else v
                
                # Set variable values
                if set_var:
                    err = None
                    if hasattr(self.main_window.ui, widget_name):
                        self.update_var_signal.emit(widget_name, str(v))
                        err = self.thread_queue.get()
                    else:
                        if not widget_name.startswith("PATHS__"):
                            err = "{} widget does not exist".format(widget_name)

                    if err is not None:
                        errors.append(err)
                    else:
                        variables_set[widget_name] = v
                        self.main_window.logger.info("Setting {} : {} ({})".format(widget_name, v, k))

        return errors, variables_set


def get_git_revision_short_hash(main_window: main.MainWindow) -> Tuple[Optional[str], Optional[Version]]:
    sha = None
    vtag = None
    try:
        process = subprocess.Popen(
            ["git", "ls-remote", main_window.cfg.settings["biapy_gui_github"]], stdout=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        sha = re.split(r"\t+", stdout.decode("ascii"))[0]
        vtag = Version(
            str(re.split(r"\t+", stdout.decode("ascii"))[-1])
            .replace("refs/tags/", "")
            .replace("^{}", "")
            .replace("\n", "")
        )
    except Exception:
        exc = traceback.format_exc()
        main_window.logger.error("There was an error getting BiaPy-GUI latest version (attempt 1)")
        main_window.logger.error(exc)

    try:
        vtag = Version(str(vtag))
    except Exception:
        exc = traceback.format_exc()
        main_window.logger.error(f"There was an error converting the vtag into Version object. vtag is {vtag}")
        main_window.logger.error(exc)

    if vtag is None:
        try:
            import requests

            response = requests.get("https://api.github.com/repos/BiaPyX/BiaPy-GUI/releases/latest")
            vtag = Version(response.json()["name"].split(" ")[-1])
        except Exception:
            exc = traceback.format_exc()
            main_window.logger.error("There was an error getting BiaPy-GUI latest version (attempt 2)")
            main_window.logger.error(exc)

    if vtag is None:
        main_window.logger.info(
            "Setting finally the version of the current GUI because other attempts failed. "
            "Please, report this issue with BiaPy developers so they can fix it."
        )
        vtag = main_window.cfg.settings["biapy_gui_version"]

    return sha, vtag


def path_in_list(list: List[str], path: str) -> bool:
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


def path_to_linux(p: str, orig_os: str = "win") -> str:
    """
    Converts given path to Linux if it is Windows.

    Parameters
    ----------
    p : str
        Path to convert.

    orig_os : str
        Origin of the path given. If it is 'win' the path will be converted to Linux.

    Returns
    -------
    win_path : str
        Converted path to Linux.
    """
    if "win" in orig_os.lower():
        win_path = PureWindowsPath(p)
        win_path = os.path.join("/" + win_path.parts[0][0], *win_path.parts[1:]).replace("\\", "/")
    else:
        win_path = p
    return win_path


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
    """
    `True` if the passed pathname is a valid pathname for the current OS _and_
    either currently exists or is hypothetically creatable; `False` otherwise.

    This function is guaranteed to _never_ raise exceptions.
    """
    try:
        # To prevent "os" module calls from raising undesirable exceptions on
        # invalid pathnames, is_pathname_valid() is explicitly called first.
        return is_pathname_valid(pathname) and (os.path.exists(pathname) or is_path_creatable(pathname))
    # Report failure on non-fatal filesystem complaints (e.g., connection
    # timeouts, permissions issues) implying this path to be inaccessible. All
    # other exceptions are unrelated fatal issues and should not be caught here.
    except OSError:
        return False


# Extracted from: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
def is_path_creatable(pathname: str) -> bool:
    """
    `True` if the current user has sufficient permissions to create the passed
    pathname; `False` otherwise.
    """
    # Parent directory of the passed path. If empty, we substitute the current
    # working directory (CWD) instead.
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)


# Sadly, Python fails to provide the following magic number for us.
ERROR_INVALID_NAME = 123
"""
Windows-specific error code indicating an invalid pathname.

See Also
----------
https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
    Official listing of all such codes.
"""


# Extracted from: https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
def is_pathname_valid(pathname: str) -> bool:
    """
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    """
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

        # Use a guaranteed-to-exist base directory
        root_dirname = tempfile.gettempdir()
        assert os.path.isdir(root_dirname)

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
                if hasattr(exc, "winerror"):
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


def check_supported_container_versions(gui_version: Version, logger: Logger):
    """
    Reads BiaPy's landing page, in the GUI history, to find the containers supported for this version of the GUI.

    Parameters
    ----------
    gui_version : str
        Version of the GUI.

    logger : Logger
        Origin of the path given. If it is 'win' the path will be converted to Linux.

    Returns
    -------
    compatible_versions : List of str
        Compatible version with the currently running GUI.
    """
    compatible_versions = []
    try:
        # Read the page
        response = urlopen(
            "https://biapyx.github.io/GUI_versions/", context=ssl.create_default_context(cafile=certifi.where())
        )

        # Parse it
        soup = BeautifulSoup(
            response.read(), from_encoding=response.headers.get_content_charset(), features="html.parser"
        )
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


def save_biapy_config(main_window: main.MainWindow, data: Dict, biapy_version: str = ""):
    """
    Save BiaPy configuration.

    Parameters
    ----------
    main_window : MainWindow
        Main window of the application.

    data: dict
        Data dict to save.

    biapy_version : str, optional
        Data version to save if there is no one in the config file.
    """
    try:
        with open(main_window.log_info["config_file"], "r") as file:
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
                if file_version < Version(biapy_version):
                    old_data["GUI_VERSION"] = biapy_version
            except:
                old_data["GUI_VERSION"] = biapy_version

    # Ensure always an str is saved
    if "GUI_VERSION" in old_data:
        old_data["GUI_VERSION"] = str(biapy_version)

    with open(main_window.log_info["config_file"], "w") as outfile:
        json.dump(old_data, outfile, indent=4)


def update_dict(old_dict: Dict, new_dict: Dict):
    """
    Update given dictionary ``old_dict`` with the values of ``new_dict`.

    Parameters
    ----------
    old_dict : dict
        Old dictionary to update.

    new_dict : dict
        Dictionary with the new key/values to set into ``old_dict``.

    Returns
    -------
    old_dict : dict
        Updated old dictionary.
    """
    for k, v in new_dict.items():
        if isinstance(v, collections.abc.Mapping):
            old_dict[k] = update_dict(old_dict.get(k, {}), v)  # type: ignore
        else:
            old_dict[k] = v
    return old_dict

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
