# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_modify_yaml.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Modify_YAML(object):
    def setupUi(self, Modify_YAML):
        if not Modify_YAML.objectName():
            Modify_YAML.setObjectName(u"Modify_YAML")
        Modify_YAML.resize(938, 731)
        self.verticalLayout = QVBoxLayout(Modify_YAML)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QFrame(Modify_YAML)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFrameShape(QFrame.Shape.NoFrame)
        self.centralwidget.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 0))
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.icon_label = QLabel(self.frame_top)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(40, 40))
        self.icon_label.setMaximumSize(QSize(40, 40))
        self.icon_label.setFrameShape(QFrame.Shape.NoFrame)
        self.icon_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_label)

        self.window_des_label = QLabel(self.frame_top)
        self.window_des_label.setObjectName(u"window_des_label")
        font = QFont()
        font.setFamilies([u"DejaVu Math TeX Gyre"])
        font.setPointSize(14)
        font.setBold(False)
        self.window_des_label.setFont(font)

        self.horizontalLayout.addWidget(self.window_des_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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
        self.bn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.bn_close)


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        font1 = QFont()
        font1.setFamilies([u"DejaVu Math TeX Gyre"])
        font1.setPointSize(12)
        self.frame_bottom.setFont(font1)
        self.frame_bottom.setStyleSheet(u"")
        self.frame_bottom.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.scrollArea = QScrollArea(self.frame_bottom)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 920, 627))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 15, -1, -1)
        self.train_label = QLabel(self.frame_2)
        self.train_label.setObjectName(u"train_label")
        self.train_label.setMaximumSize(QSize(150, 16777215))
        self.train_label.setFont(font1)

        self.verticalLayout_5.addWidget(self.train_label)

        self.train_frame = QFrame(self.frame_2)
        self.train_frame.setObjectName(u"train_frame")
        self.train_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.train_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.train_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.train_path_frame = QFrame(self.train_frame)
        self.train_path_frame.setObjectName(u"train_path_frame")
        self.train_path_frame.setMaximumSize(QSize(16777215, 16777215))
        self.train_path_frame.setFont(font1)
        self.train_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.train_path_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.train_path_frame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.train_data_label = QLabel(self.train_path_frame)
        self.train_data_label.setObjectName(u"train_data_label")
        self.train_data_label.setMinimumSize(QSize(190, 0))
        self.train_data_label.setMaximumSize(QSize(16777215, 16777215))
        self.train_data_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.train_data_label)

        self.train_data_info = QPushButton(self.train_path_frame)
        self.train_data_info.setObjectName(u"train_data_info")
        self.train_data_info.setMinimumSize(QSize(30, 30))
        self.train_data_info.setMaximumSize(QSize(30, 30))
        self.train_data_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_5.addWidget(self.train_data_info)

        self.DATA__TRAIN__PATH__INPUT = QLineEdit(self.train_path_frame)
        self.DATA__TRAIN__PATH__INPUT.setObjectName(u"DATA__TRAIN__PATH__INPUT")
        self.DATA__TRAIN__PATH__INPUT.setMinimumSize(QSize(500, 30))
        self.DATA__TRAIN__PATH__INPUT.setMaximumSize(QSize(500, 30))
        self.DATA__TRAIN__PATH__INPUT.setFont(font1)

        self.horizontalLayout_5.addWidget(self.DATA__TRAIN__PATH__INPUT)

        self.train_data_input_browse_bn = QPushButton(self.train_path_frame)
        self.train_data_input_browse_bn.setObjectName(u"train_data_input_browse_bn")
        self.train_data_input_browse_bn.setMinimumSize(QSize(0, 30))
        self.train_data_input_browse_bn.setMaximumSize(QSize(16777215, 30))
        self.train_data_input_browse_bn.setFont(font1)

        self.horizontalLayout_5.addWidget(self.train_data_input_browse_bn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addWidget(self.train_path_frame)

        self.train_gt_path_frame = QFrame(self.train_frame)
        self.train_gt_path_frame.setObjectName(u"train_gt_path_frame")
        self.train_gt_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.train_gt_path_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.train_gt_path_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.train_gt_label = QLabel(self.train_gt_path_frame)
        self.train_gt_label.setObjectName(u"train_gt_label")
        self.train_gt_label.setMinimumSize(QSize(190, 0))
        self.train_gt_label.setMaximumSize(QSize(16777215, 16777215))
        self.train_gt_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.train_gt_label)

        self.train_gt_info = QPushButton(self.train_gt_path_frame)
        self.train_gt_info.setObjectName(u"train_gt_info")
        self.train_gt_info.setMinimumSize(QSize(30, 30))
        self.train_gt_info.setMaximumSize(QSize(30, 30))
        self.train_gt_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_4.addWidget(self.train_gt_info)

        self.DATA__TRAIN__GT_PATH__INPUT = QLineEdit(self.train_gt_path_frame)
        self.DATA__TRAIN__GT_PATH__INPUT.setObjectName(u"DATA__TRAIN__GT_PATH__INPUT")
        self.DATA__TRAIN__GT_PATH__INPUT.setMinimumSize(QSize(500, 30))
        self.DATA__TRAIN__GT_PATH__INPUT.setMaximumSize(QSize(500, 30))
        self.DATA__TRAIN__GT_PATH__INPUT.setFont(font1)

        self.horizontalLayout_4.addWidget(self.DATA__TRAIN__GT_PATH__INPUT)

        self.train_data_gt_input_browse_bn = QPushButton(self.train_gt_path_frame)
        self.train_data_gt_input_browse_bn.setObjectName(u"train_data_gt_input_browse_bn")
        self.train_data_gt_input_browse_bn.setMinimumSize(QSize(0, 30))
        self.train_data_gt_input_browse_bn.setMaximumSize(QSize(130, 30))
        self.train_data_gt_input_browse_bn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.train_data_gt_input_browse_bn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addWidget(self.train_gt_path_frame)


        self.verticalLayout_5.addWidget(self.train_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.val_label = QLabel(self.frame_2)
        self.val_label.setObjectName(u"val_label")
        self.val_label.setMaximumSize(QSize(150, 16777215))
        self.val_label.setFont(font1)

        self.verticalLayout_5.addWidget(self.val_label)

        self.val_frame = QFrame(self.frame_2)
        self.val_frame.setObjectName(u"val_frame")
        self.val_frame.setMinimumSize(QSize(0, 0))
        self.val_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.val_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.val_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.val_path_frame = QFrame(self.val_frame)
        self.val_path_frame.setObjectName(u"val_path_frame")
        self.val_path_frame.setMinimumSize(QSize(0, 0))
        self.val_path_frame.setMaximumSize(QSize(16777215, 16777215))
        self.val_path_frame.setFont(font1)
        self.val_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.val_path_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.val_path_frame)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.DATA__VAL__PATH__LABEL = QLabel(self.val_path_frame)
        self.DATA__VAL__PATH__LABEL.setObjectName(u"DATA__VAL__PATH__LABEL")
        self.DATA__VAL__PATH__LABEL.setMinimumSize(QSize(190, 0))
        self.DATA__VAL__PATH__LABEL.setFont(font1)
        self.DATA__VAL__PATH__LABEL.setIndent(0)

        self.horizontalLayout_6.addWidget(self.DATA__VAL__PATH__LABEL)

        self.DATA__VAL__PATH__INFO = QPushButton(self.val_path_frame)
        self.DATA__VAL__PATH__INFO.setObjectName(u"DATA__VAL__PATH__INFO")
        self.DATA__VAL__PATH__INFO.setMinimumSize(QSize(30, 30))
        self.DATA__VAL__PATH__INFO.setMaximumSize(QSize(30, 30))
        self.DATA__VAL__PATH__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.DATA__VAL__PATH__INFO)

        self.DATA__VAL__PATH__INPUT = QLineEdit(self.val_path_frame)
        self.DATA__VAL__PATH__INPUT.setObjectName(u"DATA__VAL__PATH__INPUT")
        self.DATA__VAL__PATH__INPUT.setMinimumSize(QSize(500, 30))
        self.DATA__VAL__PATH__INPUT.setMaximumSize(QSize(450, 30))
        self.DATA__VAL__PATH__INPUT.setFont(font1)

        self.horizontalLayout_6.addWidget(self.DATA__VAL__PATH__INPUT)

        self.val_data_input_browse_bn = QPushButton(self.val_path_frame)
        self.val_data_input_browse_bn.setObjectName(u"val_data_input_browse_bn")
        self.val_data_input_browse_bn.setMaximumSize(QSize(130, 30))
        self.val_data_input_browse_bn.setFont(font1)

        self.horizontalLayout_6.addWidget(self.val_data_input_browse_bn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addWidget(self.val_path_frame)

        self.val_gt_path_frame = QFrame(self.val_frame)
        self.val_gt_path_frame.setObjectName(u"val_gt_path_frame")
        self.val_gt_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.val_gt_path_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.val_gt_path_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.validation_data_gt_label = QLabel(self.val_gt_path_frame)
        self.validation_data_gt_label.setObjectName(u"validation_data_gt_label")
        self.validation_data_gt_label.setMinimumSize(QSize(190, 0))
        self.validation_data_gt_label.setFont(font1)
        self.validation_data_gt_label.setIndent(0)

        self.horizontalLayout_3.addWidget(self.validation_data_gt_label)

        self.validation_data_gt_info = QPushButton(self.val_gt_path_frame)
        self.validation_data_gt_info.setObjectName(u"validation_data_gt_info")
        self.validation_data_gt_info.setMinimumSize(QSize(30, 30))
        self.validation_data_gt_info.setMaximumSize(QSize(30, 30))
        self.validation_data_gt_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_3.addWidget(self.validation_data_gt_info)

        self.DATA__VAL__GT_PATH__INPUT = QLineEdit(self.val_gt_path_frame)
        self.DATA__VAL__GT_PATH__INPUT.setObjectName(u"DATA__VAL__GT_PATH__INPUT")
        self.DATA__VAL__GT_PATH__INPUT.setMinimumSize(QSize(500, 30))
        self.DATA__VAL__GT_PATH__INPUT.setMaximumSize(QSize(450, 30))
        self.DATA__VAL__GT_PATH__INPUT.setFont(font1)

        self.horizontalLayout_3.addWidget(self.DATA__VAL__GT_PATH__INPUT)

        self.val_data_gt_input_browse_bn = QPushButton(self.val_gt_path_frame)
        self.val_data_gt_input_browse_bn.setObjectName(u"val_data_gt_input_browse_bn")
        self.val_data_gt_input_browse_bn.setMaximumSize(QSize(130, 30))
        self.val_data_gt_input_browse_bn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.val_data_gt_input_browse_bn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addWidget(self.val_gt_path_frame)


        self.verticalLayout_5.addWidget(self.val_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.test_label = QLabel(self.frame_2)
        self.test_label.setObjectName(u"test_label")
        self.test_label.setMaximumSize(QSize(150, 16777215))
        self.test_label.setFont(font1)

        self.verticalLayout_5.addWidget(self.test_label)

        self.test_frame = QFrame(self.frame_2)
        self.test_frame.setObjectName(u"test_frame")
        self.test_frame.setMinimumSize(QSize(50, 0))
        self.test_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.test_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.test_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.test_path_frame = QFrame(self.test_frame)
        self.test_path_frame.setObjectName(u"test_path_frame")
        self.test_path_frame.setFont(font1)
        self.test_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.test_path_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.test_path_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.test_data_label = QLabel(self.test_path_frame)
        self.test_data_label.setObjectName(u"test_data_label")
        self.test_data_label.setMinimumSize(QSize(190, 0))
        self.test_data_label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.test_data_label)

        self.DATA__TEST__PATH__INFO = QPushButton(self.test_path_frame)
        self.DATA__TEST__PATH__INFO.setObjectName(u"DATA__TEST__PATH__INFO")
        self.DATA__TEST__PATH__INFO.setMinimumSize(QSize(30, 30))
        self.DATA__TEST__PATH__INFO.setMaximumSize(QSize(30, 30))
        self.DATA__TEST__PATH__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_8.addWidget(self.DATA__TEST__PATH__INFO)

        self.DATA__TEST__PATH__INPUT = QLineEdit(self.test_path_frame)
        self.DATA__TEST__PATH__INPUT.setObjectName(u"DATA__TEST__PATH__INPUT")
        self.DATA__TEST__PATH__INPUT.setMinimumSize(QSize(500, 30))
        self.DATA__TEST__PATH__INPUT.setMaximumSize(QSize(500, 30))
        self.DATA__TEST__PATH__INPUT.setFont(font1)

        self.horizontalLayout_8.addWidget(self.DATA__TEST__PATH__INPUT)

        self.test_data_input_browse_bn = QPushButton(self.test_path_frame)
        self.test_data_input_browse_bn.setObjectName(u"test_data_input_browse_bn")
        self.test_data_input_browse_bn.setMinimumSize(QSize(0, 30))
        self.test_data_input_browse_bn.setMaximumSize(QSize(16777215, 30))
        self.test_data_input_browse_bn.setFont(font1)

        self.horizontalLayout_8.addWidget(self.test_data_input_browse_bn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.test_path_frame)

        self.test_gt_path_frame = QFrame(self.test_frame)
        self.test_gt_path_frame.setObjectName(u"test_gt_path_frame")
        self.test_gt_path_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.test_gt_path_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.test_gt_path_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.test_data_gt_label = QLabel(self.test_gt_path_frame)
        self.test_data_gt_label.setObjectName(u"test_data_gt_label")
        self.test_data_gt_label.setMinimumSize(QSize(190, 0))
        self.test_data_gt_label.setFont(font1)
        self.test_data_gt_label.setIndent(0)

        self.horizontalLayout_7.addWidget(self.test_data_gt_label)

        self.DATA__TEST__GT_PATH__INFO = QPushButton(self.test_gt_path_frame)
        self.DATA__TEST__GT_PATH__INFO.setObjectName(u"DATA__TEST__GT_PATH__INFO")
        self.DATA__TEST__GT_PATH__INFO.setMinimumSize(QSize(30, 30))
        self.DATA__TEST__GT_PATH__INFO.setMaximumSize(QSize(30, 30))
        self.DATA__TEST__GT_PATH__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_7.addWidget(self.DATA__TEST__GT_PATH__INFO)

        self.DATA__TEST__GT_PATH__INPUT = QLineEdit(self.test_gt_path_frame)
        self.DATA__TEST__GT_PATH__INPUT.setObjectName(u"DATA__TEST__GT_PATH__INPUT")
        self.DATA__TEST__GT_PATH__INPUT.setMinimumSize(QSize(500, 30))
        self.DATA__TEST__GT_PATH__INPUT.setMaximumSize(QSize(500, 30))
        self.DATA__TEST__GT_PATH__INPUT.setFont(font1)

        self.horizontalLayout_7.addWidget(self.DATA__TEST__GT_PATH__INPUT)

        self.test_data_gt_input_browse_bn = QPushButton(self.test_gt_path_frame)
        self.test_data_gt_input_browse_bn.setObjectName(u"test_data_gt_input_browse_bn")
        self.test_data_gt_input_browse_bn.setMinimumSize(QSize(0, 30))
        self.test_data_gt_input_browse_bn.setMaximumSize(QSize(16777215, 30))
        self.test_data_gt_input_browse_bn.setFont(font1)

        self.horizontalLayout_7.addWidget(self.test_data_gt_input_browse_bn)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addWidget(self.test_gt_path_frame)


        self.verticalLayout_5.addWidget(self.test_frame)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.checkpoint_label = QLabel(self.frame_2)
        self.checkpoint_label.setObjectName(u"checkpoint_label")

        self.verticalLayout_5.addWidget(self.checkpoint_label)

        self.checkpoint_frame = QFrame(self.frame_2)
        self.checkpoint_frame.setObjectName(u"checkpoint_frame")
        self.checkpoint_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.checkpoint_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.checkpoint_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, -1, 9, -1)
        self.checkpoint_file_path_browse_label = QLabel(self.checkpoint_frame)
        self.checkpoint_file_path_browse_label.setObjectName(u"checkpoint_file_path_browse_label")
        self.checkpoint_file_path_browse_label.setMinimumSize(QSize(190, 0))
        self.checkpoint_file_path_browse_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.checkpoint_file_path_browse_label)

        self.PATHS__CHECKPOINT_FILE__INFO = QPushButton(self.checkpoint_frame)
        self.PATHS__CHECKPOINT_FILE__INFO.setObjectName(u"PATHS__CHECKPOINT_FILE__INFO")
        self.PATHS__CHECKPOINT_FILE__INFO.setMinimumSize(QSize(30, 30))
        self.PATHS__CHECKPOINT_FILE__INFO.setMaximumSize(QSize(30, 30))
        self.PATHS__CHECKPOINT_FILE__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.horizontalLayout_9.addWidget(self.PATHS__CHECKPOINT_FILE__INFO)

        self.PATHS__CHECKPOINT_FILE__INPUT = QLineEdit(self.checkpoint_frame)
        self.PATHS__CHECKPOINT_FILE__INPUT.setObjectName(u"PATHS__CHECKPOINT_FILE__INPUT")
        self.PATHS__CHECKPOINT_FILE__INPUT.setMinimumSize(QSize(500, 30))
        self.PATHS__CHECKPOINT_FILE__INPUT.setMaximumSize(QSize(400, 30))
        self.PATHS__CHECKPOINT_FILE__INPUT.setFont(font1)

        self.horizontalLayout_9.addWidget(self.PATHS__CHECKPOINT_FILE__INPUT)

        self.checkpoint_file_path_browse_bn = QPushButton(self.checkpoint_frame)
        self.checkpoint_file_path_browse_bn.setObjectName(u"checkpoint_file_path_browse_bn")
        self.checkpoint_file_path_browse_bn.setMinimumSize(QSize(0, 30))
        self.checkpoint_file_path_browse_bn.setMaximumSize(QSize(16777215, 16777215))
        self.checkpoint_file_path_browse_bn.setFont(font1)

        self.horizontalLayout_9.addWidget(self.checkpoint_file_path_browse_bn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addWidget(self.checkpoint_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.frame = QFrame(self.frame_bottom)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 15, 9, 15)
        self.cfg_file_label = QLabel(self.frame)
        self.cfg_file_label.setObjectName(u"cfg_file_label")

        self.horizontalLayout_2.addWidget(self.cfg_file_label)

        self.cfg_file_path = QLineEdit(self.frame)
        self.cfg_file_path.setObjectName(u"cfg_file_path")
        self.cfg_file_path.setMinimumSize(QSize(500, 30))
        self.cfg_file_path.setMaximumSize(QSize(500, 30))

        self.horizontalLayout_2.addWidget(self.cfg_file_path)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.create_config_bn = QPushButton(self.frame)
        self.create_config_bn.setObjectName(u"create_config_bn")
        self.create_config_bn.setMinimumSize(QSize(130, 30))
        self.create_config_bn.setMaximumSize(QSize(16777215, 16777215))
        self.create_config_bn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.create_config_bn)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(Modify_YAML)

        QMetaObject.connectSlotsByName(Modify_YAML)
    # setupUi

    def retranslateUi(self, Modify_YAML):
        Modify_YAML.setWindowTitle(QCoreApplication.translate("Modify_YAML", u"Dialog", None))
        self.icon_label.setText("")
        self.window_des_label.setText(QCoreApplication.translate("Modify_YAML", u"Modify configuration file", None))
        self.bn_close.setText("")
        self.label.setText(QCoreApplication.translate("Modify_YAML", u"Your configuration file may need some adjustments, for example, updating certain paths to match those on your system. The entries highlighted in red are invalid, so please update them accordingly.", None))
        self.train_label.setText(QCoreApplication.translate("Modify_YAML", u"Train data", None))
