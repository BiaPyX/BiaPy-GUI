# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spinner.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_spinner(object):
    def setupUi(self, spinner):
        if not spinner.objectName():
            spinner.setObjectName(u"spinner")
        spinner.resize(111, 93)
        self.verticalLayout = QVBoxLayout(spinner)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(spinner)

        QMetaObject.connectSlotsByName(spinner)
    # setupUi

    def retranslateUi(self, spinner):
        spinner.setWindowTitle(QCoreApplication.translate("spinner", u"Dialog", None))
    # retranslateUi

