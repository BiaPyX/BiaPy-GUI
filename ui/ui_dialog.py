# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 235)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(600, 235))
        Dialog.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QFrame(Dialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(255,255,255);")
        self.centralwidget.setFrameShape(QFrame.NoFrame)
        self.centralwidget.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 40))
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setStyleSheet(u"background:rgb(255,255,255);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_label = QLabel(self.frame_top)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(40, 40))
        self.icon_label.setMaximumSize(QSize(40, 40))
        self.icon_label.setFrameShape(QFrame.NoFrame)
        self.icon_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_label)

        self.window_des_label = QLabel(self.frame_top)
        self.window_des_label.setObjectName(u"window_des_label")
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.window_des_label.setFont(font)

        self.horizontalLayout.addWidget(self.window_des_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFont(font)
        self.frame_bottom.setStyleSheet(u"")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 9, 0)
        self.scrollArea = QScrollArea(self.frame_bottom)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 578, 152))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.error_message_label = QLabel(self.scrollAreaWidgetContents)
        self.error_message_label.setObjectName(u"error_message_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.error_message_label.setFont(font1)
        self.error_message_label.setStyleSheet(u"background:rgb(255,255,255);")
        self.error_message_label.setAlignment(Qt.AlignCenter)
        self.error_message_label.setWordWrap(True)
        self.error_message_label.setOpenExternalLinks(True)
        self.error_message_label.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.error_message_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.frame = QFrame(self.frame_bottom)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.go_to_correct_bn = QPushButton(self.frame)
        self.go_to_correct_bn.setObjectName(u"go_to_correct_bn")
        self.go_to_correct_bn.setMinimumSize(QSize(150, 30))
        self.go_to_correct_bn.setMaximumSize(QSize(150, 16777215))
        self.go_to_correct_bn.setFont(font)
        self.go_to_correct_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	background-color: rgb(64,144,253);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.go_to_correct_bn)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.icon_label.setText("")
        self.window_des_label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.error_message_label.setText("")
        self.go_to_correct_bn.setText(QCoreApplication.translate("Dialog", u"Go to correct", None))
    # retranslateUi

