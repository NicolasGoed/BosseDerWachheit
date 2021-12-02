"""Lastenheft Modul
    * GUI-Fenster mit allen Anforderungen eines Projekts


authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from RequirementManagement import *


class LastenheftFenster(object):
    """Eine Klasse in der Anforderungen des ausgewählten Projekt in einer QListWidget eines GUI-Fensters in Textform eingefügt werden.

    Args:
        object (class): beinhaltet ein Fenster mit Widgets

    Funktionen:
        * __init__()
        * setupUi()
        * retranslateUi():
    """
    

    def __init__(self, selectedProject):
        """Konstruktor, welche selectedProject als self.selectedProject festlegt


        Args:
            selectedProject (str): ausgewähltes Projekt wird für das Fenster übernommen

        Tests:
            Es sind keine sinnvollen Tests möglich
        """
        self.selectedProject = selectedProject
        

    def setupUi(self, Dialog):
        """Setup und Initialisierung der verschiedenen GUI-Komponenten
            * Ausgabe einer Liste der Anforderungen in Textform

        Args:
            Dialog (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Komponenten in das Dialogfenster reinpassen
            * Überprüfung, ob die zu hinzufügenden Anforderungen tatsächlich ins ListWidget übernommen werden
        """
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


    def retranslateUi(self, Dialog):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten

        Args:
            Dialog (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung was passiert, wenn man dem selectedProject ein Python Befehl als Name übergibt -> potentielle Sicherheitslücke
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lastenheft"))
        self.label_2.setText(_translate("Dialog", "Anforderungen "))
        self.label_3.setText(_translate("Dialog", "Projektname"))
        self.lineEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Projektname"))
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText(self.selectedProject)


if __name__ == "__main__":
        """main Funktion: Über diese wird das Programm gestartet und in einigen Fällen beendet

         Tests:
            keine sinnvollen Tests möglich
        """
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = LastenheftFenster()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
