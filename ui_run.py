# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_run.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RunBiaPy(object):
    def setupUi(self, RunBiaPy):
        if not RunBiaPy.objectName():
            RunBiaPy.setObjectName(u"RunBiaPy")
        RunBiaPy.resize(1181, 520)
        RunBiaPy.setMinimumSize(QSize(1181, 520))
        RunBiaPy.setMaximumSize(QSize(1181, 500))
        RunBiaPy.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout = QVBoxLayout(RunBiaPy)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 6)
        self.frame_2 = QFrame(RunBiaPy)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
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

        self.bn_min = QPushButton(self.frame_top)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMinimumSize(QSize(55, 35))
        self.bn_min.setMaximumSize(QSize(55, 35))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u"images/bn_images/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon)
        self.bn_min.setIconSize(QSize(22, 12))
        self.bn_min.setAutoDefault(False)
        self.bn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_min)

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
        icon1 = QIcon()
        icon1.addFile(u"images/bn_images/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon1)
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
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 9, 0)
        self.frame_3 = QFrame(self.frame_bottom)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 150))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.biapy_container_info_label = QLabel(self.frame_4)
        self.biapy_container_info_label.setObjectName(u"biapy_container_info_label")
        self.biapy_container_info_label.setMinimumSize(QSize(0, 160))
        font1 = QFont()
        font1.setFamily(u"DejaVu Math TeX Gyre")
        font1.setPointSize(11)
        self.biapy_container_info_label.setFont(font1)
        self.biapy_container_info_label.setOpenExternalLinks(True)
        self.biapy_container_info_label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.biapy_container_info_label)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.container_state_label = QLabel(self.frame)
        self.container_state_label.setObjectName(u"container_state_label")
        font2 = QFont()
        font2.setFamily(u"DejaVu Math TeX Gyre")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.container_state_label.setFont(font2)

        self.gridLayout.addWidget(self.container_state_label, 0, 0, 1, 1)

        self.stop_container_bn = QPushButton(self.frame)
        self.stop_container_bn.setObjectName(u"stop_container_bn")
        self.stop_container_bn.setMinimumSize(QSize(0, 40))
        self.stop_container_bn.setFont(font)
        self.stop_container_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(64,144,253);\n"
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

        self.gridLayout.addWidget(self.stop_container_bn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setMaximumSize(QSize(220, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.test_progress_label = QLabel(self.frame_5)
        self.test_progress_label.setObjectName(u"test_progress_label")
        self.test_progress_label.setFont(font)

        self.gridLayout_2.addWidget(self.test_progress_label, 0, 2, 1, 1)

        self.test_progress_bar = QProgressBar(self.frame_5)
        self.test_progress_bar.setObjectName(u"test_progress_bar")
        self.test_progress_bar.setMinimumSize(QSize(70, 0))
        self.test_progress_bar.setFont(font)
        self.test_progress_bar.setValue(24)
        self.test_progress_bar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.test_progress_bar.setTextVisible(False)
        self.test_progress_bar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.test_progress_bar, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.train_progress_label = QLabel(self.frame_5)
        self.train_progress_label.setObjectName(u"train_progress_label")
        self.train_progress_label.setFont(font)
        self.train_progress_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.train_progress_label, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.train_progress_bar = QProgressBar(self.frame_5)
        self.train_progress_bar.setObjectName(u"train_progress_bar")
        self.train_progress_bar.setMinimumSize(QSize(70, 0))
        self.train_progress_bar.setMaximumSize(QSize(16777215, 16777215))
        self.train_progress_bar.setFont(font)
        self.train_progress_bar.setMaximum(100)
        self.train_progress_bar.setValue(24)
        self.train_progress_bar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.train_progress_bar.setTextVisible(False)
        self.train_progress_bar.setOrientation(Qt.Vertical)
        self.train_progress_bar.setInvertedAppearance(False)
        self.train_progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_2.addWidget(self.train_progress_bar, 1, 1, 1, 1)

        self.train_epochs_label = QLabel(self.frame_5)
        self.train_epochs_label.setObjectName(u"train_epochs_label")
        self.train_epochs_label.setFont(font)

        self.gridLayout_2.addWidget(self.train_epochs_label, 2, 1, 1, 1)

        self.test_files_label = QLabel(self.frame_5)
        self.test_files_label.setObjectName(u"test_files_label")
        self.test_files_label.setFont(font)

        self.gridLayout_2.addWidget(self.test_files_label, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.run_biapy_log = QTextBrowser(self.frame_bottom)
        self.run_biapy_log.setObjectName(u"run_biapy_log")
        self.run_biapy_log.setMinimumSize(QSize(0, 210))
        self.run_biapy_log.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Monospace")
        font3.setPointSize(10)
        self.run_biapy_log.setFont(font3)
        self.run_biapy_log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.run_biapy_log.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.run_biapy_log)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(RunBiaPy)

        QMetaObject.connectSlotsByName(RunBiaPy)
    # setupUi

    def retranslateUi(self, RunBiaPy):
        RunBiaPy.setWindowTitle(QCoreApplication.translate("RunBiaPy", u"Run BiaPy", None))
        self.lab_heading.setText("")
        self.bn_min.setText("")
        self.bn_close.setText("")
        self.biapy_container_info_label.setText(QCoreApplication.translate("RunBiaPy", u"TextLabel", None))
        self.container_state_label.setText(QCoreApplication.translate("RunBiaPy", u"TextLabel", None))
        self.stop_container_bn.setText(QCoreApplication.translate("RunBiaPy", u"   Stop running   ", None))
        self.test_progress_label.setText(QCoreApplication.translate("RunBiaPy", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Test</span></p><p align=\"center\"><span style=\" font-size:12pt;\">phase</span></p></body></html>", None))
        self.train_progress_label.setText(QCoreApplication.translate("RunBiaPy", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Training</span></p><p align=\"center\"><span style=\" font-size:12pt;\">phase</span></p></body></html>", None))
        self.train_epochs_label.setText(QCoreApplication.translate("RunBiaPy", u"<html><head/><body><p align=\"center\">Epochs</p><p align=\"center\">-/-</p></body></html>", None))
        self.test_files_label.setText(QCoreApplication.translate("RunBiaPy", u"<html><head/><body><p align=\"center\">Files</p><p align=\"center\">-/-</p></body></html>", None))
    # retranslateUi

