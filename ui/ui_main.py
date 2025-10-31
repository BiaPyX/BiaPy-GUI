# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1210, 592)
        MainWindow.setMinimumSize(QSize(800, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QFrame(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"QWidget:disabled {\n"
"background-color:#D3D3D3;\n"
"}\n"
"QFrame:disabled {\n"
"background-color:#D3D3D3;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#D3D3D3;\n"
"}")
        self.centralwidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_west = QFrame(self.centralwidget)
        self.frame_west.setObjectName(u"frame_west")
        font1 = QFont()
        font1.setFamilies([u"DejaVu Math TeX Gyre"])
        font1.setPointSize(12)
        self.frame_west.setFont(font1)
        self.frame_west.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);")
        self.frame_west.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_west.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_west)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_west)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(260, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setFont(font1)
        self.frame_bottom_west.setStyleSheet(u"QFrame{\n"
"background:rgb(64,144,253);\n"
"}\n"
"")
        self.frame_bottom_west.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.biapy_logo_frame = QFrame(self.frame_bottom_west)
        self.biapy_logo_frame.setObjectName(u"biapy_logo_frame")
        self.biapy_logo_frame.setMinimumSize(QSize(0, 250))
        self.biapy_logo_frame.setMaximumSize(QSize(16777215, 250))
        self.biapy_logo_frame.setFont(font1)
        self.biapy_logo_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.biapy_logo_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.biapy_logo_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.biapy_logo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.frame_58 = QFrame(self.biapy_logo_frame)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(240, 0))
        self.frame_58.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);")
        self.frame_58.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.biapy_logo_label = QLabel(self.frame_58)
        self.biapy_logo_label.setObjectName(u"biapy_logo_label")
        self.biapy_logo_label.setMinimumSize(QSize(0, 0))
        self.biapy_logo_label.setMaximumSize(QSize(180, 180))
        self.biapy_logo_label.setFont(font1)
        self.biapy_logo_label.setLineWidth(0)
        self.biapy_logo_label.setPixmap(QPixmap(u"../../../../.designer/backup/images/superminimal_ark_biapy2.png"))
        self.biapy_logo_label.setScaledContents(True)
        self.biapy_logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.biapy_logo_label)


        self.verticalLayout_3.addWidget(self.frame_58, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.line_2 = QFrame(self.biapy_logo_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.biapy_version = QLabel(self.biapy_logo_frame)
        self.biapy_version.setObjectName(u"biapy_version")
        self.biapy_version.setMinimumSize(QSize(0, 0))
        self.biapy_version.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"DejaVu Math TeX Gyre"])
        font2.setPointSize(7)
        self.biapy_version.setFont(font2)
        self.biapy_version.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"}")
        self.biapy_version.setLineWidth(0)
        self.biapy_version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.biapy_version)


        self.verticalLayout_14.addWidget(self.biapy_logo_frame)

        self.line = QFrame(self.frame_bottom_west)
        self.line.setObjectName(u"line")
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(0, 0))
        self.frame_home.setMaximumSize(QSize(260, 52))
        self.frame_home.setFont(font1)
        self.frame_home.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(52, 0))
        self.bn_home.setMaximumSize(QSize(260, 52))
        self.bn_home.setFont(font1)
        self.bn_home.setIconSize(QSize(257, 48))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_14.addWidget(self.frame_home)

        self.frame_wizard = QFrame(self.frame_bottom_west)
        self.frame_wizard.setObjectName(u"frame_wizard")
        self.frame_wizard.setMaximumSize(QSize(260, 52))
        self.frame_wizard.setFont(font1)
        self.frame_wizard.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_wizard.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_wizard)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bn_wizard = QPushButton(self.frame_wizard)
        self.bn_wizard.setObjectName(u"bn_wizard")
        self.bn_wizard.setMinimumSize(QSize(52, 0))
        self.bn_wizard.setMaximumSize(QSize(260, 52))
        self.bn_wizard.setFont(font1)
        self.bn_wizard.setIconSize(QSize(257, 48))
        self.bn_wizard.setFlat(True)

        self.verticalLayout_4.addWidget(self.bn_wizard)


        self.verticalLayout_14.addWidget(self.frame_wizard)

        self.frame_run_biapy = QFrame(self.frame_bottom_west)
        self.frame_run_biapy.setObjectName(u"frame_run_biapy")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_run_biapy.sizePolicy().hasHeightForWidth())
        self.frame_run_biapy.setSizePolicy(sizePolicy)
        self.frame_run_biapy.setMinimumSize(QSize(0, 0))
        self.frame_run_biapy.setMaximumSize(QSize(260, 52))
        self.frame_run_biapy.setFont(font1)
        self.frame_run_biapy.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_run_biapy.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_run_biapy)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.bn_run_biapy = QPushButton(self.frame_run_biapy)
        self.bn_run_biapy.setObjectName(u"bn_run_biapy")
        self.bn_run_biapy.setMinimumSize(QSize(52, 0))
        self.bn_run_biapy.setMaximumSize(QSize(260, 52))
        self.bn_run_biapy.setFont(font1)
        self.bn_run_biapy.setIconSize(QSize(257, 48))
        self.bn_run_biapy.setFlat(True)

        self.horizontalLayout_28.addWidget(self.bn_run_biapy)


        self.verticalLayout_14.addWidget(self.frame_run_biapy)

        self.frame_2 = QFrame(self.frame_bottom_west)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)


        self.horizontalLayout.addWidget(self.frame_west)

        self.frame_east = QFrame(self.centralwidget)
        self.frame_east.setObjectName(u"frame_east")
        self.frame_east.setEnabled(True)
        self.frame_east.setMinimumSize(QSize(0, 0))
        self.frame_east.setMaximumSize(QSize(16777215, 16777215))
        self.frame_east.setFont(font1)
        self.frame_east.setStyleSheet(u"")
        self.frame_east.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_east.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_east)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_east = QFrame(self.frame_east)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMinimumSize(QSize(0, 0))
        self.frame_top_east.setMaximumSize(QSize(16777215, 35))
        self.frame_top_east.setFont(font1)
        self.frame_top_east.setStyleSheet(u"QFrame:disabled {\n"
"background-color:#D3D3D3;\n"
"}")
        self.frame_top_east.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_empty = QFrame(self.frame_top_east)
        self.frame_empty.setObjectName(u"frame_empty")
        self.frame_empty.setMinimumSize(QSize(0, 0))
        self.frame_empty.setFont(font1)
        self.frame_empty.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_empty.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_empty)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_empty)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 35))
        self.frame_min.setMaximumSize(QSize(55, 35))
        self.frame_min.setFont(font1)
        self.frame_min.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 35))
        self.bn_min.setFont(font1)
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
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 35))
        self.frame_close.setMaximumSize(QSize(55, 35))
        self.frame_close.setFont(font1)
        self.frame_close.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 35))
        self.bn_close.setFont(font1)
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
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.verticalLayout.addWidget(self.frame_top_east)

        self.frame_bottom_east = QFrame(self.frame_east)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setMaximumSize(QSize(16777215, 16777215))
        self.frame_bottom_east.setFont(font1)
        self.frame_bottom_east.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setFont(font1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_13 = QVBoxLayout(self.page_home)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(948, 555))
        self.frame_4.setMaximumSize(QSize(948, 555))
        self.frame_4.setFont(font1)
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 0, 5, 0)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"DejaVu Math TeX Gyre"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_16.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_16)

        self.frame_ext_links = QFrame(self.frame_4)
        self.frame_ext_links.setObjectName(u"frame_ext_links")
        self.frame_ext_links.setMinimumSize(QSize(0, 0))
        self.frame_ext_links.setMaximumSize(QSize(16777215, 120))
        self.frame_ext_links.setStyleSheet(u"#frame_ext_links {border: 3px solid 	rgb(169,169,169); border-radius: 25px;}")
        self.frame_ext_links.setFrameShape(QFrame.Shape.Box)
        self.frame_ext_links.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_ext_links.setLineWidth(3)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_ext_links)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 15, 0, 15)
        self.github_frame = QFrame(self.frame_ext_links)
        self.github_frame.setObjectName(u"github_frame")
        self.github_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.github_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.github_frame)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.biapy_github_bn = QPushButton(self.github_frame)
        self.biapy_github_bn.setObjectName(u"biapy_github_bn")
        self.biapy_github_bn.setMinimumSize(QSize(55, 55))
        self.biapy_github_bn.setMaximumSize(QSize(55, 55))
        self.biapy_github_bn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#A9A9A9;\n"
