# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created: Mon May  2 01:33:05 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 139)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 281, 16))
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(50, 50, 281, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.helloButton = QtWidgets.QPushButton(Dialog)
        self.helloButton.setGeometry(QtCore.QRect(100, 90, 80, 23))
        self.helloButton.setObjectName("helloButton")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(190, 90, 80, 23))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Dialog)
        self.exitButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Demo Qt Designer"))
        self.label.setText(_translate("Dialog", "Masukkan nama Anda:"))
        self.helloButton.setText(_translate("Dialog", "Hallo"))
        self.exitButton.setText(_translate("Dialog", "Keluar"))

