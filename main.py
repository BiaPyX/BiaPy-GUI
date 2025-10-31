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
from PySide6.QtCore import Qt, QSize, QObject, QEvent, QUrl, QPoint
from PySide6.QtGui import (
    QDesktopServices,
    QColor,
    QIcon,
    QPixmap,
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
    QApplication,
    QPushButton,
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
    center_window,
)
from settings import Settings
from ui.ui_main import Ui_MainWindow
from ui.aux_windows import (
    dialog_Ui,
    modify_yaml_Ui,
    yes_no_Ui,
    spinner_Ui,
    basic_Ui,
    model_card_carrousel_Ui,
    tour_window_Ui,
)

os.environ["QT_MAC_WANTS_LAYER"] = "1"


import PySide6.QtWidgets as QtWidgets

INTERACTIVE = (
    QtWidgets.QAbstractButton,
    QtWidgets.QLineEdit, QtWidgets.QAbstractSpinBox,
    QtWidgets.QComboBox, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit,
    QtWidgets.QAbstractSlider, QtWidgets.QTabBar,
    QtWidgets.QTreeView, QtWidgets.QListView, QtWidgets.QTableView,
)

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

        # Left buttons
        self.ui.bn_home.clicked.connect(lambda: change_page(self, "bn_home", 99))
        self.ui.bn_wizard.clicked.connect(lambda: change_page(self, "bn_wizard", 99))
        self.ui.bn_run_biapy.clicked.connect(lambda: change_page(self, "bn_run_biapy", 99))

        # Home page buttons
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
            lambda: QDesktopServices.openUrl(QUrl("https://www.nature.com/articles/s41592-025-02699-y"))
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

        # Info icons
        info_icon = QIcon(self.cfg.settings["info_image"])
        info_icon_clicked = self.cfg.settings["info_image_clicked"]

        def inspect_all_widgets(main_widget, widget_names: List[str] = ["ui"]):
            for widget in main_widget.children():
                if isinstance(widget, QPushButton):
                    if "_info" in widget.objectName().lower():
                        # Set info icon
                        widget.setIcon(info_icon)
                        widget.setIconSize(QSize(30, 30))
                        # Set instant tooltip
                        widget.clicked.connect(lambda checked, a=widget.objectName(): self.showInstantToolTip(a, widget_names))
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
                    inspect_all_widgets(widget, widget_names)

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
        self.ui.check_yaml_file_bn.clicked.connect(lambda: load_yaml_config(self))
        self.ui.run_biapy_docker_bn.clicked.connect(lambda: self.UIFunction.run_biapy())

        self.yes_no = None
        self.diag = None
        self.wokflow_info = None
        self.spinner = None
        self.basic_dialog = None
        self.model_carrousel_dialog = None
        self.tour = None        
        self.modify_yaml = modify_yaml_Ui(self)
        inspect_all_widgets(self.modify_yaml.yaml_mod_window.centralwidget, widget_names=["modify_yaml", "yaml_mod_window"])

        # Variable to store model cards
        self.model_cards = None

        # Variables to control the threads/workers of spin window
        self.thread_spin = None
        self.worker_spin = None

        self.external_model_restrictions = None
        self.pretrained_model_need_to_check = None

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

    def update_variable_in_GUI(self, variable_name: str, variable_value: str, widget_names=["ui"]):
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
        widget = self
        for widget_name in widget_names:
            widget = getattr(widget, widget_name)

        err = set_text(getattr(widget, variable_name), str(variable_value))
        
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

    def report_yaml_load(self, errors: str, yaml_file: str, paths_to_change: Dict[str, str], checkpoint_needed: bool, loaded_cfg: Dict):
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
                "Configuration file succesfully loaded! You will be prompted to modify any discrepant paths.",
                "inform_user_and_go",
            )
            self.cfg.settings["yaml_config_file_path"] = os.path.dirname(self.yaml_file)

            center_window(self.modify_yaml, self.geometry())
            self.modify_yaml.display_discrepancies(paths_to_change, checkpoint_needed=checkpoint_needed, yaml_file=yaml_file, loaded_cfg=loaded_cfg)
            self.modify_yaml.exec()                    
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

    def closeEvent(self, event: QEvent):
        """
        Manages closing event to ensure all threads are killed.

        Parameters
        ----------
        event: QEvent
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
        if sha is not None:
            self.logger.info(f"Remote last version's hash: {sha}")
        self.logger.info(f"Remote last version: {vtag}")
        if sha is not None and vtag is not None and vtag > self.cfg.settings["biapy_gui_version"]:
            self.dialog_exec(
                "There is a new version of BiaPy's graphical user interface available. Please, "
                "download it <a href='https://biapyx.github.io'>here</a>",
                reason="inform_user",
            )

    def showInstantToolTip(self, gui_widget_name: str, widget_names: List[str] = ["ui"]):
        """
        Shows the tooTip of a widget.

        Parameters
        ----------
        gui_widget_name : str
            Name of the QWidget selected to show the tooltip.
        """
        widget = self
        for widget_name in widget_names:
            widget = getattr(widget, widget_name)

        QToolTip.showText(
            QCursor.pos(),
            getattr(widget, gui_widget_name).toolTip(),
        )
        self._dragging = False
        self._dragPos = QPoint()

    def _is_interactive_child(self, pos):
        w = self.childAt(pos)
        while w and w is not self:
            if isinstance(w, INTERACTIVE):
                return True
            w = w.parentWidget()
        return False

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and not self._is_interactive_child(e.position().toPoint()):
            self._dragging = True
            self._dragPos = e.globalPosition().toPoint()
            e.accept()
        else:
            super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self._dragging and (e.buttons() & Qt.LeftButton):
            delta = e.globalPosition().toPoint() - self._dragPos
            self.move(self.pos() + delta)
            self._dragPos = e.globalPosition().toPoint()
            e.accept()
        else:
            super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if self._dragging and e.button() == Qt.LeftButton:
            self._dragging = False
            e.accept()
        else:
            super().mouseReleaseEvent(e)
    


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
