# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UI_NewOPWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewQPWidget(object):
    def setupUi(self, NewQPWidget):
        NewQPWidget.setObjectName("NewQPWidget")
        NewQPWidget.setWindowModality(QtCore.Qt.ApplicationModal)
        NewQPWidget.resize(443, 157)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewQPWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(NewQPWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.qp_path_line_edit = QtWidgets.QLineEdit(NewQPWidget)
        self.qp_path_line_edit.setObjectName("qp_path_line_edit")
        self.horizontalLayout.addWidget(self.qp_path_line_edit)
        self.qp_path_tool_button = QtWidgets.QToolButton(NewQPWidget)
        self.qp_path_tool_button.setObjectName("qp_path_tool_button")
        self.horizontalLayout.addWidget(self.qp_path_tool_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(NewQPWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.qp_filename_line_edit = QtWidgets.QLineEdit(NewQPWidget)
        self.qp_filename_line_edit.setObjectName("qp_filename_line_edit")
        self.horizontalLayout_2.addWidget(self.qp_filename_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancel_push_button = QtWidgets.QPushButton(NewQPWidget)
        self.cancel_push_button.setObjectName("cancel_push_button")
        self.horizontalLayout_3.addWidget(self.cancel_push_button)
        self.create_qp_push_button = QtWidgets.QPushButton(NewQPWidget)
        self.create_qp_push_button.setObjectName("create_qp_push_button")
        self.horizontalLayout_3.addWidget(self.create_qp_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(NewQPWidget)
        QtCore.QMetaObject.connectSlotsByName(NewQPWidget)

    def retranslateUi(self, NewQPWidget):
        _translate = QtCore.QCoreApplication.translate
        NewQPWidget.setWindowTitle(_translate("NewQPWidget", "New Question Paper"))
        self.label.setText(_translate("NewQPWidget", "Path of Question Paper: "))
        self.qp_path_tool_button.setText(_translate("NewQPWidget", "..."))
        self.label_2.setText(_translate("NewQPWidget", "Question Paper File name (.qp):"))
        self.cancel_push_button.setText(_translate("NewQPWidget", "Cancel"))
        self.create_qp_push_button.setText(_translate("NewQPWidget", "Create Question Paper"))

