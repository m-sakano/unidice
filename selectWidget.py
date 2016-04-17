# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(320, 240)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        Form.setWindowOpacity(0.5)
        Form.setAutoFillBackground(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "キャプチャ範囲選択"))