#if QT_CONFIG(tooltip)
        self.train_data_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.train_data_label.setText(QCoreApplication.translate("Modify_YAML", u"Input raw image folder", None))
#if QT_CONFIG(tooltip)
        self.train_data_info.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the training data image directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_data_info.setText("")
        self.DATA__TRAIN__PATH__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"images", None))
        self.train_data_input_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.train_gt_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.train_gt_label.setText(QCoreApplication.translate("Modify_YAML", u"Input label folder", None))
#if QT_CONFIG(tooltip)
        self.train_gt_info.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the training data ground truth (GT) directory. Depending on the workflow this should point to a folder of mask labels (semantic segmentation), instance masks (instance segmentation), csv files (detection) and high resolution images (super-resolution).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.train_gt_info.setText("")
        self.DATA__TRAIN__GT_PATH__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"gt", None))
        self.train_data_gt_input_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
        self.val_label.setText(QCoreApplication.translate("Modify_YAML", u"Validation data", None))
#if QT_CONFIG(tooltip)
        self.DATA__VAL__PATH__LABEL.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.DATA__VAL__PATH__LABEL.setText(QCoreApplication.translate("Modify_YAML", u"Input raw image folder", None))
#if QT_CONFIG(tooltip)
        self.DATA__VAL__PATH__INFO.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the validation data image directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.DATA__VAL__PATH__INFO.setText("")
        self.DATA__VAL__PATH__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"images", None))
        self.val_data_input_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.validation_data_gt_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.validation_data_gt_label.setText(QCoreApplication.translate("Modify_YAML", u"Input label folder", None))
