# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tour_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_tour_window(object):
    def setupUi(self, tour_window):
        if not tour_window.objectName():
            tour_window.setObjectName(u"tour_window")
        tour_window.resize(900, 520)
        self.verticalLayout = QVBoxLayout(tour_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QFrame(tour_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFrameShape(QFrame.NoFrame)
        self.centralwidget.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 0))
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.frame_middle = QFrame(self.centralwidget)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setMinimumSize(QSize(900, 360))
        self.frame_middle.setMaximumSize(QSize(900, 360))
        font = QFont()
        font.setFamilies([u"DejaVu Math TeX Gyre"])
        font.setPointSize(12)
        self.frame_middle.setFont(font)
        self.frame_middle.setStyleSheet(u"")
        self.frame_middle.setFrameShape(QFrame.NoFrame)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_middle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.stackedWidget = QStackedWidget(self.frame_middle)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.presentation_page = QWidget()
        self.presentation_page.setObjectName(u"presentation_page")
        self.verticalLayout_4 = QVBoxLayout(self.presentation_page)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.presentation_text = QLabel(self.presentation_page)
        self.presentation_text.setObjectName(u"presentation_text")
        font1 = QFont()
        font1.setFamilies([u"DejaVu Math TeX Gyre"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.presentation_text.setFont(font1)
        self.presentation_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.presentation_text)

        self.presentation_version_text = QLabel(self.presentation_page)
        self.presentation_version_text.setObjectName(u"presentation_version_text")
        self.presentation_version_text.setFont(font)
        self.presentation_version_text.setStyleSheet(u"color: rgb(150, 150, 150)")
        self.presentation_version_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.presentation_version_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.presentation_page)
        self.description_page1 = QWidget()
        self.description_page1.setObjectName(u"description_page1")
        self.horizontalLayout_3 = QHBoxLayout(self.description_page1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.d1_label = QLabel(self.description_page1)
        self.d1_label.setObjectName(u"d1_label")

        self.horizontalLayout_3.addWidget(self.d1_label)

        self.stackedWidget.addWidget(self.description_page1)
        self.description_page2 = QWidget()
        self.description_page2.setObjectName(u"description_page2")
        self.horizontalLayout_5 = QHBoxLayout(self.description_page2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.d2_label = QLabel(self.description_page2)
        self.d2_label.setObjectName(u"d2_label")
        self.d2_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.d2_label)

        self.stackedWidget.addWidget(self.description_page2)
        self.description_page3 = QWidget()
        self.description_page3.setObjectName(u"description_page3")
        self.horizontalLayout_6 = QHBoxLayout(self.description_page3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.d3_label = QLabel(self.description_page3)
        self.d3_label.setObjectName(u"d3_label")
        self.d3_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.d3_label)

        self.stackedWidget.addWidget(self.description_page3)
        self.description_page4 = QWidget()
        self.description_page4.setObjectName(u"description_page4")
        self.horizontalLayout_7 = QHBoxLayout(self.description_page4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.d4_label = QLabel(self.description_page4)
        self.d4_label.setObjectName(u"d4_label")
        self.d4_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.d4_label)

        self.stackedWidget.addWidget(self.description_page4)
        self.release_notes_page = QWidget()
        self.release_notes_page.setObjectName(u"release_notes_page")
        self.horizontalLayout_8 = QHBoxLayout(self.release_notes_page)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.release_notes_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.d5_label = QLabel(self.frame_3)
        self.d5_label.setObjectName(u"d5_label")
        self.d5_label.setMinimumSize(QSize(600, 0))
        self.d5_label.setMaximumSize(QSize(600, 16777215))
        self.d5_label.setFont(font)

        self.verticalLayout_5.addWidget(self.d5_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.d5_release_notes_text = QLabel(self.frame_3)
        self.d5_release_notes_text.setObjectName(u"d5_release_notes_text")
        self.d5_release_notes_text.setFont(font)
        self.d5_release_notes_text.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.d5_release_notes_text)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.d5_right_text = QLabel(self.release_notes_page)
        self.d5_right_text.setObjectName(u"d5_right_text")
        self.d5_right_text.setFont(font)
        self.d5_right_text.setWordWrap(True)
        self.d5_right_text.setOpenExternalLinks(True)

        self.horizontalLayout_8.addWidget(self.d5_right_text)

        self.stackedWidget.addWidget(self.release_notes_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_middle)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_bottom)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(30, 50))
        self.frame_4.setMaximumSize(QSize(30, 50))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.left_arrow_bn = QPushButton(self.frame_4)
        self.left_arrow_bn.setObjectName(u"left_arrow_bn")
        self.left_arrow_bn.setMinimumSize(QSize(30, 50))
        self.left_arrow_bn.setMaximumSize(QSize(30, 50))
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

        self.horizontalLayout_10.addWidget(self.left_arrow_bn)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.window1_bn = QPushButton(self.frame_2)
        self.window1_bn.setObjectName(u"window1_bn")
        self.window1_bn.setMaximumSize(QSize(20, 16777215))
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

        self.horizontalLayout_4.addWidget(self.window1_bn)

        self.window2_bn = QPushButton(self.frame_2)
        self.window2_bn.setObjectName(u"window2_bn")
        self.window2_bn.setMaximumSize(QSize(20, 16777215))
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

        self.horizontalLayout_4.addWidget(self.window2_bn)

        self.window3_bn = QPushButton(self.frame_2)
        self.window3_bn.setObjectName(u"window3_bn")
        self.window3_bn.setMaximumSize(QSize(20, 16777215))
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

        self.horizontalLayout_4.addWidget(self.window3_bn)

        self.window4_bn = QPushButton(self.frame_2)
        self.window4_bn.setObjectName(u"window4_bn")
        self.window4_bn.setMaximumSize(QSize(20, 16777215))
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

        self.horizontalLayout_4.addWidget(self.window4_bn)

        self.window5_bn = QPushButton(self.frame_2)
        self.window5_bn.setObjectName(u"window5_bn")
        self.window5_bn.setMaximumSize(QSize(20, 16777215))
        self.window5_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.window5_bn)

        self.window6_bn = QPushButton(self.frame_2)
        self.window6_bn.setObjectName(u"window6_bn")
        self.window6_bn.setMaximumSize(QSize(20, 16777215))
        self.window6_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255,255,255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.window6_bn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(30, 50))
        self.frame_5.setMaximumSize(QSize(30, 50))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.right_arrow_bn = QPushButton(self.frame_5)
        self.right_arrow_bn.setObjectName(u"right_arrow_bn")
        self.right_arrow_bn.setMinimumSize(QSize(30, 50))
        self.right_arrow_bn.setMaximumSize(QSize(30, 50))
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

        self.horizontalLayout_9.addWidget(self.right_arrow_bn)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_8.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.frame = QFrame(self.frame_bottom)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dont_show_message_checkbox = QCheckBox(self.frame)
        self.dont_show_message_checkbox.setObjectName(u"dont_show_message_checkbox")
        self.dont_show_message_checkbox.setFont(font)

        self.horizontalLayout_2.addWidget(self.dont_show_message_checkbox)

        self.ok_bn = QPushButton(self.frame)
        self.ok_bn.setObjectName(u"ok_bn")
        self.ok_bn.setMinimumSize(QSize(150, 30))
        self.ok_bn.setMaximumSize(QSize(150, 16777215))
        self.ok_bn.setFont(font)
        self.ok_bn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.ok_bn)


        self.verticalLayout_8.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(tour_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(tour_window)
    # setupUi

    def retranslateUi(self, tour_window):
        tour_window.setWindowTitle(QCoreApplication.translate("tour_window", u"Dialog", None))
        self.bn_close.setText("")
        self.presentation_text.setText(QCoreApplication.translate("tour_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Welcome to BiaPy's GUI</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Take a tour</span></p></body></html>", None))
        self.presentation_version_text.setText(QCoreApplication.translate("tour_window", u"Version XXX", None))
        self.d1_label.setText("")
        self.d2_label.setText("")
        self.d3_label.setText("")
        self.d4_label.setText("")
        self.d5_right_text.setText(QCoreApplication.translate("tour_window", u"<html><head/><body><p><a name=\"docs-internal-guid-b8b2138f-7fff-57ba-34f3-3dafb7ee5dac\"/><span style=\" font-family:'Arial','sans-serif'; font-size:24pt; color:#000000; background-color:transparent;\">F</span><span style=\" font-family:'Arial','sans-serif'; font-size:24pt; color:#000000; background-color:transparent;\">urther help</span></p><p><a name=\"docs-internal-guid-c384090c-7fff-0c38-410d-e6caed5cd4d6\"/><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">F</span><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">or more information, in the \u201cHome\u201d options, click on \u201cDocumentation\u201d to get redirected to </span><a href=\"https://biapy.readthedocs.io/en/latest/index.html\"><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; text-decoration: underline; color:#0097a7; background-color:transparent;\">BiaPy\u2019s documentation site</span></a><span style=\" "
                        "font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">.</span></p><p><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">If you run into trouble, check our </span><a href=\"https://biapy.readthedocs.io/en/latest/get_started/faq.html\"><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; text-decoration: underline; color:#0097a7; background-color:transparent;\">FAQ &amp; Troubleshooting</span></a><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\"> page or leave us a comment in the </span><a href=\"https://forum.image.sc/tag/biapy\"><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; text-decoration: underline; color:#0097a7; background-color:transparent;\">image.sc forum</span></a><span style=\" font-family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">.</span></p><p><span style=\" font-"
                        "family:'Arial','sans-serif'; font-size:13pt; color:#595959; background-color:transparent;\">All feedback is welcome!</span></p></body></html>", None))
        self.left_arrow_bn.setText("")
        self.window1_bn.setText("")
        self.window2_bn.setText("")
        self.window3_bn.setText("")
        self.window4_bn.setText("")
        self.window5_bn.setText("")
        self.window6_bn.setText("")
        self.right_arrow_bn.setText("")
        self.dont_show_message_checkbox.setText(QCoreApplication.translate("tour_window", u"Do not show this message again. ", None))
        self.ok_bn.setText(QCoreApplication.translate("tour_window", u"Got it!", None))
    # retranslateUi

