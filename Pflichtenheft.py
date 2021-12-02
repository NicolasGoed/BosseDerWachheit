"""Pflichtenheft Modul
    * GUI-Fenster mit allen Anforderungen und Spezifikationen eines Projekts


authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from RequirementManagement import *

   
class PflichtenheftFenster(object):
    """[summary]

    Args:
        object (class): beinhaltet ein Fenster mit Widgets

    Funktionen:
        * __init__()
        * setupUi()
        * retranslateUi():
    """
    selectedProject = "a"


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
            * Ausgabe einer Liste der Anforderungen inkl. der zugehörigen Spezifikation in Textform

        Args:
            Dialog (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Komponenten in das Dialogfenster reinpassen
            * Überprüfung, ob die zu hinzufügenden Anforderungen inkl. deren Spezifikationen tatsächlich ins ListWidget übernommen werden
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,900)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 91, 16))
        self.label_2.setObjectName("Pflichtenheft")
    
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setGeometry(QtCore.QRect(50, 120, 700, 730))
        self.listWidget_2.setObjectName("Pflichtenheft")


        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 101, 31))
        self.label_3.setObjectName("Projektname")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)    
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 400, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit Projektname")

        reqcount = int(1)
        for aTuple in getAllRequirements(self.selectedProject):
           tup1 = ''.join(aTuple)
           self.listWidget_2.addItem(str(reqcount) + ". Anforderung: ")
           self.listWidget_2.addItem(tup1)
           reqcount = int(reqcount) + int(1) 
           self.listWidget_2.addItem("")
           specIndex = 1
           for bTuple in getSpecificationText(tup1):     
              tup2 = "".join(bTuple) 
              self.listWidget_2.addItem(str(specIndex) + ". Spezifikation: ")
              self.listWidget_2.addItem(tup2)
              specIndex = int(specIndex) + 1
           self.listWidget_2.addItem("")
           self.listWidget_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten

        Args:
            Dialog (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung ob die ListWidget-Elemente scrollbar ist, wenn mehr Text enthalten ist als die tatsächliche Größe des QListWidget-Elements
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pflichtenheft"))
        self.label_2.setText(_translate("Dialog", "Pflichtenheft"))
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
        ui = PflichtenheftFenster()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
