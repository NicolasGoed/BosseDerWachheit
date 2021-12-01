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
#from signUp import SignUp
from MainWindowRequirement import MainFunction
from RequirementManagement import getAllRequirements
from UserManagement import createUser, checkUser
from PyQt5.QtWidgets import QMessageBox

######################################################################################################
### 1. Klasse Ui_dialog

# Niki - Bitte mach du die Klassenbschreibung --> Code Testen und auf schreiben was in dieser Klasse passiert
class Ui_dialog(object):
    """[summary]

    Args:
        object ([type]): [description]
    """


    def openWindow(self):
       """öffnet ein neues Fenster um einen neuen User zu registieren
            * versteckt das aktuelle Fenster
            * öffnet das neue Fenster

       Test:
            * checkt, ob das Fenster schon geöffnet ist

        Source:
            * https://www.youtube.com/watch?v=dRRpbDFnMHI
       """
       self.window = QtWidgets.QDialog()
       self.ui = SignUp()
       self.ui.setupUi(self.window)
       dialog.hide()
       self.window.show()


    def openLogin(self):
       """
       öffnet ein neues Fenster "Projekte" in der dann eine Übersicht aller Projekt ist. 
       """
       self.window = QtWidgets.QDialog()
       self.ui = MainFunction()
       self.ui.setupUi(self.window)
       dialog.hide()
       self.window.show()

    #NIKI: Bitte Dokumentation hierfür schreiben, ist GUI
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        dialog.setAutoFillBackground(False)
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 221, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 110, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 111, 23))
        self.pushButton.setObjectName("pushButton Anmelden")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 101, 23))
        self.pushButton_2.setObjectName("pushButton Abbrechen")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 250, 61))
        self.label.setObjectName("label Willkommen! Bitte melden Sie sich an")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 100, 13))
        self.label_2.setObjectName("label Passwort")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 100, 13))
        self.label_3.setObjectName("label Username")
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 240, 221, 23))
        self.pushButton_3.setObjectName("pushButton Neuen User registrieren")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    #NIKI: Bitte Dokumentation hierfür schreiben, ist GUI
    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Anmeldung"))
        self.pushButton.setText(_translate("dialog", "Anmelden"))
        self.pushButton_2.setText(_translate("dialog", "Abbrechen"))
        self.label.setText(_translate("dialog", "Willkommen! Bitte melden Sie sich an"))
        self.label_2.setText(_translate("dialog", "Passwort"))
        self.label_3.setText(_translate("dialog", "Username"))
        self.pushButton_3.setText(_translate("dialog", "Neuen User registrieren"))
        #dialog.setWindowIcon(QIcon("dhbwStutt.png"))

        self.lineEdit.setPlaceholderText(_translate("Dialog", "Passwort"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Username"))

        self.pushButton.clicked.connect(self.login_button_click)
        self.pushButton_2.clicked.connect(gedrueckt)
        self.pushButton_3.clicked.connect(self.openWindow)

    # Thi. Dok
    def login_button_click(self):
            # shost is a QString object
            shost = self.lineEdit_2.text()
            pword = self.lineEdit.text()
            
            if (checkUser(shost, pword)):
                currentuser = shost
                self.window = QtWidgets.QDialog()
                self.ui = MainFunction(currentuser)
                self.ui.setupUi(self.window)
                dialog.hide()
                self.window.show()
                
            else:
                 wrongUserNamePasswort()
            
# Thi Dok
def wrongUserNamePasswort():
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Falscher Username oder Passwort, bitte nochmal eingeben.")
    x = msg.exec_()
        

# Niki Dok
def gedrueckt():
        QtCore.QCoreApplication.instance().quit()
        

######################################################################################################
### 2. Klasse SignUp

class SignUp(object):

    # Thi Dok
    def openAnmeldung(self):
       uname = self.lineEdit_2.text()
       pword = self.lineEdit.text()
       cword = self.lineEdit_3.text()
       if pword == cword:
            createUser(uname, pword)
            QtWidgets.QApplication.activeWindow().close()             
            self.window = QtWidgets.QDialog()
            self.ui = Ui_dialog()
            self.ui.setupUi(self.window)
            #dialog.hide()
            self.window.show()

       else:
            mmm()

    # Niki
    def setupUi(self, Dialog):
        """[summary]

        Args:
            Dialog ([type]): [description]
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 344)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 100, 13))
        self.label_2.setObjectName("label Passwort")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 90, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 150, 221, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 0, 250, 61))
        self.label.setObjectName("label Bitte neue Daten eingeben")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 70, 100, 13))
        self.label_3.setObjectName("label Username")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 210, 221, 31))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 190, 150, 16))
        self.label_4.setObjectName("label Passwort wiederholen")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 250, 101, 23))
        self.pushButton_3.setObjectName("pushButton Registrieren")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 250, 101, 23))
        self.pushButton_4.setObjectName("pushButton Schließen")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Niki
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registrieren"))
        self.label_2.setText(_translate("Dialog", "Passwort"))
        self.label.setText(_translate("Dialog", "Bitte neue Daten eingeben"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Passwort wiederholen"))
        self.pushButton_3.setText(_translate("Dialog", "Registrieren"))
        self.pushButton_4.setText(_translate("Dialog", "Schließen"))
        self.pushButton_4.pressed.connect(closeapp)

        self.pushButton_3.clicked.connect(self.openAnmeldung)


######################################################################################################
               

# Niki
def mmm():
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Passwort nicht identisch.")
    x = msg.exec_()
    

# Niki Dok
def closeapp():
    QtCore.QCoreApplication.instance().quit()  #schliesst window, wenn "Cancel" gedrückt wird



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

