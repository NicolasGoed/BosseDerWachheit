# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lastenheft.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from RequirementManagement import *


class LastenheftFenster(object):
    
    # Thi Dok
    def __init__(self, selectedProject):
        self.selectedProject = selectedProject
        
    # Niki Dok
    def setupUi(self, Dialog):
        Dialog.setObjectName("Lastenheft")
        Dialog.resize(800, 900)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 101, 31))
        self.label_2.setObjectName("Anforderungen")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setWordWrap(True)
        self.listWidget.setGeometry(QtCore.QRect(50, 120, 700, 730))
        self.listWidget.setObjectName("listWidget")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 101, 31))
        self.label_3.setObjectName("Projektname")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 400, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit Projektname")
        reqCount = 1 
        for aTuple in getAllRequirements(self.selectedProject):
            self.listWidget.addItem(str(reqCount) + ". Anforderung")
            reqCount = reqCount + 1
            self.listWidget.addItems(aTuple)
            self.listWidget.addItem("")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Niki Dok
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lastenheft"))
        self.label_2.setText(_translate("Dialog", "Anforderungen "))
        self.label_3.setText(_translate("Dialog", "Projektname"))
        self.lineEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Projektname"))
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText(self.selectedProject)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LastenheftFenster()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
