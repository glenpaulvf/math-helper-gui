# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathHelperWindow(object):
    def setupUi(self, MathHelperWindow):
        MathHelperWindow.setObjectName("MathHelperWindow")
        MathHelperWindow.resize(314, 205)
        self.MathHelperElements = QtWidgets.QWidget(MathHelperWindow)
        self.MathHelperElements.setObjectName("MathHelperElements")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MathHelperElements)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.promptLabel = QtWidgets.QLabel(self.MathHelperElements)
        self.promptLabel.setObjectName("promptLabel")
        self.verticalLayout_2.addWidget(self.promptLabel)
        self.inputBox = QtWidgets.QLineEdit(self.MathHelperElements)
        self.inputBox.setObjectName("inputBox")
        self.verticalLayout_2.addWidget(self.inputBox)
        self.resultLabel = QtWidgets.QLabel(self.MathHelperElements)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout_2.addWidget(self.resultLabel)
        self.outputLabel = QtWidgets.QLabel(self.MathHelperElements)
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout_2.addWidget(self.outputLabel)
        MathHelperWindow.setCentralWidget(self.MathHelperElements)

        self.retranslateUi(MathHelperWindow)
        QtCore.QMetaObject.connectSlotsByName(MathHelperWindow)

    def retranslateUi(self, MathHelperWindow):
        _translate = QtCore.QCoreApplication.translate
        MathHelperWindow.setWindowTitle(_translate("MathHelperWindow", "Math GUI"))
        self.promptLabel.setText(_translate("MathHelperWindow", "Enter math command:"))
        self.resultLabel.setText(_translate("MathHelperWindow", "Result:"))

