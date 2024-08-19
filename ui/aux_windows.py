import os
import pooch
from functools import partial

from PySide2 import QtCore
from PySide2.QtCore import ( QCoreApplication, QRect, QSize, Qt, QEvent)
from PySide2.QtGui import (QDesktopServices, QColor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_utils import mark_syntax_error, resource_path, change_page
from ui.ui_dialog import Ui_Dialog 
from ui.ui_yes_no import Ui_yes_no 
from ui.spinner import Ui_spinner
from ui.ui_basic import Ui_basic 
from ui.ui_model_carrousel import Ui_model_card_carrousel_dialog 

from ui.ui_workflow_info import Ui_Workflow_info 
from aux_classes.waitingspinnerwidget import QtWaitingSpinner

class workflow_explanation_Ui(QDialog):
    def __init__(self, parent=None):

        super(workflow_explanation_Ui, self).__init__(parent)
        self.workflow_info_window = Ui_Workflow_info()
        self.workflow_info_window.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.workflow_info_window.bn_close.clicked.connect(self.close)
        self.workflow_info_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
        self.workflow_info_window.ok_bn.clicked.connect(self.close)
        self.workflow_info_window.workflow_description_label.setOpenExternalLinks(True)
        self.workflow_info_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.workflow_info_window.window_des_label.setText("Workflow information")
        self.number_of_ready_to_use_examples = 10
        self.signals_created = False

        self.dragPos = self.pos()  
        def movedialogWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.workflow_info_window.frame_top.mouseMoveEvent = movedialogWindow  

        # Create ready to use example's frames 
        icon1 = QIcon()
        icon1.addFile(resource_path(os.path.join("images","ready_to_use_examples","dataset_bn.svg")), QSize(), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addFile(resource_path(os.path.join("images","ready_to_use_examples","template_bn.svg")), QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.ready_to_use_examples_frames = []
        self.ready_to_use_examples_images = []
        self.ready_to_use_examples_headings = []
        self.ready_to_use_examples_datasets = []
        self.ready_to_use_examples_templates = []
        self.ready_to_use_examples_signals_created = []
        for i in range(self.number_of_ready_to_use_examples):
            # Create the frame
            self.ready_to_use_examples_frames.append(QFrame(self.workflow_info_window.ready_to_use_samples_frame))
            self.ready_to_use_examples_frames[-1].setObjectName(u"ready_to_use_examples_frame_{}".format(i))
            self.ready_to_use_examples_frames[-1].setStyleSheet(
                "#ready_to_use_examples_frame_{}".format(i)+
                "{\nborder: 2px solid rgb(64,144,253);\nborder-radius: 15px;\n}")
            self.ready_to_use_examples_frames[-1].setFrameShape(QFrame.StyledPanel)
            self.ready_to_use_examples_frames[-1].setFrameShadow(QFrame.Raised)
            self.ready_to_use_examples_frames[-1].setMaximumSize(QSize(360, 143))
            self.ready_to_use_examples_frames[-1].setMinimumSize(QSize(360, 143))
            self.workflow_info_window.gridLayout_2.addWidget(self.ready_to_use_examples_frames[-1], i//2, i%2, 1, 1)

            # Image
            self.ready_to_use_examples_images.append(QLabel(self.ready_to_use_examples_frames[-1]))
            self.ready_to_use_examples_images[-1].setObjectName("ready_to_use_examples_image_{}".format(i))
            self.ready_to_use_examples_images[-1].setGeometry(QRect(20, 34, 91, 91))
            self.ready_to_use_examples_images[-1].setPixmap(QPixmap(u"images/ready_to_use_examples/classification_2d_butterfly.jpg"))
            self.ready_to_use_examples_images[-1].setScaledContents(True)

            # Heading
            self.ready_to_use_examples_headings.append(QLabel(self.ready_to_use_examples_frames[-1]))
            self.ready_to_use_examples_headings[-1].setObjectName("ready_to_use_examples_head_{}".format(i))
            self.ready_to_use_examples_headings[-1].setGeometry(QRect(13, 10, 330, 20))
            self.ready_to_use_examples_headings[-1].setFont(font)

            # Dataset bn
            self.ready_to_use_examples_datasets.append(QPushButton(self.ready_to_use_examples_frames[-1]))
            self.ready_to_use_examples_datasets[-1].setObjectName("ready_to_use_examples_dataset_{}".format(i))
            self.ready_to_use_examples_datasets[-1].setGeometry(QRect(130, 34, 155, 41))
            self.ready_to_use_examples_datasets[-1].setIcon(icon1)
            self.ready_to_use_examples_datasets[-1].setIconSize(QSize(133, 41))
            self.ready_to_use_examples_datasets[-1].setStyleSheet(u"QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgb(255,255,255);\n"
            "	border-radius: 15px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(255,255,255);\n"
            "	border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(255,255,255);\n"
            "	border: 2px solid rgb(0, 0, 0);\n"
            "}")
            self.ready_to_use_examples_datasets[-1].setToolTip("<html><head/><body><p><span style=\" font-size:12pt;\">"
                "Download dataset</span></p></body></html>")

            # Template bn         
            self.ready_to_use_examples_templates.append(QPushButton(self.ready_to_use_examples_frames[-1]))
            self.ready_to_use_examples_templates[-1].setObjectName("ready_to_use_examples_temp_{}".format(i))
            self.ready_to_use_examples_templates[-1].setGeometry(QRect(130, 84, 155, 41))
            self.ready_to_use_examples_templates[-1].setIcon(icon2)
            self.ready_to_use_examples_templates[-1].setIconSize(QSize(133, 41))
            self.ready_to_use_examples_templates[-1].setStyleSheet(u"QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgb(255,255,255);\n"
            "	border-radius: 15px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(255,255,255);\n"
            "	border: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(255,255,255);\n"
            "	border: 2px solid rgb(0, 0, 0);\n"
            "}")
            self.ready_to_use_examples_templates[-1].setToolTip("<html><head/><body><p><span style=\" font-size:12pt;\">"
                "Download template</span></p></body></html>")
            
            self.ready_to_use_examples_signals_created.append(False)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def openlink(self, link):
        QDesktopServices.openUrl(link)

    def infoConstrict(self, workflow_name, input_img, gt_img, workflow_description, 
        workflow_doc, workflow_ready_to_use_examples):
        self.workflow_info_window.workflow_name_label.setText(workflow_name)
        self.workflow_info_window.input_image_label.setPixmap(input_img)
        self.workflow_info_window.gt_image_label.setPixmap(gt_img)
        self.workflow_info_window.workflow_description_label.setText(workflow_description)
        if workflow_name in ["Image denoising", "Super resolution", "Self-supervised learning"]:
            self.workflow_info_window.gt_description_label.setText("Output")
        else:
            self.workflow_info_window.gt_description_label.setText("Ground truth")

        if self.signals_created:
            self.workflow_info_window.documentation_bn.clicked.disconnect() 
        
        self.workflow_info_window.documentation_bn.clicked.connect(lambda: self.openlink(workflow_doc))
        self.workflow_info_window.documentation_bn.setToolTip("<html><head/><body><p><span style=\" font-size:12pt;\">"
                "Open {} documentation</span></p></body></html>".format(workflow_name.lower()))

        c = 0
        for x in workflow_ready_to_use_examples:
            self.ready_to_use_examples_headings[c].setText(x['name'])
            self.ready_to_use_examples_images[c].setPixmap(x['image'])
            # Control if at least one signal was added so we can disconnect it
            if self.ready_to_use_examples_signals_created[c]:
                self.ready_to_use_examples_datasets[c].clicked.disconnect()
                self.ready_to_use_examples_templates[c].clicked.disconnect()
            else:
                self.ready_to_use_examples_signals_created[c] = True
            self.ready_to_use_examples_datasets[c].clicked.connect(partial(self.openlink, x['data']))
            self.ready_to_use_examples_templates[c].clicked.connect(partial(self.openlink, x['template']))
            self.ready_to_use_examples_frames[c].setVisible(True)
            c += 1

        # Hide the rest not used 
        for i in range(c, self.number_of_ready_to_use_examples):
            self.ready_to_use_examples_frames[i].setVisible(False)

        self.signals_created = True

class dialog_Ui(QDialog):
    def __init__(self, parent_ui=None):

        super(dialog_Ui, self).__init__()
        self.dialog_window = Ui_Dialog()
        self.original_width = self.geometry().width()
        self.parent_ui = parent_ui
        self.dialog_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.upbar_icon = [QPixmap(resource_path(os.path.join("images","bn_images","error.png"))),
                           QPixmap(resource_path(os.path.join("images","bn_images","info.png")))]
        self.dragPos = self.pos()  
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")

        def moveErrorWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.signals_created = False
        self.dialog_window.frame_top.mouseMoveEvent = moveErrorWindow  

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def dialog_constrict(self, message, reason):
        self.resize(self.original_width,self.geometry().height())
        self.dialog_window.window_des_label.setText("Error")
        self.dialog_window.icon_label.setPixmap(self.upbar_icon[0])
        if self.signals_created:
            self.dialog_window.go_to_correct_bn.clicked.disconnect() 
        else:
            self.signals_created = True
        if reason is not None:
            if reason == "load_yaml_error":
                self.dialog_window.window_des_label.setText("Error")
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"OK", None))
                self.dialog_window.error_message_label.setText("Configuration file not loaded because of the following errors:\n{}".format(message))
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            elif reason == "load_yaml_ok_but_errors":
                self.dialog_window.icon_label.setPixmap(self.upbar_icon[1])
                self.dialog_window.window_des_label.setText("Information")
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("OK", u"OK", None))
                m = "Configuration file loaded but with some errors. Please send BiaPy developers\
                    the following errors:"
                for i, mes in enumerate(message):
                    m += "\n"+str(i+1)+". {}".format(mes)
                self.dialog_window.error_message_label.setText(m)
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            elif reason in ["inform_user", "inform_user_and_go"]:
                self.resize(0.9*self.parent_ui.width(),self.geometry().height())
                self.dialog_window.error_message_label.setWordWrap(True)
                self.dialog_window.icon_label.setPixmap(self.upbar_icon[1])
                self.dialog_window.window_des_label.setText("Information")
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("OK", u"OK", None))
                self.dialog_window.error_message_label.setText(message)
                self.dialog_window.go_to_correct_bn.clicked.connect(lambda: self.redirect_and_close(reason))
            elif reason == "error":
                self.dialog_window.window_des_label.setText("Error")
                self.dialog_window.error_message_label.setText("{}".format(message))
                self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"OK", None))
                self.dialog_window.go_to_correct_bn.clicked.connect(self.close)
            else:
                self.dialog_window.error_message_label.setWordWrap(True)
                if reason == "docker_installation":
                    self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"OK", None))
                else:
                    self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"Go to correct", None))
                self.dialog_window.go_to_correct_bn.clicked.connect(lambda: self.redirect_and_close(reason))
                self.dialog_window.error_message_label.setText(message)
        else:
            self.dialog_window.error_message_label.setText("This error was not expected. Please contact BiaPy developers with the following message:\n\n"+message)
            self.dialog_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"Close BiaPy GUI", None))
            self.dialog_window.go_to_correct_bn.clicked.connect(self.close_all)

    def closeEvent(self, event):
        self.dialog_window.error_message_label.setWordWrap(False)
        self.dialog_window.go_to_correct_bn.click()

    def close_all(self):
        self.close()
        if self.parent_ui is not None:
            self.parent_ui.close()

    def redirect_and_close(self, reason):
        if reason == "jobname":
            change_page(self.parent_ui, 'bn_run_biapy', 99)
        elif reason == "inform_user_and_go":
            change_page(self.parent_ui, 'bn_workflow', 99)
        elif reason == "yaml_config_file_path":
            change_page(self.parent_ui, 'bn_goptions', 99)
            mark_syntax_error(self.parent_ui, "goptions_browse_yaml_path_input", ["empty", "exists"])
        elif reason == "output_folder":
            change_page(self.parent_ui, 'bn_run_biapy', 99)
            mark_syntax_error(self.parent_ui, "output_folder_input", ["empty"])
        elif reason == "select_yaml_name_label":
            change_page(self.parent_ui, 'bn_run_biapy',99)
            mark_syntax_error(self.parent_ui, "select_yaml_name_label", ["empty"])
        elif reason == "goptions_yaml_name_input":
            change_page(self.parent_ui, 'bn_goptions',99)
            mark_syntax_error(self.parent_ui, "goptions_yaml_name_input", ["empty"])
        elif reason == "docker_installation":
            change_page(self.parent_ui, 'bn_home',99)
        self.close()
    
