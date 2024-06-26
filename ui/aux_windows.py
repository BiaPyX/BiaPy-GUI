import os
from functools import partial

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QThread, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QDesktopServices, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_utils import mark_syntax_error, resource_path, change_page
from ui.ui_dialog import Ui_Dialog 
from ui.ui_yes_no import Ui_yes_no 
from ui.spinner import Ui_spinner
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