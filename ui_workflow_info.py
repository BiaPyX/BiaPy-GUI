# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_workflow_info.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Workflow_info(object):
    def setupUi(self, Workflow_info):
        if not Workflow_info.objectName():
            Workflow_info.setObjectName(u"Workflow_info")
        Workflow_info.resize(800, 700)
        Workflow_info.setMinimumSize(QSize(800, 700))
        Workflow_info.setMaximumSize(QSize(800, 700))
        Workflow_info.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout = QVBoxLayout(Workflow_info)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Workflow_info)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_2)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 40))
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lab_heading = QLabel(self.frame_top)
        self.lab_heading.setObjectName(u"lab_heading")
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.lab_heading.setFont(font)
        self.lab_heading.setStyleSheet(u"")
        self.lab_heading.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lab_heading)

        self.bn_close = QPushButton(self.frame_top)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMinimumSize(QSize(55, 35))
        self.bn_close.setMaximumSize(QSize(55, 35))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(64,144,253);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/bn_images/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setAutoDefault(False)
        self.bn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_close)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.frame_2)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFont(font)
        self.frame_bottom.setStyleSheet(u"")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_bottom)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 800, 660))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.workflow_name_label = QLabel(self.frame_6)
        self.workflow_name_label.setObjectName(u"workflow_name_label")
        self.workflow_name_label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workflow_name_label.sizePolicy().hasHeightForWidth())
        self.workflow_name_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"DejaVu Math TeX Gyre")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.workflow_name_label.setFont(font1)
        self.workflow_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.workflow_name_label)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 40)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.input_description_label = QLabel(self.frame_4)
        self.input_description_label.setObjectName(u"input_description_label")
        self.input_description_label.setMinimumSize(QSize(250, 0))
        self.input_description_label.setMaximumSize(QSize(250, 16777215))
        font2 = QFont()
        font2.setFamily(u"DejaVu Math TeX Gyre")
        self.input_description_label.setFont(font2)
        self.input_description_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.input_description_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.gt_description_label = QLabel(self.frame_4)
        self.gt_description_label.setObjectName(u"gt_description_label")
        self.gt_description_label.setMinimumSize(QSize(250, 0))
        self.gt_description_label.setMaximumSize(QSize(250, 16777215))
        self.gt_description_label.setFont(font2)
        self.gt_description_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.gt_description_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 50, 0, 0)
        self.ok_bn = QPushButton(self.frame)
        self.ok_bn.setObjectName(u"ok_bn")
        self.ok_bn.setMinimumSize(QSize(100, 30))
        self.ok_bn.setMaximumSize(QSize(100, 16777215))
        self.ok_bn.setFont(font)
        self.ok_bn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.ok_bn)


        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.input_image_label = QLabel(self.frame_5)
        self.input_image_label.setObjectName(u"input_image_label")
        self.input_image_label.setMinimumSize(QSize(200, 200))
        self.input_image_label.setMaximumSize(QSize(200, 200))
        self.input_image_label.setFrameShape(QFrame.Box)
        self.input_image_label.setLineWidth(1)

        self.horizontalLayout_4.addWidget(self.input_image_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.gt_image_label = QLabel(self.frame_5)
        self.gt_image_label.setObjectName(u"gt_image_label")
        self.gt_image_label.setMinimumSize(QSize(200, 200))
        self.gt_image_label.setMaximumSize(QSize(200, 200))
        self.gt_image_label.setFrameShape(QFrame.Box)
        self.gt_image_label.setLineWidth(1)

        self.horizontalLayout_4.addWidget(self.gt_image_label)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.workflow_description_label = QLabel(self.frame_3)
        self.workflow_description_label.setObjectName(u"workflow_description_label")
        font3 = QFont()
        font3.setFamily(u"DejaVu Math TeX Gyre")
        font3.setPointSize(12)
        font3.setKerning(True)
        self.workflow_description_label.setFont(font3)
        self.workflow_description_label.setStyleSheet(u"")
        self.workflow_description_label.setWordWrap(True)

        self.gridLayout.addWidget(self.workflow_description_label, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Workflow_info)

        QMetaObject.connectSlotsByName(Workflow_info)
    # setupUi

    def retranslateUi(self, Workflow_info):
        Workflow_info.setWindowTitle(QCoreApplication.translate("Workflow_info", u"Workflow info", None))
        self.lab_heading.setText("")
        self.bn_close.setText("")
        self.workflow_name_label.setText("")
        self.input_description_label.setText(QCoreApplication.translate("Workflow_info", u"Input image", None))
        self.gt_description_label.setText(QCoreApplication.translate("Workflow_info", u"GT", None))
        self.ok_bn.setText(QCoreApplication.translate("Workflow_info", u"OK", None))
        self.input_image_label.setText("")
        self.gt_image_label.setText("")
        self.workflow_description_label.setText(QCoreApplication.translate("Workflow_info", u"Description", None))
    # retranslateUi

