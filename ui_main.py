# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1181, 593)
        MainWindow.setMinimumSize(QSize(800, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_west = QFrame(self.centralwidget)
        self.frame_west.setObjectName(u"frame_west")
        font = QFont()
        font.setFamily(u"DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.frame_west.setFont(font)
        self.frame_west.setFrameShape(QFrame.NoFrame)
        self.frame_west.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_west)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_west)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(240, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setFont(font)
        self.frame_bottom_west.setStyleSheet(u"background:rgb(64,144,253);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.biapy_logo_frame = QFrame(self.frame_bottom_west)
        self.biapy_logo_frame.setObjectName(u"biapy_logo_frame")
        self.biapy_logo_frame.setMinimumSize(QSize(0, 0))
        self.biapy_logo_frame.setMaximumSize(QSize(16777215, 16777215))
        self.biapy_logo_frame.setFont(font)
        self.biapy_logo_frame.setFrameShape(QFrame.NoFrame)
        self.biapy_logo_frame.setFrameShadow(QFrame.Plain)
        self.biapy_logo_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.biapy_logo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.frame_58 = QFrame(self.biapy_logo_frame)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(240, 0))
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.biapy_logo_label = QLabel(self.frame_58)
        self.biapy_logo_label.setObjectName(u"biapy_logo_label")
        self.biapy_logo_label.setMinimumSize(QSize(0, 0))
        self.biapy_logo_label.setMaximumSize(QSize(180, 180))
        self.biapy_logo_label.setFont(font)
        self.biapy_logo_label.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")
        self.biapy_logo_label.setLineWidth(0)
        self.biapy_logo_label.setPixmap(QPixmap(u"images/superminimal_ark_biapy2.png"))
        self.biapy_logo_label.setScaledContents(True)
        self.biapy_logo_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.biapy_logo_label)


        self.verticalLayout_3.addWidget(self.frame_58, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.line_2 = QFrame(self.biapy_logo_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.biapy_version = QLabel(self.biapy_logo_frame)
        self.biapy_version.setObjectName(u"biapy_version")
        self.biapy_version.setMinimumSize(QSize(0, 0))
        self.biapy_version.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"DejaVu Math TeX Gyre")
        font1.setPointSize(8)
        self.biapy_version.setFont(font1)
        self.biapy_version.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")
        self.biapy_version.setLineWidth(0)
        self.biapy_version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.biapy_version)


        self.verticalLayout_14.addWidget(self.biapy_logo_frame, 0, Qt.AlignHCenter)

        self.line = QFrame(self.frame_bottom_west)
        self.line.setObjectName(u"line")
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMaximumSize(QSize(240, 55))
        self.frame_home.setFont(font)
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(240, 55))
        self.bn_home.setMaximumSize(QSize(240, 55))
        self.bn_home.setFont(font)
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/bn_images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon)
        self.bn_home.setIconSize(QSize(202, 48))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_14.addWidget(self.frame_home)

        self.frame_workflow = QFrame(self.frame_bottom_west)
        self.frame_workflow.setObjectName(u"frame_workflow")
        self.frame_workflow.setMaximumSize(QSize(240, 55))
        self.frame_workflow.setFont(font)
        self.frame_workflow.setFrameShape(QFrame.NoFrame)
        self.frame_workflow.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_workflow)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_workflow = QPushButton(self.frame_workflow)
        self.bn_workflow.setObjectName(u"bn_workflow")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bn_workflow.sizePolicy().hasHeightForWidth())
        self.bn_workflow.setSizePolicy(sizePolicy)
        self.bn_workflow.setMinimumSize(QSize(240, 55))
        self.bn_workflow.setMaximumSize(QSize(240, 55))
        self.bn_workflow.setFont(font)
        self.bn_workflow.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/bn_images/workflow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_workflow.setIcon(icon1)
        self.bn_workflow.setIconSize(QSize(202, 48))
        self.bn_workflow.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_workflow)


        self.verticalLayout_14.addWidget(self.frame_workflow)

        self.frame_goptions = QFrame(self.frame_bottom_west)
        self.frame_goptions.setObjectName(u"frame_goptions")
        self.frame_goptions.setMaximumSize(QSize(240, 55))
        self.frame_goptions.setFont(font)
        self.frame_goptions.setFrameShape(QFrame.NoFrame)
        self.frame_goptions.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_goptions)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_goptions = QPushButton(self.frame_goptions)
        self.bn_goptions.setObjectName(u"bn_goptions")
        self.bn_goptions.setMinimumSize(QSize(240, 55))
        self.bn_goptions.setMaximumSize(QSize(240, 55))
        self.bn_goptions.setFont(font)
        self.bn_goptions.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/bn_images/goptions.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_goptions.setIcon(icon2)
        self.bn_goptions.setIconSize(QSize(202, 48))
        self.bn_goptions.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_goptions)


        self.verticalLayout_14.addWidget(self.frame_goptions)

        self.frame_train = QFrame(self.frame_bottom_west)
        self.frame_train.setObjectName(u"frame_train")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_train.sizePolicy().hasHeightForWidth())
        self.frame_train.setSizePolicy(sizePolicy1)
        self.frame_train.setMaximumSize(QSize(240, 55))
        self.frame_train.setFont(font)
        self.frame_train.setFrameShape(QFrame.NoFrame)
        self.frame_train.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_train)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_train = QPushButton(self.frame_train)
        self.bn_train.setObjectName(u"bn_train")
        self.bn_train.setMinimumSize(QSize(240, 55))
        self.bn_train.setMaximumSize(QSize(240, 55))
        self.bn_train.setFont(font)
        self.bn_train.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"images/bn_images/train.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_train.setIcon(icon3)
        self.bn_train.setIconSize(QSize(202, 48))
        self.bn_train.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_train)


        self.verticalLayout_14.addWidget(self.frame_train)

        self.frame_test = QFrame(self.frame_bottom_west)
        self.frame_test.setObjectName(u"frame_test")
        sizePolicy1.setHeightForWidth(self.frame_test.sizePolicy().hasHeightForWidth())
        self.frame_test.setSizePolicy(sizePolicy1)
        self.frame_test.setMinimumSize(QSize(0, 0))
        self.frame_test.setMaximumSize(QSize(240, 55))
        self.frame_test.setFont(font)
        self.frame_test.setFrameShape(QFrame.NoFrame)
        self.frame_test.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_test)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bn_test = QPushButton(self.frame_test)
        self.bn_test.setObjectName(u"bn_test")
        self.bn_test.setMinimumSize(QSize(240, 55))
        self.bn_test.setMaximumSize(QSize(240, 55))
        self.bn_test.setFont(font)
        self.bn_test.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/bn_images/test.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_test.setIcon(icon4)
        self.bn_test.setIconSize(QSize(202, 48))
        self.bn_test.setFlat(True)

        self.horizontalLayout_24.addWidget(self.bn_test)


        self.verticalLayout_14.addWidget(self.frame_test)

        self.frame_run_biapy = QFrame(self.frame_bottom_west)
        self.frame_run_biapy.setObjectName(u"frame_run_biapy")
        sizePolicy1.setHeightForWidth(self.frame_run_biapy.sizePolicy().hasHeightForWidth())
        self.frame_run_biapy.setSizePolicy(sizePolicy1)
        self.frame_run_biapy.setMaximumSize(QSize(240, 55))
        self.frame_run_biapy.setFont(font)
        self.frame_run_biapy.setFrameShape(QFrame.NoFrame)
        self.frame_run_biapy.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_run_biapy)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.bn_run_biapy = QPushButton(self.frame_run_biapy)
        self.bn_run_biapy.setObjectName(u"bn_run_biapy")
        self.bn_run_biapy.setMinimumSize(QSize(0, 0))
        self.bn_run_biapy.setMaximumSize(QSize(240, 55))
        self.bn_run_biapy.setFont(font)
        self.bn_run_biapy.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"images/bn_images/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_run_biapy.setIcon(icon5)
        self.bn_run_biapy.setIconSize(QSize(202, 48))
        self.bn_run_biapy.setFlat(True)

        self.horizontalLayout_28.addWidget(self.bn_run_biapy)


        self.verticalLayout_14.addWidget(self.frame_run_biapy)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_14.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)


        self.horizontalLayout.addWidget(self.frame_west)

        self.frame_east = QFrame(self.centralwidget)
        self.frame_east.setObjectName(u"frame_east")
        self.frame_east.setEnabled(True)
        self.frame_east.setMinimumSize(QSize(0, 0))
        self.frame_east.setMaximumSize(QSize(16777215, 16777215))
        self.frame_east.setFont(font)
        self.frame_east.setFrameShape(QFrame.NoFrame)
        self.frame_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_east)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_east = QFrame(self.frame_east)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMinimumSize(QSize(0, 0))
        self.frame_top_east.setMaximumSize(QSize(16777215, 35))
        self.frame_top_east.setFont(font)
        self.frame_top_east.setStyleSheet(u"background:rgb(255,255,255);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_empty = QFrame(self.frame_top_east)
        self.frame_empty.setObjectName(u"frame_empty")
        self.frame_empty.setMinimumSize(QSize(0, 0))
        self.frame_empty.setFont(font)
        self.frame_empty.setFrameShape(QFrame.NoFrame)
        self.frame_empty.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_empty)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_empty)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 35))
        self.frame_min.setMaximumSize(QSize(55, 35))
        self.frame_min.setFont(font)
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 35))
        self.bn_min.setFont(font)
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
        icon6 = QIcon()
        icon6.addFile(u"images/bn_images/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon6)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 35))
        self.frame_close.setMaximumSize(QSize(55, 35))
        self.frame_close.setFont(font)
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 35))
        self.bn_close.setFont(font)
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
        icon7 = QIcon()
        icon7.addFile(u"images/bn_images/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon7)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.verticalLayout.addWidget(self.frame_top_east)

        self.frame_bottom_east = QFrame(self.frame_east)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setMaximumSize(QSize(16777215, 16777215))
        self.frame_bottom_east.setFont(font)
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(255,255,255);")
        self.verticalLayout_13 = QVBoxLayout(self.page_home)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(775, 500))
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(775, 100))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_5)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.biapy_title_label = QLabel(self.frame_5)
        self.biapy_title_label.setObjectName(u"biapy_title_label")
        self.biapy_title_label.setMinimumSize(QSize(0, 15))
        self.biapy_title_label.setMaximumSize(QSize(930, 20))
        font2 = QFont()
        font2.setFamily(u"DejaVu Math TeX Gyre")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.biapy_title_label.setFont(font2)

        self.verticalLayout_15.addWidget(self.biapy_title_label)

        self.biapy_description_label = QLabel(self.frame_5)
        self.biapy_description_label.setObjectName(u"biapy_description_label")
        self.biapy_description_label.setMaximumSize(QSize(930, 16777215))
        self.biapy_description_label.setFont(font)
        self.biapy_description_label.setWordWrap(True)
        self.biapy_description_label.setOpenExternalLinks(True)

        self.verticalLayout_15.addWidget(self.biapy_description_label)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.docker_frame = QFrame(self.frame_4)
        self.docker_frame.setObjectName(u"docker_frame")
        self.docker_frame.setMinimumSize(QSize(0, 0))
        self.docker_frame.setMaximumSize(QSize(16777215, 300))
        self.docker_frame.setStyleSheet(u"")
        self.docker_frame.setFrameShape(QFrame.NoFrame)
        self.docker_frame.setFrameShadow(QFrame.Raised)
        self.docker_frame.setLineWidth(1)
        self.gridLayout_68 = QGridLayout(self.docker_frame)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setHorizontalSpacing(15)
        self.gridLayout_68.setVerticalSpacing(0)
        self.docker_status_label = QLabel(self.docker_frame)
        self.docker_status_label.setObjectName(u"docker_status_label")
        self.docker_status_label.setMinimumSize(QSize(270, 100))
        self.docker_status_label.setMaximumSize(QSize(100, 16777215))
        self.docker_status_label.setFont(font)
        self.docker_status_label.setWordWrap(True)
        self.docker_status_label.setOpenExternalLinks(True)

        self.gridLayout_68.addWidget(self.docker_status_label, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_68.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.dependencies_label = QLabel(self.docker_frame)
        self.dependencies_label.setObjectName(u"dependencies_label")
        self.dependencies_label.setMaximumSize(QSize(16777215, 30))
        self.dependencies_label.setFont(font2)
        self.dependencies_label.setOpenExternalLinks(True)

        self.gridLayout_68.addWidget(self.dependencies_label, 0, 0, 1, 1)

        self.docker_logo = QLabel(self.docker_frame)
        self.docker_logo.setObjectName(u"docker_logo")
        self.docker_logo.setMinimumSize(QSize(250, 80))

        self.gridLayout_68.addWidget(self.docker_logo, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.docker_frame)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.create_yaml_bn = QPushButton(self.frame_6)
        self.create_yaml_bn.setObjectName(u"create_yaml_bn")
        self.create_yaml_bn.setGeometry(QRect(120, 70, 241, 40))
        self.create_yaml_bn.setFont(font)
        self.create_yaml_bn.setStyleSheet(u"QPushButton {\n"
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
        self.create_yaml_bn.setIconSize(QSize(215, 33))
        self.continue_yaml_bn = QPushButton(self.frame_6)
        self.continue_yaml_bn.setObjectName(u"continue_yaml_bn")
        self.continue_yaml_bn.setGeometry(QRect(460, 70, 361, 40))
        self.continue_yaml_bn.setFont(font)
        self.continue_yaml_bn.setStyleSheet(u"QPushButton {\n"
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
        self.continue_yaml_bn.setIconSize(QSize(341, 33))

        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_home)
        self.page_create_yaml = QWidget()
        self.page_create_yaml.setObjectName(u"page_create_yaml")
        self.page_create_yaml.setStyleSheet(u"background:rgb(255,255,255);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_create_yaml)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.page_create_yaml_frame = QFrame(self.page_create_yaml)
        self.page_create_yaml_frame.setObjectName(u"page_create_yaml_frame")
        self.page_create_yaml_frame.setMinimumSize(QSize(0, 0))
        self.page_create_yaml_frame.setMaximumSize(QSize(16777215, 16777215))
        self.page_create_yaml_frame.setFont(font)
        self.page_create_yaml_frame.setFrameShape(QFrame.StyledPanel)
        self.page_create_yaml_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.page_create_yaml_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_create_yaml_frame = QStackedWidget(self.page_create_yaml_frame)
        self.stackedWidget_create_yaml_frame.setObjectName(u"stackedWidget_create_yaml_frame")
        self.stackedWidget_create_yaml_frame.setFont(font)
        self.workflow_selection_page = QWidget()
        self.workflow_selection_page.setObjectName(u"workflow_selection_page")
        self.workflow_selection_page.setMinimumSize(QSize(0, 0))
        self.page_create_yaml_mid_frame = QFrame(self.workflow_selection_page)
        self.page_create_yaml_mid_frame.setObjectName(u"page_create_yaml_mid_frame")
        self.page_create_yaml_mid_frame.setGeometry(QRect(0, 0, 941, 461))
        self.page_create_yaml_mid_frame.setFont(font)
        self.page_create_yaml_mid_frame.setFrameShape(QFrame.NoFrame)
        self.page_create_yaml_mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.page_create_yaml_mid_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_arrow_bn = QPushButton(self.page_create_yaml_mid_frame)
        self.left_arrow_bn.setObjectName(u"left_arrow_bn")
        self.left_arrow_bn.setMaximumSize(QSize(30, 50))
        self.left_arrow_bn.setFont(font)
        self.left_arrow_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"images/bn_images/left_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.left_arrow_bn.setIcon(icon8)
        self.left_arrow_bn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.left_arrow_bn)

        self.frame_17 = QFrame(self.page_create_yaml_mid_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setMaximumSize(QSize(10, 16777215))
        self.frame_17.setFont(font)
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_17)

        self.workflow_view1_frame = QFrame(self.page_create_yaml_mid_frame)
        self.workflow_view1_frame.setObjectName(u"workflow_view1_frame")
        self.workflow_view1_frame.setMaximumSize(QSize(267, 16777215))
        self.workflow_view1_frame.setFont(font)
        self.workflow_view1_frame.setFrameShape(QFrame.NoFrame)
        self.workflow_view1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.workflow_view1_frame)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 17, -1, -1)
        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_34)

        self.workflow_view1_label = QLabel(self.workflow_view1_frame)
        self.workflow_view1_label.setObjectName(u"workflow_view1_label")
        self.workflow_view1_label.setMaximumSize(QSize(250, 250))
        self.workflow_view1_label.setFont(font)
        self.workflow_view1_label.setFrameShape(QFrame.NoFrame)
        self.workflow_view1_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.workflow_view1_label)

        self.frame_38 = QFrame(self.workflow_view1_frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 16777215))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.frame_38.setLineWidth(0)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 10, 0, 0)
        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_64)

        self.workflow_view1_seemore_bn = QPushButton(self.frame_38)
        self.workflow_view1_seemore_bn.setObjectName(u"workflow_view1_seemore_bn")
        self.workflow_view1_seemore_bn.setMinimumSize(QSize(140, 30))
        font3 = QFont()
        font3.setFamily(u"DejaVu Math TeX Gyre")
        font3.setPointSize(9)
        self.workflow_view1_seemore_bn.setFont(font3)
        self.workflow_view1_seemore_bn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_21.addWidget(self.workflow_view1_seemore_bn)


        self.verticalLayout_29.addWidget(self.frame_38)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_33)

        self.workflow_view1_name_label = QLabel(self.workflow_view1_frame)
        self.workflow_view1_name_label.setObjectName(u"workflow_view1_name_label")
        self.workflow_view1_name_label.setMaximumSize(QSize(16777215, 16777215))
        self.workflow_view1_name_label.setFont(font)
        self.workflow_view1_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.workflow_view1_name_label)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_39)


        self.horizontalLayout_3.addWidget(self.workflow_view1_frame)

        self.workflow_mid_separator1_frame = QFrame(self.page_create_yaml_mid_frame)
        self.workflow_mid_separator1_frame.setObjectName(u"workflow_mid_separator1_frame")
        self.workflow_mid_separator1_frame.setMinimumSize(QSize(0, 0))
        self.workflow_mid_separator1_frame.setMaximumSize(QSize(30, 16777215))
        self.workflow_mid_separator1_frame.setFont(font)
        self.workflow_mid_separator1_frame.setFrameShape(QFrame.NoFrame)
        self.workflow_mid_separator1_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.workflow_mid_separator1_frame)

        self.workflow_view2_frame = QFrame(self.page_create_yaml_mid_frame)
        self.workflow_view2_frame.setObjectName(u"workflow_view2_frame")
        self.workflow_view2_frame.setMinimumSize(QSize(0, 0))
        self.workflow_view2_frame.setMaximumSize(QSize(267, 16777215))
        self.workflow_view2_frame.setFont(font)
        self.workflow_view2_frame.setFrameShape(QFrame.NoFrame)
        self.workflow_view2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.workflow_view2_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_36)

        self.workflow_view2_label = QLabel(self.workflow_view2_frame)
        self.workflow_view2_label.setObjectName(u"workflow_view2_label")
        self.workflow_view2_label.setMaximumSize(QSize(250, 250))
        self.workflow_view2_label.setFont(font)
        self.workflow_view2_label.setFrameShape(QFrame.NoFrame)
        self.workflow_view2_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.workflow_view2_label)

        self.frame_59 = QFrame(self.workflow_view2_frame)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 4, 0, 0)
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_62)

        self.workflow_view2_seemore_bn = QPushButton(self.frame_59)
        self.workflow_view2_seemore_bn.setObjectName(u"workflow_view2_seemore_bn")
        self.workflow_view2_seemore_bn.setMinimumSize(QSize(140, 30))
        self.workflow_view2_seemore_bn.setFont(font3)
        self.workflow_view2_seemore_bn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_22.addWidget(self.workflow_view2_seemore_bn)


        self.verticalLayout_30.addWidget(self.frame_59)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_35)

        self.workflow_view2_name_label = QLabel(self.workflow_view2_frame)
        self.workflow_view2_name_label.setObjectName(u"workflow_view2_name_label")
        self.workflow_view2_name_label.setMaximumSize(QSize(16777215, 16777215))
        self.workflow_view2_name_label.setFont(font)
        self.workflow_view2_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.workflow_view2_name_label)

        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_40)


        self.horizontalLayout_3.addWidget(self.workflow_view2_frame)

        self.workflow_mid_separator2_frame = QFrame(self.page_create_yaml_mid_frame)
        self.workflow_mid_separator2_frame.setObjectName(u"workflow_mid_separator2_frame")
        self.workflow_mid_separator2_frame.setMinimumSize(QSize(0, 0))
        self.workflow_mid_separator2_frame.setMaximumSize(QSize(30, 16777215))
        self.workflow_mid_separator2_frame.setFont(font)
        self.workflow_mid_separator2_frame.setFrameShape(QFrame.NoFrame)
        self.workflow_mid_separator2_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.workflow_mid_separator2_frame)

        self.workflow_view3_frame = QFrame(self.page_create_yaml_mid_frame)
        self.workflow_view3_frame.setObjectName(u"workflow_view3_frame")
        self.workflow_view3_frame.setMaximumSize(QSize(267, 16777215))
        self.workflow_view3_frame.setFont(font)
        self.workflow_view3_frame.setFrameShape(QFrame.NoFrame)
        self.workflow_view3_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.workflow_view3_frame)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, 17, -1, -1)
        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_37)

        self.workflow_view3_label = QLabel(self.workflow_view3_frame)
        self.workflow_view3_label.setObjectName(u"workflow_view3_label")
        self.workflow_view3_label.setMaximumSize(QSize(250, 250))
        self.workflow_view3_label.setFont(font)
        self.workflow_view3_label.setFrameShape(QFrame.NoFrame)
        self.workflow_view3_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.workflow_view3_label)

        self.frame_60 = QFrame(self.workflow_view3_frame)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 10, 0, 0)
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_55)

        self.workflow_view3_seemore_bn = QPushButton(self.frame_60)
        self.workflow_view3_seemore_bn.setObjectName(u"workflow_view3_seemore_bn")
        self.workflow_view3_seemore_bn.setMinimumSize(QSize(140, 30))
        self.workflow_view3_seemore_bn.setFont(font3)
        self.workflow_view3_seemore_bn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_23.addWidget(self.workflow_view3_seemore_bn)


        self.verticalLayout_31.addWidget(self.frame_60)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_38)

        self.workflow_view3_name_label = QLabel(self.workflow_view3_frame)
        self.workflow_view3_name_label.setObjectName(u"workflow_view3_name_label")
        self.workflow_view3_name_label.setMaximumSize(QSize(16777215, 16777215))
        self.workflow_view3_name_label.setFont(font)
        self.workflow_view3_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.workflow_view3_name_label)

        self.verticalSpacer_41 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_41)


        self.horizontalLayout_3.addWidget(self.workflow_view3_frame)

        self.frame_18 = QFrame(self.page_create_yaml_mid_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setMaximumSize(QSize(10, 16777215))
        self.frame_18.setFont(font)
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_18)

        self.right_arrow_bn = QPushButton(self.page_create_yaml_mid_frame)
        self.right_arrow_bn.setObjectName(u"right_arrow_bn")
        self.right_arrow_bn.setMaximumSize(QSize(30, 50))
        self.right_arrow_bn.setFont(font)
        self.right_arrow_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"images/bn_images/right_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.right_arrow_bn.setIcon(icon9)
        self.right_arrow_bn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.right_arrow_bn)

        self.stackedWidget_create_yaml_frame.addWidget(self.workflow_selection_page)
        self.goptions_page = QWidget()
        self.goptions_page.setObjectName(u"goptions_page")
        self.goptions_general_frame = QFrame(self.goptions_page)
        self.goptions_general_frame.setObjectName(u"goptions_general_frame")
        self.goptions_general_frame.setGeometry(QRect(0, 0, 939, 456))
        self.goptions_general_frame.setMinimumSize(QSize(939, 396))
        self.goptions_general_frame.setFont(font)
        self.goptions_general_frame.setFrameShape(QFrame.NoFrame)
        self.goptions_general_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.goptions_general_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.goptions_scrollArea = QScrollArea(self.goptions_general_frame)
        self.goptions_scrollArea.setObjectName(u"goptions_scrollArea")
        self.goptions_scrollArea.setMinimumSize(QSize(0, 30))
        self.goptions_scrollArea.setFont(font)
        self.goptions_scrollArea.setFrameShape(QFrame.NoFrame)
        self.goptions_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 925, 493))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_26 = QFrame(self.scrollAreaWidgetContents)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 0))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_26)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(10)
        self.gridLayout_28.setVerticalSpacing(0)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.goptions_advanced_label = QLabel(self.frame_26)
        self.goptions_advanced_label.setObjectName(u"goptions_advanced_label")
        self.goptions_advanced_label.setMaximumSize(QSize(16777215, 35))
        self.goptions_advanced_label.setFont(font)

        self.gridLayout_28.addWidget(self.goptions_advanced_label, 0, 0, 1, 1)

        self.goptions_advanced_bn = QPushButton(self.frame_26)
        self.goptions_advanced_bn.setObjectName(u"goptions_advanced_bn")
        self.goptions_advanced_bn.setMaximumSize(QSize(35, 35))
        self.goptions_advanced_bn.setFont(font)
        self.goptions_advanced_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"images/bn_images/down_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.goptions_advanced_bn.setIcon(icon10)

        self.gridLayout_28.addWidget(self.goptions_advanced_bn, 0, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_19, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_26, 7, 0, 1, 2)

        self.train_disable_checkpoint_frame = QFrame(self.scrollAreaWidgetContents)
        self.train_disable_checkpoint_frame.setObjectName(u"train_disable_checkpoint_frame")
        self.train_disable_checkpoint_frame.setMinimumSize(QSize(0, 0))
        self.train_disable_checkpoint_frame.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.train_disable_checkpoint_frame.setFrameShape(QFrame.Box)
        self.train_disable_checkpoint_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.train_disable_checkpoint_frame)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_148 = QLabel(self.train_disable_checkpoint_frame)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font)

        self.gridLayout_26.addWidget(self.label_148, 1, 1, 1, 1)

        self.checkpoint_load_input = QComboBox(self.train_disable_checkpoint_frame)
        self.checkpoint_load_input.addItem("")
        self.checkpoint_load_input.addItem("")
        self.checkpoint_load_input.setObjectName(u"checkpoint_load_input")
        self.checkpoint_load_input.setMinimumSize(QSize(200, 30))
        self.checkpoint_load_input.setMaximumSize(QSize(200, 30))
        self.checkpoint_load_input.setFont(font)

        self.gridLayout_26.addWidget(self.checkpoint_load_input, 1, 2, 1, 1)

        self.checkpoint_file_path_input = QTextBrowser(self.train_disable_checkpoint_frame)
        self.checkpoint_file_path_input.setObjectName(u"checkpoint_file_path_input")
        self.checkpoint_file_path_input.setMinimumSize(QSize(500, 30))
        self.checkpoint_file_path_input.setMaximumSize(QSize(500, 30))
        self.checkpoint_file_path_input.setFont(font)
        self.checkpoint_file_path_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.checkpoint_file_path_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.checkpoint_file_path_input.setLineWrapMode(QTextEdit.NoWrap)
        self.checkpoint_file_path_input.setReadOnly(False)

        self.gridLayout_26.addWidget(self.checkpoint_file_path_input, 2, 2, 1, 1)

        self.checkpoint_file_path_browse_label = QLabel(self.train_disable_checkpoint_frame)
        self.checkpoint_file_path_browse_label.setObjectName(u"checkpoint_file_path_browse_label")
        self.checkpoint_file_path_browse_label.setFont(font)

        self.gridLayout_26.addWidget(self.checkpoint_file_path_browse_label, 2, 1, 1, 1)

        self.checkpoint_file_path_browse_bn = QPushButton(self.train_disable_checkpoint_frame)
        self.checkpoint_file_path_browse_bn.setObjectName(u"checkpoint_file_path_browse_bn")
        self.checkpoint_file_path_browse_bn.setFont(font)

        self.gridLayout_26.addWidget(self.checkpoint_file_path_browse_bn, 2, 3, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_20, 2, 4, 1, 1)


        self.gridLayout.addWidget(self.train_disable_checkpoint_frame, 6, 0, 1, 3)

        self.train_disable_checkpoint_label = QLabel(self.scrollAreaWidgetContents)
        self.train_disable_checkpoint_label.setObjectName(u"train_disable_checkpoint_label")
        self.train_disable_checkpoint_label.setMaximumSize(QSize(16777215, 16777215))
        self.train_disable_checkpoint_label.setFont(font)

        self.gridLayout.addWidget(self.train_disable_checkpoint_label, 4, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 2)

        self.goptions_advanced_options_frame = QFrame(self.scrollAreaWidgetContents)
        self.goptions_advanced_options_frame.setObjectName(u"goptions_advanced_options_frame")
        self.goptions_advanced_options_frame.setMinimumSize(QSize(880, 200))
        self.goptions_advanced_options_frame.setFont(font)
        self.goptions_advanced_options_frame.setFrameShape(QFrame.NoFrame)
        self.goptions_advanced_options_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.goptions_advanced_options_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(15, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.goptions_advanced_options_scrollarea = QScrollArea(self.goptions_advanced_options_frame)
        self.goptions_advanced_options_scrollarea.setObjectName(u"goptions_advanced_options_scrollarea")
        self.goptions_advanced_options_scrollarea.setMinimumSize(QSize(0, 0))
        self.goptions_advanced_options_scrollarea.setMaximumSize(QSize(16777215, 16777215))
        self.goptions_advanced_options_scrollarea.setFont(font)
        self.goptions_advanced_options_scrollarea.setStyleSheet(u".QFrame{border: 1px solid grey}\n"
"")
        self.goptions_advanced_options_scrollarea.setFrameShape(QFrame.Box)
        self.goptions_advanced_options_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 877, 174))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(200, 35))
        self.label_9.setFont(font)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(568, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(200, 35))
        self.label_8.setFont(font)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 1)

        self.maxcpu_combobox = QComboBox(self.frame_2)
        self.maxcpu_combobox.setObjectName(u"maxcpu_combobox")
        self.maxcpu_combobox.setMinimumSize(QSize(200, 30))
        self.maxcpu_combobox.setMaximumSize(QSize(200, 30))
        self.maxcpu_combobox.setFont(font)

        self.gridLayout_5.addWidget(self.maxcpu_combobox, 1, 2, 1, 1)

        self.gpu_input = QLineEdit(self.frame_2)
        self.gpu_input.setObjectName(u"gpu_input")
        self.gpu_input.setMinimumSize(QSize(200, 30))
        self.gpu_input.setMaximumSize(QSize(200, 30))
        self.gpu_input.setFont(font)

        self.gridLayout_5.addWidget(self.gpu_input, 0, 2, 1, 1)

        self.seed_input = QLineEdit(self.frame_2)
        self.seed_input.setObjectName(u"seed_input")
        self.seed_input.setMinimumSize(QSize(200, 30))
        self.seed_input.setMaximumSize(QSize(200, 30))
        self.seed_input.setFont(font)

        self.gridLayout_5.addWidget(self.seed_input, 3, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_63, 1, 1, 1, 1)

        self.goptions_advanced_options_scrollarea.setWidget(self.scrollAreaWidgetContents_2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.goptions_advanced_options_scrollarea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.goptions_advanced_options_frame, 8, 0, 1, 5)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_21)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.goptions_browse_yaml_path_bn = QPushButton(self.frame_21)
        self.goptions_browse_yaml_path_bn.setObjectName(u"goptions_browse_yaml_path_bn")
        self.goptions_browse_yaml_path_bn.setMaximumSize(QSize(130, 16777215))
        self.goptions_browse_yaml_path_bn.setFont(font)

        self.gridLayout_27.addWidget(self.goptions_browse_yaml_path_bn, 3, 5, 1, 1)

        self.goptions_browse_yaml_path_input = QTextBrowser(self.frame_21)
        self.goptions_browse_yaml_path_input.setObjectName(u"goptions_browse_yaml_path_input")
        self.goptions_browse_yaml_path_input.setMinimumSize(QSize(500, 30))
        self.goptions_browse_yaml_path_input.setMaximumSize(QSize(500, 30))
        self.goptions_browse_yaml_path_input.setFont(font)
        self.goptions_browse_yaml_path_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.goptions_browse_yaml_path_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.goptions_browse_yaml_path_input.setLineWrapMode(QTextEdit.NoWrap)
        self.goptions_browse_yaml_path_input.setLineWrapColumnOrWidth(0)
        self.goptions_browse_yaml_path_input.setReadOnly(False)

        self.gridLayout_27.addWidget(self.goptions_browse_yaml_path_input, 3, 3, 1, 1)

        self.goptions_yaml_name_input = QLineEdit(self.frame_21)
        self.goptions_yaml_name_input.setObjectName(u"goptions_yaml_name_input")
        self.goptions_yaml_name_input.setMinimumSize(QSize(0, 30))
        self.goptions_yaml_name_input.setMaximumSize(QSize(500, 30))
        self.goptions_yaml_name_input.setFont(font)

        self.gridLayout_27.addWidget(self.goptions_yaml_name_input, 5, 3, 1, 1)

        self.dimensions_comboBox = QComboBox(self.frame_21)
        self.dimensions_comboBox.addItem("")
        self.dimensions_comboBox.addItem("")
        self.dimensions_comboBox.setObjectName(u"dimensions_comboBox")
        self.dimensions_comboBox.setMinimumSize(QSize(100, 30))
        self.dimensions_comboBox.setMaximumSize(QSize(100, 30))
        self.dimensions_comboBox.setFont(font)

        self.gridLayout_27.addWidget(self.dimensions_comboBox, 0, 3, 1, 1)

        self.dimension_label = QLabel(self.frame_21)
        self.dimension_label.setObjectName(u"dimension_label")
        self.dimension_label.setMaximumSize(QSize(200, 35))
        self.dimension_label.setFont(font)

        self.gridLayout_27.addWidget(self.dimension_label, 0, 1, 1, 2)

        self.goptions_yaml_name_label = QLabel(self.frame_21)
        self.goptions_yaml_name_label.setObjectName(u"goptions_yaml_name_label")
        self.goptions_yaml_name_label.setMaximumSize(QSize(250, 35))
        self.goptions_yaml_name_label.setFont(font)

        self.gridLayout_27.addWidget(self.goptions_yaml_name_label, 5, 1, 1, 1)

        self.goptions_browse_yaml_path_label = QLabel(self.frame_21)
        self.goptions_browse_yaml_path_label.setObjectName(u"goptions_browse_yaml_path_label")
        self.goptions_browse_yaml_path_label.setMaximumSize(QSize(250, 35))
        self.goptions_browse_yaml_path_label.setFont(font)

        self.gridLayout_27.addWidget(self.goptions_browse_yaml_path_label, 3, 1, 1, 2)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_28, 3, 6, 1, 1)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 2, 5)

        self.goptions_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.goptions_scrollArea)

        self.stackedWidget_create_yaml_frame.addWidget(self.goptions_page)
        self.train_page = QWidget()
        self.train_page.setObjectName(u"train_page")
        self.train_general_frame = QFrame(self.train_page)
        self.train_general_frame.setObjectName(u"train_general_frame")
        self.train_general_frame.setGeometry(QRect(0, 0, 951, 463))
        self.train_general_frame.setMinimumSize(QSize(0, 0))
        self.train_general_frame.setFont(font)
        self.train_general_frame.setFrameShape(QFrame.StyledPanel)
        self.train_general_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.train_general_frame)
        self.gridLayout_14.setSpacing(9)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(9, -1, -1, -1)
        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_11, 2, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_18, 0, 1, 1, 1)

        self.frame_25 = QFrame(self.train_general_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 50))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_25)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 16777215))
        self.label_49.setFont(font)
        self.label_49.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_12.addWidget(self.label_49)

        self.enable_train_input = QComboBox(self.frame_25)
        self.enable_train_input.addItem("")
        self.enable_train_input.addItem("")
        self.enable_train_input.setObjectName(u"enable_train_input")
        self.enable_train_input.setMinimumSize(QSize(100, 0))
        self.enable_train_input.setFont(font)

        self.horizontalLayout_12.addWidget(self.enable_train_input)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_17)


        self.gridLayout_14.addWidget(self.frame_25, 0, 0, 1, 1)

        self.train_tab_widget = QTabWidget(self.train_general_frame)
        self.train_tab_widget.setObjectName(u"train_tab_widget")
        self.train_tab_widget.setFont(font)
        self.train_general_options_tab = QWidget()
        self.train_general_options_tab.setObjectName(u"train_general_options_tab")
        self.train_general_options_tab.setMaximumSize(QSize(16777215, 356))
        self.gridLayout_12 = QGridLayout(self.train_general_options_tab)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.train_scrollArea = QScrollArea(self.train_general_options_tab)
        self.train_scrollArea.setObjectName(u"train_scrollArea")
        self.train_scrollArea.setFont(font)
        self.train_scrollArea.setStyleSheet(u"")
        self.train_scrollArea.setFrameShape(QFrame.NoFrame)
        self.train_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -606, 934, 5832))
        self.scrollAreaWidgetContents_3.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.train_advanced_options_frame = QFrame(self.scrollAreaWidgetContents_3)
        self.train_advanced_options_frame.setObjectName(u"train_advanced_options_frame")
        self.train_advanced_options_frame.setMinimumSize(QSize(0, 0))
        self.train_advanced_options_frame.setMaximumSize(QSize(16777215, 16777215))
        self.train_advanced_options_frame.setFont(font)
        self.train_advanced_options_frame.setFrameShape(QFrame.NoFrame)
        self.train_advanced_options_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.train_advanced_options_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.train_advanced_options_frame_2 = QFrame(self.train_advanced_options_frame)
        self.train_advanced_options_frame_2.setObjectName(u"train_advanced_options_frame_2")
        self.train_advanced_options_frame_2.setMinimumSize(QSize(0, 0))
        self.train_advanced_options_frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.train_advanced_options_frame_2.setFont(font)
        self.train_advanced_options_frame_2.setFrameShape(QFrame.Box)
        self.gridLayout_4 = QGridLayout(self.train_advanced_options_frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 165, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 17, 0, 1, 1)

        self.frame_29 = QFrame(self.train_advanced_options_frame_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_69 = QGridLayout(self.frame_29)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setHorizontalSpacing(9)
        self.gridLayout_69.setVerticalSpacing(0)
        self.gridLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_29)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)

        self.gridLayout_69.addWidget(self.label_57, 0, 0, 1, 1)

        self.da_enable_input = QComboBox(self.frame_29)
        self.da_enable_input.addItem("")
        self.da_enable_input.addItem("")
        self.da_enable_input.setObjectName(u"da_enable_input")
        self.da_enable_input.setMinimumSize(QSize(200, 30))
        self.da_enable_input.setMaximumSize(QSize(200, 30))
        self.da_enable_input.setFont(font)

        self.gridLayout_69.addWidget(self.da_enable_input, 0, 1, 1, 1)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_69.addItem(self.horizontalSpacer_65, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_29, 14, 0, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_56, 1, 1, 1, 1)

        self.da_frame = QFrame(self.train_advanced_options_frame_2)
        self.da_frame.setObjectName(u"da_frame")
        self.da_frame.setMinimumSize(QSize(0, 0))
        self.da_frame.setFont(font)
        self.da_frame.setStyleSheet(u"background: rgb(246,246,246);")
        self.da_frame.setFrameShape(QFrame.Box)
        self.da_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.da_frame)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.da_elastic_mode_label = QLabel(self.da_frame)
        self.da_elastic_mode_label.setObjectName(u"da_elastic_mode_label")
        self.da_elastic_mode_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_mode_label, 23, 0, 1, 1)

        self.label_68 = QLabel(self.da_frame)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font)

        self.gridLayout_25.addWidget(self.label_68, 18, 0, 1, 1)

        self.da_contrast_em_mode_label = QLabel(self.da_frame)
        self.da_contrast_em_mode_label.setObjectName(u"da_contrast_em_mode_label")
        self.da_contrast_em_mode_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_em_mode_label, 43, 0, 1, 1)

        self.da_cutout_size_label = QLabel(self.da_frame)
        self.da_cutout_size_label.setObjectName(u"da_cutout_size_label")
        self.da_cutout_size_label.setMaximumSize(QSize(150, 16777215))
        self.da_cutout_size_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_size_label, 48, 0, 1, 1)

        self.da_cutout_input = QComboBox(self.da_frame)
        self.da_cutout_input.addItem("")
        self.da_cutout_input.addItem("")
        self.da_cutout_input.setObjectName(u"da_cutout_input")
        self.da_cutout_input.setMinimumSize(QSize(200, 30))
        self.da_cutout_input.setMaximumSize(QSize(200, 30))
        self.da_cutout_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_input, 46, 1, 1, 1)

        self.da_cutblur_input = QComboBox(self.da_frame)
        self.da_cutblur_input.addItem("")
        self.da_cutblur_input.addItem("")
        self.da_cutblur_input.setObjectName(u"da_cutblur_input")
        self.da_cutblur_input.setMinimumSize(QSize(200, 30))
        self.da_cutblur_input.setMaximumSize(QSize(200, 30))
        self.da_cutblur_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblur_input, 51, 1, 1, 1)

        self.da_gamma_contrast_input = QComboBox(self.da_frame)
        self.da_gamma_contrast_input.addItem("")
        self.da_gamma_contrast_input.addItem("")
        self.da_gamma_contrast_input.setObjectName(u"da_gamma_contrast_input")
        self.da_gamma_contrast_input.setMinimumSize(QSize(200, 30))
        self.da_gamma_contrast_input.setMaximumSize(QSize(200, 30))
        self.da_gamma_contrast_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gamma_contrast_input, 30, 1, 1, 1)

        self.da_grayscale_input = QComboBox(self.da_frame)
        self.da_grayscale_input.addItem("")
        self.da_grayscale_input.addItem("")
        self.da_grayscale_input.setObjectName(u"da_grayscale_input")
        self.da_grayscale_input.setMinimumSize(QSize(200, 30))
        self.da_grayscale_input.setMaximumSize(QSize(200, 30))
        self.da_grayscale_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_grayscale_input, 66, 1, 1, 1)

        self.label_107 = QLabel(self.da_frame)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font)

        self.gridLayout_25.addWidget(self.label_107, 44, 0, 1, 1)

        self.label_132 = QLabel(self.da_frame)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font)

        self.gridLayout_25.addWidget(self.label_132, 77, 0, 1, 1)

        self.da_misaligment_rotate_ratio_input = QLineEdit(self.da_frame)
        self.da_misaligment_rotate_ratio_input.setObjectName(u"da_misaligment_rotate_ratio_input")
        self.da_misaligment_rotate_ratio_input.setMinimumSize(QSize(200, 30))
        self.da_misaligment_rotate_ratio_input.setMaximumSize(QSize(200, 30))
        self.da_misaligment_rotate_ratio_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_misaligment_rotate_ratio_input, 63, 1, 1, 1)

        self.da_brightness_em_factor_label = QLabel(self.da_frame)
        self.da_brightness_em_factor_label.setObjectName(u"da_brightness_em_factor_label")
        self.da_brightness_em_factor_label.setMaximumSize(QSize(150, 16777215))
        self.da_brightness_em_factor_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_em_factor_label, 39, 0, 1, 1)

        self.da_contrast_em_mode_input = QComboBox(self.da_frame)
        self.da_contrast_em_mode_input.addItem("")
        self.da_contrast_em_mode_input.addItem("")
        self.da_contrast_em_mode_input.setObjectName(u"da_contrast_em_mode_input")
        self.da_contrast_em_mode_input.setMinimumSize(QSize(200, 30))
        self.da_contrast_em_mode_input.setMaximumSize(QSize(200, 30))
        self.da_contrast_em_mode_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_em_mode_input, 43, 1, 1, 1)

        self.label_78 = QLabel(self.da_frame)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font)

        self.gridLayout_25.addWidget(self.label_78, 28, 0, 1, 1)

        self.da_brightness_em_factor_input = QLineEdit(self.da_frame)
        self.da_brightness_em_factor_input.setObjectName(u"da_brightness_em_factor_input")
        self.da_brightness_em_factor_input.setMinimumSize(QSize(200, 30))
        self.da_brightness_em_factor_input.setMaximumSize(QSize(200, 30))
        self.da_brightness_em_factor_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_em_factor_input, 39, 1, 1, 1)

        self.da_cutblur_size_range_label = QLabel(self.da_frame)
        self.da_cutblur_size_range_label.setObjectName(u"da_cutblur_size_range_label")
        self.da_cutblur_size_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblur_size_range_label, 52, 0, 1, 1)

        self.label_73 = QLabel(self.da_frame)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font)

        self.gridLayout_25.addWidget(self.label_73, 16, 0, 1, 1)

        self.da_cutblur_inside_label = QLabel(self.da_frame)
        self.da_cutblur_inside_label.setObjectName(u"da_cutblur_inside_label")
        self.da_cutblur_inside_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblur_inside_label, 54, 0, 1, 1)

        self.label_72 = QLabel(self.da_frame)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font)

        self.gridLayout_25.addWidget(self.label_72, 17, 0, 1, 1)

        self.label_63 = QLabel(self.da_frame)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font)

        self.gridLayout_25.addWidget(self.label_63, 6, 0, 1, 1)

        self.label_109 = QLabel(self.da_frame)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font)

        self.gridLayout_25.addWidget(self.label_109, 51, 0, 1, 1)

        self.da_cuout_cval_label = QLabel(self.da_frame)
        self.da_cuout_cval_label.setObjectName(u"da_cuout_cval_label")
        self.da_cuout_cval_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cuout_cval_label, 49, 0, 1, 1)

        self.da_motion_blur_k_size_input = QLineEdit(self.da_frame)
        self.da_motion_blur_k_size_input.setObjectName(u"da_motion_blur_k_size_input")
        self.da_motion_blur_k_size_input.setMinimumSize(QSize(200, 30))
        self.da_motion_blur_k_size_input.setMaximumSize(QSize(200, 30))
        self.da_motion_blur_k_size_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_motion_blur_k_size_input, 29, 1, 1, 1)

        self.da_elastic_sigma_input = QLineEdit(self.da_frame)
        self.da_elastic_sigma_input.setObjectName(u"da_elastic_sigma_input")
        self.da_elastic_sigma_input.setMinimumSize(QSize(200, 30))
        self.da_elastic_sigma_input.setMaximumSize(QSize(200, 30))
        self.da_elastic_sigma_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_sigma_input, 22, 1, 1, 1)

        self.label_64 = QLabel(self.da_frame)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font)

        self.gridLayout_25.addWidget(self.label_64, 4, 0, 1, 1)

        self.da_vertical_flip_input = QComboBox(self.da_frame)
        self.da_vertical_flip_input.addItem("")
        self.da_vertical_flip_input.addItem("")
        self.da_vertical_flip_input.setObjectName(u"da_vertical_flip_input")
        self.da_vertical_flip_input.setMinimumSize(QSize(200, 30))
        self.da_vertical_flip_input.setMaximumSize(QSize(200, 30))
        self.da_vertical_flip_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_vertical_flip_input, 17, 1, 1, 1)

        self.da_pepper_amount_label = QLabel(self.da_frame)
        self.da_pepper_amount_label.setObjectName(u"da_pepper_amount_label")
        self.da_pepper_amount_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_pepper_amount_label, 81, 0, 1, 1)

        self.label_91 = QLabel(self.da_frame)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font)

        self.gridLayout_25.addWidget(self.label_91, 32, 0, 1, 1)

        self.label_135 = QLabel(self.da_frame)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font)

        self.gridLayout_25.addWidget(self.label_135, 73, 0, 1, 1)

        self.da_contrast_em_factor_label = QLabel(self.da_frame)
        self.da_contrast_em_factor_label.setObjectName(u"da_contrast_em_factor_label")
        self.da_contrast_em_factor_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_em_factor_label, 42, 0, 1, 1)

        self.da_cutnoise_number_iter_input = QLineEdit(self.da_frame)
        self.da_cutnoise_number_iter_input.setObjectName(u"da_cutnoise_number_iter_input")
        self.da_cutnoise_number_iter_input.setMinimumSize(QSize(200, 30))
        self.da_cutnoise_number_iter_input.setMaximumSize(QSize(200, 30))
        self.da_cutnoise_number_iter_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_number_iter_input, 59, 1, 1, 1)

        self.da_cutblut_down_range_input = QLineEdit(self.da_frame)
        self.da_cutblut_down_range_input.setObjectName(u"da_cutblut_down_range_input")
        self.da_cutblut_down_range_input.setMinimumSize(QSize(200, 30))
        self.da_cutblut_down_range_input.setMaximumSize(QSize(200, 30))
        self.da_cutblut_down_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblut_down_range_input, 53, 1, 1, 1)

        self.da_random_rot_range_input = QLineEdit(self.da_frame)
        self.da_random_rot_range_input.setObjectName(u"da_random_rot_range_input")
        self.da_random_rot_range_input.setMinimumSize(QSize(200, 30))
        self.da_random_rot_range_input.setMaximumSize(QSize(200, 30))
        self.da_random_rot_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_random_rot_range_input, 9, 1, 1, 1)

        self.da_brightness_input = QComboBox(self.da_frame)
        self.da_brightness_input.addItem("")
        self.da_brightness_input.addItem("")
        self.da_brightness_input.setObjectName(u"da_brightness_input")
        self.da_brightness_input.setMinimumSize(QSize(200, 30))
        self.da_brightness_input.setMaximumSize(QSize(200, 30))
        self.da_brightness_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_input, 32, 1, 1, 1)

        self.da_cutnoise_size_range_input = QLineEdit(self.da_frame)
        self.da_cutnoise_size_range_input.setObjectName(u"da_cutnoise_size_range_input")
        self.da_cutnoise_size_range_input.setMinimumSize(QSize(200, 30))
        self.da_cutnoise_size_range_input.setMaximumSize(QSize(200, 30))
        self.da_cutnoise_size_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_size_range_input, 60, 1, 1, 1)

        self.da_missing_sections_input = QComboBox(self.da_frame)
        self.da_missing_sections_input.addItem("")
        self.da_missing_sections_input.addItem("")
        self.da_missing_sections_input.setObjectName(u"da_missing_sections_input")
        self.da_missing_sections_input.setMinimumSize(QSize(200, 30))
        self.da_missing_sections_input.setMaximumSize(QSize(200, 30))
        self.da_missing_sections_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_missing_sections_input, 64, 1, 1, 1)

        self.da_cutnoise_label = QLabel(self.da_frame)
        self.da_cutnoise_label.setObjectName(u"da_cutnoise_label")
        self.da_cutnoise_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_label, 57, 0, 1, 1)

        self.da_zoom_range_input = QLineEdit(self.da_frame)
        self.da_zoom_range_input.setObjectName(u"da_zoom_range_input")
        self.da_zoom_range_input.setMinimumSize(QSize(200, 30))
        self.da_zoom_range_input.setMaximumSize(QSize(200, 30))
        self.da_zoom_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_zoom_range_input, 13, 1, 1, 1)

        self.da_shear_range_input = QLineEdit(self.da_frame)
        self.da_shear_range_input.setObjectName(u"da_shear_range_input")
        self.da_shear_range_input.setMinimumSize(QSize(200, 30))
        self.da_shear_range_input.setMaximumSize(QSize(200, 30))
        self.da_shear_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_shear_range_input, 11, 1, 1, 1)

        self.da_z_flip_input = QComboBox(self.da_frame)
        self.da_z_flip_input.addItem("")
        self.da_z_flip_input.addItem("")
        self.da_z_flip_input.setObjectName(u"da_z_flip_input")
        self.da_z_flip_input.setMinimumSize(QSize(200, 30))
        self.da_z_flip_input.setMaximumSize(QSize(200, 30))
        self.da_z_flip_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_z_flip_input, 19, 1, 1, 1)

        self.da_num_samples_check_input = QLineEdit(self.da_frame)
        self.da_num_samples_check_input.setObjectName(u"da_num_samples_check_input")
        self.da_num_samples_check_input.setMinimumSize(QSize(200, 30))
        self.da_num_samples_check_input.setMaximumSize(QSize(200, 30))
        self.da_num_samples_check_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_num_samples_check_input, 4, 1, 1, 1)

        self.label_123 = QLabel(self.da_frame)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font)

        self.gridLayout_25.addWidget(self.label_123, 66, 0, 1, 1)

        self.label_127 = QLabel(self.da_frame)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font)

        self.gridLayout_25.addWidget(self.label_127, 64, 0, 1, 1)

        self.da_brightness_mode_label = QLabel(self.da_frame)
        self.da_brightness_mode_label.setObjectName(u"da_brightness_mode_label")
        self.da_brightness_mode_label.setMaximumSize(QSize(150, 16777215))
        self.da_brightness_mode_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_mode_label, 34, 0, 1, 1)

        self.da_grid_ratio_label = QLabel(self.da_frame)
        self.da_grid_ratio_label.setObjectName(u"da_grid_ratio_label")
        self.da_grid_ratio_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_ratio_label, 69, 0, 1, 1)

        self.label_103 = QLabel(self.da_frame)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font)

        self.gridLayout_25.addWidget(self.label_103, 46, 0, 1, 1)

        self.da_draw_grid_input = QComboBox(self.da_frame)
        self.da_draw_grid_input.addItem("")
        self.da_draw_grid_input.addItem("")
        self.da_draw_grid_input.setObjectName(u"da_draw_grid_input")
        self.da_draw_grid_input.setMinimumSize(QSize(200, 30))
        self.da_draw_grid_input.setMaximumSize(QSize(200, 30))
        self.da_draw_grid_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_draw_grid_input, 3, 1, 1, 1)

        self.da_contrast_em_input = QComboBox(self.da_frame)
        self.da_contrast_em_input.addItem("")
        self.da_contrast_em_input.addItem("")
        self.da_contrast_em_input.setObjectName(u"da_contrast_em_input")
        self.da_contrast_em_input.setMinimumSize(QSize(200, 30))
        self.da_contrast_em_input.setMaximumSize(QSize(200, 30))
        self.da_contrast_em_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_em_input, 41, 1, 1, 1)

        self.da_contrast_factor_range_label = QLabel(self.da_frame)
        self.da_contrast_factor_range_label.setObjectName(u"da_contrast_factor_range_label")
        self.da_contrast_factor_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_factor_range_label, 36, 0, 1, 1)

        self.da_cutmix_input = QComboBox(self.da_frame)
        self.da_cutmix_input.addItem("")
        self.da_cutmix_input.addItem("")
        self.da_cutmix_input.setObjectName(u"da_cutmix_input")
        self.da_cutmix_input.setMinimumSize(QSize(200, 30))
        self.da_cutmix_input.setMaximumSize(QSize(200, 30))
        self.da_cutmix_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutmix_input, 55, 1, 1, 1)

        self.da_dropout_range_label = QLabel(self.da_frame)
        self.da_dropout_range_label.setObjectName(u"da_dropout_range_label")
        self.da_dropout_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_dropout_range_label, 45, 0, 1, 1)

        self.da_median_blur_input = QComboBox(self.da_frame)
        self.da_median_blur_input.addItem("")
        self.da_median_blur_input.addItem("")
        self.da_median_blur_input.setObjectName(u"da_median_blur_input")
        self.da_median_blur_input.setMinimumSize(QSize(200, 30))
        self.da_median_blur_input.setMaximumSize(QSize(200, 30))
        self.da_median_blur_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_median_blur_input, 26, 1, 1, 1)

        self.da_salt_input = QComboBox(self.da_frame)
        self.da_salt_input.addItem("")
        self.da_salt_input.addItem("")
        self.da_salt_input.setObjectName(u"da_salt_input")
        self.da_salt_input.setMinimumSize(QSize(200, 30))
        self.da_salt_input.setMaximumSize(QSize(200, 30))
        self.da_salt_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_input, 78, 1, 1, 1)

        self.da_cutout_to_mask_input = QComboBox(self.da_frame)
        self.da_cutout_to_mask_input.addItem("")
        self.da_cutout_to_mask_input.addItem("")
        self.da_cutout_to_mask_input.setObjectName(u"da_cutout_to_mask_input")
        self.da_cutout_to_mask_input.setMinimumSize(QSize(200, 30))
        self.da_cutout_to_mask_input.setMaximumSize(QSize(200, 30))
        self.da_cutout_to_mask_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_to_mask_input, 50, 1, 1, 1)

        self.da_gaussian_noise_var_label = QLabel(self.da_frame)
        self.da_gaussian_noise_var_label.setObjectName(u"da_gaussian_noise_var_label")
        self.da_gaussian_noise_var_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_var_label, 75, 0, 1, 1)

        self.da_salt_pepper_amount_input = QLineEdit(self.da_frame)
        self.da_salt_pepper_amount_input.setObjectName(u"da_salt_pepper_amount_input")
        self.da_salt_pepper_amount_input.setMinimumSize(QSize(200, 30))
        self.da_salt_pepper_amount_input.setMaximumSize(QSize(200, 30))
        self.da_salt_pepper_amount_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_pepper_amount_input, 83, 1, 1, 1)

        self.da_random_rot_input = QComboBox(self.da_frame)
        self.da_random_rot_input.addItem("")
        self.da_random_rot_input.addItem("")
        self.da_random_rot_input.setObjectName(u"da_random_rot_input")
        self.da_random_rot_input.setMinimumSize(QSize(200, 30))
        self.da_random_rot_input.setMaximumSize(QSize(200, 30))
        self.da_random_rot_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_random_rot_input, 8, 1, 1, 1)

        self.da_shuffle_val_input = QComboBox(self.da_frame)
        self.da_shuffle_val_input.addItem("")
        self.da_shuffle_val_input.addItem("")
        self.da_shuffle_val_input.setObjectName(u"da_shuffle_val_input")
        self.da_shuffle_val_input.setMinimumSize(QSize(200, 30))
        self.da_shuffle_val_input.setMaximumSize(QSize(200, 30))
        self.da_shuffle_val_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_shuffle_val_input, 6, 1, 1, 1)

        self.label_118 = QLabel(self.da_frame)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font)

        self.gridLayout_25.addWidget(self.label_118, 68, 0, 1, 1)

        self.label_83 = QLabel(self.da_frame)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font)

        self.gridLayout_25.addWidget(self.label_83, 26, 0, 1, 1)

        self.da_shear_input = QComboBox(self.da_frame)
        self.da_shear_input.addItem("")
        self.da_shear_input.addItem("")
        self.da_shear_input.setObjectName(u"da_shear_input")
        self.da_shear_input.setMinimumSize(QSize(200, 30))
        self.da_shear_input.setMaximumSize(QSize(200, 30))
        self.da_shear_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_shear_input, 10, 1, 1, 1)

        self.da_grid_invert_input = QComboBox(self.da_frame)
        self.da_grid_invert_input.addItem("")
        self.da_grid_invert_input.addItem("")
        self.da_grid_invert_input.setObjectName(u"da_grid_invert_input")
        self.da_grid_invert_input.setMinimumSize(QSize(200, 30))
        self.da_grid_invert_input.setMaximumSize(QSize(200, 30))
        self.da_grid_invert_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_invert_input, 72, 1, 1, 1)

        self.da_elastic_mode_input = QComboBox(self.da_frame)
        self.da_elastic_mode_input.addItem("")
        self.da_elastic_mode_input.setObjectName(u"da_elastic_mode_input")
        self.da_elastic_mode_input.setMinimumSize(QSize(200, 30))
        self.da_elastic_mode_input.setMaximumSize(QSize(200, 30))
        self.da_elastic_mode_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_mode_input, 23, 1, 1, 1)

        self.da_contrast_mode_label = QLabel(self.da_frame)
        self.da_contrast_mode_label.setObjectName(u"da_contrast_mode_label")
        self.da_contrast_mode_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_mode_label, 37, 0, 1, 1)

        self.da_cutout_to_mask_label = QLabel(self.da_frame)
        self.da_cutout_to_mask_label.setObjectName(u"da_cutout_to_mask_label")
        self.da_cutout_to_mask_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_to_mask_label, 50, 0, 1, 1)

        self.da_median_blur_k_size_label = QLabel(self.da_frame)
        self.da_median_blur_k_size_label.setObjectName(u"da_median_blur_k_size_label")
        self.da_median_blur_k_size_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_median_blur_k_size_label, 27, 0, 1, 1)

        self.da_cutnoise_scale_range_input = QLineEdit(self.da_frame)
        self.da_cutnoise_scale_range_input.setObjectName(u"da_cutnoise_scale_range_input")
        self.da_cutnoise_scale_range_input.setMinimumSize(QSize(200, 30))
        self.da_cutnoise_scale_range_input.setMaximumSize(QSize(200, 30))
        self.da_cutnoise_scale_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_scale_range_input, 58, 1, 1, 1)

        self.da_grid_d_range_input = QLineEdit(self.da_frame)
        self.da_grid_d_range_input.setObjectName(u"da_grid_d_range_input")
        self.da_grid_d_range_input.setMinimumSize(QSize(200, 30))
        self.da_grid_d_range_input.setMaximumSize(QSize(200, 30))
        self.da_grid_d_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_d_range_input, 70, 1, 1, 1)

        self.da_misaligment_displacement_label = QLabel(self.da_frame)
        self.da_misaligment_displacement_label.setObjectName(u"da_misaligment_displacement_label")
        self.da_misaligment_displacement_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_misaligment_displacement_label, 62, 0, 1, 1)

        self.da_missing_sections_iteration_range_input = QLineEdit(self.da_frame)
        self.da_missing_sections_iteration_range_input.setObjectName(u"da_missing_sections_iteration_range_input")
        self.da_missing_sections_iteration_range_input.setMinimumSize(QSize(200, 30))
        self.da_missing_sections_iteration_range_input.setMaximumSize(QSize(200, 30))
        self.da_missing_sections_iteration_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_missing_sections_iteration_range_input, 65, 1, 1, 1)

        self.da_gaussian_noise_use_input_img_label = QLabel(self.da_frame)
        self.da_gaussian_noise_use_input_img_label.setObjectName(u"da_gaussian_noise_use_input_img_label")
        self.da_gaussian_noise_use_input_img_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_use_input_img_label, 76, 0, 1, 1)

        self.da_gaussian_noise_use_input_img_input = QComboBox(self.da_frame)
        self.da_gaussian_noise_use_input_img_input.addItem("")
        self.da_gaussian_noise_use_input_img_input.addItem("")
        self.da_gaussian_noise_use_input_img_input.setObjectName(u"da_gaussian_noise_use_input_img_input")
        self.da_gaussian_noise_use_input_img_input.setMinimumSize(QSize(200, 30))
        self.da_gaussian_noise_use_input_img_input.setMaximumSize(QSize(200, 30))
        self.da_gaussian_noise_use_input_img_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_use_input_img_input, 76, 1, 1, 1)

        self.label_88 = QLabel(self.da_frame)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font)

        self.gridLayout_25.addWidget(self.label_88, 38, 0, 1, 1)

        self.da_elastic_sigma_label = QLabel(self.da_frame)
        self.da_elastic_sigma_label.setObjectName(u"da_elastic_sigma_label")
        self.da_elastic_sigma_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_sigma_label, 22, 0, 1, 1)

        self.da_dropout_input = QComboBox(self.da_frame)
        self.da_dropout_input.addItem("")
        self.da_dropout_input.addItem("")
        self.da_dropout_input.setObjectName(u"da_dropout_input")
        self.da_dropout_input.setMinimumSize(QSize(200, 30))
        self.da_dropout_input.setMaximumSize(QSize(200, 30))
        self.da_dropout_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_dropout_input, 44, 1, 1, 1)

        self.da_misaligment_input = QComboBox(self.da_frame)
        self.da_misaligment_input.addItem("")
        self.da_misaligment_input.addItem("")
        self.da_misaligment_input.setObjectName(u"da_misaligment_input")
        self.da_misaligment_input.setMinimumSize(QSize(200, 30))
        self.da_misaligment_input.setMaximumSize(QSize(200, 30))
        self.da_misaligment_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_misaligment_input, 61, 1, 1, 1)

        self.da_cutout_number_iterations_label = QLabel(self.da_frame)
        self.da_cutout_number_iterations_label.setObjectName(u"da_cutout_number_iterations_label")
        self.da_cutout_number_iterations_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_number_iterations_label, 47, 0, 1, 1)

        self.label_60 = QLabel(self.da_frame)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.gridLayout_25.addWidget(self.label_60, 1, 0, 1, 1)

        self.label_71 = QLabel(self.da_frame)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font)

        self.gridLayout_25.addWidget(self.label_71, 12, 0, 1, 1)

        self.label_62 = QLabel(self.da_frame)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font)

        self.gridLayout_25.addWidget(self.label_62, 2, 0, 1, 1)

        self.da_zoom_input = QComboBox(self.da_frame)
        self.da_zoom_input.addItem("")
        self.da_zoom_input.addItem("")
        self.da_zoom_input.setObjectName(u"da_zoom_input")
        self.da_zoom_input.setMinimumSize(QSize(200, 30))
        self.da_zoom_input.setMaximumSize(QSize(200, 30))
        self.da_zoom_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_zoom_input, 12, 1, 1, 1)

        self.da_contrast_input = QComboBox(self.da_frame)
        self.da_contrast_input.addItem("")
        self.da_contrast_input.addItem("")
        self.da_contrast_input.setObjectName(u"da_contrast_input")
        self.da_contrast_input.setMinimumSize(QSize(200, 30))
        self.da_contrast_input.setMaximumSize(QSize(200, 30))
        self.da_contrast_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_input, 35, 1, 1, 1)

        self.da_salt_amount_label = QLabel(self.da_frame)
        self.da_salt_amount_label.setObjectName(u"da_salt_amount_label")
        self.da_salt_amount_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_amount_label, 79, 0, 1, 1)

        self.da_shear_range_label = QLabel(self.da_frame)
        self.da_shear_range_label.setObjectName(u"da_shear_range_label")
        self.da_shear_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_shear_range_label, 11, 0, 1, 1)

        self.da_cutnoise_size_range_label = QLabel(self.da_frame)
        self.da_cutnoise_size_range_label.setObjectName(u"da_cutnoise_size_range_label")
        self.da_cutnoise_size_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_size_range_label, 60, 0, 1, 1)

        self.da_dropout_range_input = QLineEdit(self.da_frame)
        self.da_dropout_range_input.setObjectName(u"da_dropout_range_input")
        self.da_dropout_range_input.setMinimumSize(QSize(200, 30))
        self.da_dropout_range_input.setMaximumSize(QSize(200, 30))
        self.da_dropout_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_dropout_range_input, 45, 1, 1, 1)

        self.da_contrast_em_factor_input = QLineEdit(self.da_frame)
        self.da_contrast_em_factor_input.setObjectName(u"da_contrast_em_factor_input")
        self.da_contrast_em_factor_input.setMinimumSize(QSize(200, 30))
        self.da_contrast_em_factor_input.setMaximumSize(QSize(200, 30))
        self.da_contrast_em_factor_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_em_factor_input, 42, 1, 1, 1)

        self.da_salt_amount_input = QLineEdit(self.da_frame)
        self.da_salt_amount_input.setObjectName(u"da_salt_amount_input")
        self.da_salt_amount_input.setMinimumSize(QSize(200, 30))
        self.da_salt_amount_input.setMaximumSize(QSize(200, 30))
        self.da_salt_amount_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_amount_input, 79, 1, 1, 1)

        self.da_gamma_contrast_range_input = QLineEdit(self.da_frame)
        self.da_gamma_contrast_range_input.setObjectName(u"da_gamma_contrast_range_input")
        self.da_gamma_contrast_range_input.setMinimumSize(QSize(200, 30))
        self.da_gamma_contrast_range_input.setMaximumSize(QSize(200, 30))
        self.da_gamma_contrast_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gamma_contrast_range_input, 31, 1, 1, 1)

        self.da_gaussian_noise_mean_label = QLabel(self.da_frame)
        self.da_gaussian_noise_mean_label.setObjectName(u"da_gaussian_noise_mean_label")
        self.da_gaussian_noise_mean_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_mean_label, 74, 0, 1, 1)

        self.da_grid_rotate_label = QLabel(self.da_frame)
        self.da_grid_rotate_label.setObjectName(u"da_grid_rotate_label")
        self.da_grid_rotate_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_rotate_label, 71, 0, 1, 1)

        self.label_77 = QLabel(self.da_frame)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font)

        self.gridLayout_25.addWidget(self.label_77, 14, 0, 1, 1)

        self.da_cutblur_inside_input = QComboBox(self.da_frame)
        self.da_cutblur_inside_input.addItem("")
        self.da_cutblur_inside_input.addItem("")
        self.da_cutblur_inside_input.setObjectName(u"da_cutblur_inside_input")
        self.da_cutblur_inside_input.setMinimumSize(QSize(200, 30))
        self.da_cutblur_inside_input.setMaximumSize(QSize(200, 30))
        self.da_cutblur_inside_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblur_inside_input, 54, 1, 1, 1)

        self.da_check_input = QComboBox(self.da_frame)
        self.da_check_input.addItem("")
        self.da_check_input.addItem("")
        self.da_check_input.setObjectName(u"da_check_input")
        self.da_check_input.setMinimumSize(QSize(200, 30))
        self.da_check_input.setMaximumSize(QSize(200, 30))
        self.da_check_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_check_input, 2, 1, 1, 1)

        self.da_gaussian_noise_input = QComboBox(self.da_frame)
        self.da_gaussian_noise_input.addItem("")
        self.da_gaussian_noise_input.addItem("")
        self.da_gaussian_noise_input.setObjectName(u"da_gaussian_noise_input")
        self.da_gaussian_noise_input.setMinimumSize(QSize(200, 30))
        self.da_gaussian_noise_input.setMaximumSize(QSize(200, 30))
        self.da_gaussian_noise_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_input, 73, 1, 1, 1)

        self.da_cutnoise_input = QComboBox(self.da_frame)
        self.da_cutnoise_input.addItem("")
        self.da_cutnoise_input.addItem("")
        self.da_cutnoise_input.setObjectName(u"da_cutnoise_input")
        self.da_cutnoise_input.setMinimumSize(QSize(200, 30))
        self.da_cutnoise_input.setMaximumSize(QSize(200, 30))
        self.da_cutnoise_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_input, 57, 1, 1, 1)

        self.label_99 = QLabel(self.da_frame)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMaximumSize(QSize(150, 16777215))
        self.label_99.setFont(font)

        self.gridLayout_25.addWidget(self.label_99, 41, 0, 1, 1)

        self.da_salt_pepper_input = QComboBox(self.da_frame)
        self.da_salt_pepper_input.addItem("")
        self.da_salt_pepper_input.addItem("")
        self.da_salt_pepper_input.setObjectName(u"da_salt_pepper_input")
        self.da_salt_pepper_input.setMinimumSize(QSize(200, 30))
        self.da_salt_pepper_input.setMaximumSize(QSize(200, 30))
        self.da_salt_pepper_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_pepper_input, 82, 1, 1, 1)

        self.da_gridmask_input = QComboBox(self.da_frame)
        self.da_gridmask_input.addItem("")
        self.da_gridmask_input.addItem("")
        self.da_gridmask_input.setObjectName(u"da_gridmask_input")
        self.da_gridmask_input.setMinimumSize(QSize(200, 30))
        self.da_gridmask_input.setMaximumSize(QSize(200, 30))
        self.da_gridmask_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gridmask_input, 68, 1, 1, 1)

        self.da_cuout_cval_input = QLineEdit(self.da_frame)
        self.da_cuout_cval_input.setObjectName(u"da_cuout_cval_input")
        self.da_cuout_cval_input.setMinimumSize(QSize(200, 30))
        self.da_cuout_cval_input.setMaximumSize(QSize(200, 30))
        self.da_cuout_cval_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cuout_cval_input, 49, 1, 1, 1)

        self.da_shift_range_input = QLineEdit(self.da_frame)
        self.da_shift_range_input.setObjectName(u"da_shift_range_input")
        self.da_shift_range_input.setMinimumSize(QSize(200, 30))
        self.da_shift_range_input.setMaximumSize(QSize(200, 30))
        self.da_shift_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_shift_range_input, 15, 1, 1, 1)

        self.da_gaussian_sigma_input = QLineEdit(self.da_frame)
        self.da_gaussian_sigma_input.setObjectName(u"da_gaussian_sigma_input")
        self.da_gaussian_sigma_input.setMinimumSize(QSize(200, 30))
        self.da_gaussian_sigma_input.setMaximumSize(QSize(200, 30))
        self.da_gaussian_sigma_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_sigma_input, 25, 1, 1, 1)

        self.da_grid_invert_label = QLabel(self.da_frame)
        self.da_grid_invert_label.setObjectName(u"da_grid_invert_label")
        self.da_grid_invert_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_invert_label, 72, 0, 1, 1)

        self.da_brightness_factor_range_input = QLineEdit(self.da_frame)
        self.da_brightness_factor_range_input.setObjectName(u"da_brightness_factor_range_input")
        self.da_brightness_factor_range_input.setMinimumSize(QSize(200, 30))
        self.da_brightness_factor_range_input.setMaximumSize(QSize(200, 30))
        self.da_brightness_factor_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_factor_range_input, 33, 1, 1, 1)

        self.label_94 = QLabel(self.da_frame)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font)

        self.gridLayout_25.addWidget(self.label_94, 30, 0, 1, 1)

        self.da_pepper_amount_input = QLineEdit(self.da_frame)
        self.da_pepper_amount_input.setObjectName(u"da_pepper_amount_input")
        self.da_pepper_amount_input.setMinimumSize(QSize(200, 30))
        self.da_pepper_amount_input.setMaximumSize(QSize(200, 30))
        self.da_pepper_amount_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_pepper_amount_input, 81, 1, 1, 1)

        self.da_motion_blur_input = QComboBox(self.da_frame)
        self.da_motion_blur_input.addItem("")
        self.da_motion_blur_input.addItem("")
        self.da_motion_blur_input.setObjectName(u"da_motion_blur_input")
        self.da_motion_blur_input.setMinimumSize(QSize(200, 30))
        self.da_motion_blur_input.setMaximumSize(QSize(200, 30))
        self.da_motion_blur_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_motion_blur_input, 28, 1, 1, 1)

        self.da_zoom_range_label = QLabel(self.da_frame)
        self.da_zoom_range_label.setObjectName(u"da_zoom_range_label")
        self.da_zoom_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_zoom_range_label, 13, 0, 1, 1)

        self.da_brightness_mode_input = QComboBox(self.da_frame)
        self.da_brightness_mode_input.addItem("")
        self.da_brightness_mode_input.addItem("")
        self.da_brightness_mode_input.setObjectName(u"da_brightness_mode_input")
        self.da_brightness_mode_input.setMinimumSize(QSize(200, 30))
        self.da_brightness_mode_input.setMaximumSize(QSize(200, 30))
        self.da_brightness_mode_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_mode_input, 34, 1, 1, 1)

        self.da_cutout_size_input = QLineEdit(self.da_frame)
        self.da_cutout_size_input.setObjectName(u"da_cutout_size_input")
        self.da_cutout_size_input.setMinimumSize(QSize(200, 30))
        self.da_cutout_size_input.setMaximumSize(QSize(200, 30))
        self.da_cutout_size_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_size_input, 48, 1, 1, 1)

        self.da_prob_input = QLineEdit(self.da_frame)
        self.da_prob_input.setObjectName(u"da_prob_input")
        self.da_prob_input.setMinimumSize(QSize(200, 30))
        self.da_prob_input.setMaximumSize(QSize(200, 30))
        self.da_prob_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_prob_input, 1, 1, 1, 1)

        self.da_contrast_factor_range_input = QLineEdit(self.da_frame)
        self.da_contrast_factor_range_input.setObjectName(u"da_contrast_factor_range_input")
        self.da_contrast_factor_range_input.setMinimumSize(QSize(200, 30))
        self.da_contrast_factor_range_input.setMaximumSize(QSize(200, 30))
        self.da_contrast_factor_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_factor_range_input, 36, 1, 1, 1)

        self.da_salt_pepper_prop_input = QLineEdit(self.da_frame)
        self.da_salt_pepper_prop_input.setObjectName(u"da_salt_pepper_prop_input")
        self.da_salt_pepper_prop_input.setMinimumSize(QSize(200, 30))
        self.da_salt_pepper_prop_input.setMaximumSize(QSize(200, 30))
        self.da_salt_pepper_prop_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_pepper_prop_input, 84, 1, 1, 1)

        self.da_z_flip_label = QLabel(self.da_frame)
        self.da_z_flip_label.setObjectName(u"da_z_flip_label")
        self.da_z_flip_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_z_flip_label, 19, 0, 1, 1)

        self.da_horizontal_flip_input = QComboBox(self.da_frame)
        self.da_horizontal_flip_input.addItem("")
        self.da_horizontal_flip_input.addItem("")
        self.da_horizontal_flip_input.setObjectName(u"da_horizontal_flip_input")
        self.da_horizontal_flip_input.setMinimumSize(QSize(200, 30))
        self.da_horizontal_flip_input.setMaximumSize(QSize(200, 30))
        self.da_horizontal_flip_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_horizontal_flip_input, 18, 1, 1, 1)

        self.da_misaligment_displacement_input = QLineEdit(self.da_frame)
        self.da_misaligment_displacement_input.setObjectName(u"da_misaligment_displacement_input")
        self.da_misaligment_displacement_input.setMinimumSize(QSize(200, 30))
        self.da_misaligment_displacement_input.setMaximumSize(QSize(200, 30))
        self.da_misaligment_displacement_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_misaligment_displacement_input, 62, 1, 1, 1)

        self.label_84 = QLabel(self.da_frame)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font)

        self.gridLayout_25.addWidget(self.label_84, 20, 0, 1, 1)

        self.da_poisson_noise_input = QComboBox(self.da_frame)
        self.da_poisson_noise_input.addItem("")
        self.da_poisson_noise_input.addItem("")
        self.da_poisson_noise_input.setObjectName(u"da_poisson_noise_input")
        self.da_poisson_noise_input.setMinimumSize(QSize(200, 30))
        self.da_poisson_noise_input.setMaximumSize(QSize(200, 30))
        self.da_poisson_noise_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_poisson_noise_input, 77, 1, 1, 1)

        self.da_shuffle_train_input = QComboBox(self.da_frame)
        self.da_shuffle_train_input.addItem("")
        self.da_shuffle_train_input.addItem("")
        self.da_shuffle_train_input.setObjectName(u"da_shuffle_train_input")
        self.da_shuffle_train_input.setMinimumSize(QSize(200, 30))
        self.da_shuffle_train_input.setMaximumSize(QSize(200, 30))
        self.da_shuffle_train_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_shuffle_train_input, 5, 1, 1, 1)

        self.da_cutblut_down_range_label = QLabel(self.da_frame)
        self.da_cutblut_down_range_label.setObjectName(u"da_cutblut_down_range_label")
        self.da_cutblut_down_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblut_down_range_label, 53, 0, 1, 1)

        self.da_cutnoise_number_iter_label = QLabel(self.da_frame)
        self.da_cutnoise_number_iter_label.setObjectName(u"da_cutnoise_number_iter_label")
        self.da_cutnoise_number_iter_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_number_iter_label, 59, 0, 1, 1)

        self.da_gaussian_sigma_label = QLabel(self.da_frame)
        self.da_gaussian_sigma_label.setObjectName(u"da_gaussian_sigma_label")
        self.da_gaussian_sigma_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_sigma_label, 25, 0, 1, 1)

        self.da_cutblur_size_range_input = QLineEdit(self.da_frame)
        self.da_cutblur_size_range_input.setObjectName(u"da_cutblur_size_range_input")
        self.da_cutblur_size_range_input.setMinimumSize(QSize(200, 30))
        self.da_cutblur_size_range_input.setMaximumSize(QSize(200, 30))
        self.da_cutblur_size_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutblur_size_range_input, 52, 1, 1, 1)

        self.da_gaussian_noise_var_input = QLineEdit(self.da_frame)
        self.da_gaussian_noise_var_input.setObjectName(u"da_gaussian_noise_var_input")
        self.da_gaussian_noise_var_input.setMinimumSize(QSize(200, 30))
        self.da_gaussian_noise_var_input.setMaximumSize(QSize(200, 30))
        self.da_gaussian_noise_var_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_var_input, 75, 1, 1, 1)

        self.da_rot90_input = QComboBox(self.da_frame)
        self.da_rot90_input.addItem("")
        self.da_rot90_input.addItem("")
        self.da_rot90_input.setObjectName(u"da_rot90_input")
        self.da_rot90_input.setMinimumSize(QSize(200, 30))
        self.da_rot90_input.setMaximumSize(QSize(200, 30))
        self.da_rot90_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_rot90_input, 7, 1, 1, 1)

        self.label_110 = QLabel(self.da_frame)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font)

        self.gridLayout_25.addWidget(self.label_110, 55, 0, 1, 1)

        self.da_affine_mode_input = QComboBox(self.da_frame)
        self.da_affine_mode_input.addItem("")
        self.da_affine_mode_input.addItem("")
        self.da_affine_mode_input.addItem("")
        self.da_affine_mode_input.addItem("")
        self.da_affine_mode_input.addItem("")
        self.da_affine_mode_input.setObjectName(u"da_affine_mode_input")
        self.da_affine_mode_input.setMinimumSize(QSize(200, 30))
        self.da_affine_mode_input.setMaximumSize(QSize(200, 30))
        self.da_affine_mode_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_affine_mode_input, 16, 1, 1, 1)

        self.da_grid_d_range_label = QLabel(self.da_frame)
        self.da_grid_d_range_label.setObjectName(u"da_grid_d_range_label")
        self.da_grid_d_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_d_range_label, 70, 0, 1, 1)

        self.label_87 = QLabel(self.da_frame)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font)

        self.gridLayout_25.addWidget(self.label_87, 24, 0, 1, 1)

        self.da_missing_sections_iteration_range_label = QLabel(self.da_frame)
        self.da_missing_sections_iteration_range_label.setObjectName(u"da_missing_sections_iteration_range_label")
        self.da_missing_sections_iteration_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_missing_sections_iteration_range_label, 65, 0, 1, 1)

        self.label_65 = QLabel(self.da_frame)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font)

        self.gridLayout_25.addWidget(self.label_65, 8, 0, 1, 1)

        self.da_misaligment_rotate_ratio_label = QLabel(self.da_frame)
        self.da_misaligment_rotate_ratio_label.setObjectName(u"da_misaligment_rotate_ratio_label")
        self.da_misaligment_rotate_ratio_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_misaligment_rotate_ratio_label, 63, 0, 1, 1)

        self.label_144 = QLabel(self.da_frame)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font)

        self.gridLayout_25.addWidget(self.label_144, 80, 0, 1, 1)

        self.da_motion_blur_k_size_label = QLabel(self.da_frame)
        self.da_motion_blur_k_size_label.setObjectName(u"da_motion_blur_k_size_label")
        self.da_motion_blur_k_size_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_motion_blur_k_size_label, 29, 0, 1, 1)

        self.label_61 = QLabel(self.da_frame)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font)

        self.gridLayout_25.addWidget(self.label_61, 3, 0, 1, 1)

        self.da_salt_pepper_prop_label = QLabel(self.da_frame)
        self.da_salt_pepper_prop_label.setObjectName(u"da_salt_pepper_prop_label")
        self.da_salt_pepper_prop_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_pepper_prop_label, 84, 0, 1, 1)

        self.da_grid_ratio_input = QLineEdit(self.da_frame)
        self.da_grid_ratio_input.setObjectName(u"da_grid_ratio_input")
        self.da_grid_ratio_input.setMinimumSize(QSize(200, 30))
        self.da_grid_ratio_input.setMaximumSize(QSize(200, 30))
        self.da_grid_ratio_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_ratio_input, 69, 1, 1, 1)

        self.da_salt_pepper_amount_label = QLabel(self.da_frame)
        self.da_salt_pepper_amount_label.setObjectName(u"da_salt_pepper_amount_label")
        self.da_salt_pepper_amount_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_salt_pepper_amount_label, 83, 0, 1, 1)

        self.da_brightness_em_input = QComboBox(self.da_frame)
        self.da_brightness_em_input.addItem("")
        self.da_brightness_em_input.addItem("")
        self.da_brightness_em_input.setObjectName(u"da_brightness_em_input")
        self.da_brightness_em_input.setMinimumSize(QSize(200, 30))
        self.da_brightness_em_input.setMaximumSize(QSize(200, 30))
        self.da_brightness_em_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_em_input, 38, 1, 1, 1)

        self.da_grid_rotate_input = QLineEdit(self.da_frame)
        self.da_grid_rotate_input.setObjectName(u"da_grid_rotate_input")
        self.da_grid_rotate_input.setMinimumSize(QSize(200, 30))
        self.da_grid_rotate_input.setMaximumSize(QSize(200, 30))
        self.da_grid_rotate_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_grid_rotate_input, 71, 1, 1, 1)

        self.label_90 = QLabel(self.da_frame)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font)

        self.gridLayout_25.addWidget(self.label_90, 35, 0, 1, 1)

        self.da_channel_shuffle_input = QComboBox(self.da_frame)
        self.da_channel_shuffle_input.addItem("")
        self.da_channel_shuffle_input.addItem("")
        self.da_channel_shuffle_input.setObjectName(u"da_channel_shuffle_input")
        self.da_channel_shuffle_input.setMinimumSize(QSize(200, 30))
        self.da_channel_shuffle_input.setMaximumSize(QSize(200, 30))
        self.da_channel_shuffle_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_channel_shuffle_input, 67, 1, 1, 1)

        self.label_74 = QLabel(self.da_frame)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font)

        self.gridLayout_25.addWidget(self.label_74, 10, 0, 1, 1)

        self.da_cutmix_size_range_label = QLabel(self.da_frame)
        self.da_cutmix_size_range_label.setObjectName(u"da_cutmix_size_range_label")
        self.da_cutmix_size_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutmix_size_range_label, 56, 0, 1, 1)

        self.da_cutnoise_scale_range_label = QLabel(self.da_frame)
        self.da_cutnoise_scale_range_label.setObjectName(u"da_cutnoise_scale_range_label")
        self.da_cutnoise_scale_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutnoise_scale_range_label, 58, 0, 1, 1)

        self.da_pepper_input = QComboBox(self.da_frame)
        self.da_pepper_input.addItem("")
        self.da_pepper_input.addItem("")
        self.da_pepper_input.setObjectName(u"da_pepper_input")
        self.da_pepper_input.setMinimumSize(QSize(200, 30))
        self.da_pepper_input.setMaximumSize(QSize(200, 30))
        self.da_pepper_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_pepper_input, 80, 1, 1, 1)

        self.da_brightness_factor_range_label = QLabel(self.da_frame)
        self.da_brightness_factor_range_label.setObjectName(u"da_brightness_factor_range_label")
        self.da_brightness_factor_range_label.setMaximumSize(QSize(190, 16777215))
        self.da_brightness_factor_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_factor_range_label, 33, 0, 1, 1)

        self.da_shift_range_label = QLabel(self.da_frame)
        self.da_shift_range_label.setObjectName(u"da_shift_range_label")
        self.da_shift_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_shift_range_label, 15, 0, 1, 1)

        self.label_67 = QLabel(self.da_frame)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font)

        self.gridLayout_25.addWidget(self.label_67, 7, 0, 1, 1)

        self.da_elastic_alpha_label = QLabel(self.da_frame)
        self.da_elastic_alpha_label.setObjectName(u"da_elastic_alpha_label")
        self.da_elastic_alpha_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_alpha_label, 21, 0, 1, 1)

        self.da_random_rot_range_label = QLabel(self.da_frame)
        self.da_random_rot_range_label.setObjectName(u"da_random_rot_range_label")
        self.da_random_rot_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_random_rot_range_label, 9, 0, 1, 1)

        self.da_cutmix_size_range_input = QLineEdit(self.da_frame)
        self.da_cutmix_size_range_input.setObjectName(u"da_cutmix_size_range_input")
        self.da_cutmix_size_range_input.setMinimumSize(QSize(200, 30))
        self.da_cutmix_size_range_input.setMaximumSize(QSize(200, 30))
        self.da_cutmix_size_range_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutmix_size_range_input, 56, 1, 1, 1)

        self.da_elastic_input = QComboBox(self.da_frame)
        self.da_elastic_input.addItem("")
        self.da_elastic_input.addItem("")
        self.da_elastic_input.setObjectName(u"da_elastic_input")
        self.da_elastic_input.setMinimumSize(QSize(200, 30))
        self.da_elastic_input.setMaximumSize(QSize(200, 30))
        self.da_elastic_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_input, 20, 1, 1, 1)

        self.da_median_blur_k_size_input = QLineEdit(self.da_frame)
        self.da_median_blur_k_size_input.setObjectName(u"da_median_blur_k_size_input")
        self.da_median_blur_k_size_input.setMinimumSize(QSize(200, 30))
        self.da_median_blur_k_size_input.setMaximumSize(QSize(200, 30))
        self.da_median_blur_k_size_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_median_blur_k_size_input, 27, 1, 1, 1)

        self.da_brightness_em_mode_input = QComboBox(self.da_frame)
        self.da_brightness_em_mode_input.addItem("")
        self.da_brightness_em_mode_input.addItem("")
        self.da_brightness_em_mode_input.setObjectName(u"da_brightness_em_mode_input")
        self.da_brightness_em_mode_input.setMinimumSize(QSize(200, 30))
        self.da_brightness_em_mode_input.setMaximumSize(QSize(200, 30))
        self.da_brightness_em_mode_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_em_mode_input, 40, 1, 1, 1)

        self.da_contrast_mode_input = QComboBox(self.da_frame)
        self.da_contrast_mode_input.addItem("")
        self.da_contrast_mode_input.addItem("")
        self.da_contrast_mode_input.setObjectName(u"da_contrast_mode_input")
        self.da_contrast_mode_input.setMinimumSize(QSize(200, 30))
        self.da_contrast_mode_input.setMaximumSize(QSize(200, 30))
        self.da_contrast_mode_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_contrast_mode_input, 37, 1, 1, 1)

        self.da_gamma_contrast_range_label = QLabel(self.da_frame)
        self.da_gamma_contrast_range_label.setObjectName(u"da_gamma_contrast_range_label")
        self.da_gamma_contrast_range_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_gamma_contrast_range_label, 31, 0, 1, 1)

        self.da_brightness_em_mode_label = QLabel(self.da_frame)
        self.da_brightness_em_mode_label.setObjectName(u"da_brightness_em_mode_label")
        self.da_brightness_em_mode_label.setFont(font)

        self.gridLayout_25.addWidget(self.da_brightness_em_mode_label, 40, 0, 1, 1)

        self.label_122 = QLabel(self.da_frame)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font)

        self.gridLayout_25.addWidget(self.label_122, 67, 0, 1, 1)

        self.da_gaussian_noise_mean_input = QLineEdit(self.da_frame)
        self.da_gaussian_noise_mean_input.setObjectName(u"da_gaussian_noise_mean_input")
        self.da_gaussian_noise_mean_input.setMinimumSize(QSize(200, 30))
        self.da_gaussian_noise_mean_input.setMaximumSize(QSize(200, 30))
        self.da_gaussian_noise_mean_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_noise_mean_input, 74, 1, 1, 1)

        self.da_cutout_number_iterations_input = QLineEdit(self.da_frame)
        self.da_cutout_number_iterations_input.setObjectName(u"da_cutout_number_iterations_input")
        self.da_cutout_number_iterations_input.setMinimumSize(QSize(200, 30))
        self.da_cutout_number_iterations_input.setMaximumSize(QSize(200, 30))
        self.da_cutout_number_iterations_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_cutout_number_iterations_input, 47, 1, 1, 1)

        self.label_66 = QLabel(self.da_frame)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font)

        self.gridLayout_25.addWidget(self.label_66, 5, 0, 1, 1)

        self.da_elastic_alpha_input = QLineEdit(self.da_frame)
        self.da_elastic_alpha_input.setObjectName(u"da_elastic_alpha_input")
        self.da_elastic_alpha_input.setMinimumSize(QSize(200, 30))
        self.da_elastic_alpha_input.setMaximumSize(QSize(200, 30))
        self.da_elastic_alpha_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_elastic_alpha_input, 21, 1, 1, 1)

        self.da_shift_input = QComboBox(self.da_frame)
        self.da_shift_input.addItem("")
        self.da_shift_input.addItem("")
        self.da_shift_input.setObjectName(u"da_shift_input")
        self.da_shift_input.setMinimumSize(QSize(200, 30))
        self.da_shift_input.setMaximumSize(QSize(200, 30))
        self.da_shift_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_shift_input, 14, 1, 1, 1)

        self.label_119 = QLabel(self.da_frame)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font)

        self.gridLayout_25.addWidget(self.label_119, 61, 0, 1, 1)

        self.label_141 = QLabel(self.da_frame)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font)

        self.gridLayout_25.addWidget(self.label_141, 82, 0, 1, 1)

        self.da_gaussian_blur_input = QComboBox(self.da_frame)
        self.da_gaussian_blur_input.addItem("")
        self.da_gaussian_blur_input.addItem("")
        self.da_gaussian_blur_input.setObjectName(u"da_gaussian_blur_input")
        self.da_gaussian_blur_input.setMinimumSize(QSize(200, 30))
        self.da_gaussian_blur_input.setMaximumSize(QSize(200, 30))
        self.da_gaussian_blur_input.setFont(font)

        self.gridLayout_25.addWidget(self.da_gaussian_blur_input, 24, 1, 1, 1)

        self.label_128 = QLabel(self.da_frame)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font)

        self.gridLayout_25.addWidget(self.label_128, 78, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_16, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.da_frame, 15, 0, 1, 1)

        self.unet_model_like_frame = QFrame(self.train_advanced_options_frame_2)
        self.unet_model_like_frame.setObjectName(u"unet_model_like_frame")
        self.unet_model_like_frame.setMinimumSize(QSize(0, 0))
        self.unet_model_like_frame.setFont(font)
        self.unet_model_like_frame.setStyleSheet(u"background: rgb(246,246,246);")
        self.unet_model_like_frame.setFrameShape(QFrame.Box)
        self.unet_model_like_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.unet_model_like_frame)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.kernel_size_input = QLineEdit(self.unet_model_like_frame)
        self.kernel_size_input.setObjectName(u"kernel_size_input")
        self.kernel_size_input.setMinimumSize(QSize(100, 30))
        self.kernel_size_input.setMaximumSize(QSize(200, 30))
        self.kernel_size_input.setFont(font)

        self.gridLayout_22.addWidget(self.kernel_size_input, 5, 1, 1, 1)

        self.label_36 = QLabel(self.unet_model_like_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 16777215))
        self.label_36.setFont(font)

        self.gridLayout_22.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_38 = QLabel(self.unet_model_like_frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 16777215))
        self.label_38.setFont(font)

        self.gridLayout_22.addWidget(self.label_38, 2, 0, 1, 1)

        self.label_39 = QLabel(self.unet_model_like_frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 16777215))
        self.label_39.setFont(font)

        self.gridLayout_22.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_37 = QLabel(self.unet_model_like_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 16777215))
        self.label_37.setFont(font)

        self.gridLayout_22.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_41 = QLabel(self.unet_model_like_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 16777215))
        self.label_41.setFont(font)

        self.gridLayout_22.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_40 = QLabel(self.unet_model_like_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 16777215))
        self.label_40.setFont(font)

        self.gridLayout_22.addWidget(self.label_40, 4, 0, 1, 1)

        self.label_43 = QLabel(self.unet_model_like_frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 16777215))
        self.label_43.setFont(font)

        self.gridLayout_22.addWidget(self.label_43, 6, 0, 1, 1)

        self.label_45 = QLabel(self.unet_model_like_frame)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 16777215))
        self.label_45.setFont(font)

        self.gridLayout_22.addWidget(self.label_45, 8, 0, 1, 1)

        self.label_46 = QLabel(self.unet_model_like_frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 16777215))
        self.label_46.setFont(font)

        self.gridLayout_22.addWidget(self.label_46, 9, 0, 1, 1)

        self.label_47 = QLabel(self.unet_model_like_frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 16777215))
        self.label_47.setFont(font)

        self.gridLayout_22.addWidget(self.label_47, 7, 0, 1, 1)

        self.dropout_input = QLineEdit(self.unet_model_like_frame)
        self.dropout_input.setObjectName(u"dropout_input")
        self.dropout_input.setMinimumSize(QSize(200, 30))
        self.dropout_input.setMaximumSize(QSize(200, 30))
        self.dropout_input.setFont(font)

        self.gridLayout_22.addWidget(self.dropout_input, 1, 1, 1, 1)

        self.feature_maps_input = QLineEdit(self.unet_model_like_frame)
        self.feature_maps_input.setObjectName(u"feature_maps_input")
        self.feature_maps_input.setMinimumSize(QSize(200, 30))
        self.feature_maps_input.setMaximumSize(QSize(200, 30))
        self.feature_maps_input.setFont(font)

        self.gridLayout_22.addWidget(self.feature_maps_input, 0, 1, 1, 1)

        self.z_down_input = QLineEdit(self.unet_model_like_frame)
        self.z_down_input.setObjectName(u"z_down_input")
        self.z_down_input.setMinimumSize(QSize(200, 30))
        self.z_down_input.setMaximumSize(QSize(200, 30))
        self.z_down_input.setFont(font)

        self.gridLayout_22.addWidget(self.z_down_input, 9, 1, 1, 1)

        self.batch_normalization_input = QComboBox(self.unet_model_like_frame)
        self.batch_normalization_input.addItem("")
        self.batch_normalization_input.addItem("")
        self.batch_normalization_input.setObjectName(u"batch_normalization_input")
        self.batch_normalization_input.setMinimumSize(QSize(100, 30))
        self.batch_normalization_input.setMaximumSize(QSize(200, 30))
        self.batch_normalization_input.setFont(font)

        self.gridLayout_22.addWidget(self.batch_normalization_input, 3, 1, 1, 1)

        self.kernel_init_input = QComboBox(self.unet_model_like_frame)
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.addItem("")
        self.kernel_init_input.setObjectName(u"kernel_init_input")
        self.kernel_init_input.setMinimumSize(QSize(200, 30))
        self.kernel_init_input.setMaximumSize(QSize(200, 30))
        self.kernel_init_input.setFont(font)

        self.gridLayout_22.addWidget(self.kernel_init_input, 4, 1, 1, 1)

        self.spatial_dropout_input = QComboBox(self.unet_model_like_frame)
        self.spatial_dropout_input.addItem("")
        self.spatial_dropout_input.addItem("")
        self.spatial_dropout_input.setObjectName(u"spatial_dropout_input")
        self.spatial_dropout_input.setMinimumSize(QSize(100, 30))
        self.spatial_dropout_input.setMaximumSize(QSize(200, 30))
        self.spatial_dropout_input.setFont(font)

        self.gridLayout_22.addWidget(self.spatial_dropout_input, 2, 1, 1, 1)

        self.upsample_layer_input = QComboBox(self.unet_model_like_frame)
        self.upsample_layer_input.addItem("")
        self.upsample_layer_input.addItem("")
        self.upsample_layer_input.setObjectName(u"upsample_layer_input")
        self.upsample_layer_input.setMinimumSize(QSize(200, 30))
        self.upsample_layer_input.setMaximumSize(QSize(200, 30))
        self.upsample_layer_input.setFont(font)

        self.gridLayout_22.addWidget(self.upsample_layer_input, 6, 1, 1, 1)

        self.activation_input = QComboBox(self.unet_model_like_frame)
        self.activation_input.addItem("")
        self.activation_input.addItem("")
        self.activation_input.addItem("")
        self.activation_input.setObjectName(u"activation_input")
        self.activation_input.setMinimumSize(QSize(200, 30))
        self.activation_input.setMaximumSize(QSize(200, 30))
        self.activation_input.setFont(font)

        self.gridLayout_22.addWidget(self.activation_input, 7, 1, 1, 1)

        self.last_activation_input = QComboBox(self.unet_model_like_frame)
        self.last_activation_input.addItem("")
        self.last_activation_input.addItem("")
        self.last_activation_input.addItem("")
        self.last_activation_input.addItem("")
        self.last_activation_input.setObjectName(u"last_activation_input")
        self.last_activation_input.setMinimumSize(QSize(200, 30))
        self.last_activation_input.setMaximumSize(QSize(200, 30))
        self.last_activation_input.setFont(font)

        self.gridLayout_22.addWidget(self.last_activation_input, 8, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.unet_model_like_frame, 7, 0, 1, 1)

        self.frame_14 = QFrame(self.train_advanced_options_frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFont(font)
        self.frame_14.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_14)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.custom_mean_input = QLineEdit(self.frame_14)
        self.custom_mean_input.setObjectName(u"custom_mean_input")
        self.custom_mean_input.setMinimumSize(QSize(200, 30))
        self.custom_mean_input.setMaximumSize(QSize(200, 30))
        self.custom_mean_input.setFont(font)

        self.gridLayout_15.addWidget(self.custom_mean_input, 8, 3, 1, 1)

        self.normalization_type_input = QComboBox(self.frame_14)
        self.normalization_type_input.addItem("")
        self.normalization_type_input.addItem("")
        self.normalization_type_input.setObjectName(u"normalization_type_input")
        self.normalization_type_input.setMinimumSize(QSize(200, 30))
        self.normalization_type_input.setMaximumSize(QSize(200, 30))
        self.normalization_type_input.setFont(font)

        self.gridLayout_15.addWidget(self.normalization_type_input, 5, 3, 2, 1)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setFont(font)

        self.gridLayout_15.addWidget(self.label_12, 5, 1, 2, 2)

        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setFont(font)

        self.gridLayout_15.addWidget(self.label_7, 1, 1, 1, 2)

        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setFont(font)

        self.gridLayout_15.addWidget(self.label_6, 0, 1, 1, 1)

        self.extract_random_patch_input = QComboBox(self.frame_14)
        self.extract_random_patch_input.addItem("")
        self.extract_random_patch_input.addItem("")
        self.extract_random_patch_input.setObjectName(u"extract_random_patch_input")
        self.extract_random_patch_input.setMinimumSize(QSize(200, 30))
        self.extract_random_patch_input.setMaximumSize(QSize(200, 30))
        self.extract_random_patch_input.setFont(font)

        self.gridLayout_15.addWidget(self.extract_random_patch_input, 1, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.patch_size_input = QLineEdit(self.frame_14)
        self.patch_size_input.setObjectName(u"patch_size_input")
        self.patch_size_input.setMinimumSize(QSize(200, 30))
        self.patch_size_input.setMaximumSize(QSize(200, 30))
        self.patch_size_input.setFont(font)

        self.gridLayout_15.addWidget(self.patch_size_input, 0, 3, 1, 1)

        self.custom_mean_label = QLabel(self.frame_14)
        self.custom_mean_label.setObjectName(u"custom_mean_label")
        self.custom_mean_label.setMaximumSize(QSize(16777215, 16777215))
        self.custom_mean_label.setFont(font)

        self.gridLayout_15.addWidget(self.custom_mean_label, 8, 1, 1, 1)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_15.addWidget(self.label_11, 2, 1, 1, 2)

        self.reflect_to_complete_shape_input = QComboBox(self.frame_14)
        self.reflect_to_complete_shape_input.addItem("")
        self.reflect_to_complete_shape_input.addItem("")
        self.reflect_to_complete_shape_input.setObjectName(u"reflect_to_complete_shape_input")
        self.reflect_to_complete_shape_input.setMinimumSize(QSize(200, 30))
        self.reflect_to_complete_shape_input.setMaximumSize(QSize(200, 30))
        self.reflect_to_complete_shape_input.setFont(font)

        self.gridLayout_15.addWidget(self.reflect_to_complete_shape_input, 2, 3, 1, 1)

        self.custom_std_label = QLabel(self.frame_14)
        self.custom_std_label.setObjectName(u"custom_std_label")
        self.custom_std_label.setMaximumSize(QSize(16777215, 16777215))
        self.custom_std_label.setFont(font)

        self.gridLayout_15.addWidget(self.custom_std_label, 9, 1, 1, 1)

        self.check_gen_label = QLabel(self.frame_14)
        self.check_gen_label.setObjectName(u"check_gen_label")
        self.check_gen_label.setMaximumSize(QSize(16777215, 16777215))
        self.check_gen_label.setFont(font)

        self.gridLayout_15.addWidget(self.check_gen_label, 10, 1, 1, 1)

        self.check_gen_input = QComboBox(self.frame_14)
        self.check_gen_input.addItem("")
        self.check_gen_input.addItem("")
        self.check_gen_input.setObjectName(u"check_gen_input")
        self.check_gen_input.setMinimumSize(QSize(200, 30))
        self.check_gen_input.setMaximumSize(QSize(200, 30))
        self.check_gen_input.setFont(font)

        self.gridLayout_15.addWidget(self.check_gen_input, 10, 3, 1, 1)

        self.custom_std_input = QLineEdit(self.frame_14)
        self.custom_std_input.setObjectName(u"custom_std_input")
        self.custom_std_input.setMinimumSize(QSize(200, 30))
        self.custom_std_input.setMaximumSize(QSize(200, 30))
        self.custom_std_input.setFont(font)

        self.gridLayout_15.addWidget(self.custom_std_input, 9, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_14, 1, 0, 1, 1)

        self.label_31 = QLabel(self.train_advanced_options_frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(150, 16777215))
        self.label_31.setFont(font)

        self.gridLayout_4.addWidget(self.label_31, 4, 0, 1, 1)

        self.frame_28 = QFrame(self.train_advanced_options_frame_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_28)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.lr_schel_reduce_on_plat_patience_label = QLabel(self.frame_28)
        self.lr_schel_reduce_on_plat_patience_label.setObjectName(u"lr_schel_reduce_on_plat_patience_label")
        self.lr_schel_reduce_on_plat_patience_label.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_reduce_on_plat_patience_label, 11, 0, 1, 1)

        self.lr_schel_warmupcosine_lr_label = QLabel(self.frame_28)
        self.lr_schel_warmupcosine_lr_label.setObjectName(u"lr_schel_warmupcosine_lr_label")
        self.lr_schel_warmupcosine_lr_label.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_warmupcosine_lr_label, 14, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_14, 19, 0, 1, 1)

        self.lr_schel_reduce_on_plat_factor_label = QLabel(self.frame_28)
        self.lr_schel_reduce_on_plat_factor_label.setObjectName(u"lr_schel_reduce_on_plat_factor_label")
        self.lr_schel_reduce_on_plat_factor_label.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_reduce_on_plat_factor_label, 12, 0, 1, 1)

        self.label_149 = QLabel(self.frame_28)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font)

        self.gridLayout_29.addWidget(self.label_149, 2, 0, 1, 1)

        self.lr_schel_input = QComboBox(self.frame_28)
        self.lr_schel_input.addItem("")
        self.lr_schel_input.addItem("")
        self.lr_schel_input.addItem("")
        self.lr_schel_input.addItem("")
        self.lr_schel_input.setObjectName(u"lr_schel_input")
        self.lr_schel_input.setMinimumSize(QSize(200, 0))
        self.lr_schel_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_input, 7, 1, 1, 1)

        self.lr_schel_min_lr_input = QLineEdit(self.frame_28)
        self.lr_schel_min_lr_input.setObjectName(u"lr_schel_min_lr_input")
        self.lr_schel_min_lr_input.setMinimumSize(QSize(200, 30))
        self.lr_schel_min_lr_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_min_lr_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_min_lr_input, 9, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_21, 2, 2, 1, 1)

        self.lr_schel_warmupcosine_epochs_input = QLineEdit(self.frame_28)
        self.lr_schel_warmupcosine_epochs_input.setObjectName(u"lr_schel_warmupcosine_epochs_input")
        self.lr_schel_warmupcosine_epochs_input.setMinimumSize(QSize(200, 30))
        self.lr_schel_warmupcosine_epochs_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_warmupcosine_epochs_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_warmupcosine_epochs_input, 15, 1, 1, 1)

        self.profiler_batch_range_input = QLineEdit(self.frame_28)
        self.profiler_batch_range_input.setObjectName(u"profiler_batch_range_input")
        self.profiler_batch_range_input.setMinimumSize(QSize(200, 0))
        self.profiler_batch_range_input.setMaximumSize(QSize(200, 30))
        self.profiler_batch_range_input.setFont(font)

        self.gridLayout_29.addWidget(self.profiler_batch_range_input, 6, 1, 1, 1)

        self.lr_schel_min_lr_label = QLabel(self.frame_28)
        self.lr_schel_min_lr_label.setObjectName(u"lr_schel_min_lr_label")
        self.lr_schel_min_lr_label.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_min_lr_label, 9, 0, 1, 1)

        self.learning_rate_input = QLineEdit(self.frame_28)
        self.learning_rate_input.setObjectName(u"learning_rate_input")
        self.learning_rate_input.setMinimumSize(QSize(200, 0))
        self.learning_rate_input.setMaximumSize(QSize(200, 30))
        self.learning_rate_input.setFont(font)

        self.gridLayout_29.addWidget(self.learning_rate_input, 1, 1, 1, 1)

        self.label_159 = QLabel(self.frame_28)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setFont(font)

        self.gridLayout_29.addWidget(self.label_159, 4, 0, 1, 1)

        self.batch_size_input = QLineEdit(self.frame_28)
        self.batch_size_input.setObjectName(u"batch_size_input")
        self.batch_size_input.setMinimumSize(QSize(200, 0))
        self.batch_size_input.setMaximumSize(QSize(200, 30))
        self.batch_size_input.setFont(font)

        self.gridLayout_29.addWidget(self.batch_size_input, 2, 1, 1, 1)

        self.label_150 = QLabel(self.frame_28)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font)

        self.gridLayout_29.addWidget(self.label_150, 3, 0, 1, 1)

        self.label_162 = QLabel(self.frame_28)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setFont(font)

        self.gridLayout_29.addWidget(self.label_162, 7, 0, 1, 1)

        self.label_143 = QLabel(self.frame_28)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font)

        self.gridLayout_29.addWidget(self.label_143, 0, 0, 1, 1)

        self.label_151 = QLabel(self.frame_28)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font)

        self.gridLayout_29.addWidget(self.label_151, 1, 0, 1, 1)

        self.lr_schel_warmupcosine_epochs_label = QLabel(self.frame_28)
        self.lr_schel_warmupcosine_epochs_label.setObjectName(u"lr_schel_warmupcosine_epochs_label")
        self.lr_schel_warmupcosine_epochs_label.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_warmupcosine_epochs_label, 15, 0, 1, 1)

        self.label_160 = QLabel(self.frame_28)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setFont(font)

        self.gridLayout_29.addWidget(self.label_160, 5, 0, 1, 1)

        self.lr_schel_warmupcosine_hold_epochs_label = QLabel(self.frame_28)
        self.lr_schel_warmupcosine_hold_epochs_label.setObjectName(u"lr_schel_warmupcosine_hold_epochs_label")
        self.lr_schel_warmupcosine_hold_epochs_label.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_warmupcosine_hold_epochs_label, 18, 0, 1, 1)

        self.profiler_input = QComboBox(self.frame_28)
        self.profiler_input.addItem("")
        self.profiler_input.addItem("")
        self.profiler_input.setObjectName(u"profiler_input")
        self.profiler_input.setMinimumSize(QSize(200, 0))
        self.profiler_input.setMaximumSize(QSize(200, 30))
        self.profiler_input.setFont(font)

        self.gridLayout_29.addWidget(self.profiler_input, 5, 1, 1, 1)

        self.profiler_batch_range_label = QLabel(self.frame_28)
        self.profiler_batch_range_label.setObjectName(u"profiler_batch_range_label")
        self.profiler_batch_range_label.setFont(font)

        self.gridLayout_29.addWidget(self.profiler_batch_range_label, 6, 0, 1, 1)

        self.checkpoint_monitor_input = QComboBox(self.frame_28)
        self.checkpoint_monitor_input.addItem("")
        self.checkpoint_monitor_input.addItem("")
        self.checkpoint_monitor_input.setObjectName(u"checkpoint_monitor_input")
        self.checkpoint_monitor_input.setMinimumSize(QSize(200, 0))
        self.checkpoint_monitor_input.setMaximumSize(QSize(200, 30))
        self.checkpoint_monitor_input.setFont(font)

        self.gridLayout_29.addWidget(self.checkpoint_monitor_input, 4, 1, 1, 1)

        self.lr_schel_warmupcosine_lr_input = QLineEdit(self.frame_28)
        self.lr_schel_warmupcosine_lr_input.setObjectName(u"lr_schel_warmupcosine_lr_input")
        self.lr_schel_warmupcosine_lr_input.setMinimumSize(QSize(200, 30))
        self.lr_schel_warmupcosine_lr_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_warmupcosine_lr_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_warmupcosine_lr_input, 14, 1, 1, 1)

        self.optimizer_input = QComboBox(self.frame_28)
        self.optimizer_input.addItem("")
        self.optimizer_input.addItem("")
        self.optimizer_input.setObjectName(u"optimizer_input")
        self.optimizer_input.setMinimumSize(QSize(200, 0))
        self.optimizer_input.setMaximumSize(QSize(200, 30))
        self.optimizer_input.setFont(font)

        self.gridLayout_29.addWidget(self.optimizer_input, 0, 1, 1, 1)

        self.early_stopping_input = QComboBox(self.frame_28)
        self.early_stopping_input.addItem("")
        self.early_stopping_input.addItem("")
        self.early_stopping_input.setObjectName(u"early_stopping_input")
        self.early_stopping_input.setMinimumSize(QSize(200, 0))
        self.early_stopping_input.setMaximumSize(QSize(200, 30))
        self.early_stopping_input.setFont(font)

        self.gridLayout_29.addWidget(self.early_stopping_input, 3, 1, 1, 1)

        self.lr_schel_reduce_on_plat_factor_input = QLineEdit(self.frame_28)
        self.lr_schel_reduce_on_plat_factor_input.setObjectName(u"lr_schel_reduce_on_plat_factor_input")
        self.lr_schel_reduce_on_plat_factor_input.setMinimumSize(QSize(200, 30))
        self.lr_schel_reduce_on_plat_factor_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_reduce_on_plat_factor_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_reduce_on_plat_factor_input, 12, 1, 1, 1)

        self.lr_schel_warmupcosine_hold_epochs_input = QLineEdit(self.frame_28)
        self.lr_schel_warmupcosine_hold_epochs_input.setObjectName(u"lr_schel_warmupcosine_hold_epochs_input")
        self.lr_schel_warmupcosine_hold_epochs_input.setMinimumSize(QSize(200, 30))
        self.lr_schel_warmupcosine_hold_epochs_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_warmupcosine_hold_epochs_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_warmupcosine_hold_epochs_input, 18, 1, 1, 1)

        self.lr_schel_reduce_on_plat_patience_input = QLineEdit(self.frame_28)
        self.lr_schel_reduce_on_plat_patience_input.setObjectName(u"lr_schel_reduce_on_plat_patience_input")
        self.lr_schel_reduce_on_plat_patience_input.setMinimumSize(QSize(200, 30))
        self.lr_schel_reduce_on_plat_patience_input.setMaximumSize(QSize(200, 30))
        self.lr_schel_reduce_on_plat_patience_input.setFont(font)

        self.gridLayout_29.addWidget(self.lr_schel_reduce_on_plat_patience_input, 11, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_28, 13, 0, 1, 1)

        self.frame_16 = QFrame(self.train_advanced_options_frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setFont(font)
        self.frame_16.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_16)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 16777215))
        self.label_22.setFont(font)

        self.gridLayout_20.addWidget(self.label_22, 2, 0, 1, 1)

        self.train_resolution_label = QLabel(self.frame_16)
        self.train_resolution_label.setObjectName(u"train_resolution_label")
        self.train_resolution_label.setMaximumSize(QSize(16777215, 16777215))
        self.train_resolution_label.setFont(font)

        self.gridLayout_20.addWidget(self.train_resolution_label, 1, 0, 1, 1)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_20.addWidget(self.label_21, 0, 0, 1, 2)

        self.train_padding_input = QLineEdit(self.frame_16)
        self.train_padding_input.setObjectName(u"train_padding_input")
        self.train_padding_input.setMinimumSize(QSize(200, 0))
        self.train_padding_input.setMaximumSize(QSize(200, 30))
        self.train_padding_input.setFont(font)

        self.gridLayout_20.addWidget(self.train_padding_input, 3, 2, 1, 1)

        self.replicate_data_input = QLineEdit(self.frame_16)
        self.replicate_data_input.setObjectName(u"replicate_data_input")
        self.replicate_data_input.setMinimumSize(QSize(200, 0))
        self.replicate_data_input.setMaximumSize(QSize(200, 30))
        self.replicate_data_input.setFont(font)

        self.gridLayout_20.addWidget(self.replicate_data_input, 0, 2, 1, 1)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 16777215))
        self.label_23.setFont(font)

        self.gridLayout_20.addWidget(self.label_23, 3, 0, 1, 1)

        self.train_overlap_input = QLineEdit(self.frame_16)
        self.train_overlap_input.setObjectName(u"train_overlap_input")
        self.train_overlap_input.setMinimumSize(QSize(200, 0))
        self.train_overlap_input.setMaximumSize(QSize(200, 30))
        self.train_overlap_input.setFont(font)

        self.gridLayout_20.addWidget(self.train_overlap_input, 2, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_11, 0, 4, 1, 1)

        self.train_resolution_input = QLineEdit(self.frame_16)
        self.train_resolution_input.setObjectName(u"train_resolution_input")
        self.train_resolution_input.setMinimumSize(QSize(200, 0))
        self.train_resolution_input.setMaximumSize(QSize(200, 30))
        self.train_resolution_input.setFont(font)

        self.gridLayout_20.addWidget(self.train_resolution_input, 1, 2, 1, 2)

        self.train_median_padding_label = QLabel(self.frame_16)
        self.train_median_padding_label.setObjectName(u"train_median_padding_label")
        self.train_median_padding_label.setFont(font)

        self.gridLayout_20.addWidget(self.train_median_padding_label, 5, 0, 1, 1)

        self.train_median_padding_input = QComboBox(self.frame_16)
        self.train_median_padding_input.addItem("")
        self.train_median_padding_input.addItem("")
        self.train_median_padding_input.setObjectName(u"train_median_padding_input")
        self.train_median_padding_input.setMinimumSize(QSize(200, 30))
        self.train_median_padding_input.setMaximumSize(QSize(200, 30))
        self.train_median_padding_input.setFont(font)

        self.gridLayout_20.addWidget(self.train_median_padding_input, 5, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame_16, 3, 0, 1, 1)

        self.unet_model_like_label = QLabel(self.train_advanced_options_frame_2)
        self.unet_model_like_label.setObjectName(u"unet_model_like_label")
        self.unet_model_like_label.setFont(font)

        self.gridLayout_4.addWidget(self.unet_model_like_label, 6, 0, 1, 1)

        self.frame_19 = QFrame(self.train_advanced_options_frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 0))
        self.frame_19.setFont(font)
        self.frame_19.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_19)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.validation_overlap_input = QLineEdit(self.frame_19)
        self.validation_overlap_input.setObjectName(u"validation_overlap_input")
        self.validation_overlap_input.setMinimumSize(QSize(200, 30))
        self.validation_overlap_input.setMaximumSize(QSize(200, 30))
        self.validation_overlap_input.setFont(font)

        self.gridLayout_21.addWidget(self.validation_overlap_input, 1, 1, 1, 1)

        self.validation_padding_label = QLabel(self.frame_19)
        self.validation_padding_label.setObjectName(u"validation_padding_label")
        self.validation_padding_label.setMaximumSize(QSize(16777215, 16777215))
        self.validation_padding_label.setFont(font)

        self.gridLayout_21.addWidget(self.validation_padding_label, 2, 0, 1, 1)

        self.validation_overlap_label = QLabel(self.frame_19)
        self.validation_overlap_label.setObjectName(u"validation_overlap_label")
        self.validation_overlap_label.setMaximumSize(QSize(16777215, 16777215))
        self.validation_overlap_label.setFont(font)

        self.gridLayout_21.addWidget(self.validation_overlap_label, 1, 0, 1, 1)

        self.validation_padding_input = QLineEdit(self.frame_19)
        self.validation_padding_input.setObjectName(u"validation_padding_input")
        self.validation_padding_input.setMinimumSize(QSize(200, 30))
        self.validation_padding_input.setMaximumSize(QSize(200, 30))
        self.validation_padding_input.setFont(font)

        self.gridLayout_21.addWidget(self.validation_padding_input, 2, 1, 1, 1)

        self.random_val_label = QLabel(self.frame_19)
        self.random_val_label.setObjectName(u"random_val_label")
        self.random_val_label.setMaximumSize(QSize(16777215, 16777215))
        self.random_val_label.setFont(font)

        self.gridLayout_21.addWidget(self.random_val_label, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.random_val_input = QComboBox(self.frame_19)
        self.random_val_input.addItem("")
        self.random_val_input.addItem("")
        self.random_val_input.setObjectName(u"random_val_input")
        self.random_val_input.setMinimumSize(QSize(200, 30))
        self.random_val_input.setMaximumSize(QSize(200, 30))
        self.random_val_input.setFont(font)

        self.gridLayout_21.addWidget(self.random_val_input, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_19)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.gridLayout_21.addWidget(self.label_33, 3, 0, 1, 1)

        self.validation_resolution_input = QLineEdit(self.frame_19)
        self.validation_resolution_input.setObjectName(u"validation_resolution_input")
        self.validation_resolution_input.setMinimumSize(QSize(200, 30))
        self.validation_resolution_input.setMaximumSize(QSize(200, 30))
        self.validation_resolution_input.setFont(font)

        self.gridLayout_21.addWidget(self.validation_resolution_input, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_19, 5, 0, 1, 1)

        self.unetr_label = QLabel(self.train_advanced_options_frame_2)
        self.unetr_label.setObjectName(u"unetr_label")
        self.unetr_label.setMaximumSize(QSize(16777215, 16777215))
        self.unetr_label.setFont(font)

        self.gridLayout_4.addWidget(self.unetr_label, 10, 0, 1, 1)

        self.tiramisu_frame = QFrame(self.train_advanced_options_frame_2)
        self.tiramisu_frame.setObjectName(u"tiramisu_frame")
        self.tiramisu_frame.setMinimumSize(QSize(0, 0))
        self.tiramisu_frame.setFont(font)
        self.tiramisu_frame.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.tiramisu_frame.setFrameShape(QFrame.Box)
        self.tiramisu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.tiramisu_frame)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.tiramisu_depth_input = QLineEdit(self.tiramisu_frame)
        self.tiramisu_depth_input.setObjectName(u"tiramisu_depth_input")
        self.tiramisu_depth_input.setMinimumSize(QSize(200, 30))
        self.tiramisu_depth_input.setMaximumSize(QSize(200, 30))
        self.tiramisu_depth_input.setFont(font)

        self.gridLayout_24.addWidget(self.tiramisu_depth_input, 0, 1, 1, 1)

        self.label_140 = QLabel(self.tiramisu_frame)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMaximumSize(QSize(16777215, 16777215))
        self.label_140.setFont(font)

        self.gridLayout_24.addWidget(self.label_140, 1, 0, 1, 1)

        self.tiramisu_feature_maps_input = QLineEdit(self.tiramisu_frame)
        self.tiramisu_feature_maps_input.setObjectName(u"tiramisu_feature_maps_input")
        self.tiramisu_feature_maps_input.setMinimumSize(QSize(200, 30))
        self.tiramisu_feature_maps_input.setMaximumSize(QSize(200, 30))
        self.tiramisu_feature_maps_input.setFont(font)

        self.gridLayout_24.addWidget(self.tiramisu_feature_maps_input, 1, 1, 1, 1)

        self.label_56 = QLabel(self.tiramisu_frame)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(16777215, 16777215))
        self.label_56.setFont(font)

        self.gridLayout_24.addWidget(self.label_56, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_15, 0, 2, 1, 1)

        self.label_142 = QLabel(self.tiramisu_frame)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMaximumSize(QSize(16777215, 16777215))
        self.label_142.setFont(font)

        self.gridLayout_24.addWidget(self.label_142, 2, 0, 1, 1)

        self.tiramisu_dropout_input = QLineEdit(self.tiramisu_frame)
        self.tiramisu_dropout_input.setObjectName(u"tiramisu_dropout_input")
        self.tiramisu_dropout_input.setMinimumSize(QSize(200, 30))
        self.tiramisu_dropout_input.setMaximumSize(QSize(200, 30))
        self.tiramisu_dropout_input.setFont(font)

        self.gridLayout_24.addWidget(self.tiramisu_dropout_input, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.tiramisu_frame, 9, 0, 1, 1)

        self.unetr_frame = QFrame(self.train_advanced_options_frame_2)
        self.unetr_frame.setObjectName(u"unetr_frame")
        self.unetr_frame.setMinimumSize(QSize(0, 0))
        self.unetr_frame.setFont(font)
        self.unetr_frame.setStyleSheet(u"background: rgb(246,246,246);")
        self.unetr_frame.setFrameShape(QFrame.Box)
        self.unetr_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.unetr_frame)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.unetr_vit_hidden_multiple_input = QLineEdit(self.unetr_frame)
        self.unetr_vit_hidden_multiple_input.setObjectName(u"unetr_vit_hidden_multiple_input")
        self.unetr_vit_hidden_multiple_input.setMinimumSize(QSize(200, 30))
        self.unetr_vit_hidden_multiple_input.setMaximumSize(QSize(200, 30))
        self.unetr_vit_hidden_multiple_input.setFont(font)

        self.gridLayout_23.addWidget(self.unetr_vit_hidden_multiple_input, 5, 1, 1, 1)

        self.unetr_num_heads_input = QLineEdit(self.unetr_frame)
        self.unetr_num_heads_input.setObjectName(u"unetr_num_heads_input")
        self.unetr_num_heads_input.setMinimumSize(QSize(200, 30))
        self.unetr_num_heads_input.setMaximumSize(QSize(200, 30))
        self.unetr_num_heads_input.setFont(font)

        self.gridLayout_23.addWidget(self.unetr_num_heads_input, 4, 1, 1, 1)

        self.unetr_mlp_hidden_units_input = QLineEdit(self.unetr_frame)
        self.unetr_mlp_hidden_units_input.setObjectName(u"unetr_mlp_hidden_units_input")
        self.unetr_mlp_hidden_units_input.setMinimumSize(QSize(200, 30))
        self.unetr_mlp_hidden_units_input.setMaximumSize(QSize(200, 30))
        self.unetr_mlp_hidden_units_input.setFont(font)

        self.gridLayout_23.addWidget(self.unetr_mlp_hidden_units_input, 3, 1, 1, 1)

        self.label_52 = QLabel(self.unetr_frame)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 16777215))
        self.label_52.setFont(font)

        self.gridLayout_23.addWidget(self.label_52, 4, 0, 1, 1)

        self.label_53 = QLabel(self.unetr_frame)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(16777215, 16777215))
        self.label_53.setFont(font)

        self.gridLayout_23.addWidget(self.label_53, 2, 0, 1, 1)

        self.label_50 = QLabel(self.unetr_frame)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 16777215))
        self.label_50.setFont(font)

        self.gridLayout_23.addWidget(self.label_50, 0, 0, 1, 1)

        self.label_54 = QLabel(self.unetr_frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 16777215))
        self.label_54.setFont(font)

        self.gridLayout_23.addWidget(self.label_54, 5, 0, 1, 1)

        self.label_51 = QLabel(self.unetr_frame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 16777215))
        self.label_51.setFont(font)

        self.gridLayout_23.addWidget(self.label_51, 1, 0, 1, 1)

        self.unetr_token_size_input = QLineEdit(self.unetr_frame)
        self.unetr_token_size_input.setObjectName(u"unetr_token_size_input")
        self.unetr_token_size_input.setMinimumSize(QSize(200, 30))
        self.unetr_token_size_input.setMaximumSize(QSize(200, 30))
        self.unetr_token_size_input.setFont(font)

        self.gridLayout_23.addWidget(self.unetr_token_size_input, 0, 1, 1, 1)

        self.label_55 = QLabel(self.unetr_frame)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(16777215, 16777215))
        self.label_55.setFont(font)

        self.gridLayout_23.addWidget(self.label_55, 3, 0, 1, 1)

        self.unetr_embed_dims_input = QLineEdit(self.unetr_frame)
        self.unetr_embed_dims_input.setObjectName(u"unetr_embed_dims_input")
        self.unetr_embed_dims_input.setMinimumSize(QSize(200, 30))
        self.unetr_embed_dims_input.setMaximumSize(QSize(200, 30))
        self.unetr_embed_dims_input.setFont(font)

        self.gridLayout_23.addWidget(self.unetr_embed_dims_input, 1, 1, 1, 1)

        self.unetr_depth_input = QLineEdit(self.unetr_frame)
        self.unetr_depth_input.setObjectName(u"unetr_depth_input")
        self.unetr_depth_input.setMinimumSize(QSize(200, 30))
        self.unetr_depth_input.setMaximumSize(QSize(200, 30))
        self.unetr_depth_input.setFont(font)

        self.gridLayout_23.addWidget(self.unetr_depth_input, 2, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_14, 3, 2, 1, 1)


        self.gridLayout_4.addWidget(self.unetr_frame, 11, 0, 1, 1)

        self.label_10 = QLabel(self.train_advanced_options_frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(200, 35))
        self.label_10.setFont(font)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_30 = QLabel(self.train_advanced_options_frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(100, 16777215))
        self.label_30.setFont(font)

        self.gridLayout_4.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_42 = QLabel(self.train_advanced_options_frame_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)

        self.gridLayout_4.addWidget(self.label_42, 12, 0, 1, 1)

        self.tiramisu_label = QLabel(self.train_advanced_options_frame_2)
        self.tiramisu_label.setObjectName(u"tiramisu_label")
        self.tiramisu_label.setMaximumSize(QSize(16777215, 16777215))
        self.tiramisu_label.setFont(font)

        self.gridLayout_4.addWidget(self.tiramisu_label, 8, 0, 1, 1)


        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.train_advanced_options_frame_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_5)


        self.gridLayout_3.addWidget(self.train_advanced_options_frame, 11, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 12, 9, 1, 1)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 30))
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.train_advanced_label = QLabel(self.frame_13)
        self.train_advanced_label.setObjectName(u"train_advanced_label")
        self.train_advanced_label.setMaximumSize(QSize(150, 35))
        self.train_advanced_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.train_advanced_label)

        self.train_advanced_bn = QPushButton(self.frame_13)
        self.train_advanced_bn.setObjectName(u"train_advanced_bn")
        self.train_advanced_bn.setMaximumSize(QSize(35, 35))
        self.train_advanced_bn.setFont(font)
        self.train_advanced_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.train_advanced_bn.setIcon(icon10)

        self.horizontalLayout_10.addWidget(self.train_advanced_bn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.gridLayout_3.addWidget(self.frame_13, 10, 0, 1, 1)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.number_of_epochs_input = QLineEdit(self.frame_12)
        self.number_of_epochs_input.setObjectName(u"number_of_epochs_input")
        self.number_of_epochs_input.setMinimumSize(QSize(200, 30))
        self.number_of_epochs_input.setMaximumSize(QSize(200, 30))
        self.number_of_epochs_input.setFont(font)

        self.gridLayout_13.addWidget(self.number_of_epochs_input, 1, 2, 1, 1)

        self.number_of_classes_input = QLineEdit(self.frame_12)
        self.number_of_classes_input.setObjectName(u"number_of_classes_input")
        self.number_of_classes_input.setMinimumSize(QSize(200, 30))
        self.number_of_classes_input.setMaximumSize(QSize(200, 30))
        self.number_of_classes_input.setFont(font)

        self.gridLayout_13.addWidget(self.number_of_classes_input, 5, 2, 1, 1)

        self.label_34 = QLabel(self.frame_12)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 16777215))
        self.label_34.setFont(font)

        self.gridLayout_13.addWidget(self.label_34, 4, 0, 1, 1)

        self.label_44 = QLabel(self.frame_12)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(16777215, 16777215))
        self.label_44.setFont(font)

        self.gridLayout_13.addWidget(self.label_44, 5, 0, 1, 1)

        self.patience_label = QLabel(self.frame_12)
        self.patience_label.setObjectName(u"patience_label")
        self.patience_label.setFont(font)

        self.gridLayout_13.addWidget(self.patience_label, 2, 0, 1, 1)

        self.number_of_epochs_label = QLabel(self.frame_12)
        self.number_of_epochs_label.setObjectName(u"number_of_epochs_label")
        self.number_of_epochs_label.setFont(font)

        self.gridLayout_13.addWidget(self.number_of_epochs_label, 1, 0, 1, 1)

        self.patience_input = QLineEdit(self.frame_12)
        self.patience_input.setObjectName(u"patience_input")
        self.patience_input.setMinimumSize(QSize(200, 30))
        self.patience_input.setMaximumSize(QSize(200, 30))
        self.patience_input.setFont(font)

        self.gridLayout_13.addWidget(self.patience_input, 2, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 4, 3, 1, 1)

        self.model_input = QComboBox(self.frame_12)
        self.model_input.setObjectName(u"model_input")
        self.model_input.setMinimumSize(QSize(200, 30))
        self.model_input.setMaximumSize(QSize(16777215, 30))
        self.model_input.setFont(font)

        self.gridLayout_13.addWidget(self.model_input, 4, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_12, 6, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.train_data_input = QTextBrowser(self.frame_3)
        self.train_data_input.setObjectName(u"train_data_input")
        self.train_data_input.setMinimumSize(QSize(500, 30))
        self.train_data_input.setMaximumSize(QSize(500, 30))
        self.train_data_input.setFont(font)
        self.train_data_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_data_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_data_input.setLineWrapMode(QTextEdit.NoWrap)
        self.train_data_input.setReadOnly(False)

        self.gridLayout_6.addWidget(self.train_data_input, 0, 2, 1, 1)

        self.train_in_memory_comboBox = QComboBox(self.frame_3)
        self.train_in_memory_comboBox.addItem("")
        self.train_in_memory_comboBox.addItem("")
        self.train_in_memory_comboBox.setObjectName(u"train_in_memory_comboBox")
        self.train_in_memory_comboBox.setMinimumSize(QSize(200, 30))
        self.train_in_memory_comboBox.setMaximumSize(QSize(200, 30))
        self.train_in_memory_comboBox.setFont(font)

        self.gridLayout_6.addWidget(self.train_in_memory_comboBox, 4, 2, 1, 1)

        self.train_data_in_memory = QLabel(self.frame_3)
        self.train_data_in_memory.setObjectName(u"train_data_in_memory")
        self.train_data_in_memory.setMaximumSize(QSize(16777215, 16777215))
        self.train_data_in_memory.setFont(font)

        self.gridLayout_6.addWidget(self.train_data_in_memory, 4, 1, 1, 1)

        self.train_data_input_browse_bn = QPushButton(self.frame_3)
        self.train_data_input_browse_bn.setObjectName(u"train_data_input_browse_bn")
        self.train_data_input_browse_bn.setFont(font)

        self.gridLayout_6.addWidget(self.train_data_input_browse_bn, 0, 3, 1, 1)

        self.train_data_label = QLabel(self.frame_3)
        self.train_data_label.setObjectName(u"train_data_label")
        self.train_data_label.setMaximumSize(QSize(200, 35))
        self.train_data_label.setFont(font)

        self.gridLayout_6.addWidget(self.train_data_label, 0, 1, 1, 1)

        self.train_gt_label = QLabel(self.frame_3)
        self.train_gt_label.setObjectName(u"train_gt_label")
        self.train_gt_label.setMaximumSize(QSize(200, 35))
        self.train_gt_label.setFont(font)

        self.gridLayout_6.addWidget(self.train_gt_label, 1, 1, 1, 1)

        self.train_data_gt_input = QTextBrowser(self.frame_3)
        self.train_data_gt_input.setObjectName(u"train_data_gt_input")
        self.train_data_gt_input.setMinimumSize(QSize(500, 30))
        self.train_data_gt_input.setMaximumSize(QSize(500, 30))
        self.train_data_gt_input.setFont(font)
        self.train_data_gt_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_data_gt_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_data_gt_input.setLineWrapMode(QTextEdit.NoWrap)
        self.train_data_gt_input.setReadOnly(False)

        self.gridLayout_6.addWidget(self.train_data_gt_input, 1, 2, 1, 1)

        self.train_data_gt_input_browse_bn = QPushButton(self.frame_3)
        self.train_data_gt_input_browse_bn.setObjectName(u"train_data_gt_input_browse_bn")
        self.train_data_gt_input_browse_bn.setMaximumSize(QSize(130, 16777215))
        self.train_data_gt_input_browse_bn.setFont(font)

        self.gridLayout_6.addWidget(self.train_data_gt_input_browse_bn, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFont(font)
        self.frame_11.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.cross_validation_nfolds_input = QLineEdit(self.frame_11)
        self.cross_validation_nfolds_input.setObjectName(u"cross_validation_nfolds_input")
        self.cross_validation_nfolds_input.setMinimumSize(QSize(200, 30))
        self.cross_validation_nfolds_input.setMaximumSize(QSize(200, 30))
        self.cross_validation_nfolds_input.setFont(font)

        self.gridLayout_11.addWidget(self.cross_validation_nfolds_input, 1, 2, 1, 1)

        self.cross_validation_fold_input = QLineEdit(self.frame_11)
        self.cross_validation_fold_input.setObjectName(u"cross_validation_fold_input")
        self.cross_validation_fold_input.setMinimumSize(QSize(200, 30))
        self.cross_validation_fold_input.setMaximumSize(QSize(200, 30))
        self.cross_validation_fold_input.setFont(font)

        self.gridLayout_11.addWidget(self.cross_validation_fold_input, 2, 2, 1, 1)

        self.validation_data_label = QLabel(self.frame_11)
        self.validation_data_label.setObjectName(u"validation_data_label")
        self.validation_data_label.setFont(font)

        self.gridLayout_11.addWidget(self.validation_data_label, 3, 0, 1, 1)

        self.validation_type_comboBox = QComboBox(self.frame_11)
        self.validation_type_comboBox.addItem("")
        self.validation_type_comboBox.addItem("")
        self.validation_type_comboBox.addItem("")
        self.validation_type_comboBox.setObjectName(u"validation_type_comboBox")
        self.validation_type_comboBox.setMinimumSize(QSize(300, 30))
        self.validation_type_comboBox.setMaximumSize(QSize(16777215, 30))
        self.validation_type_comboBox.setFont(font)

        self.gridLayout_11.addWidget(self.validation_type_comboBox, 0, 2, 1, 1)

        self.cross_validation_nfolds_label = QLabel(self.frame_11)
        self.cross_validation_nfolds_label.setObjectName(u"cross_validation_nfolds_label")
        self.cross_validation_nfolds_label.setFont(font)

        self.gridLayout_11.addWidget(self.cross_validation_nfolds_label, 1, 0, 1, 1)

        self.validation_type_label = QLabel(self.frame_11)
        self.validation_type_label.setObjectName(u"validation_type_label")
        self.validation_type_label.setFont(font)

        self.gridLayout_11.addWidget(self.validation_type_label, 0, 0, 1, 1)

        self.val_data_input_browse_bn = QPushButton(self.frame_11)
        self.val_data_input_browse_bn.setObjectName(u"val_data_input_browse_bn")
        self.val_data_input_browse_bn.setMaximumSize(QSize(130, 16777215))
        self.val_data_input_browse_bn.setFont(font)

        self.gridLayout_11.addWidget(self.val_data_input_browse_bn, 3, 3, 1, 1)

        self.val_in_memory_comboBox = QComboBox(self.frame_11)
        self.val_in_memory_comboBox.addItem("")
        self.val_in_memory_comboBox.addItem("")
        self.val_in_memory_comboBox.setObjectName(u"val_in_memory_comboBox")
        self.val_in_memory_comboBox.setMinimumSize(QSize(200, 30))
        self.val_in_memory_comboBox.setMaximumSize(QSize(200, 30))
        self.val_in_memory_comboBox.setFont(font)

        self.gridLayout_11.addWidget(self.val_in_memory_comboBox, 7, 2, 1, 1)

        self.percentage_validation_input = QLineEdit(self.frame_11)
        self.percentage_validation_input.setObjectName(u"percentage_validation_input")
        self.percentage_validation_input.setMinimumSize(QSize(200, 30))
        self.percentage_validation_input.setMaximumSize(QSize(200, 30))
        self.percentage_validation_input.setFont(font)

        self.gridLayout_11.addWidget(self.percentage_validation_input, 9, 2, 1, 1)

        self.val_in_memory_label = QLabel(self.frame_11)
        self.val_in_memory_label.setObjectName(u"val_in_memory_label")
        self.val_in_memory_label.setFont(font)

        self.gridLayout_11.addWidget(self.val_in_memory_label, 7, 0, 1, 1)

        self.validation_data_gt_input = QTextBrowser(self.frame_11)
        self.validation_data_gt_input.setObjectName(u"validation_data_gt_input")
        self.validation_data_gt_input.setMinimumSize(QSize(500, 30))
        self.validation_data_gt_input.setMaximumSize(QSize(500, 30))
        self.validation_data_gt_input.setFont(font)
        self.validation_data_gt_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.validation_data_gt_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.validation_data_gt_input.setLineWrapMode(QTextEdit.NoWrap)
        self.validation_data_gt_input.setReadOnly(False)

        self.gridLayout_11.addWidget(self.validation_data_gt_input, 4, 2, 1, 1)

        self.percentage_validation_label = QLabel(self.frame_11)
        self.percentage_validation_label.setObjectName(u"percentage_validation_label")
        self.percentage_validation_label.setFont(font)

        self.gridLayout_11.addWidget(self.percentage_validation_label, 9, 0, 1, 1)

        self.validation_data_gt_label = QLabel(self.frame_11)
        self.validation_data_gt_label.setObjectName(u"validation_data_gt_label")
        self.validation_data_gt_label.setFont(font)

        self.gridLayout_11.addWidget(self.validation_data_gt_label, 4, 0, 1, 1)

        self.validation_data_input = QTextBrowser(self.frame_11)
        self.validation_data_input.setObjectName(u"validation_data_input")
        self.validation_data_input.setMinimumSize(QSize(500, 30))
        self.validation_data_input.setMaximumSize(QSize(500, 30))
        self.validation_data_input.setFont(font)
        self.validation_data_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.validation_data_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.validation_data_input.setLineWrapMode(QTextEdit.NoWrap)
        self.validation_data_input.setReadOnly(False)

        self.gridLayout_11.addWidget(self.validation_data_input, 3, 2, 1, 1)

        self.cross_validation_fold_label = QLabel(self.frame_11)
        self.cross_validation_fold_label.setObjectName(u"cross_validation_fold_label")
        self.cross_validation_fold_label.setFont(font)

        self.gridLayout_11.addWidget(self.cross_validation_fold_label, 2, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_15, 10, 0, 1, 1)

        self.val_data_gt_input_browse_bn = QPushButton(self.frame_11)
        self.val_data_gt_input_browse_bn.setObjectName(u"val_data_gt_input_browse_bn")
        self.val_data_gt_input_browse_bn.setMaximumSize(QSize(130, 16777215))
        self.val_data_gt_input_browse_bn.setFont(font)

        self.gridLayout_11.addWidget(self.val_data_gt_input_browse_bn, 4, 3, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_54, 0, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_11, 4, 0, 1, 2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 3)

        self.train_label = QLabel(self.scrollAreaWidgetContents_3)
        self.train_label.setObjectName(u"train_label")
        self.train_label.setMaximumSize(QSize(150, 16777215))
        self.train_label.setFont(font)

        self.gridLayout_3.addWidget(self.train_label, 0, 0, 1, 2)

        self.train_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_12.addWidget(self.train_scrollArea, 0, 1, 1, 1)

        self.train_tab_widget.addTab(self.train_general_options_tab, "")
        self.train_workflow_specific_tab = QWidget()
        self.train_workflow_specific_tab.setObjectName(u"train_workflow_specific_tab")
        self.train_workflow_specific_tab.setMaximumSize(QSize(16777215, 356))
        self.gridLayout_16 = QGridLayout(self.train_workflow_specific_tab)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.train_workflow_specific_tab)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFont(font)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.train_workflow_specific_tab_stackedWidget = QStackedWidget(self.frame_15)
        self.train_workflow_specific_tab_stackedWidget.setObjectName(u"train_workflow_specific_tab_stackedWidget")
        self.train_workflow_specific_tab_stackedWidget.setFont(font)
        self.train_workflow_specific_tab_semantic_seg_page = QWidget()
        self.train_workflow_specific_tab_semantic_seg_page.setObjectName(u"train_workflow_specific_tab_semantic_seg_page")
        self.verticalLayout_10 = QVBoxLayout(self.train_workflow_specific_tab_semantic_seg_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.train_workflow_specific_tab_semantic_seg_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 925, 342))
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_8, 6, 0, 1, 1)

        self.extract_random_patch_frame_label = QLabel(self.scrollAreaWidgetContents_6)
        self.extract_random_patch_frame_label.setObjectName(u"extract_random_patch_frame_label")
        self.extract_random_patch_frame_label.setMinimumSize(QSize(0, 30))
        self.extract_random_patch_frame_label.setMaximumSize(QSize(16777215, 30))
        self.extract_random_patch_frame_label.setFont(font)

        self.gridLayout_18.addWidget(self.extract_random_patch_frame_label, 1, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_18.addWidget(self.label_14, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(619, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.extract_random_patch_frame = QFrame(self.scrollAreaWidgetContents_6)
        self.extract_random_patch_frame.setObjectName(u"extract_random_patch_frame")
        self.extract_random_patch_frame.setMinimumSize(QSize(0, 0))
        self.extract_random_patch_frame.setStyleSheet(u"background: rgb(246,246,246);")
        self.extract_random_patch_frame.setFrameShape(QFrame.Box)
        self.extract_random_patch_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.extract_random_patch_frame)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.sem_seg_random_patch_prob_map_input = QComboBox(self.extract_random_patch_frame)
        self.sem_seg_random_patch_prob_map_input.addItem("")
        self.sem_seg_random_patch_prob_map_input.addItem("")
        self.sem_seg_random_patch_prob_map_input.setObjectName(u"sem_seg_random_patch_prob_map_input")
        self.sem_seg_random_patch_prob_map_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_random_patch_prob_map_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_random_patch_prob_map_input.setFont(font)

        self.gridLayout_30.addWidget(self.sem_seg_random_patch_prob_map_input, 0, 1, 1, 1)

        self.label_17 = QLabel(self.extract_random_patch_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(200, 16777215))
        self.label_17.setFont(font)

        self.gridLayout_30.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_18 = QLabel(self.extract_random_patch_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        self.label_18.setFont(font)

        self.gridLayout_30.addWidget(self.label_18, 1, 0, 1, 1)

        self.sem_seg_random_patch_fore_weights_input = QLineEdit(self.extract_random_patch_frame)
        self.sem_seg_random_patch_fore_weights_input.setObjectName(u"sem_seg_random_patch_fore_weights_input")
        self.sem_seg_random_patch_fore_weights_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_random_patch_fore_weights_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_random_patch_fore_weights_input.setFont(font)

        self.gridLayout_30.addWidget(self.sem_seg_random_patch_fore_weights_input, 1, 1, 1, 1)

        self.sem_seg_random_patch_back_weights_input = QLineEdit(self.extract_random_patch_frame)
        self.sem_seg_random_patch_back_weights_input.setObjectName(u"sem_seg_random_patch_back_weights_input")
        self.sem_seg_random_patch_back_weights_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_random_patch_back_weights_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_random_patch_back_weights_input.setFont(font)

        self.gridLayout_30.addWidget(self.sem_seg_random_patch_back_weights_input, 4, 1, 1, 1)

        self.label_19 = QLabel(self.extract_random_patch_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setFont(font)

        self.gridLayout_30.addWidget(self.label_19, 4, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_23, 0, 2, 1, 1)


        self.gridLayout_18.addWidget(self.extract_random_patch_frame, 2, 0, 1, 1)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_30.setFrameShape(QFrame.Box)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_30)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.sem_seg_check_train_data_input = QComboBox(self.frame_30)
        self.sem_seg_check_train_data_input.addItem("")
        self.sem_seg_check_train_data_input.addItem("")
        self.sem_seg_check_train_data_input.setObjectName(u"sem_seg_check_train_data_input")
        self.sem_seg_check_train_data_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_check_train_data_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_check_train_data_input.setFont(font)

        self.gridLayout_31.addWidget(self.sem_seg_check_train_data_input, 1, 1, 1, 1)

        self.sem_seg_minimum_fore_percentage_input = QLineEdit(self.frame_30)
        self.sem_seg_minimum_fore_percentage_input.setObjectName(u"sem_seg_minimum_fore_percentage_input")
        self.sem_seg_minimum_fore_percentage_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_minimum_fore_percentage_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_minimum_fore_percentage_input.setFont(font)

        self.gridLayout_31.addWidget(self.sem_seg_minimum_fore_percentage_input, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_30)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 16777215))
        self.label_28.setFont(font)

        self.gridLayout_31.addWidget(self.label_28, 2, 0, 1, 1)

        self.label_20 = QLabel(self.frame_30)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 16777215))
        self.label_20.setFont(font)

        self.gridLayout_31.addWidget(self.label_20, 1, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_25, 1, 2, 1, 1)


        self.gridLayout_18.addWidget(self.frame_30, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_semantic_seg_page)
        self.train_workflow_specific_tab_instance_seg_page = QWidget()
        self.train_workflow_specific_tab_instance_seg_page.setObjectName(u"train_workflow_specific_tab_instance_seg_page")
        self.train_workflow_specific_tab_instance_seg_page.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_22 = QVBoxLayout(self.train_workflow_specific_tab_instance_seg_page)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.train_workflow_specific_tab_instance_seg_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 915, 340))
        self.gridLayout_17 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_9, 4, 0, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font)

        self.gridLayout_17.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.gridLayout_17.addWidget(self.label_27, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.frame_31 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 0))
        self.frame_31.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_31.setFrameShape(QFrame.Box)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_31)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.inst_seg_minimum_fore_percentage_input = QLineEdit(self.frame_31)
        self.inst_seg_minimum_fore_percentage_input.setObjectName(u"inst_seg_minimum_fore_percentage_input")
        self.inst_seg_minimum_fore_percentage_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_minimum_fore_percentage_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_minimum_fore_percentage_input.setFont(font)

        self.gridLayout_33.addWidget(self.inst_seg_minimum_fore_percentage_input, 0, 1, 1, 1)

        self.label_26 = QLabel(self.frame_31)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 16777215))
        self.label_26.setFont(font)

        self.gridLayout_33.addWidget(self.label_26, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_33.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.frame_31, 1, 0, 1, 1)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 50))
        self.frame_32.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_32.setFrameShape(QFrame.Box)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_32)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_69 = QLabel(self.frame_32)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font)

        self.gridLayout_32.addWidget(self.label_69, 0, 0, 1, 1)

        self.inst_seg_data_channels_input = QComboBox(self.frame_32)
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.addItem("")
        self.inst_seg_data_channels_input.setObjectName(u"inst_seg_data_channels_input")
        self.inst_seg_data_channels_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_data_channels_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_data_channels_input.setFont(font)

        self.gridLayout_32.addWidget(self.inst_seg_data_channels_input, 0, 1, 1, 1)

        self.inst_seg_channel_weigths_input = QLineEdit(self.frame_32)
        self.inst_seg_channel_weigths_input.setObjectName(u"inst_seg_channel_weigths_input")
        self.inst_seg_channel_weigths_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_channel_weigths_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_channel_weigths_input.setFont(font)

        self.gridLayout_32.addWidget(self.inst_seg_channel_weigths_input, 1, 1, 1, 1)

        self.label_70 = QLabel(self.frame_32)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font)

        self.gridLayout_32.addWidget(self.label_70, 1, 0, 1, 1)

        self.label_75 = QLabel(self.frame_32)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font)

        self.gridLayout_32.addWidget(self.label_75, 2, 0, 1, 1)

        self.inst_seg_contour_mode_combobox = QComboBox(self.frame_32)
        self.inst_seg_contour_mode_combobox.addItem("")
        self.inst_seg_contour_mode_combobox.addItem("")
        self.inst_seg_contour_mode_combobox.addItem("")
        self.inst_seg_contour_mode_combobox.addItem("")
        self.inst_seg_contour_mode_combobox.setObjectName(u"inst_seg_contour_mode_combobox")
        self.inst_seg_contour_mode_combobox.setMinimumSize(QSize(200, 30))
        self.inst_seg_contour_mode_combobox.setMaximumSize(QSize(200, 30))
        self.inst_seg_contour_mode_combobox.setFont(font)

        self.gridLayout_32.addWidget(self.inst_seg_contour_mode_combobox, 2, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_22, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.frame_32, 3, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_22.addWidget(self.scrollArea_2)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_instance_seg_page)
        self.train_workflow_specific_tab_detection_page = QWidget()
        self.train_workflow_specific_tab_detection_page.setObjectName(u"train_workflow_specific_tab_detection_page")
        self.verticalLayout_23 = QVBoxLayout(self.train_workflow_specific_tab_detection_page)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.train_workflow_specific_tab_detection_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFont(font)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 913, 338))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_48 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_19.addWidget(self.label_48, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_10, 6, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_24, 4, 1, 1, 1)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_34.setFrameShape(QFrame.Box)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_34)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.det_check_created_point_input = QComboBox(self.frame_34)
        self.det_check_created_point_input.addItem("")
        self.det_check_created_point_input.addItem("")
        self.det_check_created_point_input.setObjectName(u"det_check_created_point_input")
        self.det_check_created_point_input.setMinimumSize(QSize(200, 30))
        self.det_check_created_point_input.setMaximumSize(QSize(200, 30))
        self.det_check_created_point_input.setFont(font)

        self.gridLayout_35.addWidget(self.det_check_created_point_input, 1, 1, 1, 1)

        self.det_central_point_dilation_input = QLineEdit(self.frame_34)
        self.det_central_point_dilation_input.setObjectName(u"det_central_point_dilation_input")
        self.det_central_point_dilation_input.setMinimumSize(QSize(200, 30))
        self.det_central_point_dilation_input.setMaximumSize(QSize(200, 30))
        self.det_central_point_dilation_input.setFont(font)

        self.gridLayout_35.addWidget(self.det_central_point_dilation_input, 0, 1, 1, 1)

        self.label_76 = QLabel(self.frame_34)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(16777215, 16777215))
        self.label_76.setFont(font)

        self.gridLayout_35.addWidget(self.label_76, 0, 0, 1, 1)

        self.label_79 = QLabel(self.frame_34)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(16777215, 16777215))
        self.label_79.setFont(font)

        self.gridLayout_35.addWidget(self.label_79, 1, 0, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_32, 0, 2, 1, 1)


        self.gridLayout_19.addWidget(self.frame_34, 5, 0, 1, 1)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 50))
        self.frame_33.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_33.setFrameShape(QFrame.Box)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_33)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_29 = QLabel(self.frame_33)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(300, 16777215))
        self.label_29.setFont(font)

        self.gridLayout_34.addWidget(self.label_29, 0, 0, 1, 1)

        self.det_minimum_fore_percentage_input = QLineEdit(self.frame_33)
        self.det_minimum_fore_percentage_input.setObjectName(u"det_minimum_fore_percentage_input")
        self.det_minimum_fore_percentage_input.setMinimumSize(QSize(200, 30))
        self.det_minimum_fore_percentage_input.setMaximumSize(QSize(200, 30))
        self.det_minimum_fore_percentage_input.setFont(font)

        self.gridLayout_34.addWidget(self.det_minimum_fore_percentage_input, 0, 1, 1, 1)

        self.label_35 = QLabel(self.frame_33)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.gridLayout_34.addWidget(self.label_35, 1, 0, 1, 1)

        self.det_loss_type_input = QComboBox(self.frame_33)
        self.det_loss_type_input.addItem("")
        self.det_loss_type_input.addItem("")
        self.det_loss_type_input.addItem("")
        self.det_loss_type_input.setObjectName(u"det_loss_type_input")
        self.det_loss_type_input.setMinimumSize(QSize(200, 30))
        self.det_loss_type_input.setMaximumSize(QSize(200, 30))
        self.det_loss_type_input.setFont(font)

        self.gridLayout_34.addWidget(self.det_loss_type_input, 1, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_31, 1, 2, 1, 1)


        self.gridLayout_19.addWidget(self.frame_33, 1, 0, 1, 1)

        self.label_80 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMaximumSize(QSize(16777215, 16777215))
        self.label_80.setFont(font)

        self.gridLayout_19.addWidget(self.label_80, 4, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_23.addWidget(self.scrollArea_3)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_detection_page)
        self.train_workflow_specific_tab_denoising_page = QWidget()
        self.train_workflow_specific_tab_denoising_page.setObjectName(u"train_workflow_specific_tab_denoising_page")
        self.verticalLayout_24 = QVBoxLayout(self.train_workflow_specific_tab_denoising_page)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.train_workflow_specific_tab_denoising_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFont(font)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 913, 338))
        self.gridLayout_49 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.frame_44 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_44.setFrameShape(QFrame.Box)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_44)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.deno_n2v_perc_pix_label = QLabel(self.frame_44)
        self.deno_n2v_perc_pix_label.setObjectName(u"deno_n2v_perc_pix_label")
        self.deno_n2v_perc_pix_label.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_perc_pix_label, 0, 0, 1, 1)

        self.deno_n2v_manipulator_label = QLabel(self.frame_44)
        self.deno_n2v_manipulator_label.setObjectName(u"deno_n2v_manipulator_label")
        self.deno_n2v_manipulator_label.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_manipulator_label, 1, 0, 1, 1)

        self.deno_n2v_neighborhood_radius_label = QLabel(self.frame_44)
        self.deno_n2v_neighborhood_radius_label.setObjectName(u"deno_n2v_neighborhood_radius_label")
        self.deno_n2v_neighborhood_radius_label.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_neighborhood_radius_label, 2, 0, 1, 1)

        self.deno_n2v_neighborhood_struct_label = QLabel(self.frame_44)
        self.deno_n2v_neighborhood_struct_label.setObjectName(u"deno_n2v_neighborhood_struct_label")
        self.deno_n2v_neighborhood_struct_label.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_neighborhood_struct_label, 3, 0, 1, 1)

        self.deno_n2v_neighborhood_struct_input = QComboBox(self.frame_44)
        self.deno_n2v_neighborhood_struct_input.addItem("")
        self.deno_n2v_neighborhood_struct_input.addItem("")
        self.deno_n2v_neighborhood_struct_input.setObjectName(u"deno_n2v_neighborhood_struct_input")
        self.deno_n2v_neighborhood_struct_input.setMinimumSize(QSize(200, 30))
        self.deno_n2v_neighborhood_struct_input.setMaximumSize(QSize(200, 30))
        self.deno_n2v_neighborhood_struct_input.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_neighborhood_struct_input, 3, 1, 1, 1)

        self.deno_n2v_neighborhood_radius_input = QLineEdit(self.frame_44)
        self.deno_n2v_neighborhood_radius_input.setObjectName(u"deno_n2v_neighborhood_radius_input")
        self.deno_n2v_neighborhood_radius_input.setMinimumSize(QSize(200, 30))
        self.deno_n2v_neighborhood_radius_input.setMaximumSize(QSize(200, 30))
        self.deno_n2v_neighborhood_radius_input.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_neighborhood_radius_input, 2, 1, 1, 1)

        self.deno_n2v_perc_pix_input = QLineEdit(self.frame_44)
        self.deno_n2v_perc_pix_input.setObjectName(u"deno_n2v_perc_pix_input")
        self.deno_n2v_perc_pix_input.setMinimumSize(QSize(200, 30))
        self.deno_n2v_perc_pix_input.setMaximumSize(QSize(200, 30))
        self.deno_n2v_perc_pix_input.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_perc_pix_input, 0, 1, 1, 1)

        self.deno_n2v_manipulator_input = QComboBox(self.frame_44)
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.addItem("")
        self.deno_n2v_manipulator_input.setObjectName(u"deno_n2v_manipulator_input")
        self.deno_n2v_manipulator_input.setMinimumSize(QSize(200, 30))
        self.deno_n2v_manipulator_input.setMaximumSize(QSize(200, 30))
        self.deno_n2v_manipulator_input.setFont(font)

        self.gridLayout_48.addWidget(self.deno_n2v_manipulator_input, 1, 1, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_37, 1, 2, 1, 1)


        self.gridLayout_49.addWidget(self.frame_44, 1, 0, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_49.addItem(self.horizontalSpacer_38, 0, 1, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_49.addWidget(self.label_15, 0, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_49.addItem(self.verticalSpacer_19, 2, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_24.addWidget(self.scrollArea_4)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_denoising_page)
        self.train_workflow_specific_tab_sr_page = QWidget()
        self.train_workflow_specific_tab_sr_page.setObjectName(u"train_workflow_specific_tab_sr_page")
        self.verticalLayout_25 = QVBoxLayout(self.train_workflow_specific_tab_sr_page)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.train_workflow_specific_tab_sr_page)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setFont(font)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 913, 338))
        self.gridLayout_50 = QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_21, 3, 0, 1, 1)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_48.setFrameShape(QFrame.Box)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_56 = QGridLayout(self.frame_48)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.sr_upscaling_label = QLabel(self.frame_48)
        self.sr_upscaling_label.setObjectName(u"sr_upscaling_label")
        self.sr_upscaling_label.setFont(font)

        self.gridLayout_56.addWidget(self.sr_upscaling_label, 0, 0, 1, 1)

        self.sr_upscaling_input = QComboBox(self.frame_48)
        self.sr_upscaling_input.addItem("")
        self.sr_upscaling_input.addItem("")
        self.sr_upscaling_input.setObjectName(u"sr_upscaling_input")
        self.sr_upscaling_input.setMinimumSize(QSize(200, 30))
        self.sr_upscaling_input.setMaximumSize(QSize(200, 30))
        self.sr_upscaling_input.setFont(font)

        self.gridLayout_56.addWidget(self.sr_upscaling_input, 0, 1, 1, 1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_53, 0, 2, 1, 1)


        self.gridLayout_50.addWidget(self.frame_48, 1, 0, 1, 1)

        self.label_95 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font)

        self.gridLayout_50.addWidget(self.label_95, 0, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_40, 1, 1, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_25.addWidget(self.scrollArea_5)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_sr_page)
        self.train_workflow_specific_tab_ssl_page = QWidget()
        self.train_workflow_specific_tab_ssl_page.setObjectName(u"train_workflow_specific_tab_ssl_page")
        self.verticalLayout_26 = QVBoxLayout(self.train_workflow_specific_tab_ssl_page)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.train_workflow_specific_tab_ssl_page)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setFont(font)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 913, 338))
        self.gridLayout_51 = QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_51.addItem(self.verticalSpacer_22, 3, 0, 1, 1)

        self.label_96 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font)

        self.gridLayout_51.addWidget(self.label_96, 0, 0, 1, 1)

        self.frame_49 = QFrame(self.scrollAreaWidgetContents_10)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 0))
        self.frame_49.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_49.setFrameShape(QFrame.Box)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_49)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.ssl_resizing_factor_label = QLabel(self.frame_49)
        self.ssl_resizing_factor_label.setObjectName(u"ssl_resizing_factor_label")
        self.ssl_resizing_factor_label.setFont(font)

        self.gridLayout_57.addWidget(self.ssl_resizing_factor_label, 0, 0, 1, 1)

        self.ssl_noise_input = QLineEdit(self.frame_49)
        self.ssl_noise_input.setObjectName(u"ssl_noise_input")
        self.ssl_noise_input.setMinimumSize(QSize(200, 30))
        self.ssl_noise_input.setMaximumSize(QSize(200, 30))
        self.ssl_noise_input.setFont(font)

        self.gridLayout_57.addWidget(self.ssl_noise_input, 1, 1, 1, 1)

        self.ssl_noise_label = QLabel(self.frame_49)
        self.ssl_noise_label.setObjectName(u"ssl_noise_label")
        self.ssl_noise_label.setFont(font)

        self.gridLayout_57.addWidget(self.ssl_noise_label, 1, 0, 1, 1)

        self.ssl_resizing_factor_input = QComboBox(self.frame_49)
        self.ssl_resizing_factor_input.addItem("")
        self.ssl_resizing_factor_input.addItem("")
        self.ssl_resizing_factor_input.addItem("")
        self.ssl_resizing_factor_input.setObjectName(u"ssl_resizing_factor_input")
        self.ssl_resizing_factor_input.setMinimumSize(QSize(200, 30))
        self.ssl_resizing_factor_input.setMaximumSize(QSize(200, 30))
        self.ssl_resizing_factor_input.setFont(font)

        self.gridLayout_57.addWidget(self.ssl_resizing_factor_input, 0, 1, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_46, 0, 2, 1, 1)


        self.gridLayout_51.addWidget(self.frame_49, 2, 0, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_41, 2, 1, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_26.addWidget(self.scrollArea_6)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_ssl_page)
        self.train_workflow_specific_tab_classification_page = QWidget()
        self.train_workflow_specific_tab_classification_page.setObjectName(u"train_workflow_specific_tab_classification_page")
        self.verticalLayout_27 = QVBoxLayout(self.train_workflow_specific_tab_classification_page)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.train_workflow_specific_tab_classification_page)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setFont(font)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 913, 338))
        self.gridLayout_52 = QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_52.addItem(self.horizontalSpacer_42, 0, 1, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_11)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_52.addWidget(self.label_25, 0, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_52.addItem(self.verticalSpacer_23, 1, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_27.addWidget(self.scrollArea_7)

        self.train_workflow_specific_tab_stackedWidget.addWidget(self.train_workflow_specific_tab_classification_page)

        self.verticalLayout_9.addWidget(self.train_workflow_specific_tab_stackedWidget)


        self.gridLayout_16.addWidget(self.frame_15, 0, 0, 1, 1)

        self.train_tab_widget.addTab(self.train_workflow_specific_tab, "")

        self.gridLayout_14.addWidget(self.train_tab_widget, 3, 0, 1, 2)

        self.stackedWidget_create_yaml_frame.addWidget(self.train_page)
        self.test_page = QWidget()
        self.test_page.setObjectName(u"test_page")
        self.test_general_frame = QFrame(self.test_page)
        self.test_general_frame.setObjectName(u"test_general_frame")
        self.test_general_frame.setGeometry(QRect(0, 0, 951, 463))
        self.test_general_frame.setFrameShape(QFrame.StyledPanel)
        self.test_general_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.test_general_frame)
        self.gridLayout_36.setSpacing(9)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_27, 0, 1, 1, 1)

        self.frame_35 = QFrame(self.test_general_frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 50))
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.frame_35)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMaximumSize(QSize(16777215, 16777215))
        self.label_81.setFont(font)
        self.label_81.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_13.addWidget(self.label_81)

        self.enable_test_input = QComboBox(self.frame_35)
        self.enable_test_input.addItem("")
        self.enable_test_input.addItem("")
        self.enable_test_input.setObjectName(u"enable_test_input")
        self.enable_test_input.setMinimumSize(QSize(100, 0))
        self.enable_test_input.setFont(font)

        self.horizontalLayout_13.addWidget(self.enable_test_input)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_26)


        self.gridLayout_36.addWidget(self.frame_35, 0, 0, 1, 1)

        self.test_tab_widget = QTabWidget(self.test_general_frame)
        self.test_tab_widget.setObjectName(u"test_tab_widget")
        self.test_tab_widget.setFont(font)
        self.test_general_options_tab = QWidget()
        self.test_general_options_tab.setObjectName(u"test_general_options_tab")
        self.gridLayout_40 = QGridLayout(self.test_general_options_tab)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.test_scrollArea = QScrollArea(self.test_general_options_tab)
        self.test_scrollArea.setObjectName(u"test_scrollArea")
        self.test_scrollArea.setFrameShape(QFrame.NoFrame)
        self.test_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 913, 995))
        self.gridLayout_37 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.test_advanced_options_frame = QFrame(self.scrollAreaWidgetContents_5)
        self.test_advanced_options_frame.setObjectName(u"test_advanced_options_frame")
        self.test_advanced_options_frame.setMinimumSize(QSize(0, 0))
        self.test_advanced_options_frame.setFrameShape(QFrame.NoFrame)
        self.test_advanced_options_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.test_advanced_options_frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_32)

        self.test_advanced_options_frame_2 = QFrame(self.test_advanced_options_frame)
        self.test_advanced_options_frame_2.setObjectName(u"test_advanced_options_frame_2")
        self.test_advanced_options_frame_2.setFrameShape(QFrame.Box)
        self.test_advanced_options_frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.test_advanced_options_frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_89 = QLabel(self.test_advanced_options_frame_2)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font)

        self.gridLayout_8.addWidget(self.label_89, 2, 0, 2, 2)

        self.label_105 = QLabel(self.test_advanced_options_frame_2)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font)

        self.gridLayout_8.addWidget(self.label_105, 6, 0, 1, 1)

        self.label_92 = QLabel(self.test_advanced_options_frame_2)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font)

        self.gridLayout_8.addWidget(self.label_92, 0, 0, 1, 1)

        self.frame_41 = QFrame(self.test_advanced_options_frame_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 0))
        self.frame_41.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_41.setFrameShape(QFrame.Box)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_41)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.test_median_padding_label = QLabel(self.frame_41)
        self.test_median_padding_label.setObjectName(u"test_median_padding_label")
        self.test_median_padding_label.setFont(font)

        self.gridLayout_43.addWidget(self.test_median_padding_label, 2, 0, 1, 1)

        self.test_overlap_label = QLabel(self.frame_41)
        self.test_overlap_label.setObjectName(u"test_overlap_label")
        self.test_overlap_label.setFont(font)

        self.gridLayout_43.addWidget(self.test_overlap_label, 0, 0, 1, 1)

        self.test_resolution_input = QLineEdit(self.frame_41)
        self.test_resolution_input.setObjectName(u"test_resolution_input")
        self.test_resolution_input.setMinimumSize(QSize(200, 30))
        self.test_resolution_input.setMaximumSize(QSize(200, 30))
        self.test_resolution_input.setFont(font)

        self.gridLayout_43.addWidget(self.test_resolution_input, 3, 2, 1, 1)

        self.test_padding_input = QLineEdit(self.frame_41)
        self.test_padding_input.setObjectName(u"test_padding_input")
        self.test_padding_input.setMinimumSize(QSize(200, 30))
        self.test_padding_input.setMaximumSize(QSize(200, 30))
        self.test_padding_input.setFont(font)

        self.gridLayout_43.addWidget(self.test_padding_input, 1, 2, 1, 1)

        self.test_resolution_label = QLabel(self.frame_41)
        self.test_resolution_label.setObjectName(u"test_resolution_label")
        self.test_resolution_label.setFont(font)

        self.gridLayout_43.addWidget(self.test_resolution_label, 3, 0, 1, 1)

        self.test_overlap_input = QLineEdit(self.frame_41)
        self.test_overlap_input.setObjectName(u"test_overlap_input")
        self.test_overlap_input.setMinimumSize(QSize(200, 30))
        self.test_overlap_input.setMaximumSize(QSize(200, 30))
        self.test_overlap_input.setFont(font)

        self.gridLayout_43.addWidget(self.test_overlap_input, 0, 2, 1, 1)

        self.test_padding_label = QLabel(self.frame_41)
        self.test_padding_label.setObjectName(u"test_padding_label")
        self.test_padding_label.setFont(font)

        self.gridLayout_43.addWidget(self.test_padding_label, 1, 0, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_43.addItem(self.horizontalSpacer_34, 0, 4, 1, 1)

        self.test_argmax_label = QLabel(self.frame_41)
        self.test_argmax_label.setObjectName(u"test_argmax_label")
        self.test_argmax_label.setFont(font)

        self.gridLayout_43.addWidget(self.test_argmax_label, 4, 0, 1, 1)

        self.test_argmax_input = QComboBox(self.frame_41)
        self.test_argmax_input.addItem("")
        self.test_argmax_input.addItem("")
        self.test_argmax_input.setObjectName(u"test_argmax_input")
        self.test_argmax_input.setMinimumSize(QSize(200, 30))
        self.test_argmax_input.setMaximumSize(QSize(200, 30))
        self.test_argmax_input.setFont(font)

        self.gridLayout_43.addWidget(self.test_argmax_input, 4, 2, 1, 1)

        self.test_median_padding_input = QComboBox(self.frame_41)
        self.test_median_padding_input.addItem("")
        self.test_median_padding_input.addItem("")
        self.test_median_padding_input.setObjectName(u"test_median_padding_input")
        self.test_median_padding_input.setMinimumSize(QSize(200, 30))
        self.test_median_padding_input.setMaximumSize(QSize(200, 30))
        self.test_median_padding_input.setFont(font)

        self.gridLayout_43.addWidget(self.test_median_padding_input, 2, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_41, 4, 0, 1, 2)

        self.frame_55 = QFrame(self.test_advanced_options_frame_2)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_55.setFrameShape(QFrame.Box)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_55)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.test_apply_bin_mask_input = QComboBox(self.frame_55)
        self.test_apply_bin_mask_input.addItem("")
        self.test_apply_bin_mask_input.addItem("")
        self.test_apply_bin_mask_input.setObjectName(u"test_apply_bin_mask_input")
        self.test_apply_bin_mask_input.setMinimumSize(QSize(200, 30))
        self.test_apply_bin_mask_input.setMaximumSize(QSize(200, 30))
        self.test_apply_bin_mask_input.setFont(font)

        self.gridLayout_63.addWidget(self.test_apply_bin_mask_input, 0, 1, 1, 1)

        self.test_apply_bin_mask_label = QLabel(self.frame_55)
        self.test_apply_bin_mask_label.setObjectName(u"test_apply_bin_mask_label")
        self.test_apply_bin_mask_label.setFont(font)

        self.gridLayout_63.addWidget(self.test_apply_bin_mask_label, 0, 0, 1, 1)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_63.addItem(self.horizontalSpacer_57, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_55, 7, 0, 1, 1)

        self.frame_46 = QFrame(self.test_advanced_options_frame_2)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 0))
        self.frame_46.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_46.setFrameShape(QFrame.Box)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.frame_46)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.test_full_image_label = QLabel(self.frame_46)
        self.test_full_image_label.setObjectName(u"test_full_image_label")
        self.test_full_image_label.setFont(font)

        self.gridLayout_54.addWidget(self.test_full_image_label, 3, 0, 1, 1)

        self.test_full_image_input = QComboBox(self.frame_46)
        self.test_full_image_input.addItem("")
        self.test_full_image_input.addItem("")
        self.test_full_image_input.setObjectName(u"test_full_image_input")
        self.test_full_image_input.setMinimumSize(QSize(200, 30))
        self.test_full_image_input.setMaximumSize(QSize(200, 30))
        self.test_full_image_input.setFont(font)

        self.gridLayout_54.addWidget(self.test_full_image_input, 3, 1, 1, 1)

        self.test_merge_patches_input = QComboBox(self.frame_46)
        self.test_merge_patches_input.addItem("")
        self.test_merge_patches_input.addItem("")
        self.test_merge_patches_input.setObjectName(u"test_merge_patches_input")
        self.test_merge_patches_input.setMinimumSize(QSize(200, 30))
        self.test_merge_patches_input.setMaximumSize(QSize(200, 30))
        self.test_merge_patches_input.setFont(font)

        self.gridLayout_54.addWidget(self.test_merge_patches_input, 2, 1, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_54.addItem(self.verticalSpacer_24, 4, 0, 1, 1)

        self.test_merge_patches_label = QLabel(self.frame_46)
        self.test_merge_patches_label.setObjectName(u"test_merge_patches_label")
        self.test_merge_patches_label.setFont(font)

        self.gridLayout_54.addWidget(self.test_merge_patches_label, 2, 0, 1, 1)

        self.test_evaluate_label = QLabel(self.frame_46)
        self.test_evaluate_label.setObjectName(u"test_evaluate_label")
        self.test_evaluate_label.setFont(font)

        self.gridLayout_54.addWidget(self.test_evaluate_label, 0, 0, 1, 1)

        self.test_evaluate_input = QComboBox(self.frame_46)
        self.test_evaluate_input.addItem("")
        self.test_evaluate_input.addItem("")
        self.test_evaluate_input.setObjectName(u"test_evaluate_input")
        self.test_evaluate_input.setMinimumSize(QSize(200, 30))
        self.test_evaluate_input.setMaximumSize(QSize(200, 30))
        self.test_evaluate_input.setFont(font)

        self.gridLayout_54.addWidget(self.test_evaluate_input, 0, 1, 1, 1)

        self.test_per_patch_label = QLabel(self.frame_46)
        self.test_per_patch_label.setObjectName(u"test_per_patch_label")
        self.test_per_patch_label.setFont(font)

        self.gridLayout_54.addWidget(self.test_per_patch_label, 1, 0, 1, 1)

        self.test_per_patch_input = QComboBox(self.frame_46)
        self.test_per_patch_input.addItem("")
        self.test_per_patch_input.addItem("")
        self.test_per_patch_input.setObjectName(u"test_per_patch_input")
        self.test_per_patch_input.setMinimumSize(QSize(200, 30))
        self.test_per_patch_input.setMaximumSize(QSize(200, 30))
        self.test_per_patch_input.setFont(font)

        self.gridLayout_54.addWidget(self.test_per_patch_input, 1, 1, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_43, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_46, 9, 0, 1, 1)

        self.frame_45 = QFrame(self.test_advanced_options_frame_2)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 0))
        self.frame_45.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_45.setFrameShape(QFrame.Box)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_45)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.test_reduce_memory_label = QLabel(self.frame_45)
        self.test_reduce_memory_label.setObjectName(u"test_reduce_memory_label")
        self.test_reduce_memory_label.setFont(font)

        self.gridLayout_53.addWidget(self.test_reduce_memory_label, 0, 0, 1, 1)

        self.test_tta_label = QLabel(self.frame_45)
        self.test_tta_label.setObjectName(u"test_tta_label")
        self.test_tta_label.setFont(font)

        self.gridLayout_53.addWidget(self.test_tta_label, 3, 0, 1, 1)

        self.test_tta_input = QComboBox(self.frame_45)
        self.test_tta_input.addItem("")
        self.test_tta_input.addItem("")
        self.test_tta_input.setObjectName(u"test_tta_input")
        self.test_tta_input.setMinimumSize(QSize(200, 30))
        self.test_tta_input.setMaximumSize(QSize(200, 30))
        self.test_tta_input.setFont(font)

        self.gridLayout_53.addWidget(self.test_tta_input, 3, 1, 1, 1)

        self.test_2d_as_3d_stack_input = QComboBox(self.frame_45)
        self.test_2d_as_3d_stack_input.addItem("")
        self.test_2d_as_3d_stack_input.addItem("")
        self.test_2d_as_3d_stack_input.setObjectName(u"test_2d_as_3d_stack_input")
        self.test_2d_as_3d_stack_input.setMinimumSize(QSize(200, 30))
        self.test_2d_as_3d_stack_input.setMaximumSize(QSize(200, 30))
        self.test_2d_as_3d_stack_input.setFont(font)

        self.gridLayout_53.addWidget(self.test_2d_as_3d_stack_input, 4, 1, 1, 1)

        self.test_2d_as_3d_stack_label = QLabel(self.frame_45)
        self.test_2d_as_3d_stack_label.setObjectName(u"test_2d_as_3d_stack_label")
        self.test_2d_as_3d_stack_label.setFont(font)

        self.gridLayout_53.addWidget(self.test_2d_as_3d_stack_label, 4, 0, 1, 1)

        self.test_verbose_input = QComboBox(self.frame_45)
        self.test_verbose_input.addItem("")
        self.test_verbose_input.addItem("")
        self.test_verbose_input.setObjectName(u"test_verbose_input")
        self.test_verbose_input.setMinimumSize(QSize(200, 30))
        self.test_verbose_input.setMaximumSize(QSize(200, 30))
        self.test_verbose_input.setFont(font)

        self.gridLayout_53.addWidget(self.test_verbose_input, 1, 1, 1, 1)

        self.test_verbose_label = QLabel(self.frame_45)
        self.test_verbose_label.setObjectName(u"test_verbose_label")
        self.test_verbose_label.setFont(font)

        self.gridLayout_53.addWidget(self.test_verbose_label, 1, 0, 1, 1)

        self.test_reduce_memory_input = QComboBox(self.frame_45)
        self.test_reduce_memory_input.addItem("")
        self.test_reduce_memory_input.addItem("")
        self.test_reduce_memory_input.setObjectName(u"test_reduce_memory_input")
        self.test_reduce_memory_input.setMinimumSize(QSize(200, 30))
        self.test_reduce_memory_input.setMaximumSize(QSize(200, 30))
        self.test_reduce_memory_input.setFont(font)

        self.gridLayout_53.addWidget(self.test_reduce_memory_input, 0, 1, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_44, 1, 2, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_53.addItem(self.verticalSpacer_25, 5, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_45, 1, 0, 1, 1)

        self.label_98 = QLabel(self.test_advanced_options_frame_2)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font)

        self.gridLayout_8.addWidget(self.label_98, 8, 0, 1, 1)


        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.test_advanced_options_frame_2)


        self.gridLayout_37.addWidget(self.test_advanced_options_frame, 3, 0, 1, 1)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 30))
        self.frame_37.setFont(font)
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.train_advanced_label_2 = QLabel(self.frame_37)
        self.train_advanced_label_2.setObjectName(u"train_advanced_label_2")
        self.train_advanced_label_2.setMaximumSize(QSize(150, 35))
        self.train_advanced_label_2.setFont(font)

        self.horizontalLayout_14.addWidget(self.train_advanced_label_2)

        self.test_advanced_bn = QPushButton(self.frame_37)
        self.test_advanced_bn.setObjectName(u"test_advanced_bn")
        self.test_advanced_bn.setMaximumSize(QSize(35, 35))
        self.test_advanced_bn.setFont(font)
        self.test_advanced_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.test_advanced_bn.setIcon(icon10)

        self.horizontalLayout_14.addWidget(self.test_advanced_bn)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_29)


        self.gridLayout_37.addWidget(self.frame_37, 2, 0, 1, 1)

        self.label_85 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMaximumSize(QSize(150, 16777215))
        self.label_85.setFont(font)

        self.gridLayout_37.addWidget(self.label_85, 0, 0, 1, 1)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFont(font)
        self.frame_36.setStyleSheet(u"background: rgb(246,246,246);\n"
"")
        self.frame_36.setFrameShape(QFrame.Box)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_36)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.use_val_as_test = QLabel(self.frame_36)
        self.use_val_as_test.setObjectName(u"use_val_as_test")
        self.use_val_as_test.setMinimumSize(QSize(0, 0))
        self.use_val_as_test.setMaximumSize(QSize(200, 16777215))
        self.use_val_as_test.setFont(font)

        self.gridLayout_38.addWidget(self.use_val_as_test, 1, 1, 1, 1)

        self.test_data_gt_input_browse_bn = QPushButton(self.frame_36)
        self.test_data_gt_input_browse_bn.setObjectName(u"test_data_gt_input_browse_bn")
        self.test_data_gt_input_browse_bn.setFont(font)

        self.gridLayout_38.addWidget(self.test_data_gt_input_browse_bn, 4, 3, 1, 1)

        self.test_data_gt_label = QLabel(self.frame_36)
        self.test_data_gt_label.setObjectName(u"test_data_gt_label")
        self.test_data_gt_label.setFont(font)

        self.gridLayout_38.addWidget(self.test_data_gt_label, 4, 1, 1, 1)

        self.test_data_label = QLabel(self.frame_36)
        self.test_data_label.setObjectName(u"test_data_label")
        self.test_data_label.setFont(font)

        self.gridLayout_38.addWidget(self.test_data_label, 2, 1, 1, 1)

        self.test_data_in_memory_label = QLabel(self.frame_36)
        self.test_data_in_memory_label.setObjectName(u"test_data_in_memory_label")
        self.test_data_in_memory_label.setFont(font)

        self.gridLayout_38.addWidget(self.test_data_in_memory_label, 5, 1, 1, 1)

        self.test_data_input_browse_bn = QPushButton(self.frame_36)
        self.test_data_input_browse_bn.setObjectName(u"test_data_input_browse_bn")
        self.test_data_input_browse_bn.setFont(font)

        self.gridLayout_38.addWidget(self.test_data_input_browse_bn, 2, 3, 1, 1)

        self.test_data_input = QTextBrowser(self.frame_36)
        self.test_data_input.setObjectName(u"test_data_input")
        self.test_data_input.setMinimumSize(QSize(500, 0))
        self.test_data_input.setMaximumSize(QSize(500, 30))
        self.test_data_input.setFont(font)
        self.test_data_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_data_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_data_input.setLineWrapMode(QTextEdit.NoWrap)
        self.test_data_input.setReadOnly(False)

        self.gridLayout_38.addWidget(self.test_data_input, 2, 2, 1, 1)

        self.test_data_gt_input = QTextBrowser(self.frame_36)
        self.test_data_gt_input.setObjectName(u"test_data_gt_input")
        self.test_data_gt_input.setMaximumSize(QSize(500, 30))
        self.test_data_gt_input.setFont(font)
        self.test_data_gt_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_data_gt_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_data_gt_input.setLineWrapMode(QTextEdit.NoWrap)
        self.test_data_gt_input.setReadOnly(False)

        self.gridLayout_38.addWidget(self.test_data_gt_input, 4, 2, 1, 1)

        self.test_data_in_memory_input = QComboBox(self.frame_36)
        self.test_data_in_memory_input.addItem("")
        self.test_data_in_memory_input.addItem("")
        self.test_data_in_memory_input.setObjectName(u"test_data_in_memory_input")
        self.test_data_in_memory_input.setMinimumSize(QSize(200, 30))
        self.test_data_in_memory_input.setMaximumSize(QSize(200, 30))
        self.test_data_in_memory_input.setFont(font)

        self.gridLayout_38.addWidget(self.test_data_in_memory_input, 5, 2, 1, 1)

        self.test_exists_gt_label = QLabel(self.frame_36)
        self.test_exists_gt_label.setObjectName(u"test_exists_gt_label")
        self.test_exists_gt_label.setFont(font)

        self.gridLayout_38.addWidget(self.test_exists_gt_label, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_4, 2, 4, 1, 1)

        self.use_val_as_test_input = QComboBox(self.frame_36)
        self.use_val_as_test_input.addItem("")
        self.use_val_as_test_input.addItem("")
        self.use_val_as_test_input.setObjectName(u"use_val_as_test_input")
        self.use_val_as_test_input.setMinimumSize(QSize(200, 30))
        self.use_val_as_test_input.setMaximumSize(QSize(200, 30))
        self.use_val_as_test_input.setFont(font)

        self.gridLayout_38.addWidget(self.use_val_as_test_input, 1, 2, 1, 1)

        self.test_exists_gt_input = QComboBox(self.frame_36)
        self.test_exists_gt_input.addItem("")
        self.test_exists_gt_input.addItem("")
        self.test_exists_gt_input.setObjectName(u"test_exists_gt_input")
        self.test_exists_gt_input.setMinimumSize(QSize(200, 30))
        self.test_exists_gt_input.setMaximumSize(QSize(200, 30))
        self.test_exists_gt_input.setFont(font)

        self.gridLayout_38.addWidget(self.test_exists_gt_input, 3, 2, 1, 1)


        self.gridLayout_37.addWidget(self.frame_36, 1, 0, 1, 2)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_37.addItem(self.verticalSpacer_17, 4, 0, 1, 1)

        self.test_scrollArea.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_40.addWidget(self.test_scrollArea, 0, 0, 1, 1)

        self.test_tab_widget.addTab(self.test_general_options_tab, "")
        self.test_workflow_specific_tab = QWidget()
        self.test_workflow_specific_tab.setObjectName(u"test_workflow_specific_tab")
        self.frame_39 = QFrame(self.test_workflow_specific_tab)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(-1, -1, 929, 356))
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_39)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.test_workflow_specific_tab_stackedWidget = QStackedWidget(self.frame_39)
        self.test_workflow_specific_tab_stackedWidget.setObjectName(u"test_workflow_specific_tab_stackedWidget")
        self.test_workflow_specific_tab_semantic_seg_page = QWidget()
        self.test_workflow_specific_tab_semantic_seg_page.setObjectName(u"test_workflow_specific_tab_semantic_seg_page")
        self.verticalLayout_12 = QVBoxLayout(self.test_workflow_specific_tab_semantic_seg_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8 = QScrollArea(self.test_workflow_specific_tab_semantic_seg_page)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 927, 354))
        self.gridLayout_61 = QGridLayout(self.scrollAreaWidgetContents_12)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.label_82 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(16777215, 16777215))
        self.label_82.setFont(font)

        self.gridLayout_61.addWidget(self.label_82, 0, 0, 1, 1)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents_12)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_40.setFrameShape(QFrame.Box)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_40)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.sem_seg_check_data_input = QComboBox(self.frame_40)
        self.sem_seg_check_data_input.addItem("")
        self.sem_seg_check_data_input.addItem("")
        self.sem_seg_check_data_input.setObjectName(u"sem_seg_check_data_input")
        self.sem_seg_check_data_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_check_data_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_check_data_input.setFont(font)

        self.gridLayout_42.addWidget(self.sem_seg_check_data_input, 0, 1, 1, 1)

        self.sem_seg_check_data_label = QLabel(self.frame_40)
        self.sem_seg_check_data_label.setObjectName(u"sem_seg_check_data_label")
        self.sem_seg_check_data_label.setFont(font)

        self.gridLayout_42.addWidget(self.sem_seg_check_data_label, 0, 0, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_33, 0, 2, 1, 1)


        self.gridLayout_61.addWidget(self.frame_40, 2, 0, 1, 1)

        self.label_101 = QLabel(self.scrollAreaWidgetContents_12)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font)

        self.gridLayout_61.addWidget(self.label_101, 3, 0, 1, 1)

        self.frame_52 = QFrame(self.scrollAreaWidgetContents_12)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 0))
        self.frame_52.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_52.setFrameShape(QFrame.Box)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_52)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.sem_seg_yz_filtering_label = QLabel(self.frame_52)
        self.sem_seg_yz_filtering_label.setObjectName(u"sem_seg_yz_filtering_label")
        self.sem_seg_yz_filtering_label.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_yz_filtering_label, 0, 0, 1, 1)

        self.sem_seg_z_filtering_label = QLabel(self.frame_52)
        self.sem_seg_z_filtering_label.setObjectName(u"sem_seg_z_filtering_label")
        self.sem_seg_z_filtering_label.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_z_filtering_label, 2, 0, 1, 1)

        self.sem_seg_yz_filtering_size_label = QLabel(self.frame_52)
        self.sem_seg_yz_filtering_size_label.setObjectName(u"sem_seg_yz_filtering_size_label")
        self.sem_seg_yz_filtering_size_label.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_yz_filtering_size_label, 1, 0, 1, 1)

        self.sem_seg_z_filtering_size_label = QLabel(self.frame_52)
        self.sem_seg_z_filtering_size_label.setObjectName(u"sem_seg_z_filtering_size_label")
        self.sem_seg_z_filtering_size_label.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_z_filtering_size_label, 3, 0, 1, 1)

        self.sem_seg_z_filtering_size_input = QLineEdit(self.frame_52)
        self.sem_seg_z_filtering_size_input.setObjectName(u"sem_seg_z_filtering_size_input")
        self.sem_seg_z_filtering_size_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_z_filtering_size_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_z_filtering_size_input.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_z_filtering_size_input, 3, 1, 1, 1)

        self.sem_seg_yz_filtering_size_input = QLineEdit(self.frame_52)
        self.sem_seg_yz_filtering_size_input.setObjectName(u"sem_seg_yz_filtering_size_input")
        self.sem_seg_yz_filtering_size_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_yz_filtering_size_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_yz_filtering_size_input.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_yz_filtering_size_input, 1, 1, 1, 1)

        self.sem_seg_yz_filtering_input = QComboBox(self.frame_52)
        self.sem_seg_yz_filtering_input.addItem("")
        self.sem_seg_yz_filtering_input.addItem("")
        self.sem_seg_yz_filtering_input.setObjectName(u"sem_seg_yz_filtering_input")
        self.sem_seg_yz_filtering_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_yz_filtering_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_yz_filtering_input.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_yz_filtering_input, 0, 1, 1, 1)

        self.sem_seg_z_filtering_input = QComboBox(self.frame_52)
        self.sem_seg_z_filtering_input.addItem("")
        self.sem_seg_z_filtering_input.addItem("")
        self.sem_seg_z_filtering_input.setObjectName(u"sem_seg_z_filtering_input")
        self.sem_seg_z_filtering_input.setMinimumSize(QSize(200, 30))
        self.sem_seg_z_filtering_input.setMaximumSize(QSize(200, 30))
        self.sem_seg_z_filtering_input.setFont(font)

        self.gridLayout_60.addWidget(self.sem_seg_z_filtering_input, 2, 1, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_51, 1, 2, 1, 1)


        self.gridLayout_61.addWidget(self.frame_52, 4, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_61.addItem(self.horizontalSpacer_30, 0, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_61.addItem(self.verticalSpacer_18, 5, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_12.addWidget(self.scrollArea_8)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_semantic_seg_page)
        self.test_workflow_specific_tab_instance_seg_page = QWidget()
        self.test_workflow_specific_tab_instance_seg_page.setObjectName(u"test_workflow_specific_tab_instance_seg_page")
        self.verticalLayout_16 = QVBoxLayout(self.test_workflow_specific_tab_instance_seg_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_9 = QScrollArea(self.test_workflow_specific_tab_instance_seg_page)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, -769, 913, 1128))
        self.gridLayout_44 = QGridLayout(self.scrollAreaWidgetContents_13)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_35, 0, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)

        self.gridLayout_44.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_86 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font)

        self.gridLayout_44.addWidget(self.label_86, 3, 0, 1, 1)

        self.frame_50 = QFrame(self.scrollAreaWidgetContents_13)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 0))
        self.frame_50.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_50.setFrameShape(QFrame.Box)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_50)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.inst_seg_repare_large_blobs_input = QLineEdit(self.frame_50)
        self.inst_seg_repare_large_blobs_input.setObjectName(u"inst_seg_repare_large_blobs_input")
        self.inst_seg_repare_large_blobs_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_repare_large_blobs_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_repare_large_blobs_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_repare_large_blobs_input, 6, 1, 1, 1)

        self.inst_seg_repare_large_blobs_label = QLabel(self.frame_50)
        self.inst_seg_repare_large_blobs_label.setObjectName(u"inst_seg_repare_large_blobs_label")
        self.inst_seg_repare_large_blobs_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_repare_large_blobs_label, 6, 0, 1, 1)

        self.inst_seg_circularity_filtering_label = QLabel(self.frame_50)
        self.inst_seg_circularity_filtering_label.setObjectName(u"inst_seg_circularity_filtering_label")
        self.inst_seg_circularity_filtering_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_circularity_filtering_label, 4, 0, 1, 1)

        self.inst_seg_voronoi_label = QLabel(self.frame_50)
        self.inst_seg_voronoi_label.setObjectName(u"inst_seg_voronoi_label")
        self.inst_seg_voronoi_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_voronoi_label, 5, 0, 1, 1)

        self.inst_seg_voronoi_input = QComboBox(self.frame_50)
        self.inst_seg_voronoi_input.addItem("")
        self.inst_seg_voronoi_input.addItem("")
        self.inst_seg_voronoi_input.setObjectName(u"inst_seg_voronoi_input")
        self.inst_seg_voronoi_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_voronoi_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_voronoi_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_voronoi_input, 5, 1, 1, 1)

        self.inst_seg_circularity_filtering_input = QLineEdit(self.frame_50)
        self.inst_seg_circularity_filtering_input.setObjectName(u"inst_seg_circularity_filtering_input")
        self.inst_seg_circularity_filtering_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_circularity_filtering_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_circularity_filtering_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_circularity_filtering_input, 4, 1, 1, 1)

        self.inst_seg_yz_filtering_label = QLabel(self.frame_50)
        self.inst_seg_yz_filtering_label.setObjectName(u"inst_seg_yz_filtering_label")
        self.inst_seg_yz_filtering_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_yz_filtering_label, 0, 0, 1, 1)

        self.inst_seg_yz_filtering_size_label = QLabel(self.frame_50)
        self.inst_seg_yz_filtering_size_label.setObjectName(u"inst_seg_yz_filtering_size_label")
        self.inst_seg_yz_filtering_size_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_yz_filtering_size_label, 1, 0, 1, 1)

        self.inst_seg_z_filtering_size_label = QLabel(self.frame_50)
        self.inst_seg_z_filtering_size_label.setObjectName(u"inst_seg_z_filtering_size_label")
        self.inst_seg_z_filtering_size_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_z_filtering_size_label, 3, 0, 1, 1)

        self.inst_seg_z_filtering_label = QLabel(self.frame_50)
        self.inst_seg_z_filtering_label.setObjectName(u"inst_seg_z_filtering_label")
        self.inst_seg_z_filtering_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_z_filtering_label, 2, 0, 1, 1)

        self.inst_seg_z_filtering_size_input = QLineEdit(self.frame_50)
        self.inst_seg_z_filtering_size_input.setObjectName(u"inst_seg_z_filtering_size_input")
        self.inst_seg_z_filtering_size_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_z_filtering_size_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_z_filtering_size_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_z_filtering_size_input, 3, 1, 1, 1)

        self.inst_seg_yz_filtering_size_input = QLineEdit(self.frame_50)
        self.inst_seg_yz_filtering_size_input.setObjectName(u"inst_seg_yz_filtering_size_input")
        self.inst_seg_yz_filtering_size_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_yz_filtering_size_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_yz_filtering_size_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_yz_filtering_size_input, 1, 1, 1, 1)

        self.inst_seg_yz_filtering_input = QComboBox(self.frame_50)
        self.inst_seg_yz_filtering_input.addItem("")
        self.inst_seg_yz_filtering_input.addItem("")
        self.inst_seg_yz_filtering_input.setObjectName(u"inst_seg_yz_filtering_input")
        self.inst_seg_yz_filtering_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_yz_filtering_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_yz_filtering_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_yz_filtering_input, 0, 1, 1, 1)

        self.inst_seg_z_filtering_input = QComboBox(self.frame_50)
        self.inst_seg_z_filtering_input.addItem("")
        self.inst_seg_z_filtering_input.addItem("")
        self.inst_seg_z_filtering_input.setObjectName(u"inst_seg_z_filtering_input")
        self.inst_seg_z_filtering_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_z_filtering_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_z_filtering_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_z_filtering_input, 2, 1, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_58.addItem(self.horizontalSpacer_48, 1, 2, 1, 1)

        self.inst_seg_remove_close_points_label = QLabel(self.frame_50)
        self.inst_seg_remove_close_points_label.setObjectName(u"inst_seg_remove_close_points_label")
        self.inst_seg_remove_close_points_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_remove_close_points_label, 7, 0, 1, 1)

        self.inst_seg_remove_close_points_input = QComboBox(self.frame_50)
        self.inst_seg_remove_close_points_input.addItem("")
        self.inst_seg_remove_close_points_input.addItem("")
        self.inst_seg_remove_close_points_input.setObjectName(u"inst_seg_remove_close_points_input")
        self.inst_seg_remove_close_points_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_remove_close_points_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_remove_close_points_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_remove_close_points_input, 7, 1, 1, 1)

        self.inst_seg_remove_close_points_radius_label = QLabel(self.frame_50)
        self.inst_seg_remove_close_points_radius_label.setObjectName(u"inst_seg_remove_close_points_radius_label")
        self.inst_seg_remove_close_points_radius_label.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_remove_close_points_radius_label, 8, 0, 1, 1)

        self.inst_seg_remove_close_points_radius_input = QLineEdit(self.frame_50)
        self.inst_seg_remove_close_points_radius_input.setObjectName(u"inst_seg_remove_close_points_radius_input")
        self.inst_seg_remove_close_points_radius_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_remove_close_points_radius_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_remove_close_points_radius_input.setFont(font)

        self.gridLayout_58.addWidget(self.inst_seg_remove_close_points_radius_input, 8, 1, 1, 1)


        self.gridLayout_44.addWidget(self.frame_50, 6, 0, 1, 1)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents_13)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_42.setFrameShape(QFrame.Box)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_42)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.inst_seg_b_channel_th_input = QLineEdit(self.frame_42)
        self.inst_seg_b_channel_th_input.setObjectName(u"inst_seg_b_channel_th_input")
        self.inst_seg_b_channel_th_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_b_channel_th_input.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_b_channel_th_input, 0, 1, 1, 1)

        self.inst_seg_c_channel_th_label = QLabel(self.frame_42)
        self.inst_seg_c_channel_th_label.setObjectName(u"inst_seg_c_channel_th_label")
        self.inst_seg_c_channel_th_label.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_c_channel_th_label, 1, 0, 1, 1)

        self.inst_seg_d_channel_th_label = QLabel(self.frame_42)
        self.inst_seg_d_channel_th_label.setObjectName(u"inst_seg_d_channel_th_label")
        self.inst_seg_d_channel_th_label.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_d_channel_th_label, 2, 0, 1, 1)

        self.inst_seg_fore_mask_th_label = QLabel(self.frame_42)
        self.inst_seg_fore_mask_th_label.setObjectName(u"inst_seg_fore_mask_th_label")
        self.inst_seg_fore_mask_th_label.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_fore_mask_th_label, 6, 0, 1, 1)

        self.inst_seg_b_channel_th_label = QLabel(self.frame_42)
        self.inst_seg_b_channel_th_label.setObjectName(u"inst_seg_b_channel_th_label")
        self.inst_seg_b_channel_th_label.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_b_channel_th_label, 0, 0, 1, 1)

        self.inst_seg_p_channel_th_label = QLabel(self.frame_42)
        self.inst_seg_p_channel_th_label.setObjectName(u"inst_seg_p_channel_th_label")
        self.inst_seg_p_channel_th_label.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_p_channel_th_label, 5, 0, 1, 1)

        self.inst_seg_d_channel_th_input = QLineEdit(self.frame_42)
        self.inst_seg_d_channel_th_input.setObjectName(u"inst_seg_d_channel_th_input")
        self.inst_seg_d_channel_th_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_d_channel_th_input.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_d_channel_th_input, 2, 1, 1, 1)

        self.inst_seg_c_channel_th_input = QLineEdit(self.frame_42)
        self.inst_seg_c_channel_th_input.setObjectName(u"inst_seg_c_channel_th_input")
        self.inst_seg_c_channel_th_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_c_channel_th_input.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_c_channel_th_input, 1, 1, 1, 1)

        self.inst_seg_fore_mask_th_input = QLineEdit(self.frame_42)
        self.inst_seg_fore_mask_th_input.setObjectName(u"inst_seg_fore_mask_th_input")
        self.inst_seg_fore_mask_th_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_fore_mask_th_input.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_fore_mask_th_input, 6, 1, 1, 1)

        self.inst_seg_p_channel_th_input = QLineEdit(self.frame_42)
        self.inst_seg_p_channel_th_input.setObjectName(u"inst_seg_p_channel_th_input")
        self.inst_seg_p_channel_th_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_p_channel_th_input.setFont(font)

        self.gridLayout_45.addWidget(self.inst_seg_p_channel_th_input, 5, 1, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_45.addItem(self.horizontalSpacer_36, 0, 2, 1, 1)


        self.gridLayout_44.addWidget(self.frame_42, 2, 0, 1, 1)

        self.frame_43 = QFrame(self.scrollAreaWidgetContents_13)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_43.setFrameShape(QFrame.Box)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_43)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.inst_seg_fore_ero_label = QLabel(self.frame_43)
        self.inst_seg_fore_ero_label.setObjectName(u"inst_seg_fore_ero_label")
        self.inst_seg_fore_ero_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_fore_ero_label, 6, 1, 1, 1)

        self.inst_seg_moph_op_rad_input = QLineEdit(self.frame_43)
        self.inst_seg_moph_op_rad_input.setObjectName(u"inst_seg_moph_op_rad_input")
        self.inst_seg_moph_op_rad_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_moph_op_rad_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_moph_op_rad_input, 2, 3, 1, 1)

        self.inst_seg_moph_op_rad_label = QLabel(self.frame_43)
        self.inst_seg_moph_op_rad_label.setObjectName(u"inst_seg_moph_op_rad_label")
        self.inst_seg_moph_op_rad_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_moph_op_rad_label, 2, 1, 1, 1)

        self.inst_seg_small_obj_fil_before_size_label = QLabel(self.frame_43)
        self.inst_seg_small_obj_fil_before_size_label.setObjectName(u"inst_seg_small_obj_fil_before_size_label")
        self.inst_seg_small_obj_fil_before_size_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_before_size_label, 8, 1, 1, 1)

        self.inst_seg_small_obj_fil_before_size_input = QLineEdit(self.frame_43)
        self.inst_seg_small_obj_fil_before_size_input.setObjectName(u"inst_seg_small_obj_fil_before_size_input")
        self.inst_seg_small_obj_fil_before_size_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_before_size_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_before_size_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_before_size_input, 8, 3, 1, 1)

        self.inst_seg_ero_dil_fore_input = QComboBox(self.frame_43)
        self.inst_seg_ero_dil_fore_input.addItem("")
        self.inst_seg_ero_dil_fore_input.addItem("")
        self.inst_seg_ero_dil_fore_input.setObjectName(u"inst_seg_ero_dil_fore_input")
        self.inst_seg_ero_dil_fore_input.setMinimumSize(QSize(100, 0))
        self.inst_seg_ero_dil_fore_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_ero_dil_fore_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_ero_dil_fore_input, 4, 3, 1, 1)

        self.inst_seg_small_obj_fil_after_size_label = QLabel(self.frame_43)
        self.inst_seg_small_obj_fil_after_size_label.setObjectName(u"inst_seg_small_obj_fil_after_size_label")
        self.inst_seg_small_obj_fil_after_size_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_after_size_label, 12, 1, 1, 1)

        self.inst_seg_small_obj_fil_after_input = QComboBox(self.frame_43)
        self.inst_seg_small_obj_fil_after_input.addItem("")
        self.inst_seg_small_obj_fil_after_input.addItem("")
        self.inst_seg_small_obj_fil_after_input.setObjectName(u"inst_seg_small_obj_fil_after_input")
        self.inst_seg_small_obj_fil_after_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_after_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_after_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_after_input, 11, 3, 1, 1)

        self.inst_seg_ero_dil_fore_label = QLabel(self.frame_43)
        self.inst_seg_ero_dil_fore_label.setObjectName(u"inst_seg_ero_dil_fore_label")
        self.inst_seg_ero_dil_fore_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_ero_dil_fore_label, 4, 1, 1, 1)

        self.inst_seg_moph_op_label = QLabel(self.frame_43)
        self.inst_seg_moph_op_label.setObjectName(u"inst_seg_moph_op_label")
        self.inst_seg_moph_op_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_moph_op_label, 1, 1, 1, 1)

        self.inst_seg_small_obj_fil_after_label = QLabel(self.frame_43)
        self.inst_seg_small_obj_fil_after_label.setObjectName(u"inst_seg_small_obj_fil_after_label")
        self.inst_seg_small_obj_fil_after_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_after_label, 11, 1, 1, 1)

        self.inst_seg_small_obj_fil_after_size_input = QLineEdit(self.frame_43)
        self.inst_seg_small_obj_fil_after_size_input.setObjectName(u"inst_seg_small_obj_fil_after_size_input")
        self.inst_seg_small_obj_fil_after_size_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_after_size_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_after_size_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_after_size_input, 12, 3, 1, 1)

        self.inst_seg_fore_dil_label = QLabel(self.frame_43)
        self.inst_seg_fore_dil_label.setObjectName(u"inst_seg_fore_dil_label")
        self.inst_seg_fore_dil_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_fore_dil_label, 5, 1, 1, 1)

        self.inst_seg_fore_dil_input = QLineEdit(self.frame_43)
        self.inst_seg_fore_dil_input.setObjectName(u"inst_seg_fore_dil_input")
        self.inst_seg_fore_dil_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_fore_dil_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_fore_dil_input, 5, 3, 1, 1)

        self.inst_seg_small_obj_fil_before_input = QComboBox(self.frame_43)
        self.inst_seg_small_obj_fil_before_input.addItem("")
        self.inst_seg_small_obj_fil_before_input.addItem("")
        self.inst_seg_small_obj_fil_before_input.setObjectName(u"inst_seg_small_obj_fil_before_input")
        self.inst_seg_small_obj_fil_before_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_before_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_small_obj_fil_before_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_before_input, 7, 3, 1, 1)

        self.inst_seg_save_water_files_label = QLabel(self.frame_43)
        self.inst_seg_save_water_files_label.setObjectName(u"inst_seg_save_water_files_label")
        self.inst_seg_save_water_files_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_save_water_files_label, 13, 1, 1, 1)

        self.inst_seg_fore_ero_input = QLineEdit(self.frame_43)
        self.inst_seg_fore_ero_input.setObjectName(u"inst_seg_fore_ero_input")
        self.inst_seg_fore_ero_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_fore_ero_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_fore_ero_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_fore_ero_input, 6, 3, 1, 1)

        self.inst_seg_small_obj_fil_before_label = QLabel(self.frame_43)
        self.inst_seg_small_obj_fil_before_label.setObjectName(u"inst_seg_small_obj_fil_before_label")
        self.inst_seg_small_obj_fil_before_label.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_small_obj_fil_before_label, 7, 1, 1, 1)

        self.inst_seg_moph_op_input = QLineEdit(self.frame_43)
        self.inst_seg_moph_op_input.setObjectName(u"inst_seg_moph_op_input")
        self.inst_seg_moph_op_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_moph_op_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_moph_op_input, 1, 3, 1, 1)

        self.inst_seg_save_water_files_input = QComboBox(self.frame_43)
        self.inst_seg_save_water_files_input.addItem("")
        self.inst_seg_save_water_files_input.addItem("")
        self.inst_seg_save_water_files_input.setObjectName(u"inst_seg_save_water_files_input")
        self.inst_seg_save_water_files_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_save_water_files_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_save_water_files_input.setFont(font)

        self.gridLayout_46.addWidget(self.inst_seg_save_water_files_input, 13, 3, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_47, 1, 4, 1, 1)


        self.gridLayout_44.addWidget(self.frame_43, 4, 0, 1, 1)

        self.label_97 = QLabel(self.scrollAreaWidgetContents_13)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font)

        self.gridLayout_44.addWidget(self.label_97, 5, 0, 1, 1)

        self.inst_seg_metrics_frame = QFrame(self.scrollAreaWidgetContents_13)
        self.inst_seg_metrics_frame.setObjectName(u"inst_seg_metrics_frame")
        self.inst_seg_metrics_frame.setMinimumSize(QSize(0, 0))
        self.inst_seg_metrics_frame.setStyleSheet(u"background: rgb(246,246,246);")
        self.inst_seg_metrics_frame.setFrameShape(QFrame.Box)
        self.inst_seg_metrics_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.inst_seg_metrics_frame)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.inst_seg_matching_stats_label = QLabel(self.inst_seg_metrics_frame)
        self.inst_seg_matching_stats_label.setObjectName(u"inst_seg_matching_stats_label")
        self.inst_seg_matching_stats_label.setFont(font)

        self.gridLayout_55.addWidget(self.inst_seg_matching_stats_label, 0, 0, 1, 1)

        self.inst_seg_matching_stats_ths_label = QLabel(self.inst_seg_metrics_frame)
        self.inst_seg_matching_stats_ths_label.setObjectName(u"inst_seg_matching_stats_ths_label")
        self.inst_seg_matching_stats_ths_label.setFont(font)

        self.gridLayout_55.addWidget(self.inst_seg_matching_stats_ths_label, 1, 0, 1, 1)

        self.inst_seg_matching_stats_colores_img_ths_label = QLabel(self.inst_seg_metrics_frame)
        self.inst_seg_matching_stats_colores_img_ths_label.setObjectName(u"inst_seg_matching_stats_colores_img_ths_label")
        self.inst_seg_matching_stats_colores_img_ths_label.setFont(font)

        self.gridLayout_55.addWidget(self.inst_seg_matching_stats_colores_img_ths_label, 2, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_55.addItem(self.verticalSpacer_26, 3, 0, 1, 1)

        self.inst_seg_matching_stats_input = QComboBox(self.inst_seg_metrics_frame)
        self.inst_seg_matching_stats_input.addItem("")
        self.inst_seg_matching_stats_input.addItem("")
        self.inst_seg_matching_stats_input.setObjectName(u"inst_seg_matching_stats_input")
        self.inst_seg_matching_stats_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_matching_stats_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_matching_stats_input.setFont(font)

        self.gridLayout_55.addWidget(self.inst_seg_matching_stats_input, 0, 1, 1, 1)

        self.inst_seg_matching_stats_ths_input = QLineEdit(self.inst_seg_metrics_frame)
        self.inst_seg_matching_stats_ths_input.setObjectName(u"inst_seg_matching_stats_ths_input")
        self.inst_seg_matching_stats_ths_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_matching_stats_ths_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_matching_stats_ths_input.setFont(font)

        self.gridLayout_55.addWidget(self.inst_seg_matching_stats_ths_input, 1, 1, 1, 1)

        self.inst_seg_matching_stats_colores_img_ths_input = QLineEdit(self.inst_seg_metrics_frame)
        self.inst_seg_matching_stats_colores_img_ths_input.setObjectName(u"inst_seg_matching_stats_colores_img_ths_input")
        self.inst_seg_matching_stats_colores_img_ths_input.setMinimumSize(QSize(200, 30))
        self.inst_seg_matching_stats_colores_img_ths_input.setMaximumSize(QSize(200, 30))
        self.inst_seg_matching_stats_colores_img_ths_input.setFont(font)

        self.gridLayout_55.addWidget(self.inst_seg_matching_stats_colores_img_ths_input, 2, 1, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_49, 1, 2, 1, 1)


        self.gridLayout_44.addWidget(self.inst_seg_metrics_frame, 8, 0, 1, 1)

        self.inst_seg_metrics_label = QLabel(self.scrollAreaWidgetContents_13)
        self.inst_seg_metrics_label.setObjectName(u"inst_seg_metrics_label")
        self.inst_seg_metrics_label.setFont(font)

        self.gridLayout_44.addWidget(self.inst_seg_metrics_label, 7, 0, 1, 1)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_16.addWidget(self.scrollArea_9)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_instance_seg_page)
        self.test_workflow_specific_tab_detection_page = QWidget()
        self.test_workflow_specific_tab_detection_page.setObjectName(u"test_workflow_specific_tab_detection_page")
        self.verticalLayout_17 = QVBoxLayout(self.test_workflow_specific_tab_detection_page)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10 = QScrollArea(self.test_workflow_specific_tab_detection_page)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 913, 732))
        self.gridLayout_47 = QGridLayout(self.scrollAreaWidgetContents_14)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.label_100 = QLabel(self.scrollAreaWidgetContents_14)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font)

        self.gridLayout_47.addWidget(self.label_100, 2, 0, 1, 1)

        self.frame_51 = QFrame(self.scrollAreaWidgetContents_14)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_51.setFrameShape(QFrame.Box)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_51)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.label_108 = QLabel(self.frame_51)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setFont(font)

        self.gridLayout_59.addWidget(self.label_108, 5, 0, 1, 1)

        self.det_circularity_filtering_input = QLineEdit(self.frame_51)
        self.det_circularity_filtering_input.setObjectName(u"det_circularity_filtering_input")
        self.det_circularity_filtering_input.setMinimumSize(QSize(200, 30))
        self.det_circularity_filtering_input.setMaximumSize(QSize(200, 30))
        self.det_circularity_filtering_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_circularity_filtering_input, 5, 1, 1, 1)

        self.det_watershed_input = QComboBox(self.frame_51)
        self.det_watershed_input.addItem("")
        self.det_watershed_input.addItem("")
        self.det_watershed_input.setObjectName(u"det_watershed_input")
        self.det_watershed_input.setMinimumSize(QSize(200, 30))
        self.det_watershed_input.setMaximumSize(QSize(200, 30))
        self.det_watershed_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_input, 8, 1, 1, 1)

        self.det_watershed_label = QLabel(self.frame_51)
        self.det_watershed_label.setObjectName(u"det_watershed_label")
        self.det_watershed_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_label, 8, 0, 1, 1)

        self.det_watershed_first_dilation_label = QLabel(self.frame_51)
        self.det_watershed_first_dilation_label.setObjectName(u"det_watershed_first_dilation_label")
        self.det_watershed_first_dilation_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_first_dilation_label, 9, 0, 1, 1)

        self.det_watershed_donuts_patch_label = QLabel(self.frame_51)
        self.det_watershed_donuts_patch_label.setObjectName(u"det_watershed_donuts_patch_label")
        self.det_watershed_donuts_patch_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_donuts_patch_label, 11, 0, 1, 1)

        self.det_watershed_donuts_classes_label = QLabel(self.frame_51)
        self.det_watershed_donuts_classes_label.setObjectName(u"det_watershed_donuts_classes_label")
        self.det_watershed_donuts_classes_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_donuts_classes_label, 10, 0, 1, 1)

        self.det_watershed_donuts_nucleus_diam_label = QLabel(self.frame_51)
        self.det_watershed_donuts_nucleus_diam_label.setObjectName(u"det_watershed_donuts_nucleus_diam_label")
        self.det_watershed_donuts_nucleus_diam_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_donuts_nucleus_diam_label, 12, 0, 1, 1)

        self.det_watershed_first_dilation_input = QLineEdit(self.frame_51)
        self.det_watershed_first_dilation_input.setObjectName(u"det_watershed_first_dilation_input")
        self.det_watershed_first_dilation_input.setMinimumSize(QSize(200, 30))
        self.det_watershed_first_dilation_input.setMaximumSize(QSize(200, 30))
        self.det_watershed_first_dilation_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_first_dilation_input, 9, 1, 1, 1)

        self.det_watershed_donuts_classes_input = QLineEdit(self.frame_51)
        self.det_watershed_donuts_classes_input.setObjectName(u"det_watershed_donuts_classes_input")
        self.det_watershed_donuts_classes_input.setMinimumSize(QSize(200, 30))
        self.det_watershed_donuts_classes_input.setMaximumSize(QSize(200, 30))
        self.det_watershed_donuts_classes_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_donuts_classes_input, 10, 1, 1, 1)

        self.det_watershed_donuts_patch_input = QLineEdit(self.frame_51)
        self.det_watershed_donuts_patch_input.setObjectName(u"det_watershed_donuts_patch_input")
        self.det_watershed_donuts_patch_input.setMinimumSize(QSize(200, 30))
        self.det_watershed_donuts_patch_input.setMaximumSize(QSize(200, 30))
        self.det_watershed_donuts_patch_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_donuts_patch_input, 11, 1, 1, 1)

        self.det_watershed_donuts_nucleus_diam_input = QLineEdit(self.frame_51)
        self.det_watershed_donuts_nucleus_diam_input.setObjectName(u"det_watershed_donuts_nucleus_diam_input")
        self.det_watershed_donuts_nucleus_diam_input.setMinimumSize(QSize(200, 30))
        self.det_watershed_donuts_nucleus_diam_input.setMaximumSize(QSize(200, 30))
        self.det_watershed_donuts_nucleus_diam_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_watershed_donuts_nucleus_diam_input, 12, 1, 1, 1)

        self.det_z_filtering_label = QLabel(self.frame_51)
        self.det_z_filtering_label.setObjectName(u"det_z_filtering_label")
        self.det_z_filtering_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_z_filtering_label, 2, 0, 1, 1)

        self.det_yz_filtering_label = QLabel(self.frame_51)
        self.det_yz_filtering_label.setObjectName(u"det_yz_filtering_label")
        self.det_yz_filtering_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_yz_filtering_label, 0, 0, 1, 1)

        self.det_z_filtering_input = QComboBox(self.frame_51)
        self.det_z_filtering_input.addItem("")
        self.det_z_filtering_input.addItem("")
        self.det_z_filtering_input.setObjectName(u"det_z_filtering_input")
        self.det_z_filtering_input.setMinimumSize(QSize(200, 30))
        self.det_z_filtering_input.setMaximumSize(QSize(200, 30))
        self.det_z_filtering_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_z_filtering_input, 2, 1, 1, 1)

        self.det_yz_filtering_input = QComboBox(self.frame_51)
        self.det_yz_filtering_input.addItem("")
        self.det_yz_filtering_input.addItem("")
        self.det_yz_filtering_input.setObjectName(u"det_yz_filtering_input")
        self.det_yz_filtering_input.setMinimumSize(QSize(200, 30))
        self.det_yz_filtering_input.setMaximumSize(QSize(200, 30))
        self.det_yz_filtering_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_yz_filtering_input, 0, 1, 1, 1)

        self.det_z_filtering_size_input = QLineEdit(self.frame_51)
        self.det_z_filtering_size_input.setObjectName(u"det_z_filtering_size_input")
        self.det_z_filtering_size_input.setMinimumSize(QSize(200, 30))
        self.det_z_filtering_size_input.setMaximumSize(QSize(200, 30))
        self.det_z_filtering_size_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_z_filtering_size_input, 3, 1, 1, 1)

        self.det_z_filtering_size_label = QLabel(self.frame_51)
        self.det_z_filtering_size_label.setObjectName(u"det_z_filtering_size_label")
        self.det_z_filtering_size_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_z_filtering_size_label, 3, 0, 1, 1)

        self.det_yz_filtering_size_input = QLineEdit(self.frame_51)
        self.det_yz_filtering_size_input.setObjectName(u"det_yz_filtering_size_input")
        self.det_yz_filtering_size_input.setMinimumSize(QSize(200, 30))
        self.det_yz_filtering_size_input.setMaximumSize(QSize(200, 30))
        self.det_yz_filtering_size_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_yz_filtering_size_input, 1, 1, 1, 1)

        self.det_yz_filtering_size_label = QLabel(self.frame_51)
        self.det_yz_filtering_size_label.setObjectName(u"det_yz_filtering_size_label")
        self.det_yz_filtering_size_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_yz_filtering_size_label, 1, 0, 1, 1)

        self.det_remove_close_points_radius_input = QLineEdit(self.frame_51)
        self.det_remove_close_points_radius_input.setObjectName(u"det_remove_close_points_radius_input")
        self.det_remove_close_points_radius_input.setMinimumSize(QSize(200, 30))
        self.det_remove_close_points_radius_input.setMaximumSize(QSize(200, 30))
        self.det_remove_close_points_radius_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_remove_close_points_radius_input, 7, 1, 1, 1)

        self.det_remove_close_points_label = QLabel(self.frame_51)
        self.det_remove_close_points_label.setObjectName(u"det_remove_close_points_label")
        self.det_remove_close_points_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_remove_close_points_label, 6, 0, 1, 1)

        self.det_remove_close_points_radius_label = QLabel(self.frame_51)
        self.det_remove_close_points_radius_label.setObjectName(u"det_remove_close_points_radius_label")
        self.det_remove_close_points_radius_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_remove_close_points_radius_label, 7, 0, 1, 1)

        self.det_remove_close_points_input = QComboBox(self.frame_51)
        self.det_remove_close_points_input.addItem("")
        self.det_remove_close_points_input.addItem("")
        self.det_remove_close_points_input.setObjectName(u"det_remove_close_points_input")
        self.det_remove_close_points_input.setMinimumSize(QSize(200, 30))
        self.det_remove_close_points_input.setMaximumSize(QSize(200, 30))
        self.det_remove_close_points_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_remove_close_points_input, 6, 1, 1, 1)

        self.det_data_watetshed_check_label = QLabel(self.frame_51)
        self.det_data_watetshed_check_label.setObjectName(u"det_data_watetshed_check_label")
        self.det_data_watetshed_check_label.setFont(font)

        self.gridLayout_59.addWidget(self.det_data_watetshed_check_label, 13, 0, 1, 1)

        self.det_data_watetshed_check_input = QComboBox(self.frame_51)
        self.det_data_watetshed_check_input.addItem("")
        self.det_data_watetshed_check_input.addItem("")
        self.det_data_watetshed_check_input.setObjectName(u"det_data_watetshed_check_input")
        self.det_data_watetshed_check_input.setMinimumSize(QSize(200, 30))
        self.det_data_watetshed_check_input.setMaximumSize(QSize(200, 30))
        self.det_data_watetshed_check_input.setFont(font)

        self.gridLayout_59.addWidget(self.det_data_watetshed_check_input, 13, 1, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_59.addItem(self.horizontalSpacer_50, 0, 2, 1, 1)


        self.gridLayout_47.addWidget(self.frame_51, 3, 0, 1, 1)

        self.label_104 = QLabel(self.scrollAreaWidgetContents_14)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font)

        self.gridLayout_47.addWidget(self.label_104, 0, 0, 1, 1)

        self.det_metrics_label = QLabel(self.scrollAreaWidgetContents_14)
        self.det_metrics_label.setObjectName(u"det_metrics_label")
        self.det_metrics_label.setFont(font)

        self.gridLayout_47.addWidget(self.det_metrics_label, 4, 0, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_39, 0, 1, 1, 1)

        self.det_metrics_frame = QFrame(self.scrollAreaWidgetContents_14)
        self.det_metrics_frame.setObjectName(u"det_metrics_frame")
        self.det_metrics_frame.setStyleSheet(u"background: rgb(246,246,246);")
        self.det_metrics_frame.setFrameShape(QFrame.Box)
        self.det_metrics_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.det_metrics_frame)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.det_tolerance_label = QLabel(self.det_metrics_frame)
        self.det_tolerance_label.setObjectName(u"det_tolerance_label")
        self.det_tolerance_label.setFont(font)

        self.gridLayout_41.addWidget(self.det_tolerance_label, 0, 0, 1, 1)

        self.det_tolerance_input = QLineEdit(self.det_metrics_frame)
        self.det_tolerance_input.setObjectName(u"det_tolerance_input")
        self.det_tolerance_input.setMinimumSize(QSize(200, 30))
        self.det_tolerance_input.setMaximumSize(QSize(200, 30))
        self.det_tolerance_input.setFont(font)

        self.gridLayout_41.addWidget(self.det_tolerance_input, 0, 1, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_52, 0, 2, 1, 1)


        self.gridLayout_47.addWidget(self.det_metrics_frame, 5, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_47.addItem(self.verticalSpacer_20, 6, 0, 1, 1)

        self.frame_54 = QFrame(self.scrollAreaWidgetContents_14)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background: rgb(246,246,246);")
        self.frame_54.setFrameShape(QFrame.Box)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_54)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.det_local_max_coords_label = QLabel(self.frame_54)
        self.det_local_max_coords_label.setObjectName(u"det_local_max_coords_label")
        self.det_local_max_coords_label.setFont(font)

        self.gridLayout_62.addWidget(self.det_local_max_coords_label, 0, 0, 1, 1)

        self.det_min_th_to_be_peak_input = QLineEdit(self.frame_54)
        self.det_min_th_to_be_peak_input.setObjectName(u"det_min_th_to_be_peak_input")
        self.det_min_th_to_be_peak_input.setMinimumSize(QSize(200, 30))
        self.det_min_th_to_be_peak_input.setMaximumSize(QSize(200, 30))
        self.det_min_th_to_be_peak_input.setFont(font)

        self.gridLayout_62.addWidget(self.det_min_th_to_be_peak_input, 1, 1, 1, 1)

        self.det_min_th_to_be_peak_label = QLabel(self.frame_54)
        self.det_min_th_to_be_peak_label.setObjectName(u"det_min_th_to_be_peak_label")
        self.det_min_th_to_be_peak_label.setFont(font)

        self.gridLayout_62.addWidget(self.det_min_th_to_be_peak_label, 1, 0, 1, 1)

        self.det_local_max_coords_input = QComboBox(self.frame_54)
        self.det_local_max_coords_input.addItem("")
        self.det_local_max_coords_input.addItem("")
        self.det_local_max_coords_input.setObjectName(u"det_local_max_coords_input")
        self.det_local_max_coords_input.setMinimumSize(QSize(200, 30))
        self.det_local_max_coords_input.setMaximumSize(QSize(200, 30))
        self.det_local_max_coords_input.setFont(font)

        self.gridLayout_62.addWidget(self.det_local_max_coords_input, 0, 1, 1, 1)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_62.addItem(self.horizontalSpacer_61, 0, 2, 1, 1)


        self.gridLayout_47.addWidget(self.frame_54, 1, 0, 1, 1)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_17.addWidget(self.scrollArea_10)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_detection_page)
        self.test_workflow_specific_tab_denoising_page = QWidget()
        self.test_workflow_specific_tab_denoising_page.setObjectName(u"test_workflow_specific_tab_denoising_page")
        self.verticalLayout_18 = QVBoxLayout(self.test_workflow_specific_tab_denoising_page)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_11 = QScrollArea(self.test_workflow_specific_tab_denoising_page)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 927, 354))
        self.gridLayout_64 = QGridLayout(self.scrollAreaWidgetContents_15)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_64.addItem(self.verticalSpacer_27, 1, 0, 1, 1)

        self.label_93 = QLabel(self.scrollAreaWidgetContents_15)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font)

        self.gridLayout_64.addWidget(self.label_93, 0, 0, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_64.addItem(self.horizontalSpacer_45, 0, 1, 1, 1)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_15)

        self.verticalLayout_18.addWidget(self.scrollArea_11)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_denoising_page)
        self.test_workflow_specific_tab_sr_page = QWidget()
        self.test_workflow_specific_tab_sr_page.setObjectName(u"test_workflow_specific_tab_sr_page")
        self.verticalLayout_19 = QVBoxLayout(self.test_workflow_specific_tab_sr_page)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_12 = QScrollArea(self.test_workflow_specific_tab_sr_page)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 927, 354))
        self.gridLayout_65 = QGridLayout(self.scrollAreaWidgetContents_16)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.label_102 = QLabel(self.scrollAreaWidgetContents_16)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font)

        self.gridLayout_65.addWidget(self.label_102, 0, 0, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(540, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_65.addItem(self.horizontalSpacer_58, 0, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_65.addItem(self.verticalSpacer_28, 1, 0, 1, 1)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_16)

        self.verticalLayout_19.addWidget(self.scrollArea_12)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_sr_page)
        self.test_workflow_specific_tab_ssl_page = QWidget()
        self.test_workflow_specific_tab_ssl_page.setObjectName(u"test_workflow_specific_tab_ssl_page")
        self.verticalLayout_20 = QVBoxLayout(self.test_workflow_specific_tab_ssl_page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_13 = QScrollArea(self.test_workflow_specific_tab_ssl_page)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 927, 354))
        self.gridLayout_66 = QGridLayout(self.scrollAreaWidgetContents_17)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.label_106 = QLabel(self.scrollAreaWidgetContents_17)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font)

        self.gridLayout_66.addWidget(self.label_106, 0, 0, 1, 1)

        self.horizontalSpacer_59 = QSpacerItem(487, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_66.addItem(self.horizontalSpacer_59, 0, 1, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_66.addItem(self.verticalSpacer_29, 1, 0, 1, 1)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_20.addWidget(self.scrollArea_13)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_ssl_page)
        self.test_workflow_specific_tab_classification_page = QWidget()
        self.test_workflow_specific_tab_classification_page.setObjectName(u"test_workflow_specific_tab_classification_page")
        self.verticalLayout_21 = QVBoxLayout(self.test_workflow_specific_tab_classification_page)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_14 = QScrollArea(self.test_workflow_specific_tab_classification_page)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 927, 354))
        self.gridLayout_67 = QGridLayout(self.scrollAreaWidgetContents_18)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.label_111 = QLabel(self.scrollAreaWidgetContents_18)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font)

        self.gridLayout_67.addWidget(self.label_111, 0, 0, 1, 1)

        self.horizontalSpacer_60 = QSpacerItem(566, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_67.addItem(self.horizontalSpacer_60, 0, 1, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_67.addItem(self.verticalSpacer_30, 1, 0, 1, 1)

        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_18)

        self.verticalLayout_21.addWidget(self.scrollArea_14)

        self.test_workflow_specific_tab_stackedWidget.addWidget(self.test_workflow_specific_tab_classification_page)

        self.verticalLayout_11.addWidget(self.test_workflow_specific_tab_stackedWidget)

        self.test_tab_widget.addTab(self.test_workflow_specific_tab, "")

        self.gridLayout_36.addWidget(self.test_tab_widget, 2, 0, 1, 2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_12, 1, 0, 1, 1)

        self.stackedWidget_create_yaml_frame.addWidget(self.test_page)

        self.verticalLayout_7.addWidget(self.stackedWidget_create_yaml_frame)

        self.page_create_yaml_bottom_frame = QFrame(self.page_create_yaml_frame)
        self.page_create_yaml_bottom_frame.setObjectName(u"page_create_yaml_bottom_frame")
        self.page_create_yaml_bottom_frame.setMinimumSize(QSize(0, 103))
        self.page_create_yaml_bottom_frame.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamily(u"DejaVu Math TeX Gyre")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.page_create_yaml_bottom_frame.setFont(font4)
        self.page_create_yaml_bottom_frame.setFrameShape(QFrame.NoFrame)
        self.page_create_yaml_bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.page_create_yaml_bottom_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 35, 0, 0)
        self.frame_20 = QFrame(self.page_create_yaml_bottom_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFont(font)
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.back_bn = QPushButton(self.frame_20)
        self.back_bn.setObjectName(u"back_bn")
        self.back_bn.setGeometry(QRect(0, 0, 91, 23))
        self.back_bn.setFont(font)
        self.back_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"images/bn_images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_bn.setIcon(icon11)
        self.back_bn.setIconSize(QSize(80, 12))

        self.horizontalLayout_8.addWidget(self.frame_20)

        self.frame_23 = QFrame(self.page_create_yaml_bottom_frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFont(font)
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_23)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.continue_bn = QPushButton(self.frame_23)
        self.continue_bn.setObjectName(u"continue_bn")
        self.continue_bn.setMinimumSize(QSize(0, 0))
        self.continue_bn.setMaximumSize(QSize(200, 77))
        font5 = QFont()
        font5.setFamily(u"DejaVu Math TeX Gyre")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        self.continue_bn.setFont(font5)
        self.continue_bn.setStyleSheet(u"QPushButton {\n"
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
        self.continue_bn.setIconSize(QSize(160, 33))
        self.continue_bn.setAutoRepeat(False)
        self.continue_bn.setFlat(False)

        self.gridLayout_7.addWidget(self.continue_bn, 0, 0, 1, 1)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFont(font)
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 10, 0, 4)
        self.frame_9 = QFrame(self.frame_24)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(30, 16777215))
        self.frame_9.setFont(font)
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_9)

        self.window1_bn = QPushButton(self.frame_24)
        self.window1_bn.setObjectName(u"window1_bn")
        self.window1_bn.setMaximumSize(QSize(20, 16777215))
        self.window1_bn.setFont(font)
        self.window1_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"images/bn_images/dot_enable.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.window1_bn.setIcon(icon12)
        self.window1_bn.setIconSize(QSize(12, 12))

        self.horizontalLayout_11.addWidget(self.window1_bn)

        self.window2_bn = QPushButton(self.frame_24)
        self.window2_bn.setObjectName(u"window2_bn")
        self.window2_bn.setMaximumSize(QSize(20, 16777215))
        self.window2_bn.setFont(font)
        self.window2_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"images/bn_images/dot_disable.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.window2_bn.setIcon(icon13)
        self.window2_bn.setIconSize(QSize(12, 12))

        self.horizontalLayout_11.addWidget(self.window2_bn)

        self.window3_bn = QPushButton(self.frame_24)
        self.window3_bn.setObjectName(u"window3_bn")
        self.window3_bn.setMinimumSize(QSize(0, 0))
        self.window3_bn.setMaximumSize(QSize(20, 16777215))
        self.window3_bn.setFont(font)
        self.window3_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        self.window3_bn.setIcon(icon13)
        self.window3_bn.setIconSize(QSize(12, 12))
        self.window3_bn.setAutoRepeatInterval(100)

        self.horizontalLayout_11.addWidget(self.window3_bn)

        self.window4_bn = QPushButton(self.frame_24)
        self.window4_bn.setObjectName(u"window4_bn")
        self.window4_bn.setMaximumSize(QSize(20, 16777215))
        self.window4_bn.setFont(font)
        self.window4_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")
        self.window4_bn.setIcon(icon13)
        self.window4_bn.setIconSize(QSize(12, 12))

        self.horizontalLayout_11.addWidget(self.window4_bn)

        self.frame_10 = QFrame(self.frame_24)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(30, 16777215))
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_10)


        self.gridLayout_7.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_24.raise_()
        self.continue_bn.raise_()

        self.horizontalLayout_8.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.page_create_yaml_bottom_frame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setFont(font)
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_22)


        self.verticalLayout_7.addWidget(self.page_create_yaml_bottom_frame)


        self.horizontalLayout_19.addWidget(self.page_create_yaml_frame)

        self.stackedWidget.addWidget(self.page_create_yaml)
        self.page_run_biapy = QWidget()
        self.page_run_biapy.setObjectName(u"page_run_biapy")
        self.page_run_biapy.setStyleSheet(u"background:rgb(255,255,255);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_run_biapy)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_run_biapy)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_72 = QGridLayout(self.frame_7)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setVerticalSpacing(40)
        self.gridLayout_72.setContentsMargins(9, 9, 9, 9)
        self.frame_56 = QFrame(self.frame_7)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 150))
        self.frame_56.setMaximumSize(QSize(16777215, 250))
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.gridLayout_70 = QGridLayout(self.frame_56)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setContentsMargins(-1, 40, -1, -1)
        self.run_biapy_docker_bn = QPushButton(self.frame_56)
        self.run_biapy_docker_bn.setObjectName(u"run_biapy_docker_bn")
        self.run_biapy_docker_bn.setMinimumSize(QSize(300, 40))
        self.run_biapy_docker_bn.setMaximumSize(QSize(300, 16777215))
        font6 = QFont()
        font6.setFamily(u"DejaVu Math TeX Gyre")
        font6.setPointSize(20)
        self.run_biapy_docker_bn.setFont(font6)
        self.run_biapy_docker_bn.setStyleSheet(u"QPushButton {\n"
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
        self.run_biapy_docker_bn.setIconSize(QSize(250, 33))

        self.gridLayout_70.addWidget(self.run_biapy_docker_bn, 0, 0, 1, 1)


        self.gridLayout_72.addWidget(self.frame_56, 2, 1, 1, 1)

        self.yaml_errors_frame = QFrame(self.frame_7)
        self.yaml_errors_frame.setObjectName(u"yaml_errors_frame")
        self.yaml_errors_frame.setMinimumSize(QSize(0, 0))
        self.yaml_errors_frame.setMaximumSize(QSize(16777215, 16777215))
        self.yaml_errors_frame.setFrameShape(QFrame.NoFrame)
        self.yaml_errors_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_73 = QGridLayout(self.yaml_errors_frame)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setVerticalSpacing(9)
        self.gridLayout_73.setContentsMargins(9, 9, 9, 0)
        self.frame_57 = QFrame(self.yaml_errors_frame)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_57)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_57)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.check_yaml_file_bn = QPushButton(self.frame_47)
        self.check_yaml_file_bn.setObjectName(u"check_yaml_file_bn")
        self.check_yaml_file_bn.setMinimumSize(QSize(200, 40))
        self.check_yaml_file_bn.setMaximumSize(QSize(100, 16777215))
        self.check_yaml_file_bn.setFont(font)
        self.check_yaml_file_bn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.check_yaml_file_bn)


        self.gridLayout_39.addWidget(self.frame_47, 0, 0, 1, 1)

        self.check_yaml_file_errors_frame = QScrollArea(self.frame_57)
        self.check_yaml_file_errors_frame.setObjectName(u"check_yaml_file_errors_frame")
        self.check_yaml_file_errors_frame.setFont(font)
        self.check_yaml_file_errors_frame.setFrameShape(QFrame.Box)
        self.check_yaml_file_errors_frame.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 889, 104))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_19)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.check_yaml_file_errors_label = QLabel(self.scrollAreaWidgetContents_19)
        self.check_yaml_file_errors_label.setObjectName(u"check_yaml_file_errors_label")
        self.check_yaml_file_errors_label.setFont(font)
        self.check_yaml_file_errors_label.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.check_yaml_file_errors_label)

        self.check_yaml_file_errors_frame.setWidget(self.scrollAreaWidgetContents_19)

        self.gridLayout_39.addWidget(self.check_yaml_file_errors_frame, 2, 0, 1, 1)


        self.gridLayout_73.addWidget(self.frame_57, 1, 1, 1, 1)

        self.check_yaml_file_errors_frame_main = QFrame(self.yaml_errors_frame)
        self.check_yaml_file_errors_frame_main.setObjectName(u"check_yaml_file_errors_frame_main")
        self.check_yaml_file_errors_frame_main.setFrameShape(QFrame.NoFrame)
        self.check_yaml_file_errors_frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.check_yaml_file_errors_frame_main)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_73.addWidget(self.check_yaml_file_errors_frame_main, 2, 2, 1, 2)


        self.gridLayout_72.addWidget(self.yaml_errors_frame, 1, 1, 1, 1)

        self.frame_27 = QFrame(self.frame_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setMaximumSize(QSize(16777215, 120))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_27)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, -1, 9, -1)
        self.label_138 = QLabel(self.frame_27)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font)

        self.gridLayout_9.addWidget(self.label_138, 1, 0, 1, 1)

        self.examine_yaml_bn = QPushButton(self.frame_27)
        self.examine_yaml_bn.setObjectName(u"examine_yaml_bn")
        self.examine_yaml_bn.setFont(font)

        self.gridLayout_9.addWidget(self.examine_yaml_bn, 0, 3, 1, 1)

        self.output_folder_label = QLabel(self.frame_27)
        self.output_folder_label.setObjectName(u"output_folder_label")
        self.output_folder_label.setMaximumSize(QSize(16777215, 35))
        self.output_folder_label.setFont(font)

        self.gridLayout_9.addWidget(self.output_folder_label, 2, 0, 1, 2)

        self.select_yaml_label = QLabel(self.frame_27)
        self.select_yaml_label.setObjectName(u"select_yaml_label")
        self.select_yaml_label.setFont(font)

        self.gridLayout_9.addWidget(self.select_yaml_label, 0, 0, 1, 2)

        self.select_yaml_name_label = QTextBrowser(self.frame_27)
        self.select_yaml_name_label.setObjectName(u"select_yaml_name_label")
        self.select_yaml_name_label.setMinimumSize(QSize(0, 30))
        self.select_yaml_name_label.setMaximumSize(QSize(500, 30))
        self.select_yaml_name_label.setFont(font)
        self.select_yaml_name_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.select_yaml_name_label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.select_yaml_name_label.setLineWrapMode(QTextEdit.NoWrap)
        self.select_yaml_name_label.setReadOnly(False)

        self.gridLayout_9.addWidget(self.select_yaml_name_label, 0, 2, 1, 1)

        self.output_folder_input = QTextBrowser(self.frame_27)
        self.output_folder_input.setObjectName(u"output_folder_input")
        self.output_folder_input.setMinimumSize(QSize(0, 30))
        self.output_folder_input.setMaximumSize(QSize(500, 30))
        self.output_folder_input.setFont(font)
        self.output_folder_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.output_folder_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.output_folder_input.setLineWrapMode(QTextEdit.NoWrap)
        self.output_folder_input.setReadOnly(False)

        self.gridLayout_9.addWidget(self.output_folder_input, 2, 2, 1, 1)

        self.job_name_input = QPlainTextEdit(self.frame_27)
        self.job_name_input.setObjectName(u"job_name_input")
        self.job_name_input.setMinimumSize(QSize(0, 30))
        self.job_name_input.setMaximumSize(QSize(500, 30))
        self.job_name_input.setFont(font)
        self.job_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.job_name_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.job_name_input.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout_9.addWidget(self.job_name_input, 1, 2, 1, 1)

        self.output_folder_bn = QPushButton(self.frame_27)
        self.output_folder_bn.setObjectName(u"output_folder_bn")
        self.output_folder_bn.setMaximumSize(QSize(130, 16777215))
        self.output_folder_bn.setFont(font)

        self.gridLayout_9.addWidget(self.output_folder_bn, 2, 3, 1, 1)


        self.gridLayout_72.addWidget(self.frame_27, 0, 1, 1, 1)


        self.horizontalLayout_29.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_run_biapy)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_bottom_east)


        self.horizontalLayout.addWidget(self.frame_east)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_create_yaml_frame.setCurrentIndex(0)
        self.train_tab_widget.setCurrentIndex(0)
        self.train_workflow_specific_tab_stackedWidget.setCurrentIndex(0)
        self.test_tab_widget.setCurrentIndex(0)
        self.test_workflow_specific_tab_stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.biapy_logo_label.setText("")
        self.biapy_version.setText(QCoreApplication.translate("MainWindow", u"BiaPy GUI - Version 1.0", None))
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_workflow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_workflow.setText("")
#if QT_CONFIG(tooltip)
        self.bn_goptions.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_goptions.setText("")
#if QT_CONFIG(tooltip)
        self.bn_train.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_train.setText("")
#if QT_CONFIG(tooltip)
        self.bn_test.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_test.setText("")
#if QT_CONFIG(tooltip)
        self.bn_run_biapy.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_run_biapy.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
        self.biapy_title_label.setText(QCoreApplication.translate("MainWindow", u"BiaPy: Bioimage analysis pipelines in Python", None))
        self.biapy_description_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/danifranco/BiaPy\"><span style=\" text-decoration: underline; color:#0000ff;\">BiaPy</span></a> is an open source Python library for building bioimage analysis pipelines, also called workflows. This repository is actively under development by the Biomedical Computer Vision group at the <a href=\"https://github.com/danifranco/BiaPy\"><span style=\" text-decoration: underline; color:#0000ff;\">University of the Basque Country </span></a>and the <a href=\"http://dipc.ehu.es/\"><span style=\" text-decoration: underline; color:#0000ff;\">Donostia International Physics Center</span></a>. The library provides an easy way to create image processing pipelines that are commonly used in the analysis of biology microscopy images in 2D and 3D. Specifically, BiaPy contains ready-to-use solutions for tasks such as <a href=\"https://biapy.readthedocs.io/en/latest/workflows/semantic_segmentation.html\"><span style=\" text-decoration: underline; color:#0000ff;\">semantic segmen"
                        "tation</span></a>, <a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html\"><span style=\" text-decoration: underline; color:#0000ff;\">instance segmentation</span></a>, <a href=\"https://biapy.readthedocs.io/en/latest/workflows/detection.html\"><span style=\" text-decoration: underline; color:#0000ff;\">object detection</span></a>, <a href=\"https://biapy.readthedocs.io/en/latest/workflows/denoising.html\"><span style=\" text-decoration: underline; color:#0000ff;\">image denoising</span></a>, <a href=\"https://biapy.readthedocs.io/en/latest/workflows/super_resolution.html\"><span style=\" text-decoration: underline; color:#0000ff;\">single image super-resolution</span></a>, <a href=\"https://biapy.readthedocs.io/en/latest/workflows/self_supervision.html\"><span style=\" text-decoration: underline; color:#0000ff;\">self-supervised learning</span></a> and <a href=\"https://biapy.readthedocs.io/en/latest/workflows/classification.html\"><span style=\" text-decoration: underline; col"
                        "or:#0000ff;\">image classification</span></a>. The source code is based on Keras/TensorFlow as the backend. As BiaPy\u2019s core is based on deep learning, it is recommended to use a machine with a graphics processing unit (GPU) for faster training and execution.</p></body></html>", None))
        self.docker_status_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.dependencies_label.setText(QCoreApplication.translate("MainWindow", u"Dependency error", None))
        self.docker_logo.setText("")
        self.create_yaml_bn.setText(QCoreApplication.translate("MainWindow", u"Create new YAML file", None))
        self.continue_yaml_bn.setText(QCoreApplication.translate("MainWindow", u"Continue with my own YAML file", None))
        self.left_arrow_bn.setText("")
        self.workflow_view1_label.setText("")
        self.workflow_view1_seemore_bn.setText(QCoreApplication.translate("MainWindow", u"See more . . .", None))
        self.workflow_view1_name_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.workflow_view2_label.setText("")
        self.workflow_view2_seemore_bn.setText(QCoreApplication.translate("MainWindow", u"See more . . .", None))
        self.workflow_view2_name_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.workflow_view3_label.setText("")
        self.workflow_view3_seemore_bn.setText(QCoreApplication.translate("MainWindow", u"See more . . .", None))
        self.workflow_view3_name_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.right_arrow_bn.setText("")
#if QT_CONFIG(tooltip)
        self.goptions_scrollArea.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.goptions_advanced_label.setText(QCoreApplication.translate("MainWindow", u"Advanced options", None))
        self.goptions_advanced_bn.setText("")
#if QT_CONFIG(tooltip)
        self.label_148.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Load previous training weigths (needed for test/inference phase or to train again but not from scratch). If the checkpoint file is empty, BiaPy will search for the checkpoint in the following manner: if the output folder and the job name match, BiaPy will locate the model's weights within the 'checkpoints' directory. On the other hand, if the checkpoint file path is specified that path will be used instead</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Load checkpoint", None))
        self.checkpoint_load_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.checkpoint_load_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.checkpoint_file_path_browse_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the model's checkpoint that will be loaded. Leave it blank to let BiaPy find it. If the output folder and the job name match, BiaPy will locate the model's weights within the 'checkpoints' directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkpoint_file_path_browse_label.setText(QCoreApplication.translate("MainWindow", u"Checkpoint file", None))
        self.checkpoint_file_path_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.train_disable_checkpoint_label.setText(QCoreApplication.translate("MainWindow", u"Checkpoint configuration", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">IDs of the GPU to run the job in. If you want to use more than one GPU add them sepated by commas. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">0,1,2,3 </span><span style=\" font-size:12pt;\">to use 4 GPUs</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"GPUs", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maximum number of CPU that BiaPy will be allowed to use. Set it to &quot;-1&quot; to set any limit. Normally a few cores will be used in this last case, as the biggest calculations will be on the GPU.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Max. CPUs", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Math seed to use. </span><span style=\" font-size:12pt; font-weight:600;\">Must be an integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.gpu_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.seed_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.goptions_browse_yaml_path_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.goptions_yaml_name_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.dimensions_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2D", None))
        self.dimensions_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"3D", None))

#if QT_CONFIG(tooltip)
        self.dimension_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of dimensions of the problem</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dimension_label.setText(QCoreApplication.translate("MainWindow", u"Dimensions", None))
#if QT_CONFIG(tooltip)
        self.goptions_yaml_name_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">YAML file name</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.goptions_yaml_name_label.setText(QCoreApplication.translate("MainWindow", u"YAML name", None))
#if QT_CONFIG(tooltip)
        self.goptions_browse_yaml_path_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to store the YAML file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.goptions_browse_yaml_path_label.setText(QCoreApplication.translate("MainWindow", u"YAML file path", None))
#if QT_CONFIG(tooltip)
        self.label_49.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to enable the training phase or not</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Enable train phase", None))
        self.enable_train_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.enable_train_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Data augmentation", None))
        self.da_enable_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_enable_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_elastic_mode_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Parameter that defines the handling of newly created pixels with the elastic transformation. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_elastic_mode_label.setText(QCoreApplication.translate("MainWindow", u"Elastic mode", None))
#if QT_CONFIG(tooltip)
        self.label_68.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable horizontal flip as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Horizontal flip", None))
#if QT_CONFIG(tooltip)
        self.da_contrast_em_mode_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">If apply the same contrast to the entire image or select one for each slice. For 2D does not matter but yes for 3D images.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_contrast_em_mode_label.setText(QCoreApplication.translate("MainWindow", u"Contrast EM mode", None))
#if QT_CONFIG(tooltip)
        self.da_cutout_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range of the size of the areas in % of the corresponding image size. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0.05,0.3)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutout_size_label.setText(QCoreApplication.translate("MainWindow", u"Cutout size", None))
        self.da_cutout_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_cutout_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_cutblur_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_cutblur_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_gamma_contrast_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_gamma_contrast_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_grayscale_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_grayscale_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_107.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Set a certain fraction of pixels in images to zero (not get confused with the dropout concept of neural networks)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Dropout", None))
#if QT_CONFIG(tooltip)
        self.label_132.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Augment the images by adding Poisson noise</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Poisson noise", None))
        self.da_misaligment_rotate_ratio_input.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.da_misaligment_rotate_ratio_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.5", None))
#if QT_CONFIG(tooltip)
        self.da_brightness_em_factor_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Strength of the brightness range. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(-0.1,0.1) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_brightness_em_factor_label.setText(QCoreApplication.translate("MainWindow", u"Brightness EM factor", None))
        self.da_contrast_em_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"3D", None))
        self.da_contrast_em_mode_input.setItemText(1, QCoreApplication.translate("MainWindow", u"2D", None))

#if QT_CONFIG(tooltip)
        self.label_78.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable motion blur as data augmentation. It blur images in a way that fakes camera or object movements</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Motion blur ", None))
        self.da_brightness_em_factor_input.setText(QCoreApplication.translate("MainWindow", u"(-0.1, 0.1)", None))
        self.da_brightness_em_factor_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(-0.1,0.1) ", None))
#if QT_CONFIG(tooltip)
        self.da_cutblur_size_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of the region to apply cutblur. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0.1,0.3)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutblur_size_range_label.setText(QCoreApplication.translate("MainWindow", u"Cutblur size range", None))
#if QT_CONFIG(tooltip)
        self.label_73.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">How to fill up the new values created with affine transformations (rotations, shear, shift and zoom). Same meaning as in skimage and </span><a href=\"https://numpy.org/doc/stable/reference/generated/numpy.pad.html\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">numpy.pad()</span></a><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Affine mode", None))
#if QT_CONFIG(tooltip)
        self.da_cutblur_inside_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to apply cut-and-paste just LR into HR image. If 'No' is selected, HR to LR will be applied also (see Figure 1 of the paper </span><a href=\" https://arxiv.org/pdf/2004.00448.pdf\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://arxiv.org/pdf/2004.00448.pdf</span></a><span style=\" font-size:12pt;\">)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutblur_inside_label.setText(QCoreApplication.translate("MainWindow", u"Cutblur inside", None))
#if QT_CONFIG(tooltip)
        self.label_72.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable vertical flip as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Vertical flip", None))
#if QT_CONFIG(tooltip)
        self.label_63.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To shuffle the validation data on every epoch</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Shuffle val data each epoch", None))
#if QT_CONFIG(tooltip)
        self.label_109.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply cutblur operation that fills one rectangular area in an image with a low resolution version of it by downsampling and upsampling that area.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Cutblur", None))
#if QT_CONFIG(tooltip)
        self.da_cuout_cval_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Value to fill the area of cutout. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cuout_cval_label.setText(QCoreApplication.translate("MainWindow", u"Cutout cval", None))
        self.da_motion_blur_k_size_input.setText(QCoreApplication.translate("MainWindow", u"(8, 12)", None))
        self.da_motion_blur_k_size_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(8, 12)", None))
        self.da_elastic_sigma_input.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.da_elastic_sigma_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(tooltip)
        self.label_64.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of samples to create. Used when 'check augmented samples' is selected</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Numer of samples during check", None))
        self.da_vertical_flip_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_vertical_flip_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_pepper_amount_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Proportion of pepper to add. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_pepper_amount_label.setText(QCoreApplication.translate("MainWindow", u"Pepper amount", None))
#if QT_CONFIG(tooltip)
        self.label_91.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable brightness changes as data augmentation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
#if QT_CONFIG(tooltip)
        self.label_135.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Augment the images by adding Gaussian noise</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Gaussian noise", None))
#if QT_CONFIG(tooltip)
        self.da_contrast_em_factor_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Strength of the contrast change range, with valid values between 0 and 1 . Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(-0.1,0.1) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_contrast_em_factor_label.setText(QCoreApplication.translate("MainWindow", u"Contrast EM factor", None))
        self.da_cutnoise_number_iter_input.setText(QCoreApplication.translate("MainWindow", u"(1, 3)", None))
        self.da_cutnoise_number_iter_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(1,3)", None))
        self.da_cutblut_down_range_input.setText(QCoreApplication.translate("MainWindow", u"(2, 8)", None))
        self.da_cutblut_down_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(2, 8)", None))
        self.da_random_rot_range_input.setText(QCoreApplication.translate("MainWindow", u"(-180, 180)", None))
        self.da_random_rot_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(-180, 180)", None))
        self.da_brightness_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_brightness_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_cutnoise_size_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.2, 0.4)", None))
        self.da_cutnoise_size_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.2,0.4)", None))
        self.da_missing_sections_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_missing_sections_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_cutnoise_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply cutnoise operation that adds noise to one or more rectangular areas in an image </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutnoise_label.setText(QCoreApplication.translate("MainWindow", u"Cutnoise", None))
        self.da_zoom_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.8, 1.2)", None))
        self.da_zoom_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.8, 1.2)", None))
        self.da_shear_range_input.setText(QCoreApplication.translate("MainWindow", u"(-20, 20)", None))
        self.da_shear_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(-20,-20)", None))
        self.da_z_flip_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_z_flip_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_num_samples_check_input.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.da_num_samples_check_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"10", None))
#if QT_CONFIG(tooltip)
        self.label_123.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Augment images by converting them into grayscale</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Grayscale", None))
#if QT_CONFIG(tooltip)
        self.label_127.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Augment the image by creating a black line in a random position</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Missing sections", None))
#if QT_CONFIG(tooltip)
        self.da_brightness_mode_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">If apply the same brightness to the entire image or select one for each slice. For 2D does not matter but yes for 3D images.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_brightness_mode_label.setText(QCoreApplication.translate("MainWindow", u"Brightness mode", None))
#if QT_CONFIG(tooltip)
        self.da_grid_ratio_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Determines the keep ratio of an input image. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1 </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_grid_ratio_label.setText(QCoreApplication.translate("MainWindow", u"Grid ratio", None))
#if QT_CONFIG(tooltip)
        self.label_103.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply cutout operation that fills one or more rectangular areas in an image using a fill mode</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Cutout", None))
        self.da_draw_grid_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.da_draw_grid_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.da_contrast_em_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_contrast_em_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_contrast_factor_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Strength of the contrast change. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(-0.1,0.1) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_contrast_factor_range_label.setText(QCoreApplication.translate("MainWindow", u"Contrast factor range", None))
        self.da_cutmix_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_cutmix_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_dropout_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range to take the probability to drop a pixel. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0,0.2)</span><span style=\" font-size:12pt;\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_dropout_range_label.setText(QCoreApplication.translate("MainWindow", u"Dropout range ", None))
        self.da_median_blur_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_median_blur_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_salt_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_salt_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_cutout_to_mask_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_cutout_to_mask_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_gaussian_noise_var_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Variance of the Gaussian</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_gaussian_noise_var_label.setText(QCoreApplication.translate("MainWindow", u"Gaussian noise variance", None))
        self.da_salt_pepper_amount_input.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_salt_pepper_amount_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_random_rot_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_random_rot_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_shuffle_val_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_shuffle_val_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_118.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply gridmask to the image. It is based on the deletion of regions of the input image. Original paper: </span><a href=\"https://arxiv.org/pdf/2001.04086v1.pdf\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://arxiv.org/pdf/2001.04086v1.pdf</span></a><span style=\" font-size:12pt;\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Gridmask", None))
#if QT_CONFIG(tooltip)
        self.label_83.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable Gaussian blur as data augmentation. It blurs an image by computing median values over neighborhoods </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Median blur", None))
        self.da_shear_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_shear_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_grid_invert_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_grid_invert_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_elastic_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"constant", None))

#if QT_CONFIG(tooltip)
        self.da_contrast_mode_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">If apply the same contrast to the entire image or select one for each slice. For 2D does not matter but yes for 3D images</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_contrast_mode_label.setText(QCoreApplication.translate("MainWindow", u"Contrast mode", None))
#if QT_CONFIG(tooltip)
        self.da_cutout_to_mask_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Wheter if the cutout will be applied to the segmentation mask too. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutout_to_mask_label.setText(QCoreApplication.translate("MainWindow", u"Cutout applied to mask", None))
#if QT_CONFIG(tooltip)
        self.da_median_blur_k_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Median blur kernel size. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(3,7)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_median_blur_k_size_label.setText(QCoreApplication.translate("MainWindow", u"Median blur kernel size range", None))
        self.da_cutnoise_scale_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.05, 0.1)", None))
        self.da_cutnoise_scale_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.05, 0.1)", None))
        self.da_grid_d_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.4, 1)", None))
        self.da_grid_d_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.4 ,1)", None))
#if QT_CONFIG(tooltip)
        self.da_misaligment_displacement_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maximum pixel displacement in 'xy'-plane for misalignment. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_misaligment_displacement_label.setText(QCoreApplication.translate("MainWindow", u"Misalignment displacement ", None))
#if QT_CONFIG(tooltip)
        self.da_missing_sections_iteration_range_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.da_missing_sections_iteration_range_input.setText(QCoreApplication.translate("MainWindow", u"(10, 30)", None))
        self.da_missing_sections_iteration_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(10,30)", None))
#if QT_CONFIG(tooltip)
        self.da_gaussian_noise_use_input_img_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to use input image's mean and variance instead of the fixed values </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_gaussian_noise_use_input_img_label.setText(QCoreApplication.translate("MainWindow", u"Gaussian noise use input img stats", None))
        self.da_gaussian_noise_use_input_img_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_gaussian_noise_use_input_img_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_88.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable brightness changes to images, based on Pytorch Connectomics library, as data augmentation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Brightness EM", None))
#if QT_CONFIG(tooltip)
        self.da_elastic_sigma_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Standard deviation of the gaussian kernel used to smooth the distortion fields.  Higher values (for 128x128 images around 5.0) lead to more water-like effects, while lower values (for128x128 images around 1.0 and lower) lead to more noisy, pixelated images. Set this to around 1/10th of alpha for visible effects. </span><span style=\" font-size:12pt; font-weight:600;\">Must be float.</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_elastic_sigma_label.setText(QCoreApplication.translate("MainWindow", u"Elastic sigma", None))
        self.da_dropout_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_dropout_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_misaligment_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_misaligment_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_cutout_number_iterations_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range of number of areas to fill the image with. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be positive integers. Reasonable values between range (0,4). E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(1,3)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutout_number_iterations_label.setText(QCoreApplication.translate("MainWindow", u"Cuout number iterations", None))
#if QT_CONFIG(tooltip)
        self.label_60.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Probability of each transformation. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Probability", None))
#if QT_CONFIG(tooltip)
        self.label_71.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable zoom as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
#if QT_CONFIG(tooltip)
        self.label_62.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Create samples of the data augmentation made. Useful to check the output images made.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Check augmented samples", None))
        self.da_zoom_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_zoom_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_contrast_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_contrast_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_salt_amount_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Proportion of salt to add. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_salt_amount_label.setText(QCoreApplication.translate("MainWindow", u"Salt amount", None))
#if QT_CONFIG(tooltip)
        self.da_shear_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Shear range. Expected value range is around [-360, 360], with reasonable values being in the range of [-45, 45]. Each time the augmentation is applied a random value in the specified range will be selected. E.g.</span><span style=\" font-size:12pt; font-weight:600;\"> [-45, 45]</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_shear_range_label.setText(QCoreApplication.translate("MainWindow", u"Shear range", None))
#if QT_CONFIG(tooltip)
        self.da_cutnoise_size_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of the regions. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0.1,0.2)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutnoise_size_range_label.setText(QCoreApplication.translate("MainWindow", u"Cutnoise size range", None))
        self.da_dropout_range_input.setText(QCoreApplication.translate("MainWindow", u"(0, 0.2)", None))
        self.da_dropout_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0,0.2)", None))
        self.da_contrast_em_factor_input.setText(QCoreApplication.translate("MainWindow", u"(-0.1, 0.1)", None))
        self.da_contrast_em_factor_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(-0.1,0.1) ", None))
        self.da_salt_amount_input.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_salt_amount_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.05", None))
#if QT_CONFIG(tooltip)
        self.da_gamma_contrast_range_input.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Exponent for the contrast adjustment. Higher values darken the image</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_gamma_contrast_range_input.setText(QCoreApplication.translate("MainWindow", u"(1.25, 1.75)", None))
        self.da_gamma_contrast_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(1.25,1.75)", None))
#if QT_CONFIG(tooltip)
        self.da_gaussian_noise_mean_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mean of the Gaussian</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_gaussian_noise_mean_label.setText(QCoreApplication.translate("MainWindow", u"Gaussian noise mean", None))
#if QT_CONFIG(tooltip)
        self.da_grid_rotate_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Rotation of the mask in GridMask. Needs to a float be between 0 and 1, where 1 is 360 degrees</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_grid_rotate_label.setText(QCoreApplication.translate("MainWindow", u"Grid rotate", None))
#if QT_CONFIG(tooltip)
        self.label_77.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable shift as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.da_cutblur_inside_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.da_cutblur_inside_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.da_check_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_check_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_gaussian_noise_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_gaussian_noise_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_cutnoise_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_cutnoise_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_99.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable contrast changes to images, based on Pytorch Connectomics library, as data augmentation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Contrast EM", None))
        self.da_salt_pepper_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_salt_pepper_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_gridmask_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_gridmask_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_cuout_cval_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.da_cuout_cval_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.", None))
        self.da_shift_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.1, 0.2)", None))
        self.da_shift_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.1, 0.2)", None))
        self.da_gaussian_sigma_input.setText(QCoreApplication.translate("MainWindow", u"(1.0, 2.0)", None))
        self.da_gaussian_sigma_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(1.0,2.0)", None))
#if QT_CONFIG(tooltip)
        self.da_grid_invert_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to invert the mask</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_grid_invert_label.setText(QCoreApplication.translate("MainWindow", u"Grid invert", None))
        self.da_brightness_factor_range_input.setText(QCoreApplication.translate("MainWindow", u"(-0.1, 0.1)", None))
        self.da_brightness_factor_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(-0.1,0.1) ", None))
#if QT_CONFIG(tooltip)
        self.label_94.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable gamma contrast as data augmentation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Gamma contrast", None))
        self.da_pepper_amount_input.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_pepper_amount_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_motion_blur_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_motion_blur_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_zoom_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Zoom range. Scaling factor to use, where 1.0 denotes \u201cno change\u201d and 0.5 is zoomed out to 50 percent of the original size. Each time the augmentation is applied a random value in the specified range will be selected. E.g.</span><span style=\" font-size:12pt; font-weight:600;\"> [0.8, 1.2]</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_zoom_range_label.setText(QCoreApplication.translate("MainWindow", u"Zoom range", None))
        self.da_brightness_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"3D", None))
        self.da_brightness_mode_input.setItemText(1, QCoreApplication.translate("MainWindow", u"2D", None))

        self.da_cutout_size_input.setText(QCoreApplication.translate("MainWindow", u"(0.05, 0.3)", None))
        self.da_cutout_size_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.05,0.3)", None))
#if QT_CONFIG(tooltip)
        self.da_prob_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.da_prob_input.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.da_prob_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.5", None))
        self.da_contrast_factor_range_input.setText(QCoreApplication.translate("MainWindow", u"(-0.1, 0.1)", None))
        self.da_contrast_factor_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(-0.1,0.1) ", None))
        self.da_salt_pepper_prop_input.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.da_salt_pepper_prop_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.5", None))
#if QT_CONFIG(tooltip)
        self.da_z_flip_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable Z-axis flip as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_z_flip_label.setText(QCoreApplication.translate("MainWindow", u"Z flip", None))
        self.da_horizontal_flip_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_horizontal_flip_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_misaligment_displacement_input.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.da_misaligment_displacement_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"16", None))
#if QT_CONFIG(tooltip)
        self.label_84.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable elastic deformation as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Elastic", None))
        self.da_poisson_noise_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_poisson_noise_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_shuffle_train_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.da_shuffle_train_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.da_cutblut_down_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range of the downsampling to be made in cutblur. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(2, 8)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutblut_down_range_label.setText(QCoreApplication.translate("MainWindow", u"Cutblur downsampling range", None))
#if QT_CONFIG(tooltip)
        self.da_cutnoise_number_iter_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of areas to fill with noise. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be positive integers. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(1,3)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutnoise_number_iter_label.setText(QCoreApplication.translate("MainWindow", u"Cutnoise number of iterations", None))
#if QT_CONFIG(tooltip)
        self.da_gaussian_sigma_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Standard deviation of the gaussian kernel. Values in the range 0.0 (no blur) to 3.0 (strong blur) are common. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(1.0,2.0)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_gaussian_sigma_label.setText(QCoreApplication.translate("MainWindow", u"Gaussian sigma", None))
#if QT_CONFIG(tooltip)
        self.da_cutblur_size_range_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.da_cutblur_size_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.2, 0.4)", None))
        self.da_cutblur_size_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.2, 0.4)", None))
        self.da_gaussian_noise_var_input.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_gaussian_noise_var_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.05", None))
        self.da_rot90_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_rot90_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_110.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply cutmix operation that fills one rectangular area in an image using a patch of another image in the training data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Cutmix", None))
        self.da_affine_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"constant", None))
        self.da_affine_mode_input.setItemText(1, QCoreApplication.translate("MainWindow", u"edge", None))
        self.da_affine_mode_input.setItemText(2, QCoreApplication.translate("MainWindow", u"symmetric", None))
        self.da_affine_mode_input.setItemText(3, QCoreApplication.translate("MainWindow", u"reflect", None))
        self.da_affine_mode_input.setItemText(4, QCoreApplication.translate("MainWindow", u"wrap", None))

#if QT_CONFIG(tooltip)
        self.da_grid_d_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range to choose a 'd' value, which determines the length of each unit. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be float. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0.5 ,1)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_grid_d_range_label.setText(QCoreApplication.translate("MainWindow", u"Grid d range ", None))
#if QT_CONFIG(tooltip)
        self.label_87.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable Gaussian blur as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Gaussian blur", None))
#if QT_CONFIG(tooltip)
        self.da_missing_sections_iteration_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range to select the iterations to dilate the missing line with. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be positive integers. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(10,30)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_missing_sections_iteration_range_label.setText(QCoreApplication.translate("MainWindow", u"Missing sections iteration range", None))
#if QT_CONFIG(tooltip)
        self.label_65.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable random rotation between a defined range as augmentation</span></p></body></html>  ", None))
#endif // QT_CONFIG(tooltip)
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Random rotation", None))
#if QT_CONFIG(tooltip)
        self.da_misaligment_rotate_ratio_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Ratio of rotation-based mis-alignment. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_misaligment_rotate_ratio_label.setText(QCoreApplication.translate("MainWindow", u"Misaligment rotate ratio", None))
#if QT_CONFIG(tooltip)
        self.label_144.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Augment the images by adding pepper, which replaces random pixels with 0 (for unsigned images) or -1 (for signed images)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Pepper", None))
#if QT_CONFIG(tooltip)
        self.da_motion_blur_k_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Motion blur kernel size. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(8,12)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_motion_blur_k_size_label.setText(QCoreApplication.translate("MainWindow", u"Motion blur kernel size range ", None))
#if QT_CONFIG(tooltip)
        self.label_61.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Draw a grid in the augmentation samples generated. Used when 'check augmented samples' is selected</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Draw grid during check", None))
#if QT_CONFIG(tooltip)
        self.da_salt_pepper_prop_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Proportion of salt vs. pepper noise. Higher values represent more salt. 0.5 represents equal ammounts. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_salt_pepper_prop_label.setText(QCoreApplication.translate("MainWindow", u"Salt and pepper proportion", None))
        self.da_grid_ratio_input.setText(QCoreApplication.translate("MainWindow", u"0.6", None))
        self.da_grid_ratio_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.6", None))
#if QT_CONFIG(tooltip)
        self.da_salt_pepper_amount_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Amount of salt and pepper to add. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_salt_pepper_amount_label.setText(QCoreApplication.translate("MainWindow", u"Salt and pepper amount", None))
        self.da_brightness_em_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_brightness_em_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_grid_rotate_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da_grid_rotate_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(tooltip)
        self.label_90.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable contrast changes as data augmentation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.da_channel_shuffle_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_channel_shuffle_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_74.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable shear as data augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Shear", None))
#if QT_CONFIG(tooltip)
        self.da_cutmix_size_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of the region to apply cutmix. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0.1,0.3)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutmix_size_range_label.setText(QCoreApplication.translate("MainWindow", u"Cutmix size range", None))
#if QT_CONFIG(tooltip)
        self.da_cutnoise_scale_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range to choose a value that will represent the % of the maximum value of the image that will be used as the std of the Gaussian Noise distribution. Each time the augmentation is applied a random value in the specified range will be selected. Values need to be between 0 and 1. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0.1,0.2)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_cutnoise_scale_range_label.setText(QCoreApplication.translate("MainWindow", u"Cutnoise scale range", None))
        self.da_pepper_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_pepper_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.da_brightness_factor_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Strength of the brightness range. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(-0.1,0.1) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_brightness_factor_range_label.setText(QCoreApplication.translate("MainWindow", u"Brightness factor range", None))
#if QT_CONFIG(tooltip)
        self.da_shift_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Shift range. Translation as a fraction of the image height/width (x-translation, y-translation), where 0 denotes 'no change' and 0.5 denotes 'half' of the axis size. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">[0.1, 0.2]</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_shift_range_label.setText(QCoreApplication.translate("MainWindow", u"Shift range", None))
#if QT_CONFIG(tooltip)
        self.label_67.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable rotation of 90\u00ba, 180\u00ba or 270\u00ba to images as augmentation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Rotation 90\u00ba", None))
#if QT_CONFIG(tooltip)
        self.da_elastic_alpha_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Strength of the distortion field. Higher values mean that pixels are moved further with respect to the distortion field\u2019s direction. Set this to around 10 times the value of sigma for visible effects. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(12,16)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_elastic_alpha_label.setText(QCoreApplication.translate("MainWindow", u"Elastic alpha", None))
#if QT_CONFIG(tooltip)
        self.da_random_rot_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Range of random rotations. Each time the augmentation is applied a random value in the specified range will be selected. </span><span style=\" font-family:'arial,sans-serif'; font-size:16px; color:#202124; background-color:#ffffff;\">Parentheses</span><span style=\" font-size:12pt;\"> are needed. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(-90, 90)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_random_rot_range_label.setText(QCoreApplication.translate("MainWindow", u"Random rotation range", None))
        self.da_cutmix_size_range_input.setText(QCoreApplication.translate("MainWindow", u"(0.2, 0.4)", None))
        self.da_cutmix_size_range_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(0.2,0.4)", None))
        self.da_elastic_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_elastic_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.da_median_blur_k_size_input.setText(QCoreApplication.translate("MainWindow", u"(3, 7)", None))
        self.da_median_blur_k_size_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(3,7)", None))
        self.da_brightness_em_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"3D", None))
        self.da_brightness_em_mode_input.setItemText(1, QCoreApplication.translate("MainWindow", u"2D", None))

        self.da_contrast_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"3D", None))
        self.da_contrast_mode_input.setItemText(1, QCoreApplication.translate("MainWindow", u"2D", None))

#if QT_CONFIG(tooltip)
        self.da_gamma_contrast_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Exponent for the contrast adjustment. Higher values darken the image. Each time the augmentation is applied a random value in the specified range will be selected. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(1.25,1.75)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_gamma_contrast_range_label.setText(QCoreApplication.translate("MainWindow", u"Gamma constrast gamma range", None))
#if QT_CONFIG(tooltip)
        self.da_brightness_em_mode_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">If apply the same brightness to the entire image or select one for each slice. For 2D does not matter but yes for 3D images.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da_brightness_em_mode_label.setText(QCoreApplication.translate("MainWindow", u"Brightness EM mode", None))
#if QT_CONFIG(tooltip)
        self.label_122.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Shuffle channels of the images</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Channel shuffle", None))
        self.da_gaussian_noise_mean_input.setText(QCoreApplication.translate("MainWindow", u"0.", None))
        self.da_gaussian_noise_mean_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0", None))
        self.da_cutout_number_iterations_input.setText(QCoreApplication.translate("MainWindow", u"(1, 3)", None))
        self.da_cutout_number_iterations_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(1,3)", None))
#if QT_CONFIG(tooltip)
        self.label_66.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To shuffle the training data on every epoch</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Shuffle train data each epoch", None))
        self.da_elastic_alpha_input.setText(QCoreApplication.translate("MainWindow", u"(12, 16)", None))
        self.da_elastic_alpha_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"(12,16)", None))
        self.da_shift_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_shift_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_119.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable misaligment augmentation to simulate the displacement of tissue that can be present in adquisitions</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Misalignment ", None))
#if QT_CONFIG(tooltip)
        self.label_141.setToolTip(QCoreApplication.translate("MainWindow", u"Augment the images by adding salt and pepper", None))
#endif // QT_CONFIG(tooltip)
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Salt and pepper", None))
        self.da_gaussian_blur_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.da_gaussian_blur_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_128.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Augment the images by adding salt, which replaces random pixels with 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Salt", None))
        self.kernel_size_input.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.kernel_size_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">3</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of feature maps on each level of the network. Brackets are needed. </span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">E.g.</span><span style=\" font-family:'Arial'; font-size:12pt; font-weight:600; color:#000000; background-color:transparent;\"> [16, 32, 64, 128, 256]</span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\"> on a 5 level U-Net </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Feature maps", None))
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To activate the Spatial Dropout instead of use the &quot;normal&quot; dropout layer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Spatial dropout", None))
#if QT_CONFIG(tooltip)
        self.label_39.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To active batch normalization</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Batch normalization", None))
#if QT_CONFIG(tooltip)
        self.label_37.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-7aa00324-7fff-fb61-fe4f-e2f1b72eacd0\"/><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">V</span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">alues to make the dropout on each model level. </span><span style=\" font-size:12pt;\">Brackets are needed and each number must be a float between 0 and 1. </span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">Set to 0 to prevent dropout. E.g. </span><span style=\" font-family:'Arial'; font-size:12pt; font-weight:600; color:#000000; background-color:transparent;\">[0, 0.1, 0.2, 0.3]</span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\"> on a 4 level U-Net </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Dropout values", None))
#if QT_CONFIG(tooltip)
        self.label_41.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Kernel size</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Kernel size", None))
#if QT_CONFIG(tooltip)
        self.label_40.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\"> Kernel type to use on convolution layers. Please visit </span><a href=\"https://keras.io/api/layers/initializers\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://keras.io/api/layers/initializers</span></a><span style=\" font-size:12pt;\"> for more info</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Kernel init", None))
#if QT_CONFIG(tooltip)
        self.label_43.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Upsampling layer to use in the model</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Upsample layer", None))
#if QT_CONFIG(tooltip)
        self.label_45.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Last activation function to use along the model. Please visit </span><a href=\"https://keras.io/api/layers/activations/\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://keras.io/api/layers/activations/</span></a><span style=\" font-size:12pt;\"> for more info</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Last activation", None))
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Downsampling to be made in Z for each level of the model. This step is only relevant for 3D problems and U-Net models, and the resulting value will be utilized in the MaxPooling function. The input for this function should be enclosed in brackets and consist only of the numbers 0, 1 or 2. Set it to 0 to avoid this option. A value of 1 indicates that no maxpooling will occur along the Z-axis at that level of the network, while a value of 2 signifies that pooling will be performed in all three dimensions. This approach is particularly useful when dealing with anisotropic datasets since better performance is typically achieved without a pooling in Z-axis. It needs to be of the same length than feature maps of the network minus one. E.g. the input </span><span style=\" font-size:12pt; font-weight:600;\">[2,1]</span><span style=\" font-size:12pt;\"> applies pooling in all dimensions for the downsampling between first and second levels of the network but only in"
                        " the X and Y dimensions for the downsampling done between the second and third level, excluding the Z dimension.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Downsampling on each level", None))
#if QT_CONFIG(tooltip)
        self.label_47.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Activation function to use along the model. Please visit </span><a href=\"https://keras.io/api/layers/activations/\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://keras.io/api/layers/activations/</span></a><span style=\" font-size:12pt;\"> for more info</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Activation", None))
        self.dropout_input.setText(QCoreApplication.translate("MainWindow", u"[0., 0., 0., 0., 0.]", None))
        self.dropout_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">[0., 0., 0., 0., 0.]</span></p></body></html>", None))
        self.feature_maps_input.setText(QCoreApplication.translate("MainWindow", u"[16, 32, 64, 128, 256]", None))
        self.feature_maps_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">[16, 32, 64, 128, 256]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.z_down_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.z_down_input.setText(QCoreApplication.translate("MainWindow", u"[0, 0, 0, 0]", None))
        self.z_down_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">[0, 0, 0, 0]</span></p></body></html>", None))
        self.batch_normalization_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.batch_normalization_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.kernel_init_input.setItemText(0, QCoreApplication.translate("MainWindow", u"he_normal", None))
        self.kernel_init_input.setItemText(1, QCoreApplication.translate("MainWindow", u"he_uniform", None))
        self.kernel_init_input.setItemText(2, QCoreApplication.translate("MainWindow", u"glorot_normal", None))
        self.kernel_init_input.setItemText(3, QCoreApplication.translate("MainWindow", u"glorot_uniform", None))
        self.kernel_init_input.setItemText(4, QCoreApplication.translate("MainWindow", u"random_normal", None))
        self.kernel_init_input.setItemText(5, QCoreApplication.translate("MainWindow", u"random_uniform", None))
        self.kernel_init_input.setItemText(6, QCoreApplication.translate("MainWindow", u"zeros", None))
        self.kernel_init_input.setItemText(7, QCoreApplication.translate("MainWindow", u"ones", None))

        self.spatial_dropout_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.spatial_dropout_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.upsample_layer_input.setItemText(0, QCoreApplication.translate("MainWindow", u"convtranspose", None))
        self.upsample_layer_input.setItemText(1, QCoreApplication.translate("MainWindow", u"upsampling", None))

        self.activation_input.setItemText(0, QCoreApplication.translate("MainWindow", u"elu", None))
        self.activation_input.setItemText(1, QCoreApplication.translate("MainWindow", u"relu", None))
        self.activation_input.setItemText(2, QCoreApplication.translate("MainWindow", u"selu", None))

        self.last_activation_input.setItemText(0, QCoreApplication.translate("MainWindow", u"sigmoid", None))
        self.last_activation_input.setItemText(1, QCoreApplication.translate("MainWindow", u"softmax", None))
        self.last_activation_input.setItemText(2, QCoreApplication.translate("MainWindow", u"linear", None))
        self.last_activation_input.setItemText(3, QCoreApplication.translate("MainWindow", u"tanh", None))

        self.custom_mean_input.setText(QCoreApplication.translate("MainWindow", u"-1.0", None))
        self.custom_mean_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"-1.0", None))
        self.normalization_type_input.setItemText(0, QCoreApplication.translate("MainWindow", u"div", None))
        self.normalization_type_input.setItemText(1, QCoreApplication.translate("MainWindow", u"custom", None))

#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Normalization type to use. Possible options: 1) 'div' to divide values from 0/255 (or 0/65535 if uint16) in [0,1] range; 2) 'custom' to use a custom mean and std to normalize the data</span><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Normalization type", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Extract random patches during data augmentation (DA). This option will prevent input images to be cropped in the patch size specified and will extract a random patch of that shape every training sample. This option will slow down each training epoch. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Extract random patch", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Input the size of the patches use to train your model (y,x,channels) order for 2D and (z,y,x,channels) for 3D. Parentheses are need. The value should be smaller or equal to the shape of the image. E. g. </span><span style=\" font-size:12pt; font-weight:600;\">(40,128,128,1)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Patch size", None))
        self.extract_random_patch_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.extract_random_patch_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.patch_size_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.custom_mean_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Custon mean to be applied if 'custom' was selected in normalization type.</span><span style=\" font-size:12pt; font-weight:600;\"> Must be a float.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.custom_mean_label.setText(QCoreApplication.translate("MainWindow", u"Custom mean", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to reshape de dimensions that do not satisfy the patch shape selected by padding it with reflection.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reflect to complete shape", None))
        self.reflect_to_complete_shape_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.reflect_to_complete_shape_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.custom_std_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Custon std to be applied if 'custom' was selected in normalization type.</span><span style=\" font-size:12pt; font-weight:600;\"> Must be a float.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.custom_std_label.setText(QCoreApplication.translate("MainWindow", u"Custom std", None))
#if QT_CONFIG(tooltip)
        self.check_gen_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Save all data of the training and validation generators in a folder named 'gen_check' in the results directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.check_gen_label.setText(QCoreApplication.translate("MainWindow", u"Check generator", None))
        self.check_gen_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.check_gen_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.custom_std_input.setText(QCoreApplication.translate("MainWindow", u"-1.0", None))
        self.custom_std_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">-1.0</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Validation data", None))
#if QT_CONFIG(tooltip)
        self.lr_schel_reduce_on_plat_patience_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of epochs with no improvement after which learning rate will be reduced in 'reduceonplateau' scheduler. Need to be less than training patience otherwise it makes no sense. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lr_schel_reduce_on_plat_patience_label.setText(QCoreApplication.translate("MainWindow", u"Reduce on plateau patience", None))
#if QT_CONFIG(tooltip)
        self.lr_schel_warmupcosine_lr_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Initial learning rate to start the warm up from in 'warmupcosine' scheduler . You can set it to 0 or a value lower than training learning rate. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lr_schel_warmupcosine_lr_label.setText(QCoreApplication.translate("MainWindow", u"Warmup cosine decay learning rate", None))
#if QT_CONFIG(tooltip)
        self.lr_schel_reduce_on_plat_factor_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Factor by which the learning rate will be reduced in 'reduceonplateau' scheduler. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lr_schel_reduce_on_plat_factor_label.setText(QCoreApplication.translate("MainWindow", u"Reduce on plateau factor", None))
#if QT_CONFIG(tooltip)
        self.label_149.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Batch size of the training process. It is a hyperparameter that defines the number of samples to work through before updating the internal model parameters. This determines how many images will be loaded into the GPU at once so a high value will lead to a GPU memory error. Set it according to your GPU memory. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Batch size", None))
        self.lr_schel_input.setItemText(0, "")
        self.lr_schel_input.setItemText(1, QCoreApplication.translate("MainWindow", u"warmupcosine", None))
        self.lr_schel_input.setItemText(2, QCoreApplication.translate("MainWindow", u"reduceonplateau", None))
        self.lr_schel_input.setItemText(3, QCoreApplication.translate("MainWindow", u"onecycle", None))

        self.lr_schel_min_lr_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.lr_schel_warmupcosine_epochs_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.profiler_batch_range_input.setText(QCoreApplication.translate("MainWindow", u"10, 100", None))
#if QT_CONFIG(tooltip)
        self.lr_schel_min_lr_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Lower bound on the learning rate used in 'warmupcosine' and 'reduceonplateau'. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive float</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lr_schel_min_lr_label.setText(QCoreApplication.translate("MainWindow", u"Minimum learning rate", None))
        self.learning_rate_input.setText(QCoreApplication.translate("MainWindow", u"0.0001", None))
#if QT_CONFIG(tooltip)
        self.label_159.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To determine which value monitor to consider save the best model. If that value is improved a checkpoint of the &quot;best&quot; model will be saved. 'val_loss' refer to the validation loss, while 'loss' refers to training data loss</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Checkpoint monitor", None))
        self.batch_size_input.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(tooltip)
        self.label_150.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To determine which value monitor to stop the training. 'val_loss' refer to the validation loss, while 'loss' refers to training data loss</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Earlystopping monitor", None))
#if QT_CONFIG(tooltip)
        self.label_162.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Set up a learning rate scheduler. A Learning rate scheduler is a predefined framework that adjusts the learning rate between epochs or iterations as the training progresses. Leave it with the first option blank to avoid applying it. Three options available: 'warmupcosine', 'reduceonplateau', 'onecycle'. </span></p><p><span style=\" font-size:12pt;\">- 'warmupcosine' refers to a cosine decay with a warm up consist in 2 phases: 1) a warm up phase which consists of increasing the learning rate from 'warmup cosine decay' to 'training learning rate' value by a factor during a certain number of epochs defined by 'warmup cosine decay hold epochs'; 2) after this will began the decay of the learning rate value using the cosine function. Find a detailed explanation in </span><a href=\"https://scorrea92.medium.com/cosine-learning-rate-decay-e8b50aa455b \"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">here</span></a></p><p><span style=\" "
                        "font-size:12pt;\">- 'reduceonplateau' reduces the learning rate when a metric has stopped improving. Models often benefit from reducing the learning rate by a factor of 2-10 once learning stagnates. This callback monitors a quantity and if no improvement is seen for a 'patience' number of epochs, the learning rate is reduced.</span></p><p><span style=\" font-size:12pt;\">- 'onecycle', sets the learning rate of each parameter group according to the 1cycle learning rate policy. The 1cycle policy anneals the learning rate from an initial learning rate to some maximum learning rate and then from that maximum learning rate to some minimum learning rate much lower than the initial learning rate. This policy was initially described in the paper: </span><a href=\"https://arxiv.org/abs/1708.07120\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">&quot;Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates&quot;</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Learning rate scheduler name", None))
#if QT_CONFIG(tooltip)
        self.label_143.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Optimizer to use during the model training.  Optimizers are algorithms or methods used to minimize an error function (the loss function) </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Optimizer", None))
#if QT_CONFIG(tooltip)
        self.label_151.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Learning rate during training phase. The learning rate is a hyperparameter that controls how much to change the model in response to the estimated error each time the model weights are updated. Choosing the learning rate is challenging as a value too small may result in a long training process that could get stuck, whereas a value too large may result in learning a sub-optimal set of weights too fast or an unstable training process</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Learning rate", None))
#if QT_CONFIG(tooltip)
        self.lr_schel_warmupcosine_epochs_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Epochs to do the warming up in 'warmupcosine' scheduler. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lr_schel_warmupcosine_epochs_label.setText(QCoreApplication.translate("MainWindow", u"Warmup cosine decay epochs", None))
#if QT_CONFIG(tooltip)
        self.label_160.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\"> Whether to add profiler callback to the training </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Profiler", None))
#if QT_CONFIG(tooltip)
        self.lr_schel_warmupcosine_hold_epochs_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of steps to hold base learning rate before decaying in 'warmupcosine' scheduler. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lr_schel_warmupcosine_hold_epochs_label.setText(QCoreApplication.translate("MainWindow", u"Warmup cosine decay hold epochs", None))
        self.profiler_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.profiler_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.profiler_batch_range_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Batch range to be analyzed in the profiler. Must two positive integers separated by a comma.</span><span style=\" font-size:12pt; font-weight:600;\"> E.g. (10, 100) means that the profiler will analise the batches from the 10th to the 100th </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.profiler_batch_range_label.setText(QCoreApplication.translate("MainWindow", u"Profiler batch range", None))
        self.checkpoint_monitor_input.setItemText(0, QCoreApplication.translate("MainWindow", u"val_loss", None))
        self.checkpoint_monitor_input.setItemText(1, QCoreApplication.translate("MainWindow", u"loss", None))

        self.lr_schel_warmupcosine_lr_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.optimizer_input.setItemText(0, QCoreApplication.translate("MainWindow", u"ADAM", None))
        self.optimizer_input.setItemText(1, QCoreApplication.translate("MainWindow", u"SGD", None))

        self.early_stopping_input.setItemText(0, QCoreApplication.translate("MainWindow", u"val_loss", None))
        self.early_stopping_input.setItemText(1, QCoreApplication.translate("MainWindow", u"loss", None))

        self.lr_schel_reduce_on_plat_factor_input.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.lr_schel_warmupcosine_hold_epochs_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.lr_schel_reduce_on_plat_patience_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Percentage of overlap in (y,x)/(z,y,x) when cropping training data. Set to 0 to calculate the minimum overlap. Parentheses are needed. The values must be floats between range [0, 1). It needs to be a 2D tuple in 2D problems and 3D tuple in 3D problems. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(0,0)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
#if QT_CONFIG(tooltip)
        self.train_resolution_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Train data resolution. It is not completely necessary but when configured it is taken into account when performing some augmentations, e.g. cutout. If defined it need to be (y,x)/(z,y,x) and needs to be to be a 2D tuple when in 2D problems and 3D tuple when in 3D problems. Parentheses are needed. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">(5,0.852,0.852)</span><span style=\" font-size:12pt;\"> represent an anisotropic data with less resolution in Z axis.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_resolution_label.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Factor to multiply the training data. With this option, each training sample will be seen more than once across multiple epochs. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Replicate train data", None))
        self.replicate_data_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.replicate_data_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Training padding to be done in (y,x) for 2D problems and (z,y,x) for 3D ones when reconstructing train data. Useful to avoid patch border effect. Parentheses are needed. A good value should be the patch size divided by 8. For instance, if the path size is (256,256,1) a good value can be </span><span style=\" font-size:12pt; font-weight:600;\">(32,32)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Padding", None))
#if QT_CONFIG(tooltip)
        self.train_median_padding_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to use median values to fill padded pixels instead of reflect when cropping all the data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_median_padding_label.setText(QCoreApplication.translate("MainWindow", u"Median padding", None))
        self.train_median_padding_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.train_median_padding_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.unet_model_like_label.setText(QCoreApplication.translate("MainWindow", u"U-Net model-like configuration", None))
#if QT_CONFIG(tooltip)
        self.validation_padding_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Padding to be done in (y,x) for 2D problems and (z,y,x) for 3D ones when loading the validation data. Useful to avoid patch border effect. Parentheses are needed. A good value should be the patch size divided by 8. For instance, if the path size is (256,256,1) a good value can be </span><span style=\" font-size:12pt; font-weight:600;\">(32,32). </span><span style=\" font-size:12pt;\">This is only used when the validation is loaded from disk, and thus, not extracted from training. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.validation_padding_label.setText(QCoreApplication.translate("MainWindow", u"Padding", None))
#if QT_CONFIG(tooltip)
        self.validation_overlap_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Overlap to be done in (y,x) for 2D problems and (z,y,x) for 3D ones when loading the validation data. Set to 0 to calculate the minimum overlap. The values must be floats between range [0, 1). It needs to be a 2D tuple in 2D problems and 3D tuple in 3D problems. This is only used when the validation is loaded from disk, and thus, not extracted from training. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.validation_overlap_label.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
#if QT_CONFIG(tooltip)
        self.validation_padding_input.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Padding to be done in (y,x) for 2D problems and (z,y,x)for 3D ones when reconstructing train data. Useful to avoid patch border effect</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.random_val_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Create the validation data with random images of the training data. Used when the validation data is extracted from the training data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.random_val_label.setText(QCoreApplication.translate("MainWindow", u"Random validation", None))
        self.random_val_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.random_val_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Validation data resolution. </span><span style=\" font-size:12pt; font-weight:600;\">Currently not used in the code, but added just in case it is needed in a future</span><span style=\" font-size:12pt;\">. If defined it need to be (y,x)/(z,y,x) and needs to be to be a 2D tuple when in 2D problems and 3D tuple when in 3D problems</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.unetr_label.setText(QCoreApplication.translate("MainWindow", u"UNETR", None))
        self.tiramisu_depth_input.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.tiramisu_depth_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.label_140.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of feature maps on each level of the network. Brackets are needed. </span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">E.g.</span><span style=\" font-family:'Arial'; font-size:12pt; font-weight:600; color:#000000; background-color:transparent;\"> [16, 32, 64, 128, 256]</span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\"> on a 5 level U-Net </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Feature maps", None))
        self.tiramisu_feature_maps_input.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.tiramisu_feature_maps_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">[16, 32, 64, 128, 256]</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Depth of the network. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
#if QT_CONFIG(tooltip)
        self.label_142.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-7aa00324-7fff-fb61-fe4f-e2f1b72eacd0\"/><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">V</span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">alues to make the dropout on each model level. </span><span style=\" font-size:12pt;\">Brackets are needed and each number must be a float between 0 and 1. </span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\">Set to 0 to prevent dropout. E.g. </span><span style=\" font-family:'Arial'; font-size:12pt; font-weight:600; color:#000000; background-color:transparent;\">[0, 0.1, 0.2, 0.3]</span><span style=\" font-family:'Arial'; font-size:12pt; color:#000000; background-color:transparent;\"> on a 4 level U-Net </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Dropout values", None))
        self.tiramisu_dropout_input.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.tiramisu_dropout_input.setProperty("html", QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">[0., 0., 0., 0., 0.]</span></p></body></html>", None))
        self.unetr_vit_hidden_multiple_input.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.unetr_vit_hidden_multiple_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"3", None))
        self.unetr_num_heads_input.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.unetr_num_heads_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(tooltip)
        self.unetr_mlp_hidden_units_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.unetr_mlp_hidden_units_input.setText(QCoreApplication.translate("MainWindow", u"[3072, 768]", None))
        self.unetr_mlp_hidden_units_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"[3072, 768]", None))
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of heads in the multi-head attention layer. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Numer of heads", None))
#if QT_CONFIG(tooltip)
        self.label_53.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of transformer encoder layers. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
#if QT_CONFIG(tooltip)
        self.label_50.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of the patches that are extracted from the input image. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Token size", None))
#if QT_CONFIG(tooltip)
        self.label_54.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Multiple of the transformer encoder layers from of which the skip connection signal is going to be extracted. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"ViT Hidden multiple", None))
#if QT_CONFIG(tooltip)
        self.label_51.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Dimension of the embedding space. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Embedding dimension", None))
        self.unetr_token_size_input.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.unetr_token_size_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"16", None))
#if QT_CONFIG(tooltip)
        self.label_55.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of units in the MLP blocks. Brackets are needed. E.g. </span><span style=\" font-size:12pt; font-weight:600;\">[3072, 768]</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"MLP hidden units", None))
        self.unetr_embed_dims_input.setText(QCoreApplication.translate("MainWindow", u"768", None))
        self.unetr_embed_dims_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"768", None))
        self.unetr_depth_input.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.unetr_depth_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"12", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">IDs of the GPU to run the job in. If you want to use more than one GPU add them sepated by commas. E.g. &quot;0,1,2,3&quot; </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data options", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Train data", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Advanced training parameters", None))
        self.tiramisu_label.setText(QCoreApplication.translate("MainWindow", u"Tiramisu", None))
        self.train_advanced_label.setText(QCoreApplication.translate("MainWindow", u"Advanced options", None))
        self.train_advanced_bn.setText("")
        self.number_of_epochs_input.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.number_of_classes_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(tooltip)
        self.label_34.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Architecture of the network</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Model", None))
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of classes without counting the background class (that should be using 0 label). </span><span style=\" font-size:12pt; font-weight:600;\">It must be an integer greater than 0.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Number of classes", None))
#if QT_CONFIG(tooltip)
        self.patience_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">How many epochs you want to wait without the model improving its results in the validation set to stop training. </span><span style=\" font-size:12pt; font-weight:600;\">Must be an integer lower than number of epochs</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.patience_label.setText(QCoreApplication.translate("MainWindow", u"Patience ", None))
#if QT_CONFIG(tooltip)
        self.number_of_epochs_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">How many epochs (rounds) the model will be trained. </span><span style=\" font-size:12pt; font-weight:600;\">Must be an integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.number_of_epochs_label.setText(QCoreApplication.translate("MainWindow", u"Number of epochs", None))
        self.patience_input.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Basic training parameters", None))
        self.train_data_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">images</span></p></body></html>", None))
        self.train_in_memory_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.train_in_memory_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.train_data_in_memory.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to load all training data in memory or not. It speeds up the training process</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_data_in_memory.setText(QCoreApplication.translate("MainWindow", u"In memory", None))
        self.train_data_input_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.train_data_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the training data image directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_data_label.setText(QCoreApplication.translate("MainWindow", u"Image path", None))
#if QT_CONFIG(tooltip)
        self.train_gt_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the training data ground truth (GT) directory. Depending on the workflow this should point to a folder of mask labels (semantic segmentation), instance masks (instance segmentation), csv files (detection) and high resolution images (super-resolution).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_gt_label.setText(QCoreApplication.translate("MainWindow", u"GT path", None))
        self.train_data_gt_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">gt</span></p></body></html>", None))
        self.train_data_gt_input_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.cross_validation_nfolds_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.cross_validation_fold_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(tooltip)
        self.validation_data_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the validation data image directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.validation_data_label.setText(QCoreApplication.translate("MainWindow", u"Image path", None))
        self.validation_type_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Extract from train (split training)", None))
        self.validation_type_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Extract from train (cross validation)", None))
        self.validation_type_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Not extracted from train (path needed)", None))

#if QT_CONFIG(tooltip)
        self.cross_validation_nfolds_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of folds in the cross validation approach. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cross_validation_nfolds_label.setText(QCoreApplication.translate("MainWindow", u"Cross validation number of folds", None))
#if QT_CONFIG(tooltip)
        self.validation_type_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Validation data can be provided in three different ways: </span></p><p><span style=\" font-size:12pt;\">1) You can extract it from the training data given a percentage (&quot;Extract from train (split training)&quot; option). </span></p><p><span style=\" font-size:12pt;\">2) You can extract from the training data following a cross validation procedure (&quot;Extract from train (cross validation)&quot; option). Cross-Validation is a statistical method of evaluating and comparing learning algorithms by dividing data into two segments: one used to learn or train a model and the other used to validate the model. In cross-validation, you make a fixed number of folds (or partitions) of the data, run the analysis on each fold, and then average the overall error estimate. </span></p><p><span style=\" font-size:12pt;\">3) Use a separate source path to load the validation data (&quot;Not extracted from train (path needed)&quot; option)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.validation_type_label.setText(QCoreApplication.translate("MainWindow", u"Validation type", None))
        self.val_data_input_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.val_in_memory_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.val_in_memory_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.percentage_validation_input.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
#if QT_CONFIG(tooltip)
        self.val_in_memory_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to load all validation data in memory or not. It speeds up the evaluation process that is done after each epoch</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.val_in_memory_label.setText(QCoreApplication.translate("MainWindow", u"In memory", None))
        self.validation_data_gt_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">gt</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.percentage_validation_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Percentage of the training data used as validation during the model training. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.percentage_validation_label.setText(QCoreApplication.translate("MainWindow", u"Train percentage for validation", None))
#if QT_CONFIG(tooltip)
        self.validation_data_gt_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the validation data ground truth (GT) directory. Depending on the workflow this should point to a folder of mask labels (semantic segmentation), instance masks (instance segmentation), csv files (detection) and high resolution images (super-resolution).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.validation_data_gt_label.setText(QCoreApplication.translate("MainWindow", u"GT path", None))
        self.validation_data_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">images</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cross_validation_fold_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number of the fold to be used as validation in the cross validation approach. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cross_validation_fold_label.setText(QCoreApplication.translate("MainWindow", u"Cross validation fold number", None))
        self.val_data_gt_input_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Validation data", None))
        self.train_label.setText(QCoreApplication.translate("MainWindow", u"Train data", None))
        self.train_tab_widget.setTabText(self.train_tab_widget.indexOf(self.train_general_options_tab), QCoreApplication.translate("MainWindow", u"General options", None))
        self.extract_random_patch_frame_label.setText(QCoreApplication.translate("MainWindow", u"Extract random patch options", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Train data options", None))
        self.sem_seg_random_patch_prob_map_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.sem_seg_random_patch_prob_map_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.label_17.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Create a probability map so the patches extracted will have a high probability of having an object in the middle of it. Useful to avoid extracting patches which have no foreground class information. Used only with </span><span style=\" font-size:12pt; font-weight:600;\">extract random patch</span><span style=\" font-size:12pt;\"> option.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Probability map", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Weight for the foreground pixels. Must sum 1 with background weigth</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Foreground weights", None))
        self.sem_seg_random_patch_fore_weights_input.setText(QCoreApplication.translate("MainWindow", u"0.94", None))
        self.sem_seg_random_patch_fore_weights_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.06", None))
        self.sem_seg_random_patch_back_weights_input.setText(QCoreApplication.translate("MainWindow", u"0.06", None))
        self.sem_seg_random_patch_back_weights_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"0.94", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Weight for the background pixels. Must sum 1 with foreground weigth</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Background weigths", None))
        self.sem_seg_check_train_data_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.sem_seg_check_train_data_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.sem_seg_minimum_fore_percentage_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.sem_seg_minimum_fore_percentage_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Minimum foreground percentage that each image loaded needs to have to not discard it. Set to &quot;-1&quot; to not do it</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Minimum foreground percentage", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to check if the data gt contains correct values, e.g. same classes as defined</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Check train data", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Instance segmentation channels", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Train data options", None))
        self.inst_seg_minimum_fore_percentage_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.inst_seg_minimum_fore_percentage_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Minimum foreground percentage that each image loaded needs to have to not discard it. Set to &quot;-1&quot; to not do it</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Minimum foreground percentage", None))
#if QT_CONFIG(tooltip)
        self.label_69.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">This variable determines the channels to be created based on input instance masks. These option are composed from these individual options:</span></p><p><br/></p><p><span style=\" font-size:12pt;\">	- 'B' stands for 'Binary segmentation', containing each instance region without the contour. </span></p><p><span style=\" font-size:12pt;\">	- 'C' stands for 'Contour', containing each instance contour. </span></p><p><span style=\" font-size:12pt;\">	- 'D' stands for 'Distance', each pixel containing the distance of it to the instance contour. </span></p><p><span style=\" font-size:12pt;\">	- 'M' stands for 'Mask', contains the B and the C channels, i.e. the foreground mask. Is simply achieved by binarizing input instance masks. </span></p><p><span style=\" font-size:12pt;\">	- 'P' stands for 'Points' and contains the central points of an instance (as in Detection workflow)</span></p><p><span style=\" font-size:12pt;\">	- 'Dv2' stands for 'Distance V2', which i"
                        "s an updated version of 'D' channel calculating background distance as well. This option is experimental.</span></p><p><span style=\" font-size:12pt;\"/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Data channels", None))
        self.inst_seg_data_channels_input.setItemText(0, QCoreApplication.translate("MainWindow", u"BC", None))
        self.inst_seg_data_channels_input.setItemText(1, QCoreApplication.translate("MainWindow", u"BP", None))
        self.inst_seg_data_channels_input.setItemText(2, QCoreApplication.translate("MainWindow", u"BD", None))
        self.inst_seg_data_channels_input.setItemText(3, QCoreApplication.translate("MainWindow", u"BCM", None))
        self.inst_seg_data_channels_input.setItemText(4, QCoreApplication.translate("MainWindow", u"BCD", None))
        self.inst_seg_data_channels_input.setItemText(5, QCoreApplication.translate("MainWindow", u"BCDv2", None))
        self.inst_seg_data_channels_input.setItemText(6, QCoreApplication.translate("MainWindow", u"BDv2", None))
        self.inst_seg_data_channels_input.setItemText(7, QCoreApplication.translate("MainWindow", u"Dv2", None))

        self.inst_seg_channel_weigths_input.setText(QCoreApplication.translate("MainWindow", u"(1,1)", None))
#if QT_CONFIG(tooltip)
        self.label_70.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Weights to be applied to the channels. Need to have the same length as the data channels selected. E.g. if selected BCD channels it needs to have three values: (1,1,1)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Channel weights", None))
#if QT_CONFIG(tooltip)
        self.label_75.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Contour creation mode. Corresponds to 'mode' arg of find_boundaries function from scikit-image. More info </span><a href=\"https://scikit-image.org/docs/stable/api/skimage.segmentation.html#skimage.segmentation.find_boundaries\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">here</span></a><span style=\" font-size:12pt;\">. It can be also set as &quot;dense&quot;, to label as contour every pixel that is not in B channel.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Contour mode", None))
        self.inst_seg_contour_mode_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"thick", None))
        self.inst_seg_contour_mode_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"inner", None))
        self.inst_seg_contour_mode_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"outer", None))
        self.inst_seg_contour_mode_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"dense", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Train data options", None))
        self.det_check_created_point_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.det_check_created_point_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.det_central_point_dilation_input.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.label_76.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of the disk that will be used to dilate the central point created from the CSV file. 0 to not dilate and only create a 3x3 square.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_76.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Central point dilation", None))
#if QT_CONFIG(tooltip)
        self.label_79.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to check the points created to see if some of them are very close that create a large label</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Check created points", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Minimum foreground percentage that each image loaded needs to have to not discard it. Set to &quot;-1&quot; to not do it</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Minimum foreground percentage", None))
        self.det_minimum_fore_percentage_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.det_minimum_fore_percentage_input.setProperty("plainText", QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Loss type, two options: 1) &quot;CE&quot; refers to cross entropy loss ; 2) &quot;W_CE_DICE&quot; refers to cross entropy and dice losses together with a weight term on each one (that must sum 1) to calculate the total loss value ; 3) &quot;MASKED_BCE&quot; refers to a binary cross-entropy loss masking pixels of value 2 out</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Loss type", None))
        self.det_loss_type_input.setItemText(0, QCoreApplication.translate("MainWindow", u"CE", None))
        self.det_loss_type_input.setItemText(1, QCoreApplication.translate("MainWindow", u"MASKED_BCE", None))
        self.det_loss_type_input.setItemText(2, QCoreApplication.translate("MainWindow", u"W_CE_DICE", None))

        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Detection options", None))
#if QT_CONFIG(tooltip)
        self.deno_n2v_perc_pix_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">This variable corresponds to </span><span style=\" font-size:12pt; font-weight:600;\">n2v_perc_pix</span><span style=\" font-size:12pt;\"> from </span><a href=\"https://arxiv.org/abs/1811.10980\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Noise2Void</span></a><span style=\" font-size:12pt;\">. It explanation is as follows: for faster training multiple pixels per input patch can be manipulated. In our experiments we manipulated about 0.198% of the input pixels per patch. For a patch size of 64 by 64 pixels this corresponds to about 8 pixels. This fraction can be tuned via this variable. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deno_n2v_perc_pix_label.setText(QCoreApplication.translate("MainWindow", u"Percentage of pixels to manipulate ", None))
#if QT_CONFIG(tooltip)
        self.deno_n2v_manipulator_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">This variable corresponds to </span><span style=\" font-size:12pt; font-weight:600;\">n2v_manipulator</span><span style=\" font-size:12pt;\"> from </span><a href=\"https://arxiv.org/abs/1811.10980\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Noise2Void</span></a><span style=\" font-size:12pt;\">. Most pixel manipulators will compute the replacement value based on a neighborhood and this variable controls how to do that</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deno_n2v_manipulator_label.setText(QCoreApplication.translate("MainWindow", u"Type of manipulator", None))
#if QT_CONFIG(tooltip)
        self.deno_n2v_neighborhood_radius_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">This variable corresponds to </span><span style=\" font-size:12pt; font-weight:600;\">n2v_neighborhood_radius</span><span style=\" font-size:12pt;\"> from </span><a href=\"https://arxiv.org/abs/1811.10980\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Noise2Void</span></a><span style=\" font-size:12pt;\">. Size of the neighborhood to compute the replacement</span><span style=\" font-size:12pt; font-style:italic;\">. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deno_n2v_neighborhood_radius_label.setText(QCoreApplication.translate("MainWindow", u"Neighborhood radius", None))
#if QT_CONFIG(tooltip)
        self.deno_n2v_neighborhood_struct_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To apply a structured mask as is proposed in </span><a href=\"https://arxiv.org/abs/1811.10980\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Noise2Void</span></a><span style=\" font-size:12pt;\"> to alleviate the limitation of the method of not removing effectively the structured noise (section 4.4 of their paper). </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deno_n2v_neighborhood_struct_label.setText(QCoreApplication.translate("MainWindow", u"Structmask", None))
        self.deno_n2v_neighborhood_struct_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.deno_n2v_neighborhood_struct_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.deno_n2v_neighborhood_radius_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.deno_n2v_perc_pix_input.setText(QCoreApplication.translate("MainWindow", u"0.198", None))
        self.deno_n2v_manipulator_input.setItemText(0, QCoreApplication.translate("MainWindow", u"uniform_withCP", None))
        self.deno_n2v_manipulator_input.setItemText(1, QCoreApplication.translate("MainWindow", u"uniform_withoutCP", None))
        self.deno_n2v_manipulator_input.setItemText(2, QCoreApplication.translate("MainWindow", u"normal_additive", None))
        self.deno_n2v_manipulator_input.setItemText(3, QCoreApplication.translate("MainWindow", u"normal_fitted", None))
        self.deno_n2v_manipulator_input.setItemText(4, QCoreApplication.translate("MainWindow", u"normal_withoutCP", None))
        self.deno_n2v_manipulator_input.setItemText(5, QCoreApplication.translate("MainWindow", u"mean", None))
        self.deno_n2v_manipulator_input.setItemText(6, QCoreApplication.translate("MainWindow", u"median", None))
        self.deno_n2v_manipulator_input.setItemText(7, QCoreApplication.translate("MainWindow", u"identity", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Noise2Void specific parameters", None))
#if QT_CONFIG(tooltip)
        self.sr_upscaling_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Times to upscale the input image to obtain the result</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sr_upscaling_label.setText(QCoreApplication.translate("MainWindow", u"Upscaling", None))
        self.sr_upscaling_input.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.sr_upscaling_input.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))

        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Model output options", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Pretext task GT creation options", None))
#if QT_CONFIG(tooltip)
        self.ssl_resizing_factor_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Downsizing factor to reshape the image. It will be downsampled and upsampled again by this factor so the quality of the image is worsens</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ssl_resizing_factor_label.setText(QCoreApplication.translate("MainWindow", u"Resizing factor", None))
        self.ssl_noise_input.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
#if QT_CONFIG(tooltip)
        self.ssl_noise_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Number between [0, 1] indicating the std of the Gaussian noise N(0,std). </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ssl_noise_label.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.ssl_resizing_factor_input.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.ssl_resizing_factor_input.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.ssl_resizing_factor_input.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"There are no specific options for classification", None))
        self.train_tab_widget.setTabText(self.train_tab_widget.indexOf(self.train_workflow_specific_tab), QCoreApplication.translate("MainWindow", u"Workflow specific options", None))
#if QT_CONFIG(tooltip)
        self.label_81.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to enable the training phase or not</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Enable test phase", None))
        self.enable_test_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.enable_test_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Test data", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Post-processing options", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Test phase", None))
#if QT_CONFIG(tooltip)
        self.test_median_padding_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to use median values to fill padded pixels or reflect it</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_median_padding_label.setText(QCoreApplication.translate("MainWindow", u"Median padding", None))
#if QT_CONFIG(tooltip)
        self.test_overlap_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Test data resolution. Currently not used in the code, but added just in case it is needed in a future. If defined it need to be (y,x)/(z,y,x) and needs to be to be a 2D tuple when in 2D problems and 3D tuple when in 3D problems</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_overlap_label.setText(QCoreApplication.translate("MainWindow", u"Overlap", None))
#if QT_CONFIG(tooltip)
        self.test_resolution_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Test data resolution. Currently not used in the code, but added just in case it is needed in a future. If defined it need to be (y,x)/(z,y,x) and needs to be to be a 2D tuple when in 2D problems and 3D tuple when in 3D problems</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_resolution_label.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
#if QT_CONFIG(tooltip)
        self.test_padding_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Test padding to be done in (y,x) for 2D problems and (z,y,x) for 3D ones when reconstructing train data. Useful to avoid patch border effect. Parentheses are needed. A good value should be the patch size divided by 8. For instance, if the path size is (256,256,1) a good value can be (32,32)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_padding_label.setText(QCoreApplication.translate("MainWindow", u"Padding", None))
#if QT_CONFIG(tooltip)
        self.test_argmax_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to apply argmax to the predicted images </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_argmax_label.setText(QCoreApplication.translate("MainWindow", u"Argmax to output", None))
        self.test_argmax_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_argmax_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.test_median_padding_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_median_padding_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.test_apply_bin_mask_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_apply_bin_mask_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.test_apply_bin_mask_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply a binary mask to remove possible segmentation outside it</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_apply_bin_mask_label.setText(QCoreApplication.translate("MainWindow", u"Apply binary mask", None))
#if QT_CONFIG(tooltip)
        self.test_full_image_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To fed the network with the complete image instead of doing in patch by patch with 'per patch' and 'merge patches' options. It can only be done with 2D images, as the 3D ones can normally not be fit in the GPU </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_full_image_label.setText(QCoreApplication.translate("MainWindow", u"Full images", None))
        self.test_full_image_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.test_full_image_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.test_merge_patches_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_merge_patches_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.test_merge_patches_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Calculate metrics when all the patches are merged. It can slightly vary from 'per patch' calculation</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_merge_patches_label.setText(QCoreApplication.translate("MainWindow", u"Merge patches", None))
#if QT_CONFIG(tooltip)
        self.test_evaluate_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to evaluate model metrics, i.e. test loss and test metric (which can be, for instance, the IoU in a semantic segmentation workflow)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_evaluate_label.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.test_evaluate_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.test_evaluate_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.test_per_patch_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Calculate metrics per patch</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_per_patch_label.setText(QCoreApplication.translate("MainWindow", u"Per patch", None))
        self.test_per_patch_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_per_patch_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.test_reduce_memory_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tries to reduce the memory footprint by separating crop/merge operations (it is slower)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_reduce_memory_label.setText(QCoreApplication.translate("MainWindow", u"Reduce memory", None))
#if QT_CONFIG(tooltip)
        self.test_tta_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Make test-time augmentation. Infer over 8 possible rotations for 2D img and 16 when 3D. This takes more time to produce each test samples but it should achieve more robust results</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_tta_label.setText(QCoreApplication.translate("MainWindow", u"Test time augmentation", None))
        self.test_tta_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_tta_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.test_2d_as_3d_stack_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_2d_as_3d_stack_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.test_2d_as_3d_stack_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Stack 2D images into a 3D image and then process it entirely instead of going image per image. This stacks images that have been merged with 'TEST.STATS.MERGE_PATCHES' = True or 'TEST.STATS.FULL_IMG' (priorizes this later)</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_2d_as_3d_stack_label.setText(QCoreApplication.translate("MainWindow", u"Analize 2D images as 3D stack", None))
        self.test_verbose_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.test_verbose_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.test_verbose_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Enable verbosity to print more detailed information</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_verbose_label.setText(QCoreApplication.translate("MainWindow", u"Verbose", None))
        self.test_reduce_memory_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_reduce_memory_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Test metrics", None))
        self.train_advanced_label_2.setText(QCoreApplication.translate("MainWindow", u"Advanced options", None))
        self.test_advanced_bn.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Test data", None))
#if QT_CONFIG(tooltip)
        self.use_val_as_test.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to use validation data as test instead of trying to load test from 'Image path' and 'GT path'. Validation needs to be set as cross validation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_val_as_test.setText(QCoreApplication.translate("MainWindow", u"Use validation as test", None))
        self.test_data_gt_input_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.test_data_gt_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to load the test gt data from</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_data_gt_label.setText(QCoreApplication.translate("MainWindow", u"GT path", None))
#if QT_CONFIG(tooltip)
        self.test_data_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to load the test data from</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_data_label.setText(QCoreApplication.translate("MainWindow", u"Image path", None))
#if QT_CONFIG(tooltip)
        self.test_data_in_memory_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Wheter the test data is fully loaded in memory or processed file by file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_data_in_memory_label.setText(QCoreApplication.translate("MainWindow", u"In memory", None))
        self.test_data_input_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.test_data_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">images</span></p></body></html>", None))
        self.test_data_gt_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Math TeX Gyre'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">gt</span></p></body></html>", None))
        self.test_data_in_memory_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_data_in_memory_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.test_exists_gt_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether there is a ground truth for the test data or not. If so, the model performance will be evaluated comparing the predictions to the ground truth data.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.test_exists_gt_label.setText(QCoreApplication.translate("MainWindow", u"Exists GT", None))
        self.use_val_as_test_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.use_val_as_test_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.test_exists_gt_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.test_exists_gt_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.test_tab_widget.setTabText(self.test_tab_widget.indexOf(self.test_general_options_tab), QCoreApplication.translate("MainWindow", u"General options", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Test data options", None))
        self.sem_seg_check_data_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.sem_seg_check_data_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.sem_seg_check_data_label.setText(QCoreApplication.translate("MainWindow", u"Check data", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Post-processing options", None))
#if QT_CONFIG(tooltip)
        self.sem_seg_yz_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply Y and Z axes filtering. It usually improves 3D output for 2D models when 'ANALIZE_2D_IMGS_AS_3D_STACK' was selected </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sem_seg_yz_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Y and Z axis filtering", None))
#if QT_CONFIG(tooltip)
        self.sem_seg_z_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply Z axis filtering. It usually improves 3D output for 2D models when 'ANALIZE_2D_IMGS_AS_3D_STACK' was selected </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sem_seg_z_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Z axis filtering", None))
#if QT_CONFIG(tooltip)
        self.sem_seg_yz_filtering_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of Y and Z axes filter. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sem_seg_yz_filtering_size_label.setText(QCoreApplication.translate("MainWindow", u"Y and Z axis filtering size", None))
#if QT_CONFIG(tooltip)
        self.sem_seg_z_filtering_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of Z axis filter. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sem_seg_z_filtering_size_label.setText(QCoreApplication.translate("MainWindow", u"Z axis filtering size ", None))
        self.sem_seg_z_filtering_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.sem_seg_yz_filtering_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.sem_seg_yz_filtering_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.sem_seg_yz_filtering_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.sem_seg_z_filtering_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.sem_seg_z_filtering_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Data channels", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Watershed instance processing options", None))
        self.inst_seg_repare_large_blobs_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_repare_large_blobs_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Set it to try to repare large instances by merging their neighbors with them and removing possible central holes. Its value determines which instances are going to be repared by size (number of pixels that compose the instance). This option is useful when PROBLEM.INSTANCE_SEG.DATA_CHANNELS is 'BP', as multiple central seeds may appear in big instances. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_repare_large_blobs_label.setText(QCoreApplication.translate("MainWindow", u"Repare large blobs ", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_circularity_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Minimum circularity that each instance need to haveto not be removed from the image. It removed, it will be marked as 'Strange' in the output csv files. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_circularity_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Circularity filtering", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_voronoi_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to apply Voronoi based on a mask that is defined using 'BC' or 'M' channels</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_voronoi_label.setText(QCoreApplication.translate("MainWindow", u"Apply Voronoi on mask", None))
        self.inst_seg_voronoi_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_voronoi_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.inst_seg_circularity_filtering_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_yz_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply Y and Z axes filtering. It usually improves 3D output for 2D models when 'ANALIZE_2D_IMGS_AS_3D_STACK' was selected </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_yz_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Y and Z axis filtering", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_yz_filtering_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of Y and Z axes filter. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_yz_filtering_size_label.setText(QCoreApplication.translate("MainWindow", u"Y and Z axis filtering size", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_z_filtering_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of Z axis filter. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_z_filtering_size_label.setText(QCoreApplication.translate("MainWindow", u"Z axis filtering size ", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_z_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply Z axis filtering. It usually improves 3D output for 2D models when 'ANALIZE_2D_IMGS_AS_3D_STACK' was selected </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_z_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Z axis filtering", None))
        self.inst_seg_z_filtering_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.inst_seg_yz_filtering_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.inst_seg_yz_filtering_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_yz_filtering_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.inst_seg_z_filtering_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_z_filtering_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.inst_seg_remove_close_points_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To remove close points to each other</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_remove_close_points_label.setText(QCoreApplication.translate("MainWindow", u"Remove close points", None))
        self.inst_seg_remove_close_points_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_remove_close_points_input.setItemText(1, QCoreApplication.translate("MainWindow", u"True", None))

#if QT_CONFIG(tooltip)
        self.inst_seg_remove_close_points_radius_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Distance between points to be considered the same. The distance calculated is the euclidean and it takes into account the data resolution. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a list of positive floats (one float per class). E.g [15.3,10.0] if there are two classes</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_remove_close_points_radius_label.setText(QCoreApplication.translate("MainWindow", u"Remove close points radius", None))
        self.inst_seg_remove_close_points_radius_input.setText(QCoreApplication.translate("MainWindow", u"[-1.0]", None))
        self.inst_seg_b_channel_th_input.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_c_channel_th_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Controls channel 'C', i.e. contour channel, in the creation of the MW seeds. This value willl be used to binarize that channel. Find a more complete description of its usage in our documentation (</span><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Instance segmentation channels)</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000;\">.</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\"/></a><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_c_channel_th_label.setText(QCoreApplication.translate("MainWindow", u"Contour threshold", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_d_channel_th_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Controls channel 'D', i.e. distance channel, in the creation of the MW seeds. This value willl be used to binarize that channel. Find a more complete description of its usage in our documentation (</span><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Instance segmentation channels)</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000;\">.</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\"/></a><span style=\" font-size:12pt; font-weight:600;\">Must be a positive float larger than 0.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_d_channel_th_label.setText(QCoreApplication.translate("MainWindow", u"Distance threshold", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_fore_mask_th_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Controls how much the seeds can grow by creating a mask from binarizing channel 'B'. This value willl be used to binarize that channel. Find a more complete description of its usage in our documentation (</span><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Instance segmentation channels)</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000;\">. </span></a><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_fore_mask_th_label.setText(QCoreApplication.translate("MainWindow", u"Foreground mask threshold", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_b_channel_th_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Controls channel 'B', binary mask channel, in the creation of the MW seeds. This value willl be used to binarize that channel. Find a more complete description of its usage in our documentation (</span><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Instance segmentation channels)</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; color:#000000;\">.</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; color:#0000ff;\"/></a><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_b_channel_th_label.setText(QCoreApplication.translate("MainWindow", u"Binary mask threshold", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_p_channel_th_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Controls channel 'P', i.e. central point channel, in the creation of the MW seeds. This value willl be used to binarize that channel. Find a more complete description of its usage in our documentation (</span><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Instance segmentation channels)</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000;\">.</span></a><a href=\"https://biapy.readthedocs.io/en/latest/workflows/instance_segmentation.html#problem-resolution\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\"/></a><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_p_channel_th_label.setText(QCoreApplication.translate("MainWindow", u"Central point threshold", None))
        self.inst_seg_d_channel_th_input.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.inst_seg_c_channel_th_input.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.inst_seg_fore_mask_th_input.setText(QCoreApplication.translate("MainWindow", u"0.3", None))
        self.inst_seg_p_channel_th_input.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_fore_ero_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Radius to dilate the foreground mask</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_fore_ero_label.setText(QCoreApplication.translate("MainWindow", u"Foreground erosion radius", None))
        self.inst_seg_moph_op_rad_input.setText(QCoreApplication.translate("MainWindow", u"[]", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_moph_op_rad_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sequence of ints to determine the radius of the erosion or dilation for instance seeds. </span><span style=\" font-size:12pt; font-weight:600;\">E.g. [2,3]</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_moph_op_rad_label.setText(QCoreApplication.translate("MainWindow", u"Morphological operations radius", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_before_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of small objects to be removed before doing watershed</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_before_size_label.setText(QCoreApplication.translate("MainWindow", u"Small object size (before growth)", None))
        self.inst_seg_small_obj_fil_before_size_input.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.inst_seg_ero_dil_fore_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_ero_dil_fore_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_after_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of small objects to be removed after doing watershed</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_after_size_label.setText(QCoreApplication.translate("MainWindow", u"Small object size (after growth)", None))
        self.inst_seg_small_obj_fil_after_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_small_obj_fil_after_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.inst_seg_ero_dil_fore_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To erode and dilate the foreground mask before using marker controlled watershed. The idea is to remove the small holes  that may be produced so the instances grow without them</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_ero_dil_fore_label.setText(QCoreApplication.translate("MainWindow", u"Erode and dilate foreground", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_moph_op_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sequence of string to determine the morphological filters to apply to instance seeds. They will be done in that order. Possible options 'dilate' and 'erode'.</span><span style=\" font-size:12pt; font-weight:600;\"> E.g. ['erode','dilate'] to erode first and dilate later.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_moph_op_label.setText(QCoreApplication.translate("MainWindow", u"Morphological operations to seeds", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_after_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to remove objects after watershed </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_after_label.setText(QCoreApplication.translate("MainWindow", u"Small objects filtering after growth", None))
        self.inst_seg_small_obj_fil_after_size_input.setText(QCoreApplication.translate("MainWindow", u"100", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_fore_dil_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Radius to erode the foreground mask</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_fore_dil_label.setText(QCoreApplication.translate("MainWindow", u"Foreground dilation raidus", None))
        self.inst_seg_fore_dil_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.inst_seg_small_obj_fil_before_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.inst_seg_small_obj_fil_before_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.inst_seg_save_water_files_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to save watershed check files</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_save_water_files_label.setText(QCoreApplication.translate("MainWindow", u"Save watershed files", None))
        self.inst_seg_fore_ero_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_before_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to remove objects before watershed </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_small_obj_fil_before_label.setText(QCoreApplication.translate("MainWindow", u"Small objects filtering before growth", None))
        self.inst_seg_moph_op_input.setText(QCoreApplication.translate("MainWindow", u"[]", None))
        self.inst_seg_save_water_files_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.inst_seg_save_water_files_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Post-processing options", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_matching_stats_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to calculate matching statistics (average overlap, accuracy, recall, precision, etc.)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_matching_stats_label.setText(QCoreApplication.translate("MainWindow", u"Matching stats", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_matching_stats_ths_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Theshold of overlap to consider a TP when calculating the metrics. If more than one value is provided the process is repeated with each of the threshold values</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_matching_stats_ths_label.setText(QCoreApplication.translate("MainWindow", u"Matching stats thresholds", None))
#if QT_CONFIG(tooltip)
        self.inst_seg_matching_stats_colores_img_ths_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Decide in which thresholds to create a colored image of the TPs, FNs and FPs. The green values correspond to TP, blue to FP and red to FN. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inst_seg_matching_stats_colores_img_ths_label.setText(QCoreApplication.translate("MainWindow", u"Matching stats colored image threshold", None))
        self.inst_seg_matching_stats_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.inst_seg_matching_stats_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.inst_seg_matching_stats_ths_input.setText(QCoreApplication.translate("MainWindow", u"[0.3, 0.5, 0.75]", None))
        self.inst_seg_matching_stats_colores_img_ths_input.setText(QCoreApplication.translate("MainWindow", u"[0.3]", None))
        self.inst_seg_metrics_label.setText(QCoreApplication.translate("MainWindow", u"Metrics options", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Post-processing options", None))
#if QT_CONFIG(tooltip)
        self.label_108.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Minimum circularity that each instance need to haveto not be removed from the image. It removed, it will be marked as 'Strange' in the output csv files. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a float between 0 and 1.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Circularity filtering", None))
        self.det_circularity_filtering_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.det_watershed_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.det_watershed_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.det_watershed_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to apply a watershed to grow the points detected</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_watershed_label.setText(QCoreApplication.translate("MainWindow", u"Apply watershed", None))
#if QT_CONFIG(tooltip)
        self.det_watershed_first_dilation_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Structure per each class to dilate the initial seeds before watershed</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_watershed_first_dilation_label.setText(QCoreApplication.translate("MainWindow", u"Watershed first dilation", None))
#if QT_CONFIG(tooltip)
        self.det_watershed_donuts_patch_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Patch shape to extract all donuts type cells. It needs to be a bit greater than bigest donuts type cell so all of them can be contained in this patch. This is used to analize that area for each point of class 'DET_WATERSHED_DONUTS_CLASSES'. </span><span style=\" font-size:12pt; font-weight:600;\">Must be in (y,x) for 2D problems and (z,y,x) for 3D ones. E.g. [10,100,100] for a 3D problem</span></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_watershed_donuts_patch_label.setText(QCoreApplication.translate("MainWindow", u"Watershed donuts patch", None))
#if QT_CONFIG(tooltip)
        self.det_watershed_donuts_classes_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">List of classes to be considered as 'donuts'. For those class points, the 'donuts' type cell means that their nucleus is to big and that the seeds need to be dilated more so the watershed can grow the instances properly.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_watershed_donuts_classes_label.setText(QCoreApplication.translate("MainWindow", u"Watershed donuts classes", None))
#if QT_CONFIG(tooltip)
        self.det_watershed_donuts_nucleus_diam_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Diameter (in pixels) that a cell need to have to be considered as donuts type</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_watershed_donuts_nucleus_diam_label.setText(QCoreApplication.translate("MainWindow", u"Watershed donuts nucleus diameter", None))
        self.det_watershed_first_dilation_input.setText(QCoreApplication.translate("MainWindow", u"[[-1,-1],]", None))
        self.det_watershed_donuts_classes_input.setText(QCoreApplication.translate("MainWindow", u"[-1]", None))
        self.det_watershed_donuts_patch_input.setText(QCoreApplication.translate("MainWindow", u"[13,120,120]", None))
        self.det_watershed_donuts_nucleus_diam_input.setText(QCoreApplication.translate("MainWindow", u"30", None))
#if QT_CONFIG(tooltip)
        self.det_z_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply Z axis filtering. It usually improves 3D output for 2D models when 'ANALIZE_2D_IMGS_AS_3D_STACK' was selected </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_z_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Z axis filtering", None))
#if QT_CONFIG(tooltip)
        self.det_yz_filtering_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Apply Y and Z axes filtering. It usually improves 3D output for 2D models when 'ANALIZE_2D_IMGS_AS_3D_STACK' was selected </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_yz_filtering_label.setText(QCoreApplication.translate("MainWindow", u"Y and Z axis filtering", None))
        self.det_z_filtering_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.det_z_filtering_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.det_yz_filtering_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.det_yz_filtering_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

        self.det_z_filtering_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(tooltip)
        self.det_z_filtering_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of Z axis filter. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_z_filtering_size_label.setText(QCoreApplication.translate("MainWindow", u"Z axis filtering size ", None))
        self.det_yz_filtering_size_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(tooltip)
        self.det_yz_filtering_size_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Size of Y and Z axes filter. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a positive integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_yz_filtering_size_label.setText(QCoreApplication.translate("MainWindow", u"Y and Z axis filtering size", None))
        self.det_remove_close_points_radius_input.setText(QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.det_remove_close_points_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">To remove close points to each other</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_remove_close_points_label.setText(QCoreApplication.translate("MainWindow", u"Remove close points", None))
#if QT_CONFIG(tooltip)
        self.det_remove_close_points_radius_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Distance between points to be considered the same. The distance calculated is the euclidean and it takes into account the data resolution. </span><span style=\" font-size:12pt; font-weight:600;\">Must be a list of positive floats (one float per class). E.g [15.3,10.0] if there are two classes</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_remove_close_points_radius_label.setText(QCoreApplication.translate("MainWindow", u"Remove close points radius", None))
        self.det_remove_close_points_input.setItemText(0, QCoreApplication.translate("MainWindow", u"No", None))
        self.det_remove_close_points_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))

#if QT_CONFIG(tooltip)
        self.det_data_watetshed_check_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to save watershed check files</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_data_watetshed_check_label.setText(QCoreApplication.translate("MainWindow", u"Check watershed data", None))
        self.det_data_watetshed_check_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.det_data_watetshed_check_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Output options", None))
        self.det_metrics_label.setText(QCoreApplication.translate("MainWindow", u"Metrics options", None))
#if QT_CONFIG(tooltip)
        self.det_tolerance_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maximum distance far away from a GT point to consider a point as a true positive</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_tolerance_label.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.det_tolerance_input.setText(QCoreApplication.translate("MainWindow", u"[10]", None))
#if QT_CONFIG(tooltip)
        self.det_local_max_coords_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Whether to return local maximum coords</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_local_max_coords_label.setText(QCoreApplication.translate("MainWindow", u"Local maximum coords", None))
        self.det_min_th_to_be_peak_input.setText(QCoreApplication.translate("MainWindow", u"[0.2]", None))
#if QT_CONFIG(tooltip)
        self.det_min_th_to_be_peak_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Minimun value to consider a point as a peak. Corresponds to 'threshold_abs' argument of the function 'peak_local_max' of skimage.feature</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.det_min_th_to_be_peak_label.setText(QCoreApplication.translate("MainWindow", u"Min threshold to be peak", None))
        self.det_local_max_coords_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.det_local_max_coords_input.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_93.setText(QCoreApplication.translate("MainWindow", u"There are no specific options for denoising", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"There are no specific options for super resolution", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"There are no specific options for self-supervised learning", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"There are no specific options for classification", None))
        self.test_tab_widget.setTabText(self.test_tab_widget.indexOf(self.test_workflow_specific_tab), QCoreApplication.translate("MainWindow", u"Workflow specific options", None))
        self.back_bn.setText("")
        self.continue_bn.setText(QCoreApplication.translate("MainWindow", u"CONTINUE", None))
        self.window1_bn.setText("")
        self.window2_bn.setText("")
        self.window3_bn.setText("")
        self.window4_bn.setText("")
#if QT_CONFIG(tooltip)
        self.run_biapy_docker_bn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.run_biapy_docker_bn.setText(QCoreApplication.translate("MainWindow", u"RUN BiaPy", None))
        self.check_yaml_file_bn.setText(QCoreApplication.translate("MainWindow", u"Check file", None))
        self.check_yaml_file_errors_label.setText("")
#if QT_CONFIG(tooltip)
        self.label_138.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Name of the job. It will be used to create a folder in the output path you selected. For instance, if the job name was set to &quot;my_semantic_segmentation&quot;, and if the output folder to save the results is &quot;/home/user/Downloads&quot;, all results of the experiment will be placed at : /home/user/Downloads/my_semantic_segmentation </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Job name", None))
        self.examine_yaml_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.output_folder_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to store the results. If you complete the proccess of creating a new one automatically this will point to the folder where you select to save the YAML file. It will be used to create a folder in the output path you selected. For instance, if the job name was set to &quot;my_semantic_segmentation&quot;, and if the output folder to save the results is &quot;/home/user/Downloads&quot;, all results of the experiment will be placed at : /home/user/Downloads/my_semantic_segmentation </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.output_folder_label.setText(QCoreApplication.translate("MainWindow", u"Output folder to save the results", None))
#if QT_CONFIG(tooltip)
        self.select_yaml_label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">YAML configuration file to run BiaPy with. If you completed the proccess of creating a new YAML file this value will be set pointing to file. However, you can change it too.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.select_yaml_label.setText(QCoreApplication.translate("MainWindow", u"Select YAML configuration file", None))
        self.output_folder_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
    # retranslateUi