class yes_no_Ui(QDialog):
    def __init__(self, parent=None):
        super(yes_no_Ui, self).__init__(parent)
        self.yes_no_window = Ui_yes_no()
        self.yes_no_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.yes_no_window.yes_bn.clicked.connect(lambda: self.submitclose(True))
        self.yes_no_window.no_bn.clicked.connect(lambda: self.submitclose(False))
        self.yes_no_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","question.png"))))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.answer = False 

    def create_question(self, question):
        self.yes_no_window.question_label.setText(question)

    def submitclose(self, answer):
        self.answer = answer 
        self.accept()

class spinner_Ui(QDialog):
    def __init__(self, parent=None):
        super(spinner_Ui, self).__init__()
        self.spinner_window = Ui_spinner()
        self.spinner_window.setupUi(self)
        self.parent = parent 

        # Create spinner 
        self.spinner = QtWaitingSpinner(parent, True, True)
        self.spinner.setRoundness(150.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(8)
        self.spinner.setLineLength(40)
        self.spinner.setLineWidth(20)
        self.spinner.setInnerRadius(30)
        self.spinner.setRevolutionsPerSecond(0.5)
        self.spinner.setColor(QColor(64,144,253))
        self.spinner_window.verticalLayout.addWidget(self.spinner)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(Qt.WA_TranslucentBackground)

    def stop(self):
        self.spinner.stop()
        self.close()

    def start(self):
        self.spinner.start()
        
    def closeEvent(self, event):
        try:
            self.parent.worker_spin.state_signal.emit(1)
        except Exception as e:
            print(f"Possible expected error during closing spin window: {e}")
        self.spinner.stop()
        super().close()

class basic_Ui(QDialog):
    def __init__(self, parent=None):
        super(basic_Ui, self).__init__(parent)
        self.basic_window = Ui_basic()
        self.basic_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.basic_window.bn_close.clicked.connect(self.close)
        self.basic_window.ok_bn.clicked.connect(self.close)
        self.basic_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
        self.basic_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.basic_window.message_label.setOpenExternalLinks(True)

    def set_info(self, text):
        self.basic_window.message_label.setText(text)


class model_card_carrousel_Ui(QDialog):
    def __init__(self, parent=None):
        super(model_card_carrousel_Ui, self).__init__()
        self.model_carrousel_window = Ui_model_card_carrousel_dialog()
        self.model_carrousel_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.model_carrousel_window.bn_close.clicked.connect(self.close)
        self.model_carrousel_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","close_icon.png"))))
        self.model_carrousel_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.parent = parent

        # Create base font
        self.font = QFont()
        self.font.setFamily(u"DejaVu Math TeX Gyre")
        self.font.setPointSize(12)      

        self.total_model_cards_created = 0
        self.model_cards = []
        self.model_row, self.model_col = -1, 0
        self.source_logo = []
        self.source_logo.append(QPixmap(resource_path(os.path.join("images","bmz_logo.png"))))
        self.source_logo.append(QPixmap(resource_path(os.path.join("images","torchvision_logo.png"))))

    def create_model_card(self, model_number, model_info):
        print("Creating model card . . .")
        # Create model card the first time (future checks will reuse the widgets)
        if model_number > (self.total_model_cards_created - 1):
            self.model_cards.append({})

            self.model_cards[model_number][f"model_card_frame_{model_number}"] = QFrame(self.model_carrousel_window.scrollAreaWidgetContents)
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setObjectName(f"model_card_frame_{model_number}")
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setMinimumSize(QSize(800, 200))
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setMaximumSize(QSize(435, 400))
            self.model_cards[model_number][f"model_card_frame_{model_number}"].setStyleSheet(f"#model_card_frame_{model_number}"" {\n"
                "border: 2px solid rgb(120,120,120);\n"
                "border-radius: 15px;\n"
                "}\n"
                "\n"
                f"#model_card_frame_{model_number}:hover"" {\n"
                "	background-color: rgb(240,240,240);\n"
                "	border: 2px solid rgb(64, 144, 253);\n"
                "   border-radius: 15px;\n"
                "}")           
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"] = QVBoxLayout(self.model_cards[model_number][f"model_card_frame_{model_number}"])
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].setObjectName(f"verticalLayout_5_{model_number}")
            self.model_cards[model_number][f"model_name_{model_number}"] = QLabel(self.model_cards[model_number][f"model_card_frame_{model_number}"])
            self.model_cards[model_number][f"model_name_{model_number}"].setObjectName(f"model_name_{model_number}")
            self.model_cards[model_number][f"model_name_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_name_{model_number}"].setStyleSheet(u"color: rgb(64,144,253);\n"
                "font-weight:bold;\nbackground-color:rgba(0, 0, 0, 0);")
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].addWidget(self.model_cards[model_number][f"model_name_{model_number}"], 0, Qt.AlignHCenter)
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"] = QFrame(self.model_cards[model_number][f"model_card_frame_{model_number}"])
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setObjectName(f"frame_2model_source_from_frame_{model_number}")
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"].setStyleSheet('background-color:rgba(0, 0, 0, 0);') 
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"] = QHBoxLayout(self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"])
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].setObjectName(f"horizontalLayout_4{model_number}")
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].setContentsMargins(5, 5, 5, 5)
            self.model_cards[model_number][f"model_source_from_text_{model_number}"] = QLabel(self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"])
            self.model_cards[model_number][f"model_source_from_text_{model_number}"].setObjectName(f"model_source_from_text_{model_number}")
            self.model_cards[model_number][f"model_source_from_text_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_source_from_text_{model_number}"].setStyleSheet(u"color: rgb(120,120,120); font-size: 11px;")
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].addWidget(self.model_cards[model_number][f"model_source_from_text_{model_number}"])
            self.model_cards[model_number][f"model_source_icon_{model_number}"] = QLabel(self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"])
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setObjectName(f"model_source_icon_{model_number}")
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setMinimumSize(QSize(30, 30))
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setMaximumSize(QSize(30, 30))
            self.model_cards[model_number][f"model_source_icon_{model_number}"].setScaledContents(True)
            self.model_cards[model_number][f"horizontalLayout_4{model_number}"].addWidget(self.model_cards[model_number][f"model_source_icon_{model_number}"])
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].addWidget(self.model_cards[model_number][f"frame_2model_source_from_frame_{model_number}"], 0, Qt.AlignHCenter)
            self.model_cards[model_number][f"model_card_subframe_{model_number}"] = QFrame(self.model_cards[model_number][f"model_card_frame_{model_number}"])
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setObjectName(f"model_card_subframe_{model_number}")
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setMinimumSize(QSize(0, 160))
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"model_card_subframe_{model_number}"].setStyleSheet('background-color:rgba(0, 0, 0, 0);') 
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"] = QHBoxLayout(self.model_cards[model_number][f"model_card_subframe_{model_number}"])
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"].setObjectName(f"horizontalLayout_2{model_number}")
            self.model_cards[model_number][f"model_img_{model_number}"] = QLabel(self.model_cards[model_number][f"model_card_subframe_{model_number}"])
            self.model_cards[model_number][f"model_img_{model_number}"].setObjectName(f"model_img_{model_number}")
            self.model_cards[model_number][f"model_img_{model_number}"].setMinimumSize(QSize(130, 130))
            self.model_cards[model_number][f"model_img_{model_number}"].setMaximumSize(QSize(130, 130))
            self.model_cards[model_number][f"model_img_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_img_{model_number}"].setScaledContents(True)
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"].addWidget(self.model_cards[model_number][f"model_img_{model_number}"])
            self.model_cards[model_number][f"model_info_frame_{model_number}"] = QFrame(self.model_cards[model_number][f"model_card_subframe_{model_number}"])
            self.model_cards[model_number][f"model_info_frame_{model_number}"].setObjectName(f"model_info_frame_{model_number}")
            self.model_cards[model_number][f"model_info_frame_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"model_info_frame_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"gridLayout{model_number}"] = QGridLayout(self.model_cards[model_number][f"model_info_frame_{model_number}"])
            self.model_cards[model_number][f"gridLayout{model_number}"].setObjectName(f"gridLayout{model_number}")
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"] = QFrame(self.model_cards[model_number][f"model_info_frame_{model_number}"])
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"].setObjectName(f"model_nick_id_frame_{model_number}")
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"].setFrameShape(QFrame.NoFrame)
            self.model_cards[model_number][f"model_nick_id_frame_{model_number}"].setFrameShadow(QFrame.Raised)
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"] = QHBoxLayout(self.model_cards[model_number][f"model_nick_id_frame_{model_number}"])
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].setObjectName(f"horizontalLayout_3{model_number}")
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].setContentsMargins(0, 0, 0, 0)
            self.model_cards[model_number][f"model_nickname_{model_number}"] = QLabel(self.model_cards[model_number][f"model_nick_id_frame_{model_number}"])
            self.model_cards[model_number][f"model_nickname_{model_number}"].setObjectName(f"model_nickname_{model_number}")
            self.model_cards[model_number][f"model_nickname_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].addWidget(self.model_cards[model_number][f"model_nickname_{model_number}"])
            self.model_cards[model_number][f"model_id_{model_number}"] = QLabel(self.model_cards[model_number][f"model_nick_id_frame_{model_number}"])
            self.model_cards[model_number][f"model_id_{model_number}"].setObjectName(f"model_id_{model_number}")
            self.model_cards[model_number][f"model_id_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"horizontalLayout_3{model_number}"].addWidget(self.model_cards[model_number][f"model_id_{model_number}"])
            self.model_cards[model_number][f"gridLayout{model_number}"].addWidget(self.model_cards[model_number][f"model_nick_id_frame_{model_number}"], 0, 0, 1, 1)
            self.model_cards[model_number][f"model_description_{model_number}"] = QLabel(self.model_cards[model_number][f"model_info_frame_{model_number}"])
            self.model_cards[model_number][f"model_description_{model_number}"].setObjectName(f"model_description_{model_number}")
            self.model_cards[model_number][f"model_description_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_description_{model_number}"].setWordWrap(True)
            self.model_cards[model_number][f"gridLayout{model_number}"].addWidget(self.model_cards[model_number][f"model_description_{model_number}"], 1, 0, 1, 1)
            self.model_cards[model_number][f"model_link_{model_number}"] = QLabel(self.model_cards[model_number][f"model_info_frame_{model_number}"])
            self.model_cards[model_number][f"model_link_{model_number}"].setObjectName(f"model_link_{model_number}")
            self.model_cards[model_number][f"model_link_{model_number}"].setFont(self.font)
            self.model_cards[model_number][f"model_link_{model_number}"].setWordWrap(True)
            self.model_cards[model_number][f"model_link_{model_number}"].setOpenExternalLinks(True)
            self.model_cards[model_number][f"gridLayout{model_number}"].addWidget(self.model_cards[model_number][f"model_link_{model_number}"], 2, 0, 1, 1)
            self.model_cards[model_number][f"horizontalLayout_2{model_number}"].addWidget(self.model_cards[model_number][f"model_info_frame_{model_number}"])
            self.model_cards[model_number][f"verticalLayout_5_{model_number}"].addWidget(self.model_cards[model_number][f"model_card_subframe_{model_number}"])
            self.model_carrousel_window.verticalLayout_6.addWidget(self.model_cards[model_number][f"model_card_frame_{model_number}"])

            self.model_cards[model_number][f"model_card_frame_{model_number}"].mousePressEvent = lambda event, a=model_info['nickname'],b=model_info['source']: self.parent.select_external_model(a,b)

            self.total_model_cards_created += 1

        # Set model description accordingly 
        try:
            local_path = pooch.retrieve(model_info['covers'], known_hash=None)
        except: 
            local_path = os.path.join("images", "bmz_model_not_found.png")
        local_path = resource_path(local_path)
        self.model_cards[model_number][f"model_name_{model_number}"].setText(model_info['name'])
        self.model_cards[model_number][f"model_source_from_text_{model_number}"].setText("from " + model_info['source'])
        source_logo = self.source_logo[0] if model_info['source'] == "BioImage Model Zoo" else self.source_logo[1]
        self.model_cards[model_number][f"model_source_icon_{model_number}"].setPixmap(source_logo)
        self.model_cards[model_number][f"model_nickname_{model_number}"].setText("<span style='color:#4090FD';>Name: </span>" + model_info['nickname']+" (" + model_info['nickname_icon'] + ")")
        self.model_cards[model_number][f"model_id_{model_number}"].setText("<span style=\"color:#4090FD\";>ID: </span>"  + model_info['id'])
        self.model_cards[model_number][f"model_description_{model_number}"].setText("<span style=\"color:#4090FD\";>Description: </span>"  + model_info['description'])
        self.model_cards[model_number][f"model_link_{model_number}"].setText("<span style=\"color:#4090FD\";>URL: </span> <a href=\""+  model_info['url'] + "\">"+model_info['url']+"</a>")
        self.model_cards[model_number][f"model_img_{model_number}"].setPixmap(QPixmap(local_path))
