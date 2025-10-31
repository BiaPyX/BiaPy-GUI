from __future__ import annotations
import os
import yaml
import pooch
from typing import Dict, List, Optional
from packaging.version import Version
from PySide6.QtCore import QCoreApplication, QSize, Qt, QEvent
from PySide6.QtGui import (
    QColor,
    QFont,
    QIcon,
    QPixmap,
    QCloseEvent,
)
from PySide6.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QVBoxLayout, QStyle, QGridLayout, QFileDialog

from ui_utils import mark_syntax_error, resource_path, change_page
from ui.ui_dialog import Ui_Dialog
from ui.ui_yes_no import Ui_yes_no
from ui.spinner import Ui_spinner
from ui.ui_basic import Ui_basic
from ui.ui_modify_yaml import Ui_Modify_YAML
from ui.ui_model_carrousel import Ui_model_card_carrousel_dialog
from ui.ui_tour_window import Ui_tour_window
from aux_classes.waitingspinnerwidget import QtWaitingSpinner
import main

from ui_utils import is_pathname_valid

class dialog_Ui(QDialog):
    def __init__(
        self,
        parent_ui: main.MainWindow,
    ):
        """
        Creates a basic dialog window to report information to the user.

        Parameters
        ----------
        parent_ui : MainWindow
            Main window.
        """
        super(dialog_Ui, self).__init__()
        self.dialog_window = Ui_Dialog()
        self.original_width = self.geometry().width()
        self.parent_ui = parent_ui
        self.dialog_window.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.upbar_icon = [
            QPixmap(resource_path(os.path.join("images", "bn_images", "error.png"))),
            QPixmap(resource_path(os.path.join("images", "bn_images", "info.png"))),
        ]
        self.dragPos = self.pos()
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")

        def moveErrorWindow(event: QCloseEvent):
            """
            Move the error window.

            Parameters
            ----------
            event: QCloseEvent
                Event that called this function.
            """
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.signals_created = False
        self.dialog_window.frame_top.mouseMoveEvent = moveErrorWindow

    def mousePressEvent(self, event: QEvent):
        """
        Mouse press event handler.

        Parameters
        ----------
        event: QEvent
            Event that called this function.
        """
        self.dragPos = event.globalPos()

    def dialog_constrict(self, message: str, reason: Optional[str]):
        """
        Sets the message of the window.

        Parameters
        ----------
        message : str
            Name of the workflow.

        reason : str, optional
            Reason of the given message.
        """

        self.resize(self.original_width, self.geometry().height())
        self.dialog_window.window_des_label.setText("Error")
        self.dialog_window.icon_label.setPixmap(self.upbar_icon[0])
        if self.signals_created:
            self.dialog_window.go_to_correct_bn.clicked.disconnect()
        else:
            self.signals_created = True
        if reason is not None:
            if reason == "load_yaml_error":
                self.dialog_window.window_des_label.setText("Error")
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", "OK", None))
                self.dialog_window.error_message_label.setText(
                    "Configuration file not loaded because of the following errors:\n{}".format(message)
                )
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            elif reason == "load_yaml_ok_but_errors":
                self.dialog_window.icon_label.setPixmap(self.upbar_icon[1])
                self.dialog_window.window_des_label.setText("Information")
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("OK", "OK", None))
                m = "Configuration file loaded but with some errors. Please send BiaPy developers\
                    the following errors:"
                for i, mes in enumerate(message):
                    m += "\n" + str(i + 1) + ". {}".format(mes)
                self.dialog_window.error_message_label.setText(m)
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            elif reason in ["inform_user", "inform_user_and_go"]:
                self.resize(int(0.9 * self.parent_ui.width()), self.geometry().height())
                self.dialog_window.error_message_label.setWordWrap(True)
                self.dialog_window.icon_label.setPixmap(self.upbar_icon[1])
                self.dialog_window.window_des_label.setText("Information")
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("OK", "OK", None))
                self.dialog_window.error_message_label.setText(message)
                self.dialog_window.go_to_correct_bn.clicked.connect(lambda: self.redirect_and_close(reason))
            elif reason == "unexpected_error":
                self.dialog_window.window_des_label.setText("Error")
                self.dialog_window.error_message_label.setText("{}".format(message))
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", "OK", None))
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            elif reason == "error":
                self.dialog_window.error_message_label.setWordWrap(True)
                self.dialog_window.window_des_label.setText("Error")
                self.dialog_window.error_message_label.setText("{}".format(message))
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", "OK", None))
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            else:
                self.dialog_window.error_message_label.setWordWrap(True)
                if reason == "docker_installation":
                    self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", "OK", None))
                else:
                    self.dialog_window.go_to_correct_bn.setText(
                        QCoreApplication.translate("Error", "Go to correct", None)
                    )
                self.dialog_window.go_to_correct_bn.clicked.connect(lambda: self.redirect_and_close(reason))
                self.dialog_window.error_message_label.setText(message)
        else:
            self.dialog_window.error_message_label.setText(
                "This error was not expected. Please contact BiaPy developers with the following message:\n\n" + message
            )
            self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", "Close BiaPy GUI", None))
            self.dialog_window.go_to_correct_bn.clicked.connect(self.close_all)

    def closeEvent(self, event: QCloseEvent):
        """
        Close event handler.

        Parameters
        ----------
        event: QCloseEvent
            Event that called this function.
        """
        self.dialog_window.error_message_label.setWordWrap(False)
        self.dialog_window.go_to_correct_bn.click()

    def close_all(self):
        self.close()
        self.parent_ui.close()

    def redirect_and_close(self, reason: str):
        """
        Sets the message of the window.

        Parameters
        ----------
        reason : str
            Reason of the redirection.
        """
        if reason == "jobname":
            change_page(self.parent_ui, "bn_run_biapy", 99)
        elif reason == "output_folder":
            change_page(self.parent_ui, "bn_run_biapy", 99)
            mark_syntax_error(self.parent_ui, "output_folder_input", ["empty"])
        elif reason == "select_yaml_name_label":
            change_page(self.parent_ui, "bn_run_biapy", 99)
            mark_syntax_error(self.parent_ui, "select_yaml_name_label", ["empty"])
        elif reason == "docker_installation":
            change_page(self.parent_ui, "bn_home", 99)
        self.close()


