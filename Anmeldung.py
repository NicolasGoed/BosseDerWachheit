
"""Anmeldung Modul
    * Beinhaltet 2 Klassen:
        - 1. Klasse: Login-Fenster
        - 2. Klasse: Sign Up-Fenster


authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
#from signUp import SignUp
from MainWindowRequirement import MainFunction
from UserManagement import createUser, checkUser
from PyQt5.QtWidgets import QMessageBox

######################################################################################################
### 1. Klasse Ui_dialog

class Ui_dialog(object):
    """Ui_dialog
        * Eine Klasse in der sich User über ein GUI-Fenster anmelden oder registrieren können 

    Args:
        object (class): beinhaltet ein Fenster mit Buttons

    Funktionen:
        * openWindow()
        * openLogin()
        * setupUi()
        * retranslateUi():
        * login_button_click()
    """

    def openWindow(self):
       """öffnet ein neues Fenster um einen neuen User zu registieren
            * versteckt das aktuelle Fenster
            * öffnet das neue Fenster

        Test:
            * checkt, ob das Fenster schon geöffnet ist um 2 gleiche Fenster zu vermeiden
            * überprüfung, ob im alten Fenster noch eingetragene Daten sind, wenn dieses geschlossen wird

        Source:
            * https://www.youtube.com/watch?v=dRRpbDFnMHI
       """
       self.window = QtWidgets.QDialog()
       self.ui = SignUp()
       self.ui.setupUi(self.window)
       dialog.hide()
       self.window.show()


    def openLogin(self):
       """öffnet ein neues Fenster "Projekte" in der dann eine Übersicht aller Projekte ist. 

        Test:
            * checkt, ob das Fenster schon geöffnet ist um 2 gleiche Fenster zu vermeiden
            * überprüfung, ob im alten Fenster noch eingetragene Daten sind, wenn dieses geschlossen wird
       """
       self.window = QtWidgets.QDialog()
       self.ui = MainFunction()
       self.ui.setupUi(self.window)
       dialog.hide()
       self.window.show()


    def setupUi(self, dialog):
        """Setup und Initialisierung der verschiedenen GUI-Komponenten

        Args:
            dialog (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Komponenten in das Dialogfenster reinpassen
            * Überprüfung, ob Passwort nicht sichtbar und nicht kopierbar dargestellt wird
        """
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        dialog.setAutoFillBackground(False)
        self.lineEdit = QtWidgets.QLineEdit(dialog)

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 250, 61))
        self.label.setObjectName("label Willkommen! Bitte melden Sie sich an")

        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 100, 13))
        self.label_3.setObjectName("label Username")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 110, 221, 31))
        self.lineEdit_2.setObjectName("Username")

        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 100, 13))
        self.label_2.setObjectName("label Passwort")
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 221, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("Passwort")

        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 111, 23))
        self.pushButton.setObjectName("pushButton Anmelden")

        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 101, 23))
        self.pushButton_2.setObjectName("pushButton Abbrechen")

        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 240, 221, 23))
        self.pushButton_3.setObjectName("pushButton Neuen User registrieren")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)


    def retranslateUi(self, dialog):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten + schafft über Connections zu den Listener Funktionen

        Args:
            dialog (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung, ob die durch die Listener erstellten Connections funktionieren.
        """
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Anmeldung"))
        self.pushButton.setText(_translate("dialog", "Anmelden"))
        self.pushButton_2.setText(_translate("dialog", "Abbrechen"))
        self.label.setText(_translate("dialog", "Willkommen! Bitte melden Sie sich an"))
        self.label_2.setText(_translate("dialog", "Passwort"))
        self.label_3.setText(_translate("dialog", "Username"))
        self.pushButton_3.setText(_translate("dialog", "Neuen User registrieren"))

        self.lineEdit.setPlaceholderText(_translate("Dialog", "Passwort"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Username"))

        self.pushButton.clicked.connect(self.login_button_click)
        self.pushButton_2.clicked.connect(gedrueckt)
        self.pushButton_3.clicked.connect(self.openWindow)


    def login_button_click(self):
        """Öffnet das Hauptfenster der Anwendung, wenn die Log-In Daten richtig sind, sonst wird die Funktion wrongUserNamePasswort ausgeführt

            Test:
                * überprüfung, was passiert, wenn kein Passwort oder Username eingegeben wird
                * Überprüfung was passiert, ob eine eine doppelte Anmeldung auf zwei parallel laufenden Instanzen der Anwendungen möglich ist
        """
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
    """Erzeugt ein Fehlerfenster, welches eine Fehlermedung ausgibt und dazu auffordert, die Daten erneut einzugeben

    Test:
        * keine sinnvollen Tests möglich
    """
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Falscher Username oder Passwort, bitte nochmal eingeben.")
    x = msg.exec_()
        

# Niki Dok
def gedrueckt():
    """beendet die Application

        Tests:
            * keine sinnvollen Tests möglich
    """
    QtCore.QCoreApplication.instance().quit()
        

######################################################################################################
### 2. Klasse SignUp

class SignUp(object):
    """ine Klasse in der sich User über ein GUI-Fenster neu registrieren können 

    Args:
        object (class): beinhaltet ein GUI-Fenster mit Buttons 

    Funktionen:
        * openAnmeldung()
        * setupUI()
        * retranslateUi()
    """


    def openAnmeldung(self):
        """Öffnet das Anmeldefenster, wenn bei der Registierung ein Passwort (pword) und Control-Passwort (cword) übereinstimmen, sonst wird die Funktion mmm ausgeführt

            Tests:
                * Überprüfen ob pword und cword = null sein dürfen
                * Überprüfen, ob Vergleich auch bei Zahlenketten (bspw. im Passwort) funktioniert
        """
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


    def setupUi(self, Dialog):
        """Setup und Initialisierung der verschiedenen GUI-Komponenten
        Args:
            Dialog (Any): GUI-Fenster erhält den Objectnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Komponenten in das Dialogfenster reinpassen
            * Überprüfung, ob Passwort nicht sichtbar und nicht kopierbar dargestellt wird
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


    def retranslateUi(self, Dialog):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten + schafft über Connections zu den Listener Funktionen

        Args:
            Dialog (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung, ob die durch die Listener erstellten Connections funktionieren.
        """
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
    """Erzeugt ein Fehlerfenster, welches eine Fehlermeldung ausgibt, dass die Passwörter nicht übereinstimmen

    Test:
        * keine sinnvollen Tests möglich
    """
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Passwort nicht identisch.")
    x = msg.exec_()
    

# Niki Dok
def closeapp():
    """beendet die Applikation

    Tests:
        * keine sinnvollen Tests möglich
    """
    QtCore.QCoreApplication.instance().quit()  #schliesst window, wenn "Cancel" gedrückt wird



if __name__ == "__main__":
    """main Funktion: Über diese Funktioniert wird das Programm gestartet und in einigen Fällen beendet
    
    Tests:
        * keine sinnvollen Tests möglich
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
