# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_basic.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_basic(object):
    def setupUi(self, basic):
        if not basic.objectName():
            basic.setObjectName(u"basic")
        basic.resize(650, 490)
        self.verticalLayout = QVBoxLayout(basic)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QFrame(basic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFrameShape(QFrame.NoFrame)
        self.centralwidget.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 0))
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.icon_label = QLabel(self.frame_top)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(48, 55))
        self.icon_label.setMaximumSize(QSize(48, 55))
        self.icon_label.setFrameShape(QFrame.NoFrame)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bn_close.sizePolicy().hasHeightForWidth())
        self.bn_close.setSizePolicy(sizePolicy)
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
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setAutoDefault(False)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 68, 353))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.message_label = QLabel(self.scrollAreaWidgetContents)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setMinimumSize(QSize(0, 0))
        self.message_label.setMaximumSize(QSize(600, 16777215))
        self.message_label.setFont(font1)
        self.message_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.message_label.setWordWrap(True)
        self.message_label.setMargin(5)
        self.message_label.setIndent(-1)
        self.message_label.setOpenExternalLinks(True)
        self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.message_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.frame_bottom)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 15, 9, 15)
        self.ok_bn = QPushButton(self.frame)
        self.ok_bn.setObjectName(u"ok_bn")
        self.ok_bn.setMinimumSize(QSize(150, 30))
        self.ok_bn.setMaximumSize(QSize(150, 16777215))
        self.ok_bn.setFont(font1)
        self.ok_bn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.ok_bn)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(basic)

        QMetaObject.connectSlotsByName(basic)
    # setupUi

    def retranslateUi(self, basic):
        basic.setWindowTitle(QCoreApplication.translate("basic", u"Dialog", None))
        self.icon_label.setText("")
        self.window_des_label.setText(QCoreApplication.translate("basic", u"Wizard help", None))
        self.bn_close.setText("")
        self.message_label.setText(QCoreApplication.translate("basic", u"<html><head/><body><p><span style=\" font-size:12pt;\">TEXT</span></p></body></html>", None))
        self.ok_bn.setText(QCoreApplication.translate("basic", u"Got it!", None))
    # retranslateUi