class yes_no_Ui(QDialog):
    def __init__(self):
        """
        Creates a yes/no question window for user interaction.
        """
        super(yes_no_Ui, self).__init__()
        self.yes_no_window = Ui_yes_no()
        self.yes_no_window.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.yes_no_window.yes_bn.clicked.connect(lambda: self.submitclose(True))
        self.yes_no_window.no_bn.clicked.connect(lambda: self.submitclose(False))
        self.yes_no_window.icon_label.setPixmap(
            QPixmap(resource_path(os.path.join("images", "bn_images", "question.png")))
        )
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.answer = False

    def create_question(self, question):
        self.yes_no_window.question_label.setText(question)

    def submitclose(self, answer):
        self.answer = answer
        self.accept()


class spinner_Ui(QDialog):
    def __init__(
        self,
        parent_ui: main.MainWindow,
    ):
        """
        Creates a spin so the user can see that the GUI is not frozen.

        Parameters
        ----------
        parent_ui : MainWindow
            Main window.
        """
        super(spinner_Ui, self).__init__()
        self.spinner_window = Ui_spinner()
        self.spinner_window.setupUi(self)
        self.parent_ui = parent_ui
   
        # Create spinner
        self.spinner = QtWaitingSpinner(self.parent_ui, True, True)
        self.spinner.setRoundness(150.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(8)
        self.spinner.setLineLength(40)
        self.spinner.setLineWidth(20)
        self.spinner.setInnerRadius(30)
        self.spinner.setRevolutionsPerSecond(0.5)
        self.spinner.setColor(QColor(64, 144, 253))
        self.spinner_window.verticalLayout.addWidget(self.spinner)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def stop(self):
        self.spinner.stop()
        self.close()

    def start(self):
        self.spinner.start()

    def closeEvent(self, event: QCloseEvent):
        """
        Close event handler.

        Parameters
        ----------
        event: QCloseEvent
            Event that called this function.
        """
        try:
            self.parent_ui.worker_spin.state_signal.emit(1)
        except Exception as e:
            print(f"Possible expected error during closing spin window: {e}")
        self.spinner.stop()
        super().close()


class basic_Ui(QDialog):
    def __init__(
        self,
    ):
        """
        Creates a basic window to report just a main message and nothing else.
        """
        super(basic_Ui, self).__init__()
        self.basic_window = Ui_basic()
        self.basic_window.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.basic_window.bn_close.clicked.connect(self.close)
        self.basic_window.bn_close.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
        self.basic_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images", "wizard", "wizard.png"))))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.basic_window.message_label.setOpenExternalLinks(True)

    def set_info(self, text: str, info_button=False):
        """
        Sets the message label.

        Parameters
        ----------
        text : str
            Message to be set.
        """
        # if info_button:
        #     self.basic_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))))
        self.basic_window.message_label.setText(text)


class model_card_carrousel_Ui(QDialog):
    def __init__(
        self,
        parent_ui: main.MainWindow,
    ):
        """
        Creates a window with a carrousel of models.

        Parameters
        ----------
        parent_ui : MainWindow
            Main window.
        """
        super(model_card_carrousel_Ui, self).__init__()
        self.model_carrousel_window = Ui_model_card_carrousel_dialog()
        self.model_carrousel_window.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.model_carrousel_window.bn_close.clicked.connect(self.close)
        self.model_carrousel_window.bn_close.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
        )
        self.model_carrousel_window.icon_label.setPixmap(
            QPixmap(resource_path(os.path.join("images", "bn_images", "info.png")))
        )
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.parent_ui = parent_ui

        # Create base font
        self.font = QFont()
        self.font.setFamily("DejaVu Math TeX Gyre")
        self.font.setPointSize(12)

        self.total_model_cards_created = 0
        self.model_cards = []
        self.model_row, self.model_col = -1, 0
        self.source_logo = []
        self.source_logo.append(QPixmap(resource_path(os.path.join("images", "bmz_logo.png"))))
        self.source_logo.append(QPixmap(resource_path(os.path.join("images", "torchvision_logo.png"))))

    def show_models(self, number_of_models: int):
        """
        Show models.

        Parameters
        ----------
        number_of_models : int
            Number of the models to show.
        """
        for i in range(number_of_models):
            self.model_cards[i][f"model_card_frame_{i}"].setVisible(True)

    def create_model_card(self, model_number: int, model_info: Dict, from_wizard: bool = True):
        """
        Create a model card. If there are no more model cards to display it this function internally creates a new model card.

        Parameters
        ----------
        model_number : int
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
        """
        print("Creating model card . . .")
        # Create model card the first time (future checks will reuse the widgets)
        if model_number > (self.total_model_cards_created - 1):
            self.model_cards.append({})

            self.model_cards[model_number][f"model_card_frame_{model_number}"] = QFrame(
                self.model_carrousel_window.scrollAreaWidgetContents
            )
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setObjectName(
                f"model_card_frame_{model_number}"
            )
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setMinimumSize(QSize(800, 200))
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setMaximumSize(QSize(435, 400))
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setStyleSheet(
                f"#model_card_frame_{model_number}"
                " {\n"
                "border: 2px solid rgb(120,120,120);\n"
                "border-radius: 15px;\n"
                "}\n"
                "\n"
                f"#model_card_frame_{model_number}:hover"
                " {\n"
                "	background-color: rgb(240,240,240);\n"
                "	border: 2px solid rgb(64, 144, 253);\n"
                "   border-radius: 15px;\n"
                "}"
            )
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"] = QVBoxLayout(
                self.model_cards[model_number][f"model_card_frame_{model_number}"]
            )
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].setObjectName(
                f"verticalLayout_5_{model_number}"
            )
            self.model_cards[model_number][f"model_name_{model_number}"] = QLabel(
                self.model_cards[model_number][f"model_card_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_name_{model_number}"].setObjectName(f"model_name_{model_number}")
            self.model_cards[model_number][f"model_name_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_name_{model_number}"].setStyleSheet(
                "color: rgb(64,144,253);\n" "font-weight:bold;\nbackground-color:rgba(0, 0, 0, 0);"
            )
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].addWidget(
                self.model_cards[model_number][f"model_name_{model_number}"], 0, Qt.AlignHCenter
            )
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"] = QFrame(
                self.model_cards[model_number][f"model_card_frame_{model_number}"]
            )
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setObjectName(
                f"frame_2model_source_from_frame_{model_number}"
            )
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setFrameShape(
                QFrame.NoFrame
            )
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setFrameShadow(
                QFrame.Raised
            )
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setStyleSheet(
                "background-color:rgba(0, 0, 0, 0);"
            )
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"] = QHBoxLayout(
                self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"]
            )
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].setObjectName(
                f"horizontalLayout_4{model_number}"
            )
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].setContentsMargins(5, 5, 5, 5)
            self.model_cards[model_number][f"model_source_from_text_{model_number}"] = QLabel(
                self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_source_from_text_{model_number}"].setObjectName(
                f"model_source_from_text_{model_number}"
            )
            self.model_cards[model_number][f"model_source_from_text_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_source_from_text_{model_number}"].setStyleSheet(
                "color: rgb(120,120,120); font-size: 11px;"
            )
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].addWidget(
                self.model_cards[model_number][f"model_source_from_text_{model_number}"]
            )
            self.model_cards[model_number][f"model_source_icon_{model_number}"] = QLabel(
                self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setObjectName(
                f"model_source_icon_{model_number}"
            )
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setMinimumSize(QSize(30, 30))
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setMaximumSize(QSize(30, 30))
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setScaledContents(True)
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].addWidget(
                self.model_cards[model_number][f"model_source_icon_{model_number}"]
            )
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].addWidget(
                self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"], 0, Qt.AlignHCenter
            )
            self.model_cards[model_number][f"model_card_subframe_{model_number}"] = QFrame(
                self.model_cards[model_number][f"model_card_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setObjectName(
                f"model_card_subframe_{model_number}"
            )
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setMinimumSize(QSize(0, 160))
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setStyleSheet(
                "background-color:rgba(0, 0, 0, 0);"
            )
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"] = QHBoxLayout(
                self.model_cards[model_number][f"model_card_subframe_{model_number}"]
            )
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"].setObjectName(
                f"horizontalLayout_2{model_number}"
            )
            self.model_cards[model_number][f"model_img_{model_number}"] = QLabel(
                self.model_cards[model_number][f"model_card_subframe_{model_number}"]
            )
            self.model_cards[model_number][f"model_img_{model_number}"].setObjectName(f"model_img_{model_number}")
            self.model_cards[model_number][f"model_img_{model_number}"].setMinimumSize(QSize(130, 130))
            self.model_cards[model_number][f"model_img_{model_number}"].setMaximumSize(QSize(130, 130))
            self.model_cards[model_number][f"model_img_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_img_{model_number}"].setScaledContents(True)
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"].addWidget(
                self.model_cards[model_number][f"model_img_{model_number}"]
            )
            self.model_cards[model_number][f"model_info_frame_{model_number}"] = QFrame(
                self.model_cards[model_number][f"model_card_subframe_{model_number}"]
            )
            self.model_cards[model_number][f"model_info_frame_{model_number}"].setObjectName(
                f"model_info_frame_{model_number}"
            )
            self.model_cards[model_number][f"model_info_frame_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"model_info_frame_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"gridLayout{model_number}"] = QGridLayout(
                self.model_cards[model_number][f"model_info_frame_{model_number}"]
            )
            self.model_cards[model_number][f"gridLayout{model_number}"].setObjectName(f"gridLayout{model_number}")
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"] = QFrame(
                self.model_cards[model_number][f"model_info_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"].setObjectName(
                f"model_nick_id_frame_{model_number}"
            )
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"] = QHBoxLayout(
                self.model_cards[model_number][f"model_nick_id_frame_{model_number}"]
            )
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].setObjectName(
                f"horizontalLayout_3{model_number}"
            )
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].setContentsMargins(0, 0, 0, 0)
            self.model_cards[model_number][f"model_nickname_{model_number}"] = QLabel(
                self.model_cards[model_number][f"model_nick_id_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_nickname_{model_number}"].setObjectName(
                f"model_nickname_{model_number}"
            )
            self.model_cards[model_number][f"model_nickname_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].addWidget(
                self.model_cards[model_number][f"model_nickname_{model_number}"]
            )
            self.model_cards[model_number][f"model_id_{model_number}"] = QLabel(
                self.model_cards[model_number][f"model_nick_id_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_id_{model_number}"].setObjectName(f"model_id_{model_number}")
            self.model_cards[model_number][f"model_id_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].addWidget(
                self.model_cards[model_number][f"model_id_{model_number}"]
            )
            self.model_cards[model_number][f"gridLayout{model_number}"].addWidget(
                self.model_cards[model_number][f"model_nick_id_frame_{model_number}"], 0, 0, 1, 1
            )
            self.model_cards[model_number][f"model_description_{model_number}"] = QLabel(
                self.model_cards[model_number][f"model_info_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_description_{model_number}"].setObjectName(
                f"model_description_{model_number}"
            )
            self.model_cards[model_number][f"model_description_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_description_{model_number}"].setWordWrap(True)
            self.model_cards[model_number][f"gridLayout{model_number}"].addWidget(
                self.model_cards[model_number][f"model_description_{model_number}"], 1, 0, 1, 1
            )
            self.model_cards[model_number][f"model_link_{model_number}"] = QLabel(
                self.model_cards[model_number][f"model_info_frame_{model_number}"]
            )
            self.model_cards[model_number][f"model_link_{model_number}"].setObjectName(f"model_link_{model_number}")
            self.model_cards[model_number][f"model_link_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_link_{model_number}"].setWordWrap(True)
            self.model_cards[model_number][f"model_link_{model_number}"].setOpenExternalLinks(True)
            self.model_cards[model_number][f"gridLayout{model_number}"].addWidget(
                self.model_cards[model_number][f"model_link_{model_number}"], 2, 0, 1, 1
            )
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"].addWidget(
                self.model_cards[model_number][f"model_info_frame_{model_number}"]
            )
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].addWidget(
                self.model_cards[model_number][f"model_card_subframe_{model_number}"]
            )
            self.model_carrousel_window.verticalLayout_6.addWidget(
                self.model_cards[model_number][f"model_card_frame_{model_number}"]
            )

            self.model_cards[model_number][f"model_card_frame_{model_number}"].mouseDoubleClickEvent = (
                lambda event, a=model_info["nickname"], b=model_info["source"], c=model_info[
                    "imposed_vars"
                ], d=from_wizard: self.parent_ui.select_external_model(a, b, c, d)
            )

            self.total_model_cards_created += 1

        # Set model description accordingly
        try:
            local_path = pooch.retrieve(model_info["covers"], known_hash=None)
        except:
            if model_info["source"] == "BioImage Model Zoo":
                local_path = os.path.join("images", "bmz_model_not_found.png")
            else:
                local_path = os.path.join("images", "torchvision_logo.png")
        local_path = resource_path(local_path)

        self.model_cards[model_number][f"model_card_frame_{model_number}"].setVisible(True)
        self.model_cards[model_number][f"model_name_{model_number}"].setText(model_info["name"])
        self.model_cards[model_number][f"model_source_from_text_{model_number}"].setText("from " + model_info["source"])
        if model_info["source"] == "BioImage Model Zoo":
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setPixmap(self.source_logo[0])
            self.model_cards[model_number][f"model_nickname_{model_number}"].setVisible(True)
            self.model_cards[model_number][f"model_nickname_{model_number}"].setText(
                "<span style='color:#4090FD';>Name: </span>"
                + model_info["nickname"]
                + " ("
                + "<span style='font-family: \"Noto Color Emoji\";'>{}</span>".format(model_info["nickname_icon"])
                + ")"
            )
            self.model_cards[model_number][f"model_id_{model_number}"].setText(
                '<span style="color:#4090FD";>ID: </span>' + model_info["id"]
            )
            self.model_cards[model_number][f"model_description_{model_number}"].setText(
                '<span style="color:#4090FD";>Description: </span>' + model_info["description"]
            )
            self.model_cards[model_number][f"model_link_{model_number}"].setText(
                '<span style="color:#4090FD";>URL: </span> <a href="'
                + model_info["url"]
                + '">'
                + model_info["url"]
                + "</a>"
            )
            self.model_cards[model_number][f"model_img_{model_number}"].setPixmap(QPixmap(local_path))
        else:
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setPixmap(self.source_logo[1])
            self.model_cards[model_number][f"model_nickname_{model_number}"].setVisible(False)
            # ID changed for description
            self.model_cards[model_number][f"model_id_{model_number}"].setText(
                '<span style="color:#4090FD";>Description: </span>' + model_info["description"]
            )
            # Description changed for URL
            self.model_cards[model_number][f"model_description_{model_number}"].setText(
                '<span style="color:#4090FD";>URL: </span> <a href="'
                + model_info["url"]
                + '">'
                + model_info["url"]
                + "</a>"
            )
            # URL used for restrictions
            if model_info["restrictions"] != "":
                self.model_cards[model_number][f"model_link_{model_number}"].setText(
                    '<span style="color:#4090FD";>Restrictions: </span><span style="color:#FF0000";><br>'
                    + model_info["restrictions"].replace("\n", "<br>")
                    + "</span>"
                )
            self.model_cards[model_number][f"model_img_{model_number}"].setPixmap(QPixmap(local_path))

        self.model_cards[model_number][f"model_card_frame_{model_number}"].mouseDoubleClickEvent = (
            lambda event, a=model_info["nickname"], b=model_info["source"], c=model_info[
                "imposed_vars"
            ], d=from_wizard: self.parent_ui.select_external_model(a, b, c, d)
        )

    def close(self):
        for i, model in enumerate(self.model_cards):
            model[f"model_card_frame_{i}"].setVisible(False)
        super().close()


class tour_window_Ui(QDialog):
    def __init__(
        self,
        dot_images: List[QIcon],
        parent_ui: main.MainWindow,
    ):
        """
        Creates the tour window.

        Parameters
        ----------
        parent_ui : MainWindow
            Main window.

        dot_images : List of icons
            Dot icons to be added into the bottom part of the tour window so the users knows where they are.
        """
        super(tour_window_Ui, self).__init__(parent_ui)
        self.basic_window = Ui_tour_window()
        self.basic_window.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.basic_window.bn_close.clicked.connect(self.close)
        self.basic_window.bn_close.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
        self.basic_window.ok_bn.clicked.connect(self.close)
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.current_tour_window = 1
        self.dot_images = dot_images

        self.basic_window.left_arrow_bn.clicked.connect(lambda: self.move_tour_view(self.current_tour_window - 1))
        self.basic_window.right_arrow_bn.clicked.connect(lambda: self.move_tour_view(self.current_tour_window + 1))
        self.basic_window.window1_bn.clicked.connect(lambda: self.move_tour_view(1))
        self.basic_window.window2_bn.clicked.connect(lambda: self.move_tour_view(2))
        self.basic_window.window3_bn.clicked.connect(lambda: self.move_tour_view(3))
        self.basic_window.window4_bn.clicked.connect(lambda: self.move_tour_view(4))
        self.basic_window.window5_bn.clicked.connect(lambda: self.move_tour_view(5))
        self.basic_window.window6_bn.clicked.connect(lambda: self.move_tour_view(6))
        self.max_windows = 6

        # Set all icons
        self.basic_window.window1_bn.setIcon(self.dot_images[0])
        self.basic_window.d1_label.setPixmap(
            QPixmap(resource_path(os.path.join("images", "tour", "description_page1.svg")))
        )
        for i in range(2, self.max_windows):
            getattr(self.basic_window, f"window{i}_bn").setIcon(self.dot_images[1])
            getattr(self.basic_window, f"d{i}_label").setPixmap(
                QPixmap(resource_path(os.path.join("images", "tour", f"description_page{i}.svg")))
            )
        getattr(self.basic_window, f"window{self.max_windows}_bn").setIcon(self.dot_images[1])
        self.basic_window.left_arrow_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "left_arrow.svg")))
        )
        self.basic_window.right_arrow_bn.setIcon(
            QPixmap(resource_path(os.path.join("images", "bn_images", "right_arrow.svg")))
        )
        self.basic_window.left_arrow_bn.setVisible(False)

    def set_biapy_version(
        self,
        version: Version | str,
    ):
        """
        Set BiaPy version number that is displayed in the tour window.

        Parameters
        ----------
        version : Version or str
            BiaPy version to display.
        """
        self.basic_window.presentation_version_text.setText(f"Version {str(version)}")
        self.basic_window.d5_release_notes_text.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">Check out version {str(version)} </span><a href=\"https://github.com/BiaPyX/BiaPy-GUI/releases/tag/v{str(version)}\"><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; text-decoration: underline; color:#0097a7; background-color:transparent;\">release notes</span></a><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">.</span></p></body></html>"
        )

    def move_tour_view(
        self,
        bn_number: int,
    ):
        """
        Moves the tour backward/forward.

        Parameters
        ----------
        bn_number : int
            Number of the window in the tour to move to.
        """
        self.current_tour_window = max(1, min(self.max_windows, bn_number))

        # Hide left/rigth arrows depending on the current window
        if self.current_tour_window == 1:
            self.basic_window.left_arrow_bn.setVisible(False)
        elif self.current_tour_window > 1:
            self.basic_window.left_arrow_bn.setVisible(True)
        if self.current_tour_window == self.max_windows:
            self.basic_window.right_arrow_bn.setVisible(False)
        elif self.current_tour_window < self.max_windows:
            self.basic_window.right_arrow_bn.setVisible(True)

        # Change page view
        if self.current_tour_window == 1:
            self.basic_window.stackedWidget.setCurrentWidget(self.basic_window.presentation_page)
        elif self.current_tour_window == 2:
            self.basic_window.stackedWidget.setCurrentWidget(self.basic_window.description_page1)
        elif self.current_tour_window == 3:
            self.basic_window.stackedWidget.setCurrentWidget(self.basic_window.description_page2)
        elif self.current_tour_window == 4:
            self.basic_window.stackedWidget.setCurrentWidget(self.basic_window.description_page3)
        elif self.current_tour_window == 5:
            self.basic_window.stackedWidget.setCurrentWidget(self.basic_window.description_page4)
        elif self.current_tour_window == 6:
            self.basic_window.stackedWidget.setCurrentWidget(self.basic_window.release_notes_page)

        # Adjust the progress dot
        for i in range(1, self.current_tour_window + 1):
            getattr(self.basic_window, f"window{i}_bn").setIcon(self.dot_images[0])

        for i in range(self.current_tour_window + 1, self.max_windows + 1):
            getattr(self.basic_window, f"window{i}_bn").setIcon(self.dot_images[1])