"}")
        self.biapy_github_bn.setIconSize(QSize(45, 45))

        self.verticalLayout_34.addWidget(self.biapy_github_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.home_project_page_label = QLabel(self.github_frame)
        self.home_project_page_label.setObjectName(u"home_project_page_label")
        self.home_project_page_label.setMinimumSize(QSize(100, 0))
        self.home_project_page_label.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"DejaVu Math TeX Gyre"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.home_project_page_label.setFont(font4)

        self.verticalLayout_34.addWidget(self.home_project_page_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_21.addWidget(self.github_frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.forum_frame = QFrame(self.frame_ext_links)
        self.forum_frame.setObjectName(u"forum_frame")
        self.forum_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.forum_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.forum_frame)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.biapy_forum_bn = QPushButton(self.forum_frame)
        self.biapy_forum_bn.setObjectName(u"biapy_forum_bn")
        self.biapy_forum_bn.setMinimumSize(QSize(55, 55))
        self.biapy_forum_bn.setMaximumSize(QSize(55, 55))
        self.biapy_forum_bn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#A9A9A9;\n"
"}")
        self.biapy_forum_bn.setIconSize(QSize(45, 45))

        self.verticalLayout_15.addWidget(self.biapy_forum_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.forum_page_label = QLabel(self.forum_frame)
        self.forum_page_label.setObjectName(u"forum_page_label")
        self.forum_page_label.setMinimumSize(QSize(100, 0))
        self.forum_page_label.setMaximumSize(QSize(16777215, 16777215))
        self.forum_page_label.setFont(font4)

        self.verticalLayout_15.addWidget(self.forum_page_label)


        self.horizontalLayout_21.addWidget(self.forum_frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doc_frame = QFrame(self.frame_ext_links)
        self.doc_frame.setObjectName(u"doc_frame")
        self.doc_frame.setMinimumSize(QSize(0, 0))
        self.doc_frame.setMaximumSize(QSize(16777215, 16777215))
        self.doc_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.doc_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.doc_frame)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.biapy_doc_bn = QPushButton(self.doc_frame)
        self.biapy_doc_bn.setObjectName(u"biapy_doc_bn")
        self.biapy_doc_bn.setMinimumSize(QSize(55, 55))
        self.biapy_doc_bn.setMaximumSize(QSize(55, 55))
        self.biapy_doc_bn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#A9A9A9;\n"
"}")
        self.biapy_doc_bn.setIconSize(QSize(45, 45))

        self.verticalLayout_35.addWidget(self.biapy_doc_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.documentation_page_label = QLabel(self.doc_frame)
        self.documentation_page_label.setObjectName(u"documentation_page_label")
        self.documentation_page_label.setMinimumSize(QSize(100, 0))
        self.documentation_page_label.setMaximumSize(QSize(16777215, 16777215))
        self.documentation_page_label.setFont(font4)

        self.verticalLayout_35.addWidget(self.documentation_page_label)


        self.horizontalLayout_21.addWidget(self.doc_frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.templates_frame = QFrame(self.frame_ext_links)
        self.templates_frame.setObjectName(u"templates_frame")
        self.templates_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.templates_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.templates_frame)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.biapy_templates_bn = QPushButton(self.templates_frame)
        self.biapy_templates_bn.setObjectName(u"biapy_templates_bn")
        self.biapy_templates_bn.setMinimumSize(QSize(55, 55))
        self.biapy_templates_bn.setMaximumSize(QSize(55, 55))
        self.biapy_templates_bn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#A9A9A9;\n"
"}")
        self.biapy_templates_bn.setIconSize(QSize(45, 45))

        self.verticalLayout_36.addWidget(self.biapy_templates_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.templates_page_label = QLabel(self.templates_frame)
        self.templates_page_label.setObjectName(u"templates_page_label")
        self.templates_page_label.setMinimumSize(QSize(100, 0))
        self.templates_page_label.setMaximumSize(QSize(16777215, 16777215))
        self.templates_page_label.setFont(font4)

        self.verticalLayout_36.addWidget(self.templates_page_label)


        self.horizontalLayout_21.addWidget(self.templates_frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.notebooks_frame = QFrame(self.frame_ext_links)
        self.notebooks_frame.setObjectName(u"notebooks_frame")
        self.notebooks_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.notebooks_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.notebooks_frame)
        self.verticalLayout_37.setSpacing(10)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.biapy_notebooks_bn = QPushButton(self.notebooks_frame)
        self.biapy_notebooks_bn.setObjectName(u"biapy_notebooks_bn")
        self.biapy_notebooks_bn.setMinimumSize(QSize(55, 55))
        self.biapy_notebooks_bn.setMaximumSize(QSize(55, 55))
        self.biapy_notebooks_bn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#A9A9A9;\n"
"}")
        self.biapy_notebooks_bn.setIconSize(QSize(45, 45))

        self.verticalLayout_37.addWidget(self.biapy_notebooks_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.notebooks_page_label = QLabel(self.notebooks_frame)
        self.notebooks_page_label.setObjectName(u"notebooks_page_label")
        self.notebooks_page_label.setMinimumSize(QSize(100, 0))
        self.notebooks_page_label.setMaximumSize(QSize(16777215, 16777215))
        self.notebooks_page_label.setFont(font4)

        self.verticalLayout_37.addWidget(self.notebooks_page_label)


        self.horizontalLayout_21.addWidget(self.notebooks_frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.citation_frame = QFrame(self.frame_ext_links)
        self.citation_frame.setObjectName(u"citation_frame")
        self.citation_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.citation_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.citation_frame)
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.biapy_citation_bn = QPushButton(self.citation_frame)
        self.biapy_citation_bn.setObjectName(u"biapy_citation_bn")
        self.biapy_citation_bn.setMinimumSize(QSize(55, 55))
        self.biapy_citation_bn.setMaximumSize(QSize(55, 55))
        self.biapy_citation_bn.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#A9A9A9;\n"
"}")
        self.biapy_citation_bn.setIconSize(QSize(33, 33))

        self.verticalLayout_38.addWidget(self.biapy_citation_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.citation_page_label = QLabel(self.citation_frame)
        self.citation_page_label.setObjectName(u"citation_page_label")
        self.citation_page_label.setMinimumSize(QSize(100, 0))
        self.citation_page_label.setMaximumSize(QSize(16777215, 16777215))
        self.citation_page_label.setFont(font4)

        self.verticalLayout_38.addWidget(self.citation_page_label)


        self.horizontalLayout_21.addWidget(self.citation_frame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_ext_links)

        self.dependencies_frame = QFrame(self.frame_4)
        self.dependencies_frame.setObjectName(u"dependencies_frame")
        self.dependencies_frame.setMinimumSize(QSize(0, 200))
        self.dependencies_frame.setMaximumSize(QSize(16777215, 16777215))
        self.dependencies_frame.setStyleSheet(u"")
        self.dependencies_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.dependencies_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.dependencies_frame.setLineWidth(1)
        self.gridLayout_68 = QGridLayout(self.dependencies_frame)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setHorizontalSpacing(15)
        self.gridLayout_68.setVerticalSpacing(9)
        self.gridLayout_68.setContentsMargins(-1, 20, -1, 20)
        self.docker_frame = QFrame(self.dependencies_frame)
        self.docker_frame.setObjectName(u"docker_frame")
        self.docker_frame.setStyleSheet(u"QLabel:disabled {\n"
"border: 3px solid 	rgb(169,169,169);\n"
"border-radius: 25px;\n"
"}\n"
"")
        self.docker_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.docker_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.docker_frame)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(9, 9, 9, 9)
        self.docker_logo = QLabel(self.docker_frame)
        self.docker_logo.setObjectName(u"docker_logo")
        self.docker_logo.setMinimumSize(QSize(220, 56))
        self.docker_logo.setMaximumSize(QSize(220, 56))
        self.docker_logo.setFont(font1)
        self.docker_logo.setScaledContents(True)

        self.verticalLayout_28.addWidget(self.docker_logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.docker_status_label = QLabel(self.docker_frame)
        self.docker_status_label.setObjectName(u"docker_status_label")
        self.docker_status_label.setMinimumSize(QSize(350, 0))
        self.docker_status_label.setFont(font1)
        self.docker_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.docker_status_label.setWordWrap(True)
        self.docker_status_label.setOpenExternalLinks(True)

        self.verticalLayout_28.addWidget(self.docker_status_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_68.addWidget(self.docker_frame, 1, 0, 1, 1)

        self.gpu_head_label = QLabel(self.dependencies_frame)
        self.gpu_head_label.setObjectName(u"gpu_head_label")
        self.gpu_head_label.setMinimumSize(QSize(0, 30))
        self.gpu_head_label.setMaximumSize(QSize(16777215, 30))
        self.gpu_head_label.setFont(font3)

        self.gridLayout_68.addWidget(self.gpu_head_label, 0, 1, 1, 1)

        self.gpu_frame = QFrame(self.dependencies_frame)
        self.gpu_frame.setObjectName(u"gpu_frame")
        self.gpu_frame.setToolTipDuration(3)
        self.gpu_frame.setStyleSheet(u"QLabel:disabled {\n"
"border: 3px solid 	rgb(169,169,169);\n"
"border-radius: 25px;\n"
"}")
        self.gpu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gpu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.gpu_frame)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 9)
        self.gpu_icon_label = QLabel(self.gpu_frame)
        self.gpu_icon_label.setObjectName(u"gpu_icon_label")
        self.gpu_icon_label.setMinimumSize(QSize(122, 80))
        self.gpu_icon_label.setMaximumSize(QSize(122, 80))
        self.gpu_icon_label.setFont(font1)
        self.gpu_icon_label.setScaledContents(True)

        self.verticalLayout_33.addWidget(self.gpu_icon_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gpu_status_label = QLabel(self.gpu_frame)
        self.gpu_status_label.setObjectName(u"gpu_status_label")
        self.gpu_status_label.setMinimumSize(QSize(350, 0))
        self.gpu_status_label.setFont(font1)
        self.gpu_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gpu_status_label.setWordWrap(True)
        self.gpu_status_label.setOpenExternalLinks(True)

        self.verticalLayout_33.addWidget(self.gpu_status_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_68.addWidget(self.gpu_frame, 1, 1, 1, 1)

        self.docker_head_label = QLabel(self.dependencies_frame)
        self.docker_head_label.setObjectName(u"docker_head_label")
        self.docker_head_label.setMinimumSize(QSize(0, 30))
        self.docker_head_label.setMaximumSize(QSize(16777215, 30))
        self.docker_head_label.setFont(font3)
        self.docker_head_label.setOpenExternalLinks(True)

        self.gridLayout_68.addWidget(self.docker_head_label, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.dependencies_frame)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 170))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFont(font1)
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_6)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.frame_31 = QFrame(self.frame_6)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 136))
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_31)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.main_window_wizard_question_wizard_icon = QPushButton(self.frame_31)
        self.main_window_wizard_question_wizard_icon.setObjectName(u"main_window_wizard_question_wizard_icon")
        self.main_window_wizard_question_wizard_icon.setMinimumSize(QSize(194, 85))
        self.main_window_wizard_question_wizard_icon.setMaximumSize(QSize(194, 85))
        self.main_window_wizard_question_wizard_icon.setIconSize(QSize(184, 75))

        self.verticalLayout_41.addWidget(self.main_window_wizard_question_wizard_icon)


        self.gridLayout_33.addWidget(self.frame_31, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 136))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_5)
        self.verticalLayout_42.setSpacing(15)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.load_yaml_bn = QPushButton(self.frame_5)
        self.load_yaml_bn.setObjectName(u"load_yaml_bn")
        self.load_yaml_bn.setMinimumSize(QSize(300, 40))
        self.load_yaml_bn.setMaximumSize(QSize(300, 40))
        self.load_yaml_bn.setFont(font1)
        self.load_yaml_bn.setIconSize(QSize(215, 33))

        self.verticalLayout_42.addWidget(self.load_yaml_bn)


        self.gridLayout_33.addWidget(self.frame_5, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 30))
        self.label_26.setMaximumSize(QSize(16777215, 30))
        self.label_26.setFont(font3)

        self.gridLayout_33.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setMaximumSize(QSize(16777215, 30))
        self.label_27.setFont(font3)

        self.gridLayout_33.addWidget(self.label_27, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_home)
        self.page_wizard = QWidget()
        self.page_wizard.setObjectName(u"page_wizard")
        self.page_wizard.setStyleSheet(u"QFrame:disabled {\n"
"background-color:#D3D3D3;\n"
"}")
        self.wizard_frame = QFrame(self.page_wizard)
        self.wizard_frame.setObjectName(u"wizard_frame")
        self.wizard_frame.setGeometry(QRect(0, 0, 948, 555))
        self.wizard_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.wizard_frame)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.wizard_main_frame = QStackedWidget(self.wizard_frame)
        self.wizard_main_frame.setObjectName(u"wizard_main_frame")
        self.wizard_start_page = QWidget()
        self.wizard_start_page.setObjectName(u"wizard_start_page")
        self.verticalLayout_54 = QVBoxLayout(self.wizard_start_page)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.wizard_start_page)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_67)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 300))
        font5 = QFont()
        font5.setFamilies([u"DejaVu Math TeX Gyre"])
        self.frame_68.setFont(font5)
        self.frame_68.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_68.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_39.setSpacing(30)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(120, 50, 120, 50)
        self.wizard_start_message = QLabel(self.frame_68)
        self.wizard_start_message.setObjectName(u"wizard_start_message")
        self.wizard_start_message.setMinimumSize(QSize(0, 0))
        self.wizard_start_message.setMaximumSize(QSize(16777215, 16777215))
        self.wizard_start_message.setFont(font1)
        self.wizard_start_message.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.wizard_start_message.setWordWrap(True)

        self.horizontalLayout_39.addWidget(self.wizard_start_message)

        self.wizard_start_wizard_icon = QLabel(self.frame_68)
        self.wizard_start_wizard_icon.setObjectName(u"wizard_start_wizard_icon")
        self.wizard_start_wizard_icon.setMinimumSize(QSize(130, 148))
        self.wizard_start_wizard_icon.setMaximumSize(QSize(130, 148))
        self.wizard_start_wizard_icon.setFont(font1)
        self.wizard_start_wizard_icon.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.wizard_start_wizard_icon)


        self.verticalLayout_53.addWidget(self.frame_68)

        self.wizard_start_page_paths_frame = QFrame(self.frame_67)
        self.wizard_start_page_paths_frame.setObjectName(u"wizard_start_page_paths_frame")
        self.wizard_start_page_paths_frame.setMinimumSize(QSize(0, 0))
        self.wizard_start_page_paths_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_start_page_paths_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_80 = QGridLayout(self.wizard_start_page_paths_frame)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.wizard_browse_yaml_path_info = QPushButton(self.wizard_start_page_paths_frame)
        self.wizard_browse_yaml_path_info.setObjectName(u"wizard_browse_yaml_path_info")
        self.wizard_browse_yaml_path_info.setMinimumSize(QSize(30, 30))
        self.wizard_browse_yaml_path_info.setMaximumSize(QSize(30, 30))
        self.wizard_browse_yaml_path_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_80.addWidget(self.wizard_browse_yaml_path_info, 3, 3, 1, 1)

        self.WIZARD_PROBLEM__NDIM__INFO = QPushButton(self.wizard_start_page_paths_frame)
        self.WIZARD_PROBLEM__NDIM__INFO.setObjectName(u"WIZARD_PROBLEM__NDIM__INFO")
        self.WIZARD_PROBLEM__NDIM__INFO.setMinimumSize(QSize(30, 30))
        self.WIZARD_PROBLEM__NDIM__INFO.setMaximumSize(QSize(30, 30))
        self.WIZARD_PROBLEM__NDIM__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_80.addWidget(self.WIZARD_PROBLEM__NDIM__INFO, 0, 3, 1, 1)

        self.wizard_browse_yaml_path_bn = QPushButton(self.wizard_start_page_paths_frame)
        self.wizard_browse_yaml_path_bn.setObjectName(u"wizard_browse_yaml_path_bn")
        self.wizard_browse_yaml_path_bn.setMaximumSize(QSize(130, 16777215))
        self.wizard_browse_yaml_path_bn.setFont(font1)

        self.gridLayout_80.addWidget(self.wizard_browse_yaml_path_bn, 0, 6, 1, 1)

        self.wizard_browse_yaml_path_label = QLabel(self.wizard_start_page_paths_frame)
        self.wizard_browse_yaml_path_label.setObjectName(u"wizard_browse_yaml_path_label")
        self.wizard_browse_yaml_path_label.setMaximumSize(QSize(250, 35))
        self.wizard_browse_yaml_path_label.setFont(font1)

        self.gridLayout_80.addWidget(self.wizard_browse_yaml_path_label, 0, 1, 1, 1)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_80.addItem(self.horizontalSpacer_87, 0, 7, 1, 1)

        self.wizard_browse_yaml_path_input = QLineEdit(self.wizard_start_page_paths_frame)
        self.wizard_browse_yaml_path_input.setObjectName(u"wizard_browse_yaml_path_input")
        self.wizard_browse_yaml_path_input.setMinimumSize(QSize(500, 30))
        self.wizard_browse_yaml_path_input.setMaximumSize(QSize(500, 30))
        self.wizard_browse_yaml_path_input.setFont(font1)
        self.wizard_browse_yaml_path_input.setReadOnly(True)

        self.gridLayout_80.addWidget(self.wizard_browse_yaml_path_input, 0, 5, 1, 1)

        self.wizard_yaml_name_label = QLabel(self.wizard_start_page_paths_frame)
        self.wizard_yaml_name_label.setObjectName(u"wizard_yaml_name_label")
        self.wizard_yaml_name_label.setMaximumSize(QSize(250, 35))
        self.wizard_yaml_name_label.setFont(font1)

        self.gridLayout_80.addWidget(self.wizard_yaml_name_label, 3, 1, 1, 1)

        self.wizard_yaml_name_input = QLineEdit(self.wizard_start_page_paths_frame)
        self.wizard_yaml_name_input.setObjectName(u"wizard_yaml_name_input")
        self.wizard_yaml_name_input.setMinimumSize(QSize(0, 30))
        self.wizard_yaml_name_input.setMaximumSize(QSize(500, 30))
        self.wizard_yaml_name_input.setFont(font1)

        self.gridLayout_80.addWidget(self.wizard_yaml_name_input, 3, 5, 1, 1)


        self.verticalLayout_53.addWidget(self.wizard_start_page_paths_frame)

        self.frame_69 = QFrame(self.frame_67)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_69.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_69)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.wizard_start_bn = QPushButton(self.frame_69)
        self.wizard_start_bn.setObjectName(u"wizard_start_bn")
        self.wizard_start_bn.setMinimumSize(QSize(220, 40))
        self.wizard_start_bn.setMaximumSize(QSize(220, 77))
        self.wizard_start_bn.setFont(font1)

        self.verticalLayout_55.addWidget(self.wizard_start_bn)


        self.verticalLayout_53.addWidget(self.frame_69, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_54.addWidget(self.frame_67)

        self.wizard_main_frame.addWidget(self.wizard_start_page)
        self.questionary_page = QWidget()
        self.questionary_page.setObjectName(u"questionary_page")
        self.verticalLayout_49 = QVBoxLayout(self.questionary_page)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.questionary_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_70 = QFrame(self.frame_8)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(300, 0))
        self.frame_70.setMaximumSize(QSize(300, 16777215))
        self.frame_70.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_56 = QVBoxLayout(self.frame_70)
        self.verticalLayout_56.setSpacing(10)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(6, 6, 6, 6)
        self.wizard_treeView = QTreeView(self.frame_70)
        self.wizard_treeView.setObjectName(u"wizard_treeView")
        self.wizard_treeView.setMinimumSize(QSize(0, 0))
        self.wizard_treeView.setMaximumSize(QSize(16777215, 16777215))
        self.wizard_treeView.setFont(font1)
        self.wizard_treeView.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_treeView.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.wizard_treeView.setAlternatingRowColors(False)
        self.wizard_treeView.setIndentation(10)
        self.wizard_treeView.setHeaderHidden(True)

        self.verticalLayout_56.addWidget(self.wizard_treeView)

        self.frame_74 = QFrame(self.frame_70)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.wizard_clear_answers_bn = QPushButton(self.frame_74)
        self.wizard_clear_answers_bn.setObjectName(u"wizard_clear_answers_bn")
        self.wizard_clear_answers_bn.setMinimumSize(QSize(160, 30))
        self.wizard_clear_answers_bn.setFont(font1)

        self.horizontalLayout_43.addWidget(self.wizard_clear_answers_bn)


        self.verticalLayout_56.addWidget(self.frame_74, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_40.addWidget(self.frame_70)

        self.frame_65 = QFrame(self.frame_8)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 0))
        self.frame_65.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_65)
        self.verticalLayout_51.setSpacing(20)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 100))
        self.frame_66.setMaximumSize(QSize(16777215, 100))
        self.frame_66.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.wizard_question_label = QLabel(self.frame_66)
        self.wizard_question_label.setObjectName(u"wizard_question_label")
        self.wizard_question_label.setFont(font1)

        self.horizontalLayout_38.addWidget(self.wizard_question_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_82)

        self.wizard_question_wizard_icon = QPushButton(self.frame_66)
        self.wizard_question_wizard_icon.setObjectName(u"wizard_question_wizard_icon")
        self.wizard_question_wizard_icon.setMinimumSize(QSize(194, 85))
        self.wizard_question_wizard_icon.setMaximumSize(QSize(194, 85))
        self.wizard_question_wizard_icon.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(197,234,250);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(197,234,250);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"")
        self.wizard_question_wizard_icon.setIconSize(QSize(184, 75))

        self.horizontalLayout_38.addWidget(self.wizard_question_wizard_icon)


        self.verticalLayout_51.addWidget(self.frame_66)

        self.wizard_quest_frame = QFrame(self.frame_65)
        self.wizard_quest_frame.setObjectName(u"wizard_quest_frame")
        self.wizard_quest_frame.setMinimumSize(QSize(0, 0))
        self.wizard_quest_frame.setStyleSheet(u"#wizard_quest_frame {\n"
"border: 5px solid rgb(64,144,253);\n"
"border-radius: 35px;\n"
"}")
        self.wizard_quest_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_quest_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.wizard_quest_frame)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(30, 30, 30, 30)
        self.wizard_question = QLabel(self.wizard_quest_frame)
        self.wizard_question.setObjectName(u"wizard_question")
        self.wizard_question.setMinimumSize(QSize(0, 100))
        self.wizard_question.setFont(font1)
        self.wizard_question.setStyleSheet(u"")
        self.wizard_question.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_question.setFrameShadow(QFrame.Shadow.Plain)
        self.wizard_question.setWordWrap(True)

        self.verticalLayout_52.addWidget(self.wizard_question)


        self.verticalLayout_51.addWidget(self.wizard_quest_frame)

        self.scrollArea_17 = QScrollArea(self.frame_65)
        self.scrollArea_17.setObjectName(u"scrollArea_17")
        self.scrollArea_17.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollAreaWidgetContents_22 = QWidget()
        self.scrollAreaWidgetContents_22.setObjectName(u"scrollAreaWidgetContents_22")
        self.scrollAreaWidgetContents_22.setGeometry(QRect(0, 0, 592, 295))
        self.verticalLayout_59 = QVBoxLayout(self.scrollAreaWidgetContents_22)
        self.verticalLayout_59.setSpacing(6)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.wizard_question_answer_frame = QFrame(self.scrollAreaWidgetContents_22)
        self.wizard_question_answer_frame.setObjectName(u"wizard_question_answer_frame")
        self.wizard_question_answer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_question_answer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_81 = QGridLayout(self.wizard_question_answer_frame)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setHorizontalSpacing(6)
        self.gridLayout_81.setContentsMargins(0, 0, 0, 0)
        self.wizard_question_answer = QComboBox(self.wizard_question_answer_frame)
        self.wizard_question_answer.setObjectName(u"wizard_question_answer")
        self.wizard_question_answer.setMinimumSize(QSize(0, 30))
        self.wizard_question_answer.setFont(font1)

        self.gridLayout_81.addWidget(self.wizard_question_answer, 1, 0, 1, 1)

        self.label_113 = QLabel(self.wizard_question_answer_frame)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font1)

        self.gridLayout_81.addWidget(self.label_113, 0, 0, 1, 1)

        self.verticalSpacer_57 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_81.addItem(self.verticalSpacer_57, 2, 0, 1, 1)


        self.verticalLayout_59.addWidget(self.wizard_question_answer_frame)

        self.wizard_path_input_frame = QFrame(self.scrollAreaWidgetContents_22)
        self.wizard_path_input_frame.setObjectName(u"wizard_path_input_frame")
        self.wizard_path_input_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_path_input_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.wizard_path_input_frame)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 9)
        self.label_112 = QLabel(self.wizard_path_input_frame)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font1)

        self.verticalLayout_57.addWidget(self.label_112)

        self.frame_75 = QFrame(self.wizard_path_input_frame)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.wizard_path_input = QLineEdit(self.frame_75)
        self.wizard_path_input.setObjectName(u"wizard_path_input")
        self.wizard_path_input.setMinimumSize(QSize(500, 30))
        self.wizard_path_input.setMaximumSize(QSize(500, 16777215))
        self.wizard_path_input.setFont(font1)
        self.wizard_path_input.setReadOnly(True)

        self.horizontalLayout_41.addWidget(self.wizard_path_input)

        self.wizard_path_input_bn = QPushButton(self.frame_75)
        self.wizard_path_input_bn.setObjectName(u"wizard_path_input_bn")
        self.wizard_path_input_bn.setMinimumSize(QSize(0, 30))
        self.wizard_path_input_bn.setFont(font1)
        self.wizard_path_input_bn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_41.addWidget(self.wizard_path_input_bn)

        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_86)


        self.verticalLayout_57.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.wizard_path_input_frame)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_45.setSpacing(30)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.wizard_path_check = QPushButton(self.frame_76)
        self.wizard_path_check.setObjectName(u"wizard_path_check")
        self.wizard_path_check.setMinimumSize(QSize(170, 35))
        self.wizard_path_check.setFont(font1)
        self.wizard_path_check.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_45.addWidget(self.wizard_path_check, 0, Qt.AlignmentFlag.AlignHCenter)

        self.wizard_data_checked_label = QLabel(self.frame_76)
        self.wizard_data_checked_label.setObjectName(u"wizard_data_checked_label")
        self.wizard_data_checked_label.setFont(font3)

        self.horizontalLayout_45.addWidget(self.wizard_data_checked_label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_57.addWidget(self.frame_76, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_58 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_57.addItem(self.verticalSpacer_58)


        self.verticalLayout_59.addWidget(self.wizard_path_input_frame)

        self.wizard_model_input_frame = QFrame(self.scrollAreaWidgetContents_22)
        self.wizard_model_input_frame.setObjectName(u"wizard_model_input_frame")
        self.wizard_model_input_frame.setMinimumSize(QSize(0, 0))
        self.wizard_model_input_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.wizard_model_input_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.wizard_model_input_frame)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_116 = QLabel(self.wizard_model_input_frame)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setFont(font1)

        self.verticalLayout_60.addWidget(self.label_116)

        self.frame_77 = QFrame(self.wizard_model_input_frame)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.wizard_model_input = QLineEdit(self.frame_77)
        self.wizard_model_input.setObjectName(u"wizard_model_input")
        self.wizard_model_input.setMinimumSize(QSize(500, 30))
        self.wizard_model_input.setFont(font1)
        self.wizard_model_input.setReadOnly(True)

        self.horizontalLayout_44.addWidget(self.wizard_model_input)

        self.wizard_model_browse_bn = QPushButton(self.frame_77)
        self.wizard_model_browse_bn.setObjectName(u"wizard_model_browse_bn")
        self.wizard_model_browse_bn.setMinimumSize(QSize(0, 30))
        self.wizard_model_browse_bn.setFont(font1)
        self.wizard_model_browse_bn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_44.addWidget(self.wizard_model_browse_bn)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_85)


        self.verticalLayout_60.addWidget(self.frame_77)

        self.wizard_model_check_bn = QPushButton(self.wizard_model_input_frame)
        self.wizard_model_check_bn.setObjectName(u"wizard_model_check_bn")
        self.wizard_model_check_bn.setMinimumSize(QSize(170, 35))
        self.wizard_model_check_bn.setFont(font1)
        self.wizard_model_check_bn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout_60.addWidget(self.wizard_model_check_bn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_59 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_59)


        self.verticalLayout_59.addWidget(self.wizard_model_input_frame)

        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_22)

        self.verticalLayout_51.addWidget(self.scrollArea_17)

        self.frame_52 = QFrame(self.frame_65)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 50))
        self.frame_52.setMaximumSize(QSize(16777215, 50))
        self.frame_52.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.wizard_back_bn = QPushButton(self.frame_52)
        self.wizard_back_bn.setObjectName(u"wizard_back_bn")
        self.wizard_back_bn.setMinimumSize(QSize(100, 35))
        font6 = QFont()
        font6.setFamilies([u"DejaVu Math TeX Gyre"])
        font6.setPointSize(20)
        self.wizard_back_bn.setFont(font6)
        self.wizard_back_bn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_37.addWidget(self.wizard_back_bn)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_81)

        self.wizard_cont_bn = QPushButton(self.frame_52)
        self.wizard_cont_bn.setObjectName(u"wizard_cont_bn")
        self.wizard_cont_bn.setMinimumSize(QSize(100, 35))
        self.wizard_cont_bn.setFont(font6)
        self.wizard_cont_bn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_37.addWidget(self.wizard_cont_bn)


        self.verticalLayout_51.addWidget(self.frame_52)


        self.horizontalLayout_40.addWidget(self.frame_65)


        self.verticalLayout_49.addWidget(self.frame_8)

        self.wizard_main_frame.addWidget(self.questionary_page)
        self.summary_page = QWidget()
        self.summary_page.setObjectName(u"summary_page")
        self.frame_71 = QFrame(self.summary_page)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setGeometry(QRect(0, 0, 948, 555))
        self.frame_71.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_71.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_71)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_72 = QFrame(self.frame_71)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 450))
        self.frame_72.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_72.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_72)
        self.verticalLayout_61.setSpacing(25)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_108 = QLabel(self.frame_72)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamilies([u"DejaVu Math TeX Gyre"])
        font7.setBold(True)
        self.label_108.setFont(font7)
        self.label_108.setStyleSheet(u"color: rgb(64,144,253);\n"
"font-weight: bold;")

        self.verticalLayout_61.addWidget(self.label_108)

        self.frame_78 = QFrame(self.frame_72)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_78.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_79 = QGridLayout(self.frame_78)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.gridLayout_79.setHorizontalSpacing(0)
        self.gridLayout_79.setVerticalSpacing(10)
        self.gridLayout_79.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_78)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_79.addWidget(self.label_24, 0, 0, 1, 1)

        self.wizard_config_file_label = QLabel(self.frame_78)
        self.wizard_config_file_label.setObjectName(u"wizard_config_file_label")
        font8 = QFont()
        font8.setFamilies([u"DejaVu Math TeX Gyre"])
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(True)
        self.wizard_config_file_label.setFont(font8)
        self.wizard_config_file_label.setStyleSheet(u"color: rgb(120,120,120);\n"
"font: italic;")

        self.gridLayout_79.addWidget(self.wizard_config_file_label, 1, 0, 1, 1)


        self.verticalLayout_61.addWidget(self.frame_78)

        self.scrollArea_18 = QScrollArea(self.frame_72)
        self.scrollArea_18.setObjectName(u"scrollArea_18")
        self.scrollArea_18.setStyleSheet(u"background:rgb(255,255,255);\n"
"")
        self.scrollArea_18.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_18.setWidgetResizable(True)
        self.scrollAreaWidgetContents_23 = QWidget()
        self.scrollAreaWidgetContents_23.setObjectName(u"scrollAreaWidgetContents_23")
        self.scrollAreaWidgetContents_23.setGeometry(QRect(0, 0, 930, 173))
        self.verticalLayout_62 = QVBoxLayout(self.scrollAreaWidgetContents_23)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.scrollArea_18.setWidget(self.scrollAreaWidgetContents_23)

        self.verticalLayout_61.addWidget(self.scrollArea_18)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_61.addItem(self.verticalSpacer_31)


        self.verticalLayout_50.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_71)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.wizard_summary_back_bn = QPushButton(self.frame_73)
        self.wizard_summary_back_bn.setObjectName(u"wizard_summary_back_bn")
        self.wizard_summary_back_bn.setMinimumSize(QSize(91, 24))
        font9 = QFont()
        font9.setPointSize(12)
        self.wizard_summary_back_bn.setFont(font9)
        self.wizard_summary_back_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.wizard_summary_back_bn.setIconSize(QSize(80, 14))

        self.horizontalLayout_42.addWidget(self.wizard_summary_back_bn)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_83)

        self.summary_end_bn = QPushButton(self.frame_73)
        self.summary_end_bn.setObjectName(u"summary_end_bn")
        self.summary_end_bn.setMinimumSize(QSize(180, 35))
        self.summary_end_bn.setFont(font1)
        self.summary_end_bn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_42.addWidget(self.summary_end_bn)

        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_84)


        self.verticalLayout_50.addWidget(self.frame_73, 0, Qt.AlignmentFlag.AlignVCenter)

        self.wizard_main_frame.addWidget(self.summary_page)

        self.verticalLayout_48.addWidget(self.wizard_main_frame)

        self.stackedWidget.addWidget(self.page_wizard)
        self.page_run_biapy = QWidget()
        self.page_run_biapy.setObjectName(u"page_run_biapy")
        self.horizontalLayout_29 = QHBoxLayout(self.page_run_biapy)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_run_biapy)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font1)
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_72 = QGridLayout(self.frame_7)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setVerticalSpacing(15)
        self.gridLayout_72.setContentsMargins(9, 9, 9, 9)
        self.frame_47 = QFrame(self.frame_7)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.check_yaml_file_bn = QPushButton(self.frame_47)
        self.check_yaml_file_bn.setObjectName(u"check_yaml_file_bn")
        self.check_yaml_file_bn.setMinimumSize(QSize(200, 40))
        self.check_yaml_file_bn.setMaximumSize(QSize(100, 16777215))
        self.check_yaml_file_bn.setFont(font1)

        self.horizontalLayout_6.addWidget(self.check_yaml_file_bn)


        self.gridLayout_72.addWidget(self.frame_47, 2, 1, 1, 1)

        self.tabWidget = QTabWidget(self.frame_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_39 = QGridLayout(self.tab)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        font10 = QFont()
        font10.setFamilies([u"DejaVu Math TeX Gyre"])
        font10.setPointSize(12)
        font10.setBold(False)
        self.label_9.setFont(font10)

        self.gridLayout_39.addWidget(self.label_9, 0, 0, 1, 1)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_89, 0, 3, 1, 1)

        self.container_info = QPushButton(self.tab)
        self.container_info.setObjectName(u"container_info")
        self.container_info.setMinimumSize(QSize(30, 30))
        self.container_info.setMaximumSize(QSize(30, 30))
        self.container_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_39.addWidget(self.container_info, 1, 1, 1, 1)

        self.container_version_label = QLabel(self.tab)
        self.container_version_label.setObjectName(u"container_version_label")
        self.container_version_label.setFont(font10)

        self.gridLayout_39.addWidget(self.container_version_label, 1, 0, 1, 1)

        self.device_input = QComboBox(self.tab)
        self.device_input.setObjectName(u"device_input")
        self.device_input.setMinimumSize(QSize(300, 30))
        self.device_input.setMaximumSize(QSize(16777215, 30))
        self.device_input.setFont(font1)

        self.gridLayout_39.addWidget(self.device_input, 0, 2, 1, 1)

        self.container_input = QComboBox(self.tab)
        self.container_input.setObjectName(u"container_input")
        self.container_input.setMinimumSize(QSize(0, 30))
        self.container_input.setMaximumSize(QSize(16777215, 30))
        self.container_input.setFont(font1)

        self.gridLayout_39.addWidget(self.container_input, 1, 2, 1, 1)

        self.device_info = QPushButton(self.tab)
        self.device_info.setObjectName(u"device_info")
        self.device_info.setMinimumSize(QSize(30, 30))
        self.device_info.setMaximumSize(QSize(30, 30))
        self.device_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_39.addWidget(self.device_info, 0, 1, 1, 1)

        self.verticalSpacer_62 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_39.addItem(self.verticalSpacer_62, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.SYSTEM__NUM_CPUS__INFO = QPushButton(self.tab_2)
        self.SYSTEM__NUM_CPUS__INFO.setObjectName(u"SYSTEM__NUM_CPUS__INFO")
        self.SYSTEM__NUM_CPUS__INFO.setMinimumSize(QSize(30, 30))
        self.SYSTEM__NUM_CPUS__INFO.setMaximumSize(QSize(30, 30))
        self.SYSTEM__NUM_CPUS__INFO.setFont(font1)
        self.SYSTEM__NUM_CPUS__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_5.addWidget(self.SYSTEM__NUM_CPUS__INFO, 0, 1, 1, 1)

        self.SYSTEM__SEED__INFO = QPushButton(self.tab_2)
        self.SYSTEM__SEED__INFO.setObjectName(u"SYSTEM__SEED__INFO")
        self.SYSTEM__SEED__INFO.setMinimumSize(QSize(30, 30))
        self.SYSTEM__SEED__INFO.setMaximumSize(QSize(30, 30))
        self.SYSTEM__SEED__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_5.addWidget(self.SYSTEM__SEED__INFO, 2, 1, 1, 1)

        self.SYSTEM__SEED__INPUT = QLineEdit(self.tab_2)
        self.SYSTEM__SEED__INPUT.setObjectName(u"SYSTEM__SEED__INPUT")
        self.SYSTEM__SEED__INPUT.setMinimumSize(QSize(200, 30))
        self.SYSTEM__SEED__INPUT.setMaximumSize(QSize(200, 30))
        self.SYSTEM__SEED__INPUT.setFont(font1)

        self.gridLayout_5.addWidget(self.SYSTEM__SEED__INPUT, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(479, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.SYSTEM__NUM_CPUS__INPUT = QComboBox(self.tab_2)
        self.SYSTEM__NUM_CPUS__INPUT.setObjectName(u"SYSTEM__NUM_CPUS__INPUT")
        self.SYSTEM__NUM_CPUS__INPUT.setMinimumSize(QSize(200, 30))
        self.SYSTEM__NUM_CPUS__INPUT.setMaximumSize(QSize(200, 30))
        self.SYSTEM__NUM_CPUS__INPUT.setFont(font1)

        self.gridLayout_5.addWidget(self.SYSTEM__NUM_CPUS__INPUT, 0, 2, 1, 1)

        self.SYSTEM__NUM_CPUS__LABEL = QLabel(self.tab_2)
        self.SYSTEM__NUM_CPUS__LABEL.setObjectName(u"SYSTEM__NUM_CPUS__LABEL")
        self.SYSTEM__NUM_CPUS__LABEL.setFont(font1)

        self.gridLayout_5.addWidget(self.SYSTEM__NUM_CPUS__LABEL, 0, 0, 1, 1)

        self.SYSTEM__NUM_WORKERS__INPUT = QComboBox(self.tab_2)
        self.SYSTEM__NUM_WORKERS__INPUT.setObjectName(u"SYSTEM__NUM_WORKERS__INPUT")
        self.SYSTEM__NUM_WORKERS__INPUT.setMinimumSize(QSize(200, 30))
        self.SYSTEM__NUM_WORKERS__INPUT.setMaximumSize(QSize(200, 30))
        self.SYSTEM__NUM_WORKERS__INPUT.setFont(font1)

        self.gridLayout_5.addWidget(self.SYSTEM__NUM_WORKERS__INPUT, 1, 2, 1, 1)

        self.SYSTEM__NUM_WORKERS__INFO = QPushButton(self.tab_2)
        self.SYSTEM__NUM_WORKERS__INFO.setObjectName(u"SYSTEM__NUM_WORKERS__INFO")
        self.SYSTEM__NUM_WORKERS__INFO.setMinimumSize(QSize(30, 30))
        self.SYSTEM__NUM_WORKERS__INFO.setMaximumSize(QSize(30, 30))
        self.SYSTEM__NUM_WORKERS__INFO.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_5.addWidget(self.SYSTEM__NUM_WORKERS__INFO, 1, 1, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(200, 35))
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.verticalSpacer_63 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_63, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_72.addWidget(self.tabWidget, 3, 1, 1, 1)

        self.output_final_directory_label = QLabel(self.frame_7)
        self.output_final_directory_label.setObjectName(u"output_final_directory_label")
        self.output_final_directory_label.setFont(font1)
        self.output_final_directory_label.setWordWrap(True)

        self.gridLayout_72.addWidget(self.output_final_directory_label, 1, 1, 1, 1)

        self.frame_27 = QFrame(self.frame_7)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setMaximumSize(QSize(16777215, 120))
        self.frame_27.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_27)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(6)
        self.gridLayout_9.setContentsMargins(0, -1, 9, -1)
        self.examine_yaml_bn = QPushButton(self.frame_27)
        self.examine_yaml_bn.setObjectName(u"examine_yaml_bn")
        self.examine_yaml_bn.setMinimumSize(QSize(0, 30))
        self.examine_yaml_bn.setMaximumSize(QSize(16777215, 30))
        self.examine_yaml_bn.setFont(font1)

        self.gridLayout_9.addWidget(self.examine_yaml_bn, 0, 5, 1, 1)

        self.select_yaml_name_label = QLineEdit(self.frame_27)
        self.select_yaml_name_label.setObjectName(u"select_yaml_name_label")
        self.select_yaml_name_label.setMinimumSize(QSize(450, 30))
        self.select_yaml_name_label.setMaximumSize(QSize(450, 30))
        self.select_yaml_name_label.setFont(font1)

        self.gridLayout_9.addWidget(self.select_yaml_name_label, 0, 3, 1, 1)

        self.select_yaml_name_info = QPushButton(self.frame_27)
        self.select_yaml_name_info.setObjectName(u"select_yaml_name_info")
        self.select_yaml_name_info.setMinimumSize(QSize(30, 30))
        self.select_yaml_name_info.setMaximumSize(QSize(30, 30))
        self.select_yaml_name_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_9.addWidget(self.select_yaml_name_info, 0, 2, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_24, 0, 6, 1, 1)

        self.output_folder_bn = QPushButton(self.frame_27)
        self.output_folder_bn.setObjectName(u"output_folder_bn")
        self.output_folder_bn.setMinimumSize(QSize(0, 30))
        self.output_folder_bn.setMaximumSize(QSize(16777215, 30))
        self.output_folder_bn.setFont(font1)

        self.gridLayout_9.addWidget(self.output_folder_bn, 3, 5, 1, 1)

        self.output_folder_info = QPushButton(self.frame_27)
        self.output_folder_info.setObjectName(u"output_folder_info")
        self.output_folder_info.setMinimumSize(QSize(30, 30))
        self.output_folder_info.setMaximumSize(QSize(30, 30))
        self.output_folder_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_9.addWidget(self.output_folder_info, 3, 2, 1, 1)

        self.select_yaml_label = QLabel(self.frame_27)
        self.select_yaml_label.setObjectName(u"select_yaml_label")
        self.select_yaml_label.setFont(font1)

        self.gridLayout_9.addWidget(self.select_yaml_label, 0, 0, 1, 2)

        self.label_138 = QLabel(self.frame_27)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font1)

        self.gridLayout_9.addWidget(self.label_138, 2, 0, 1, 1)

        self.job_name_info = QPushButton(self.frame_27)
        self.job_name_info.setObjectName(u"job_name_info")
        self.job_name_info.setMinimumSize(QSize(30, 30))
        self.job_name_info.setMaximumSize(QSize(30, 30))
        self.job_name_info.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"}")

        self.gridLayout_9.addWidget(self.job_name_info, 2, 2, 1, 1)

        self.output_folder_input = QLineEdit(self.frame_27)
        self.output_folder_input.setObjectName(u"output_folder_input")
        self.output_folder_input.setMinimumSize(QSize(450, 30))
        self.output_folder_input.setMaximumSize(QSize(450, 30))
        self.output_folder_input.setFont(font1)

        self.gridLayout_9.addWidget(self.output_folder_input, 3, 3, 1, 1)

        self.output_folder_label = QLabel(self.frame_27)
        self.output_folder_label.setObjectName(u"output_folder_label")
        self.output_folder_label.setMaximumSize(QSize(16777215, 35))
        self.output_folder_label.setFont(font1)

        self.gridLayout_9.addWidget(self.output_folder_label, 3, 0, 1, 2)

        self.job_name_input = QPlainTextEdit(self.frame_27)
        self.job_name_input.setObjectName(u"job_name_input")
        self.job_name_input.setMinimumSize(QSize(450, 30))
        self.job_name_input.setMaximumSize(QSize(450, 30))
        self.job_name_input.setFont(font1)
        self.job_name_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.job_name_input.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.job_name_input.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.gridLayout_9.addWidget(self.job_name_input, 2, 3, 1, 1)


        self.gridLayout_72.addWidget(self.frame_27, 0, 1, 1, 1)

        self.frame_64 = QFrame(self.frame_7)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_64)
        self.verticalLayout_39.setSpacing(11)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(11, 11, 11, 11)
        self.run_biapy_docker_bn = QPushButton(self.frame_64)
        self.run_biapy_docker_bn.setObjectName(u"run_biapy_docker_bn")
        self.run_biapy_docker_bn.setMinimumSize(QSize(300, 40))
        self.run_biapy_docker_bn.setMaximumSize(QSize(300, 16777215))
        self.run_biapy_docker_bn.setFont(font1)
        self.run_biapy_docker_bn.setIconSize(QSize(250, 33))

        self.verticalLayout_39.addWidget(self.run_biapy_docker_bn)


        self.gridLayout_72.addWidget(self.frame_64, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_29.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_run_biapy)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_bottom_east)


        self.horizontalLayout.addWidget(self.frame_east)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.wizard_main_frame.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.biapy_logo_label.setText("")
        self.biapy_version.setText(QCoreApplication.translate("MainWindow", u"Version 3.3.8 - GUI: 1.0.0", None))
        self.bn_home.setText("")
        self.bn_wizard.setText("")
        self.bn_run_biapy.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"  External links", None))
        self.biapy_github_bn.setText("")
        self.home_project_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Project page</p></body></html>", None))
        self.biapy_forum_bn.setText("")
        self.forum_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Forum</p></body></html>", None))
        self.biapy_doc_bn.setText("")
        self.documentation_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Documentation</p></body></html>", None))
        self.biapy_templates_bn.setText("")
        self.templates_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Templates</p></body></html>", None))
        self.biapy_notebooks_bn.setText("")
        self.notebooks_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Notebooks</p></body></html>", None))
        self.biapy_citation_bn.setText("")
        self.citation_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Citation</p></body></html>", None))
        self.gpu_head_label.setText(QCoreApplication.translate("MainWindow", u"GPU dependency", None))
        self.docker_head_label.setText(QCoreApplication.translate("MainWindow", u"Docker dependency", None))
        self.main_window_wizard_question_wizard_icon.setText("")
        self.load_yaml_bn.setText(QCoreApplication.translate("MainWindow", u"Load and modify workflow", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"First timers: talk to the Wizard!", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Frequent users", None))
        self.wizard_start_message.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Hello, I'm the wizard of BiaPy, and I'll be guiding you through this process. During the questionnaire, you can click on me to get more information about each question.</p><p>This questionnaire will guide you in creating a configuration file needed to run BiaPy. To start, please fill in the fields below to specify where the configuration file should be created. Once completed, click the &quot;Start&quot; button to begin the questionnaire.</p></body></html>", None))
        self.wizard_start_wizard_icon.setText("")
#if QT_CONFIG(tooltip)
        self.wizard_browse_yaml_path_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Configuration file name: You don\u2019t need to include the file extension. BiaPy will automatically add the .yaml extension, which is the format used for the configuration file created by the Wizard.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wizard_browse_yaml_path_info.setText("")
#if QT_CONFIG(tooltip)
        self.WIZARD_PROBLEM__NDIM__INFO.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Directory to save the configuration file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.WIZARD_PROBLEM__NDIM__INFO.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.WIZARD_PROBLEM__NDIM__INFO.setText("")
        self.wizard_browse_yaml_path_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.wizard_browse_yaml_path_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.wizard_browse_yaml_path_label.setText(QCoreApplication.translate("MainWindow", u"Configuration file directory", None))
#if QT_CONFIG(statustip)
        self.wizard_browse_yaml_path_input.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.wizard_yaml_name_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.wizard_yaml_name_label.setText(QCoreApplication.translate("MainWindow", u"Configuration file name", None))
#if QT_CONFIG(tooltip)
        self.wizard_yaml_name_input.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.wizard_yaml_name_input.setText("")
        self.wizard_start_bn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.wizard_clear_answers_bn.setText(QCoreApplication.translate("MainWindow", u"Clear all answers", None))
        self.wizard_question_label.setText(QCoreApplication.translate("MainWindow", u"Question 1", None))
        self.wizard_question_wizard_icon.setText("")
        self.wizard_question.setText("")
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Answers", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Selected path", None))
        self.wizard_path_input_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.wizard_path_check.setText(QCoreApplication.translate("MainWindow", u"Check data", None))
        self.wizard_data_checked_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u2190</span> Data not checked yet</p></body></html>", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Selected model", None))
        self.wizard_model_browse_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.wizard_model_check_bn.setText(QCoreApplication.translate("MainWindow", u"Check models", None))
        self.wizard_back_bn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.wizard_cont_bn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"SUMMARY", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Configuration file", None))
        self.wizard_config_file_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.wizard_summary_back_bn.setText("")
        self.summary_end_bn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.check_yaml_file_bn.setText(QCoreApplication.translate("MainWindow", u"Check file", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select device to run workflow", None))
#if QT_CONFIG(tooltip)
        self.container_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Which container of BiaPy to use. The GUI has always a default container version linked but if there are new available they will be listed too.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.container_info.setText("")
        self.container_version_label.setText(QCoreApplication.translate("MainWindow", u"Container to use", None))
#if QT_CONFIG(tooltip)
        self.device_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Select the device in which you want to run BiaPy. If a GPU is used the process will be much faster (specially the training).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.device_info.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Basic settings", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Math seed", None))
