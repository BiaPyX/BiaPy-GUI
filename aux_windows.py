import os

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QThread, QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_dialog import Ui_Dialog 
from ui_error import Ui_Error 
from ui_yes_no import Ui_yes_no 
from ui_workflow_info import Ui_Workflow_info 
from ui_utils import mark_syntax_error, resource_path, buttonPressed

class workflow_explanation_Ui(QDialog):
    def __init__(self, parent=None):

        super(workflow_explanation_Ui, self).__init__(parent)
        self.workflow_info_window = Ui_Workflow_info()
        self.workflow_info_window.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.workflow_info_window.bn_close.clicked.connect(self.close)
        self.workflow_info_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","closeAsset 43.png"))))
        self.workflow_info_window.ok_bn.clicked.connect(self.close)
        self.workflow_info_window.workflow_description_label.setOpenExternalLinks(True)
        self.workflow_info_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))).scaledToWidth(40,aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")

        self.dragPos = self.pos()  
        def movedialogWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.workflow_info_window.frame_top.mouseMoveEvent = movedialogWindow  

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def infoConstrict(self, workflow_name, input_img, gt_img, workflow_description):
        self.workflow_info_window.workflow_name_label.setText(workflow_name)
        self.workflow_info_window.input_image_label.setPixmap(input_img)
        self.workflow_info_window.gt_image_label.setPixmap(gt_img)
        self.workflow_info_window.workflow_description_label.setText(workflow_description)
        if workflow_name in ["Image denoising", "Super resolution", "Self-supervised learning"]:
            self.workflow_info_window.gt_description_label.setText("Output")
        else:
            self.workflow_info_window.gt_description_label.setText("Ground truth")

class dialog_Ui(QDialog):
    def __init__(self, parent=None):

        super(dialog_Ui, self).__init__(parent)
        self.info_window = Ui_Dialog()
        self.info_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.info_window.bn_min.clicked.connect(self.showMinimized)
        self.info_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","hideAsset 53.png.png"))))
        self.info_window.bn_close.clicked.connect(self.close)
        self.info_window.bn_close.setIcon(QPixmap(resource_path(os.path.join("images","bn_images","closeAsset 43.png"))))
        self.info_window.ok_bn.clicked.connect(self.close)
        self.info_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))).scaledToWidth(40,aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")

        self.dragPos = self.pos()  
        def movedialogWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.info_window.frame_top.mouseMoveEvent = movedialogWindow  

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def dialog_constrict(self, message):
        self.info_window.yaml_path_label.setText(message)

class error_Ui(QDialog):
    def __init__(self, parent_ui=None):

        super(error_Ui, self).__init__()
        self.error_window = Ui_Error()
        self.parent_ui = parent_ui
        self.error_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.upbar_icon = [QPixmap(resource_path(os.path.join("images","bn_images","error.png"))),
                           QPixmap(resource_path(os.path.join("images","bn_images","info.png"))).scaledToWidth(40,aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)]
        self.dragPos = self.pos()  
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")

        def moveErrorWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.error_window.frame_top.mouseMoveEvent = moveErrorWindow  
        self.setVisible(False)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def error_constrict(self, message, reason):
        self.setVisible(False)
        if reason is not None:
            if reason == "main_window_error":
                self.setFixedSize(self.width(), 235)
                self.error_window.icon_label.setPixmap(self.upbar_icon[0])
                self.error_window.error_message_label.setText("<b>This error was not expected. Please contact BiaPy developers copying the output of the temporary file: {}".format(message))
                self.error_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"Close BiaPy GUI", None))
                self.error_window.go_to_correct_bn.clicked.connect(self.close_all)
            else:
                self.setFixedSize(self.width(), self.minimumSizeHint().height())
                self.error_window.icon_label.setPixmap(self.upbar_icon[1])
                if reason == "docker_installation":
                    self.error_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"OK", None))
                else:
                    self.error_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"Go to correct", None))
                self.error_window.go_to_correct_bn.clicked.connect(lambda: self.run_func_and_close(reason))
                self.error_window.error_message_label.setText(message)
        else:
            self.setFixedSize(self.width(), 235)
            self.error_window.icon_label.setPixmap(self.upbar_icon[0])
            self.error_window.error_message_label.setText("<b>This error was not expected. Please contact BiaPy developers with the following message:</b><br><br>"+message)
            self.error_window.go_to_correct_bn.setText(QCoreApplication.translate("Error", u"Close BiaPy GUI", None))
            self.error_window.go_to_correct_bn.clicked.connect(self.close_all)
        self.setVisible(True)

    def close_all(self):
        self.close()
        if self.parent_ui is not None:
            self.parent_ui.close()

    def run_func_and_close(self, reason):
        if reason == "jobname":
            buttonPressed(self.parent_ui, 'bn_run_biapy', 99)
        elif reason == "yaml_config_file_path":
            buttonPressed(self.parent_ui, 'bn_goptions', 99)
            mark_syntax_error(self.parent_ui, "goptions_browse_yaml_path_input", ["empty", "exists"])
        elif reason == "output_folder":
            buttonPressed(self.parent_ui, 'bn_run_biapy', 99)
            mark_syntax_error(self.parent_ui, "output_folder_input", ["empty"])
        elif reason == "select_yaml_name_label":
            buttonPressed(self.parent_ui, 'bn_run_biapy',99)
            mark_syntax_error(self.parent_ui, "select_yaml_name_label", ["empty"])
        elif reason == "goptions_yaml_name_input":
            buttonPressed(self.parent_ui, 'bn_goptions',99)
            mark_syntax_error(self.parent_ui, "goptions_yaml_name_input", ["empty"])
        elif reason == "docker_installation":
            buttonPressed(self.parent_ui, 'bn_home',99)
        self.close()
    
class yes_no_Ui(QDialog):
    def __init__(self, parent=None):
        super(yes_no_Ui, self).__init__(parent)
        self.yes_no_window = Ui_yes_no()
        self.yes_no_window.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.yes_no_window.yes_bn.clicked.connect(lambda: self.submitclose(True))
        self.yes_no_window.no_bn.clicked.connect(lambda: self.submitclose(False))
        self.yes_no_window.icon_label.setPixmap(QPixmap(resource_path(os.path.join("images","bn_images","info.png"))).scaledToWidth(40,aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.setStyleSheet("#centralwidget{ border: 1px solid black;} QWidget{ font-size:16px;}")
        self.answer = False 

    def create_question(self, question):
        self.yes_no_window.question_label.setText(question)

    def submitclose(self, answer):
        self.answer = answer 
        self.accept()