class modify_yaml_Ui(QDialog):
    def __init__(
        self,
        parent_ui: main.MainWindow,
    ):
        """
        Creates a window to inform the user about YAML discrepancies and allow them to go to the correct section.
        """
        super(modify_yaml_Ui, self).__init__()
        self.yaml_mod_window = Ui_Modify_YAML()
        self.yaml_mod_window.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.yaml_mod_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images", "bn_images", "info.png"))))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.parent_ui = parent_ui

        self.yaml_mod_window.train_data_input_browse_bn.clicked.connect(lambda: self.examine("DATA__TRAIN__PATH__INPUT", False))
        self.yaml_mod_window.train_data_gt_input_browse_bn.clicked.connect(lambda: self.examine("DATA__TRAIN__GT_PATH__INPUT", False))
        self.yaml_mod_window.val_data_input_browse_bn.clicked.connect(lambda: self.examine("DATA__VAL__PATH__INPUT", False))
        self.yaml_mod_window.val_data_gt_input_browse_bn.clicked.connect(lambda: self.examine("DATA__VAL__GT_PATH__INPUT", False))
        self.yaml_mod_window.test_data_input_browse_bn.clicked.connect(lambda: self.examine("DATA__TEST__PATH__INPUT", False))
        self.yaml_mod_window.test_data_gt_input_browse_bn.clicked.connect(lambda: self.examine("DATA__TEST__GT_PATH__INPUT", False))
        self.yaml_mod_window.checkpoint_file_path_browse_bn.clicked.connect(lambda: self.examine("PATHS__CHECKPOINT_FILE__INPUT", True))
        self.yaml_mod_window.create_config_bn.clicked.connect(self.save_new_yaml)
        self.loaded_cfg = None

        def moveErrorWindow(event: QEvent):
            """
            Move the error window.

            Parameters
            ----------
            event: QEvent
                Event that called this function.
            """
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.allow_instant_exit = False
        self.yaml_mod_window.frame_top.mouseMoveEvent = moveErrorWindow
        self.yaml_file = ""

        self.yaml_mod_window.DATA__TRAIN__PATH__INPUT.textChanged.connect(lambda: self.mark_syntax_error("DATA__TRAIN__PATH__INPUT"))
        self.yaml_mod_window.DATA__TRAIN__GT_PATH__INPUT.textChanged.connect(lambda: self.mark_syntax_error("DATA__TRAIN__GT_PATH__INPUT"))
        self.yaml_mod_window.DATA__VAL__PATH__INPUT.textChanged.connect(lambda: self.mark_syntax_error("DATA__VAL__PATH__INPUT"))
        self.yaml_mod_window.DATA__VAL__GT_PATH__INPUT.textChanged.connect(lambda: self.mark_syntax_error("DATA__VAL__GT_PATH__INPUT"))
        self.yaml_mod_window.DATA__TEST__PATH__INPUT.textChanged.connect(lambda: self.mark_syntax_error("DATA__TEST__PATH__INPUT"))
        self.yaml_mod_window.DATA__TEST__GT_PATH__INPUT.textChanged.connect(lambda: self.mark_syntax_error("DATA__TEST__GT_PATH__INPUT"))
        self.yaml_mod_window.PATHS__CHECKPOINT_FILE__INPUT.textChanged.connect(lambda: self.mark_syntax_error("PATHS__CHECKPOINT_FILE__INPUT"))

    def examine(self, save_in_obj_tag: str, is_file: bool = True) -> str:
        """
        Find an item in disk. Can be a file or a directory.

        Parameters
        ----------
        save_in_obj_tag : str
            Name of the widget to set the item's name into.

        is_file : bool, optional
            Whether the item to find is a file or a directory.
        """
        if not is_file:
            out = QFileDialog.getExistingDirectory(self, "Select a directory")
        else:
            out = QFileDialog.getOpenFileName()[0]

        if out == "":
            return out  # If no file was selected

        if save_in_obj_tag is not None:
            getattr(self.yaml_mod_window, save_in_obj_tag).setText(os.path.normpath(out))

        return out

    def mark_syntax_error(self, widget_name: str):
        """
        Marks syntax errors in the given widget.

        Parameters
        ----------
        widget_name : str
            Name of the widget to mark.
        """
        widget = getattr(self.yaml_mod_window, widget_name)
        file = widget.text()
        if not (is_pathname_valid(file) and os.path.exists(file)):
            widget.setStyleSheet("border: 2px solid red;")
        else:
            widget.setStyleSheet("border: 2px solid green;")

    def save_new_yaml(self):
        # Writing YAML file
        replace = True
        yaml_file = self.yaml_mod_window.cfg_file_path.text()
        if not is_pathname_valid(yaml_file):
            self.parent_ui.dialog_exec(
                "The YAML file path provided is not valid. Please check it and try again.",
                reason="error",
            )
            return
        basedir = os.path.dirname(yaml_file)
        
        if os.path.exists(yaml_file):
            self.parent_ui.yes_no_exec("The file '{}' already exists. Do you want to overwrite it?".format(yaml_file))
            assert self.parent_ui.yes_no
            replace = True if self.parent_ui.yes_no.answer else False
        if replace:
            self.parent_ui.logger.info("Creating YAML file")

            assert self.loaded_cfg is not None, "No configuration loaded to modify. BiaPy GUI internal error."
            train_path = self.yaml_mod_window.DATA__TRAIN__PATH__INPUT.text()
            val_path = self.yaml_mod_window.DATA__VAL__PATH__INPUT.text()
            test_path = self.yaml_mod_window.DATA__TEST__PATH__INPUT.text()
            train_gt_path = self.yaml_mod_window.DATA__TRAIN__GT_PATH__INPUT.text()
            val_gt_path = self.yaml_mod_window.DATA__VAL__GT_PATH__INPUT.text()
            test_gt_path = self.yaml_mod_window.DATA__TEST__GT_PATH__INPUT.text()
            chk_pt_path = self.yaml_mod_window.PATHS__CHECKPOINT_FILE__INPUT.text()
            
            if train_path != "" and "DATA" in self.loaded_cfg and "TRAIN" in self.loaded_cfg["DATA"]:
                if not (is_pathname_valid(train_path) and os.path.exists(train_path)):
                    self.parent_ui.dialog_exec(
                        "The training data path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["DATA"]["TRAIN"]["PATH"] = train_path

            if train_gt_path != "" and "DATA" in self.loaded_cfg and "TRAIN" in self.loaded_cfg["DATA"]:
                if not (is_pathname_valid(train_gt_path) and os.path.exists(train_gt_path)):
                    self.parent_ui.dialog_exec(
                        "The training ground truth path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["DATA"]["TRAIN"]["GT_PATH"] = train_gt_path
            if val_path != "" and "DATA" in self.loaded_cfg and "VAL" in self.loaded_cfg["DATA"]:
                if not (is_pathname_valid(val_path) and os.path.exists(val_path)):
                    self.parent_ui.dialog_exec(
                        "The validation data path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["DATA"]["VAL"]["PATH"] = val_path
            if val_gt_path != "" and "DATA" in self.loaded_cfg and "VAL" in self.loaded_cfg["DATA"]:
                if not (is_pathname_valid(val_gt_path) and os.path.exists(val_gt_path)):
                    self.parent_ui.dialog_exec(
                        "The validation ground truth path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["DATA"]["VAL"]["GT_PATH"] = val_gt_path
            if test_path != "" and "DATA" in self.loaded_cfg and "TEST" in self.loaded_cfg["DATA"]:
                if not (is_pathname_valid(test_path) and os.path.exists(test_path)):
                    self.parent_ui.dialog_exec(
                        "The test data path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["DATA"]["TEST"]["PATH"] = test_path
            if test_gt_path != "" and "DATA" in self.loaded_cfg and "TEST" in self.loaded_cfg["DATA"]:
                if not (is_pathname_valid(test_gt_path) and os.path.exists(test_gt_path)):
                    self.parent_ui.dialog_exec(
                        "The test ground truth path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["DATA"]["TEST"]["GT_PATH"] = test_gt_path
            if chk_pt_path != "" and "PATHS" in self.loaded_cfg:
                if not (is_pathname_valid(chk_pt_path) and os.path.exists(chk_pt_path)):
                    self.parent_ui.dialog_exec(
                        "The checkpoint file path provided does not exist. Please check it and try again.",
                        reason="error",
                    )
                    return
                self.loaded_cfg["PATHS"]["CHECKPOINT_FILE"] = chk_pt_path

            os.makedirs(basedir, exist_ok=True)
            with open(yaml_file, "w", encoding="utf8") as outfile:
                yaml.dump(self.loaded_cfg, outfile, default_flow_style=False)

            self.parent_ui.dialog_exec(
                "Configuration file saved successfully at '{}'.".format(yaml_file),
                "inform_user",
            )
            
            # Set Run window parameters accordingly
            out_write = os.path.basename(os.path.normpath(yaml_file))
            self.parent_ui.cfg.settings["yaml_config_filename"] = out_write
            self.parent_ui.cfg.settings["yaml_config_file_path"] = os.path.dirname(basedir)
            self.parent_ui.ui.job_name_input.setPlainText(os.path.splitext(out_write)[0])
            self.parent_ui.ui.select_yaml_name_label.setText(os.path.normpath(yaml_file))
            change_page(self.parent_ui, "bn_run_biapy", 99)

            self.allow_instant_exit = True
            self.close()

    def closeEvent(self, event: QCloseEvent):
        """
        Close event handler.

        Parameters
        ----------
        event: QCloseEvent
            Event that called this function.
        """
        if self.allow_instant_exit:
            event.accept()
            return True
        
        self.parent_ui.yes_no_exec("Are you sure you want to exit editing the configuration file? It may not work properly if you do so.")
        assert self.parent_ui.yes_no
        if self.parent_ui.yes_no.answer:
            event.accept()
            return True
        else:
            event.ignore()
            return False

    def reject(self):
        event = QCloseEvent()
        if self.closeEvent(event):
            super().reject()  # only close if accepted

    def mousePressEvent(self, event: QEvent):
        """
        Mouse press event handler.

        Parameters
        ----------
        event: QEvent
            Event that called this function.
        """
        self.dragPos = event.globalPos()

    def clear_display(self):
        self.allow_instant_exit = False
        self.yaml_mod_window.train_label.setVisible(False)
        self.yaml_mod_window.train_frame.setVisible(False)
        self.yaml_mod_window.DATA__TRAIN__PATH__INPUT.setText("")
        self.yaml_mod_window.train_gt_path_frame.setVisible(False)
        self.yaml_mod_window.DATA__TRAIN__GT_PATH__INPUT.setText("")

        self.yaml_mod_window.val_label.setVisible(False)
        self.yaml_mod_window.val_frame.setVisible(False)
        self.yaml_mod_window.DATA__VAL__PATH__INPUT.setText("")
        self.yaml_mod_window.val_gt_path_frame.setVisible(False)
        self.yaml_mod_window.DATA__VAL__GT_PATH__INPUT.setText("")

        self.yaml_mod_window.test_label.setVisible(False)
        self.yaml_mod_window.test_frame.setVisible(False)
        self.yaml_mod_window.DATA__TEST__PATH__INPUT.setText("")
        self.yaml_mod_window.test_gt_path_frame.setVisible(False)
        self.yaml_mod_window.DATA__TEST__GT_PATH__INPUT.setText("")
    
    def display_discrepancies(self, paths_to_change: Dict[str, str], checkpoint_needed: bool = False, yaml_file: str = "", loaded_cfg: Dict = {}):
        """
        Sets the message of the window.

        Parameters
        ----------
        paths_to_change : dict[str, bool]
            Dictionary of paths to change and their status.
        """
        self.clear_display()
        for key, path in paths_to_change.items():
            if "TRAIN" in key:
                self.yaml_mod_window.train_frame.setVisible(True)
                self.yaml_mod_window.train_label.setVisible(True)
                if "GT" in key:
                    self.yaml_mod_window.train_gt_path_frame.setVisible(True)
                    self.yaml_mod_window.DATA__TRAIN__GT_PATH__INPUT.setText(path)
                else:
                    self.yaml_mod_window.train_frame.setVisible(True)
                    self.yaml_mod_window.DATA__TRAIN__PATH__INPUT.setText(path)
            elif "VAL" in key:
                self.yaml_mod_window.val_frame.setVisible(True)
                self.yaml_mod_window.val_label.setVisible(True)
                if "GT" in key:
                    self.yaml_mod_window.val_gt_path_frame.setVisible(True)
                    self.yaml_mod_window.DATA__VAL__GT_PATH__INPUT.setText(path)
                else:
                    self.yaml_mod_window.val_frame.setVisible(True)
                    self.yaml_mod_window.DATA__VAL__PATH__INPUT.setText(path)
            elif "TEST" in key:
                self.yaml_mod_window.test_frame.setVisible(True)
                self.yaml_mod_window.test_label.setVisible(True)
                if "GT" in key:
                    self.yaml_mod_window.test_gt_path_frame.setVisible(True)
                    self.yaml_mod_window.DATA__TEST__GT_PATH__INPUT.setText(path)
                else:
                    self.yaml_mod_window.test_frame.setVisible(True)
                    self.yaml_mod_window.DATA__TEST__PATH__INPUT.setText(path)

        # Ask for checkpoint file if needed
        if checkpoint_needed:
            self.yaml_mod_window.checkpoint_label.setVisible(True)
            self.yaml_mod_window.checkpoint_frame.setVisible(True)
            path = "" if "PATHS" not in loaded_cfg or "CHECKPOINT_FILE" not in loaded_cfg["PATHS"] else loaded_cfg["PATHS"]["CHECKPOINT_FILE"]
            self.yaml_mod_window.PATHS__CHECKPOINT_FILE__INPUT.setText(path)
        else:
            self.yaml_mod_window.checkpoint_label.setVisible(False)
            self.yaml_mod_window.checkpoint_frame.setVisible(False)

        self.yaml_mod_window.cfg_file_path.setText(yaml_file.replace(".yml", "_modified.yml").replace(".yaml", "_modified.yaml"))
        self.loaded_cfg = loaded_cfg