#if QT_CONFIG(tooltip)
        self.validation_data_gt_info.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the validation data ground truth (GT) directory. Depending on the workflow this should point to a folder of mask labels (semantic segmentation), instance masks (instance segmentation), csv files (detection) and high resolution images (super-resolution).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.validation_data_gt_info.setText("")
        self.DATA__VAL__GT_PATH__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"gt", None))
        self.val_data_gt_input_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
        self.test_label.setText(QCoreApplication.translate("Modify_YAML", u"Test data", None))
#if QT_CONFIG(tooltip)
        self.test_data_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.test_data_label.setText(QCoreApplication.translate("Modify_YAML", u"Input raw image folder", None))
#if QT_CONFIG(tooltip)
        self.DATA__TEST__PATH__INFO.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to load the test data from</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.DATA__TEST__PATH__INFO.setText("")
        self.DATA__TEST__PATH__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"images", None))
        self.test_data_input_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.test_data_gt_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.test_data_gt_label.setText(QCoreApplication.translate("Modify_YAML", u"Input label folder", None))
#if QT_CONFIG(tooltip)
        self.DATA__TEST__GT_PATH__INFO.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to load the test gt data from</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.DATA__TEST__GT_PATH__INFO.setText("")
        self.DATA__TEST__GT_PATH__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"gt", None))
        self.test_data_gt_input_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
        self.checkpoint_label.setText(QCoreApplication.translate("Modify_YAML", u"Checkpoint file", None))
#if QT_CONFIG(tooltip)
        self.checkpoint_file_path_browse_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.checkpoint_file_path_browse_label.setText(QCoreApplication.translate("Modify_YAML", u"Model file", None))
#if QT_CONFIG(tooltip)
        self.PATHS__CHECKPOINT_FILE__INFO.setToolTip(QCoreApplication.translate("Modify_YAML", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to the model's checkpoint that will be loaded. Leave it blank to let BiaPy find it. If the output folder and the job name match, BiaPy will locate the model's weights within the 'checkpoints' directory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.PATHS__CHECKPOINT_FILE__INFO.setText("")
        self.PATHS__CHECKPOINT_FILE__INPUT.setText(QCoreApplication.translate("Modify_YAML", u"model_weights.pth", None))
        self.checkpoint_file_path_browse_bn.setText(QCoreApplication.translate("Modify_YAML", u"Browse", None))
        self.cfg_file_label.setText(QCoreApplication.translate("Modify_YAML", u"New configuration file:", None))
        self.create_config_bn.setText(QCoreApplication.translate("Modify_YAML", u"Save file", None))
    # retranslateUi

