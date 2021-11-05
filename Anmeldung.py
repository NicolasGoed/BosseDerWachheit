# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ft.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from signUp import Ui_Dialog

class Ui_dialog(object):
    def openWindow(self):
       self.window = QtWidgets.QDialog()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.window)
       dialog.hide()
       self.window.show()

    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        dialog.setAutoFillBackground(False)
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 221, 31))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 110, 221, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 211, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 240, 221, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Testtttt"))
        self.pushButton.setText(_translate("dialog", "Login"))
        self.pushButton_2.setText(_translate("dialog", "Cancel"))
        self.label.setText(_translate("dialog", "Welcome! Please log in"))
        self.label_2.setText(_translate("dialog", "Password"))
        self.label_3.setText(_translate("dialog", "Username"))
        self.pushButton_3.setText(_translate("dialog", "Create new User"))
        dialog.setWindowIcon(QIcon("dhbwStutt.png"))
        self.pushButton_2.clicked.connect(gedrueckt)
        self.pushButton_3.clicked.connect(self.openWindow)


def gedrueckt():
        QtCore.QCoreApplication.instance().quit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
