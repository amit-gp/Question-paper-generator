# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UI_QPDWelcomeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QPDWelcomeDialog(object):
    def setupUi(self, QPDWelcomeDialog):
        QPDWelcomeDialog.setObjectName("QPDWelcomeDialog")
        QPDWelcomeDialog.resize(448, 152)
        self.verticalLayout = QtWidgets.QVBoxLayout(QPDWelcomeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QPDWelcomeDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_push_button = QtWidgets.QPushButton(QPDWelcomeDialog)
        self.create_push_button.setObjectName("create_push_button")
        self.horizontalLayout.addWidget(self.create_push_button)
        self.open_push_button = QtWidgets.QPushButton(QPDWelcomeDialog)
        self.open_push_button.setObjectName("open_push_button")
        self.horizontalLayout.addWidget(self.open_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QPDWelcomeDialog)
        QtCore.QMetaObject.connectSlotsByName(QPDWelcomeDialog)

    def retranslateUi(self, QPDWelcomeDialog):
        _translate = QtCore.QCoreApplication.translate
        QPDWelcomeDialog.setWindowTitle(_translate("QPDWelcomeDialog", "Welcome"))
        self.label.setText(_translate("QPDWelcomeDialog", "Welcome to QPD Editor.."))
        self.create_push_button.setText(_translate("QPDWelcomeDialog", "Create a new QPD file"))
        self.open_push_button.setText(_translate("QPDWelcomeDialog", "Open existing QPD file"))