#if QT_CONFIG(tooltip)
        self.SYSTEM__NUM_CPUS__INFO.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maximum number of CPUs to use. Set it to &quot;-1&quot; to not set a limit.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SYSTEM__NUM_CPUS__INFO.setText("")
#if QT_CONFIG(tooltip)
        self.SYSTEM__SEED__INFO.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Math seed to generate random numbers. Used to ensure reproducibility in the results. </span><span style=\" font-size:12pt; font-weight:600;\">Must be an integer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SYSTEM__SEED__INFO.setText("")
        self.SYSTEM__SEED__INPUT.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SYSTEM__NUM_CPUS__LABEL.setText(QCoreApplication.translate("MainWindow", u"Number of CPUs", None))
#if QT_CONFIG(tooltip)
        self.SYSTEM__NUM_WORKERS__INFO.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maximum number of workers to use. You can disable this option by setting 0</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SYSTEM__NUM_WORKERS__INFO.setText("")
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number of workers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Advanced options", None))
        self.output_final_directory_label.setText("")
        self.examine_yaml_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.select_yaml_name_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">YAML configuration file to run BiaPy with. If you completed the proccess of creating a new YAML file this value will be set pointing to file. However, you can change it too.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.select_yaml_name_info.setText("")
        self.output_folder_bn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.output_folder_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Path to store the results. If you complete the proccess of creating a new one automatically this will point to the folder where you select to save the YAML file. It will be used to create a folder in the output path you selected. For instance, if the job name was set to &quot;my_semantic_segmentation&quot;, and if the output folder to save the results is &quot;/home/user/Downloads&quot;, all results of the experiment will be placed at : /home/user/Downloads/my_semantic_segmentation </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.output_folder_info.setText("")
#if QT_CONFIG(tooltip)
        self.select_yaml_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.select_yaml_label.setText(QCoreApplication.translate("MainWindow", u"Select configuration file", None))
#if QT_CONFIG(tooltip)
        self.label_138.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Job name", None))
#if QT_CONFIG(tooltip)
        self.job_name_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Name of the job. It will be used to create a folder in the output path you selected. For instance, if the job name was set to &quot;my_semantic_segmentation&quot;, and if the output folder to save the results is &quot;/home/user/Downloads&quot;, all results of the experiment will be placed at : /home/user/Downloads/my_semantic_segmentation </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.job_name_info.setText("")
#if QT_CONFIG(tooltip)
        self.output_folder_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.output_folder_label.setText(QCoreApplication.translate("MainWindow", u"Output folder to save the results", None))
#if QT_CONFIG(tooltip)
        self.run_biapy_docker_bn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.run_biapy_docker_bn.setText(QCoreApplication.translate("MainWindow", u"Run Workflow", None))
    # retranslateUi

