# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_yes_no.ui'
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_yes_no(object):
    def setupUi(self, yes_no):
        if not yes_no.objectName():
            yes_no.setObjectName(u"yes_no")
        yes_no.resize(600, 235)
        yes_no.setMinimumSize(QSize(600, 235))
        yes_no.setMaximumSize(QSize(600, 235))
        self.verticalLayout = QVBoxLayout(yes_no)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QFrame(yes_no)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFrameShape(QFrame.NoFrame)
        self.centralwidget.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(40, 40))
        self.frame_top.setMaximumSize(QSize(40, 40))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
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


        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        font = QFont()
        font.setFamilies([u"DejaVu Math TeX Gyre"])
        font.setPointSize(12)
        self.frame_bottom.setFont(font)
        self.frame_bottom.setStyleSheet(u"")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 9, 0)
        self.question_label = QLabel(self.frame_bottom)
        self.question_label.setObjectName(u"question_label")
        font1 = QFont()
        font1.setFamilies([u"DejaVu Math TeX Gyre"])
        font1.setPointSize(12)
        font1.setKerning(True)
        self.question_label.setFont(font1)
        self.question_label.setStyleSheet(u"")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.question_label)

        self.frame = QFrame(self.frame_bottom)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.yes_bn = QPushButton(self.frame)
        self.yes_bn.setObjectName(u"yes_bn")
        self.yes_bn.setMinimumSize(QSize(0, 0))
        self.yes_bn.setMaximumSize(QSize(100, 30))
        self.yes_bn.setFont(font)
        self.yes_bn.setFocusPolicy(Qt.NoFocus)
        self.yes_bn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.yes_bn)

        self.no_bn = QPushButton(self.frame)
        self.no_bn.setObjectName(u"no_bn")
        self.no_bn.setMaximumSize(QSize(100, 30))
        self.no_bn.setFont(font)
        self.no_bn.setFocusPolicy(Qt.NoFocus)
        self.no_bn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.no_bn)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(yes_no)

        QMetaObject.connectSlotsByName(yes_no)
    # setupUi

    def retranslateUi(self, yes_no):
        yes_no.setWindowTitle(QCoreApplication.translate("yes_no", u"yes_no", None))
        self.icon_label.setText("")
        self.question_label.setText(QCoreApplication.translate("yes_no", u"TEXT", None))
        self.yes_bn.setText(QCoreApplication.translate("yes_no", u"Yes", None))
        self.no_bn.setText(QCoreApplication.translate("yes_no", u"No", None))
    # retranslateUi

