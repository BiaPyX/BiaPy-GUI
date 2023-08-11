# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_build.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BuildBiaPy(object):
    def setupUi(self, BuildBiaPy):
        if not BuildBiaPy.objectName():
            BuildBiaPy.setObjectName(u"BuildBiaPy")
        BuildBiaPy.resize(550, 520)
        BuildBiaPy.setMinimumSize(QSize(550, 520))
        BuildBiaPy.setMaximumSize(QSize(550, 520))
        BuildBiaPy.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout = QVBoxLayout(BuildBiaPy)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 6)
        self.centralwidget = QFrame(BuildBiaPy)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
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
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_label = QLabel(self.frame_top)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(40, 40))
        self.icon_label.setMaximumSize(QSize(40, 40))
        self.icon_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_label)

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
        icon.addFile(u"images/bn_images/hide_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"images/bn_images/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon1)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setAutoDefault(False)
        self.bn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_close)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
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
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.biapy_container_info_label = QLabel(self.frame_4)
        self.biapy_container_info_label.setObjectName(u"biapy_container_info_label")
        self.biapy_container_info_label.setMinimumSize(QSize(0, 100))
        self.biapy_container_info_label.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setFamily(u"DejaVu Math TeX Gyre")
        font1.setPointSize(11)
        self.biapy_container_info_label.setFont(font1)
        self.biapy_container_info_label.setOpenExternalLinks(True)
        self.biapy_container_info_label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.biapy_container_info_label)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"DejaVu Math TeX Gyre")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.verticalLayout_4.addWidget(self.label)

        self.build_progress_bar = QProgressBar(self.frame_4)
        self.build_progress_bar.setObjectName(u"build_progress_bar")
        self.build_progress_bar.setMinimumSize(QSize(70, 0))
        self.build_progress_bar.setMaximumSize(QSize(16777215, 16777215))
        self.build_progress_bar.setFont(font)
        self.build_progress_bar.setMaximum(100)
        self.build_progress_bar.setValue(24)
        self.build_progress_bar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.build_progress_bar.setTextVisible(False)
        self.build_progress_bar.setOrientation(Qt.Horizontal)
        self.build_progress_bar.setInvertedAppearance(False)
        self.build_progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.build_progress_bar)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.build_biapy_log = QTextBrowser(self.frame_bottom)
        self.build_biapy_log.setObjectName(u"build_biapy_log")
        self.build_biapy_log.setMinimumSize(QSize(0, 0))
        self.build_biapy_log.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Monospace")
        font3.setPointSize(10)
        self.build_biapy_log.setFont(font3)
        self.build_biapy_log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.build_biapy_log.setLineWrapMode(QTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.build_biapy_log)

        self.ok_frame = QFrame(self.frame_bottom)
        self.ok_frame.setObjectName(u"ok_frame")
        self.ok_frame.setFrameShape(QFrame.NoFrame)
        self.ok_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ok_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.ok_frame)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(BuildBiaPy)

        QMetaObject.connectSlotsByName(BuildBiaPy)
    # setupUi

    def retranslateUi(self, BuildBiaPy):
        BuildBiaPy.setWindowTitle(QCoreApplication.translate("BuildBiaPy", u"Run BiaPy", None))
        self.icon_label.setText("")
        self.lab_heading.setText("")
        self.bn_min.setText("")
        self.bn_close.setText("")
        self.biapy_container_info_label.setText(QCoreApplication.translate("BuildBiaPy", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("BuildBiaPy", u"Progress:", None))
    # retranslateUi

