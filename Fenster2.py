"""Fenster2 Modul
    * 1. Klasse: Anforderungsliste
        - beinhaltet mehrere Buttons mit der Anforderungen und Spezifikationen erstellt, bearbeitet und gelöscht werden können
        - Anzeige der aktuellen Anforderungsliste
        - Lastenheft-Button: öffnet ein Lastenheft in einem neuen Fenster
        - PFlichtenheft-Button: öffnet ein Pflichtenheft in einem neuen Fenster
    * 2. Klasse: Requirement erstellen
        - Neue Anforderungen und Spezifikationen können zu einem angezeigten Projekt erstellt werden
    * 3. Klasse: Requirement bearbeiten
        - Ausgewählte Anforderungen inkl. Spezifikation kann bearbeitet werden

authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
license: Public Domain
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from RequirementManagement import *
from Lastenheft import LastenheftFenster
from Pflichtenheft import PflichtenheftFenster
from PyQt5.QtWidgets import QMessageBox


############################################################################################################
### 1. Klasse - Fenster - Anforderungsliste

class Anforderungsliste(object):
    """Eine Klasse mit einem GUI-Fenster und mehreren Buttons
        * aktuelle Anforderungen werden in einer Anforderungsliste angezeigt
        * beinhaltet Buttons mit denen Anforderungen und Spezifikationen erstellt, bearbeitet und gelöscht werden können
        * beinhaltet Buttons zur Erstellung eines Lastenheftes oder Pflichtenheftes

    Args:
        object (class): beinhaltet ein Fenster mit einer Liste und verschiedenen Buttons

    Funktionen:
        * __init__()
        * openCreateRequirement()
        * openUpdateRequirement()
        * openLastenheft()
        * openPflichtenheft()
        * deleteAnforderung()
        * setupUi()
        * retranslateUi()

    Test:
        * Fenstergröße kann verstellt werden ohne dass die Buttons auf dem Screen "einfrieren"
        * Wenn mehr Anforderungen hinzugefügt wurden, als die tatsächliche Größe der Anforderungsliste,
          lässt sich die Anforderungsliste (QListWidget) scrollen

    """

    def __init__(self, selectedProject, currentuser):
        """Konstruktor, welche selectedProject und currentuser, als self.selectedProject und self.currentunser festlegt

        Args:
            selectedProject (str): ausgewähltes Projekt wird für das Fenster übernommen
            currentuser (str): eingeloggter User

        Tests:
            Es sind keine sinnvollen Tests möglich
        """
        self.selectedProject = selectedProject
        self.currentuser = currentuser


    def openCreateRequirement(self):
        """öffnet ein neues Fenster um ein neues Requirement zu erstellen

        Test:
            * Überprüfung, ob zwei gleichnamige Requirements erstellt werden können
            * überprüfung, ob im alten Fenster eingetragene Daten in das neue übernommen werden
        """
        QtWidgets.QApplication.activeWindow().close()
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AnforderungUndSpezifikation(self.selectedProject, self.currentuser)
        self.ui.setupUi(self.window)
        self.window.show()
    

    def openUpdateRequirement(self):
        """öffnet eine in der Anforderungsliste ausgewählte Anforderung inkl. Spezifikation zur Überarbeitung
            * Fehlermeldung wird ausgegeben, wenn keine Anforderung ausgewählt wurde
        
        Test:
            * Überprüfung, ob gleichzeitiges updaten in mehreren Fenstern funktioniert
            * Überprüfung, ob das Löschen des Requirements während der Editierung zu einem Fehler führt
        """
        try:
            selectedreq = self.LastenUndPflichtenheft.currentItem().text()
            QtWidgets.QApplication.activeWindow().close()
            self.window = QtWidgets.QDialog()
            self.ui = Ui_UpdateAnforderungUndSpezifikation(self.selectedProject, self.currentuser, selectedreq)
            self.ui.setupUi(self.window)
            self.window.show()   
        except:
            mmm1()

    def openLastenheft(self):
        """Öffnet ein neues Fenster, in welchem das Lastenheft zu sehen ist

        Test:
        keine sinnvollen Tests möglich
        """
        self.window = QtWidgets.QDialog()
        self.ui = LastenheftFenster(self.selectedProject)
        self.ui.setupUi(self.window)
        self.window.show()

       
    def openPflichtenheft(self):
        """Öffnet ein neues Fenster, in welchem das Pflichtenheft zu sehen ist

        Test:
        keine sinnvollen Tests möglich
        """
        self.window = QtWidgets.QDialog()
        self.ui = PflichtenheftFenster(self.selectedProject)
        self.ui.setupUi(self.window)
        self.window.show()


    def deleteAnforderung(self):
        """Diese Funktion erlaubt es, eine ausgewählte Anforderung inkl. Spezifikation zu löschen.
            * Fehlermeldung wird ausgegeben, wenn keine Anforderung ausgewählt wurde

        Test:
            * Überprüfung: Kann ein Requirement gelöscht werden, wenn es gerade editiert wird
            * Überprüfung: Können mehrere Requirements zum Löschen ausgewählt werden und gleichzeitig gelöscht werden
        """
        try:
            selectedRequirement = self.LastenUndPflichtenheft.currentItem().text()
            deleteRequirement(selectedRequirement)

            self.window = QtWidgets.QDialog()
            self.ui = Anforderungsliste(self.selectedProject, self.currentuser )
            self.ui.setupUi(self.window)
            QtWidgets.QApplication.activeWindow().close()
            self.window.show()

        except:
            mmm()
        

    def setupUi(self, Fenster2):
        """Initialisiert und verändert die verschiedenen GUI-Komponenten 
            * alle vorhandenen Anforderungen (Requirements) werden in einer Anforderungsliste (QWidgetList) aufgelistet

        Args:
            Fenster2 (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Elemente im Fenster sind, wenn das Fenster in der Größe verändert wird
            * Überprüfung, ob die Anforderungsliste (QWidgetList) scrollbar ist, wenn mehr Anforderungen in der Liste sind, als die tatsächliche Fenstergröße
        """
        Fenster2.setObjectName("Lasten und Pflichten")
        Fenster2.resize(500, 600)

        self.label_7 = QtWidgets.QLabel(Fenster2)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 101, 31))
        self.label_7.setObjectName("Projektname")
        self.lineEdit_7 = QtWidgets.QLineEdit(Fenster2)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 50, 418, 22))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit Projektname")

        self.label_4 = QtWidgets.QLabel(Fenster2)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 400, 16))
        self.label_4.setObjectName("label Anforderung und Spezifikation")

        self.pushButton_3 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 120, 93, 28))
        self.pushButton_3.setObjectName("pushButton Erstellen")

        self.pushButton_4 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_4.setGeometry(QtCore.QRect(202, 120, 93, 28))
        self.pushButton_4.setObjectName("pushButton Bearbeiten")

        self.pushButton_5 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_5.setGeometry(QtCore.QRect(365, 120, 93, 28))
        self.pushButton_5.setObjectName("pushButton Löschen")

        self.label = QtWidgets.QLabel(Fenster2)
        self.label.setGeometry(QtCore.QRect(40, 180, 251, 16))
        self.label.setObjectName("label Anforderungsliste")

        self.LastenUndPflichtenheft = QtWidgets.QListWidget(Fenster2)
        self.LastenUndPflichtenheft.setWordWrap(True)
        # Adding requirements to QListWidget with ProjectName = SelectedProject 
        # Adding projects from Database to QListObjects
        for aTuple in getAllRequirements(self.selectedProject):
            self.LastenUndPflichtenheft.addItems(aTuple)
        self.LastenUndPflichtenheft.setGeometry(QtCore.QRect(40, 200, 418, 280))
        self.LastenUndPflichtenheft.setObjectName("LastenUndPflichtenheft")

        self.pushButton = QtWidgets.QPushButton(Fenster2)
        self.pushButton.setGeometry(QtCore.QRect(40, 530, 101, 28))
        self.pushButton.setObjectName("pushButton Lastenheft")

        self.pushButton_2 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_2.setGeometry(QtCore.QRect(365, 530, 93, 28))
        self.pushButton_2.setObjectName("pushButton Pflichtenheft")

        self.retranslateUi(Fenster2)
        QtCore.QMetaObject.connectSlotsByName(Fenster2)


    def retranslateUi(self, Fenster2):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten + schafft über Connections zu den Listener Funktionen

        Args:
            Fenster2 (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung, ob die durch die Listener erstellten Connections funktionieren.
        """
        _translate = QtCore.QCoreApplication.translate

        self.label_7.setText(_translate("Fenster2", "Projektname"))
        self.lineEdit_7.setPlaceholderText(_translate("Fenster2", "Projektname"))
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setText(self.selectedProject)

        self.pushButton.setText(_translate("Fenster2", "Lastenheft"))
        self.pushButton_2.setText(_translate("Fenster2", "Pflichtenheft"))
        self.pushButton_3.setText(_translate("Fenster2", "Erstellen"))
        self.pushButton_4.setText(_translate("Fenster2", "Bearbeiten"))
        self.pushButton_5.setText(_translate("Fenster2", "Löschen"))
        self.label.setText(_translate("Fenster2", "Anforderungsliste"))
        self.label_4.setText(_translate("Fenster2", "Anforderung und Spezifikation"))
        Fenster2.setWindowTitle("Lasten und Pflichten")

        self.pushButton_3.clicked.connect(self.openCreateRequirement)
        self.pushButton_4.clicked.connect(self.openUpdateRequirement)
        
        self.pushButton.clicked.connect(self.openLastenheft)
        self.pushButton_2.clicked.connect(self.openPflichtenheft)
        self.pushButton_5.clicked.connect(self.deleteAnforderung)

       
        
############################################################################################################
### 2. Klasse - Fenster - Anforderung erstellen

class Ui_AnforderungUndSpezifikation(object):
    """Eine Klasse mit einem GUI-Fenster und mehreren Buttons
        * Anforderungen können in das Feld "Anforderungen" (QTextEdit) geschrieben werden
        * Spezifikationen können in das Feld "Spezifikationen" (QTextEdit) geschrieben werden
        * Angaben können über den Button "Speichern" gespeichert werden und in die Anforderungsliste der Klasse "Anforderungsliste" übernommen werden

    Args:
        object (class): beinhaltet ein Fenster mit verschiedenen GUI-Komponenten wie Projektname, User, Anforderung und Spezifikation

    Funktionen:
        * __init__()
        * setupUi()
        * retranslateUi()
        * openFensterAfterSaving()

    Tests:
        * Fenstergröße kann verstellt werden ohne dass die GUI-Elemente auf dem Screen "einfrieren"
        * Wenn mehr Anforderungen bzw. Spezifikationen hinzugefügt wurden, als die tatsächliche Größe der QTextEdits,
          lassen sich die QTextEdits scrollen
    """


    def __init__(self, selectedProject, currentuser):
        """Konstruktor, welche selectedProject und currentuser, als self.selectedProject und self.currentunser festlegt

        Args:
            selectedProject (str): ausgewähltes Projekt, dem eine Anforderung hinzugefügt werden soll
            currentuser (str): eingeloggter User

        Tests:
            Es sind keine sinnvollen Tests möglich
        """
        self.selectedProject = selectedProject
        self.currentuser = currentuser


    def setupUi(self, AnforderungUndSpezifikation):
        """Initialisiert die verschiedenen GUI-Komponenten bzgl:
            * Projectname
            * User
            * Anforderung
            * Spezifikation
            * Speichern

        Args:
            AnforderungUndSpezifikation (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Elemente im Fenster sind, wenn das Fenster in der Größe verändert wird
            * Überprüfung, ob die Widgets "Anforderung" und "Spezifikation" (QTextEdit) scrollbar sind, wenn mehr Text in den Listen steht, als die tatsächliche QTextEdit-Größe
        """
        AnforderungUndSpezifikation.setObjectName("AnforderungUndSpezifikation")
        AnforderungUndSpezifikation.resize(450, 700)

        self.label_2 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_2.setGeometry(QtCore.QRect(10, 525, 411, 41))
        self.label_2.setObjectName("label_2")

        self.label_6 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 100, 20))
        self.label_6.setObjectName("Überschrift User")
        self.lineEdit_4 = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 60, 361, 22))
        self.lineEdit_4.setObjectName("lineEdit User")

        self.label = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label.setGeometry(QtCore.QRect(40, 120, 500, 16))
        self.label.setObjectName("Überschrift Projektname")
        self.lineEdit = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit.setGeometry(QtCore.QRect(40, 140, 361, 22))
        self.lineEdit.setObjectName("lineEdit Projektname")

        self.label_4 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 100, 20))
        self.label_4.setObjectName("Überschrift Anforderung")
        self.textEdit_1 = QtWidgets.QTextEdit(AnforderungUndSpezifikation)
        self.textEdit_1.setGeometry(QtCore.QRect(40, 220, 361, 131))
        self.textEdit_1.setText("")
        self.textEdit_1.setObjectName("lineEdit Anforderung")

        self.label_5 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_5.setGeometry(QtCore.QRect(40, 410, 100, 20))
        self.label_5.setObjectName("Überschrift Spezifikation/en")
        self.textEdit = QtWidgets.QTextEdit(AnforderungUndSpezifikation)
        self.textEdit.setGeometry(QtCore.QRect(40, 430, 361, 131))
        self.textEdit.setObjectName("textEdit Spezifikation")
        
        self.pushButton = QtWidgets.QPushButton(AnforderungUndSpezifikation)
        self.pushButton.setGeometry(QtCore.QRect(180, 590, 93, 28))
        self.pushButton.setObjectName("pushButton Speichern")

        self.retranslateUi(AnforderungUndSpezifikation)
        QtCore.QMetaObject.connectSlotsByName(AnforderungUndSpezifikation)


    def retranslateUi(self, AnforderungUndSpezifikation):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten + schafft über Connections zu den Listener Funktionen

        Args:
            AnforderungUndSpezifikation (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung, ob die durch die Listener erstellten Connections funktionieren.
        """
        _translate = QtCore.QCoreApplication.translate
        AnforderungUndSpezifikation.setWindowTitle(_translate("AnforderungUndSpezifikation", "Anforderung und Spezifikation"))
        self.pushButton.setText(_translate("AnforderungUndSpezifikation", "Speichern"))
        self.textEdit_1.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.lineEdit_4.setPlaceholderText(_translate("AnforderungUndSpezifikation", "User"))
        
        # User ist nicht änderbar! // Thi
        self.lineEdit_4.setEnabled(False)
              
        self.textEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Spezifikation"))
        self.lineEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Projektname"))

        # Projektname ist nicht änderbar!
        self.lineEdit.setEnabled(False)

        self.label_6.setText(_translate("AnforderungUndSpezifikation", "User"))
        self.label.setText(_translate("AnforderungUndSpezifikation", "Projektname"))
        self.label_4.setText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.label_5.setText(_translate("AnforderungUndSpezifikation", "Spezifikation/en"))

        AnforderungUndSpezifikation.setWindowTitle("Requirement erstellen")

        self.lineEdit.setText(self.selectedProject)
        self.lineEdit_4.setText(self.currentuser)

        #Speichern --> Speichert alle Werte des Fensters + Schließt das Fenster + Kehrt zum Fenster2 zurück + Updated die Liste der Anforderungen
        self.pushButton.clicked.connect(self.openFensterAfterSaving)
    

    def openFensterAfterSaving(self):
        """Aufruf des Fensters der Klasse "Anforderungsliste"
            * Übergabe von Werten und Aufruf der Funktion createRequirement

            Tests:
            * Leerzeichen oder leere Absätze werden nicht als Anforderung in die Liste übernommen
            * im neuen Fenster sind alle übernommenen Anforderungen sichtbar
        """
        self.projectname = self.selectedProject
        self.reqname = self.textEdit_1.toPlainText()
        specText = self.textEdit.toPlainText()
        lines = specText.split("\n")


        #createRequirement(projectname,reqname, sepcText)
        #createRequirement(self.projectname, self.reqname)
        for eachSpec in lines:
            createRequirement(self.projectname, self.reqname, eachSpec)
      
        QtWidgets.QApplication.activeWindow().close()
        self.window = QtWidgets.QDialog()
        self.ui = Anforderungsliste(self.selectedProject, self.currentuser )
        self.ui.setupUi(self.window)
        self.window.hide()
        self.window.show()
    

############################################################################################################
### 3. Klasse - Fenster - Anforderung bearbeiten

class Ui_UpdateAnforderungUndSpezifikation(object):
    """Eine Klasse mit einem GUI-Fenster und mehreren Buttons
        * ausgewählte Anforderungen können im Feld "Anforderungen" (QTextEdit) überarbeitet werden
        * ausgewählte Spezifikationen können im Feld "Spezifikationen" (QTextEdit) überarbeitet werden
        * Angaben können über den Button "Speichern" gespeichert werden und in die Anforderungsliste der Klasse "Anforderungsliste" übernommen werden

    Args:
        object (class): beinhaltet ein Fenster mit verschiedenen GUI-Komponenten wie Projektname, User, Anforderung und Spezifikation

    Funktionen:
        Funktionen:
        * __init__()
        * setupUi()
        * retranslateUi()
        * UpdateProject()

    Tests:
        * Fenstergröße kann verstellt werden ohne dass die GUI-Elemente auf dem Screen "einfrieren"
        * Wenn mehr Anforderungen bzw. Spezifikationen hinzugefügt wurden, als die tatsächliche Größe der QTextEdits,
          lassen sich die QTextEdits scrollen
    """

    
    def __init__(self, selectedProject, currentuser, selectedreq):
        """Konstruktor, welche selectedProject, currentuserund selectedreq, als self.selectedProject, self.currentunser und self.selectedreq festlegt

        Args:
            selectedProject (str): ausgewählte Projekt, das geändert werden soll
            currentuser (str): eingeloggter User
            selectedreq (str): Ausgewählte Anforderung, die geändert werden soll

        Tests:
            Es sind keine sinnvollen Tests möglich
        """
        self.selectedProject = selectedProject
        self.currentuser = currentuser
        self.selectedreq = selectedreq


    def setupUi(self, AnforderungUndSpezifikation):
        """Initialisiert die verschiedenen GUI-Komponenten bzgl:
            * Projectname
            * User
            * Anforderung
            * Spezifikation
            * Speichern

        Args:
            AnforderungUndSpezifikation (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Elemente im Fenster sind, wenn das Fenster in der Größe verändert wird
            * Überprüfung, ob die Widgets "Anforderung" und "Spezifikation" (QTextEdit) scrollbar sind, wenn mehr Text in den Listen steht, als die tatsächliche QTextEdit-Größe
        """
        AnforderungUndSpezifikation.setObjectName("AnforderungUndSpezifikation")
        AnforderungUndSpezifikation.resize(450, 700)

        self.label_2 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_2.setGeometry(QtCore.QRect(10, 525, 411, 41))
        self.label_2.setObjectName("label_2")

        self.label_6 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 100, 20))
        self.label_6.setObjectName("Überschrift User")
        self.lineEdit_4 = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 60, 361, 22))
        self.lineEdit_4.setObjectName("lineEdit User")

        self.label = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label.setGeometry(QtCore.QRect(40, 120, 500, 16))
        self.label.setObjectName("Überschrift Projektname")
        self.lineEdit = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit.setGeometry(QtCore.QRect(40, 140, 361, 22))
        self.lineEdit.setObjectName("lineEdit Projektname")

        self.label_4 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 100, 20))
        self.label_4.setObjectName("Überschrift Anforderung")
        self.textEdit_2 = QtWidgets.QTextEdit(AnforderungUndSpezifikation)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 220, 361, 131))
        self.textEdit_2.setText("")
        self.textEdit_2.setObjectName("lineEdit Anforderung")

        self.label_5 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_5.setGeometry(QtCore.QRect(40, 410, 100, 20))
        self.label_5.setObjectName("Überschrift Spezifikation/en")
        self.textEdit = QtWidgets.QTextEdit(AnforderungUndSpezifikation)
        self.textEdit.setGeometry(QtCore.QRect(40, 430, 361, 131))
        self.textEdit.setObjectName("textEdit Spezifikation")

        self.pushButton = QtWidgets.QPushButton(AnforderungUndSpezifikation)
        self.pushButton.setGeometry(QtCore.QRect(180, 590, 93, 28))
        self.pushButton.setObjectName("pushButton Speichern")

        self.retranslateUi(AnforderungUndSpezifikation)
        QtCore.QMetaObject.connectSlotsByName(AnforderungUndSpezifikation)


    def retranslateUi(self, AnforderungUndSpezifikation):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten + schafft über Connections zu den Listener Funktionen
            * Funktion ruft beim Speichern die Funktion UpdateProject auf, dass die ausgewählte Anforderung erst löscht und die überarbeiteten Änderungen als neue Anforderung übernimmt

        Args:
            AnforderungUndSpezifikation (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung, ob die durch die Listener erstellten Connections funktionieren.
        """
        _translate = QtCore.QCoreApplication.translate
        AnforderungUndSpezifikation.setWindowTitle(_translate("AnforderungUndSpezifikation", "Anforderung und Spezifikation"))
        self.pushButton.setText(_translate("AnforderungUndSpezifikation", "Speichern"))
        self.textEdit_2.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.lineEdit_4.setPlaceholderText(_translate("AnforderungUndSpezifikation", "User"))
        
        # User ist nicht änderbar!
        self.lineEdit_4.setEnabled(False)

        self.textEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Spezifikation"))
        self.lineEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Projektname"))
        
        # Projektname ist nicht änderbar!
        self.lineEdit.setEnabled(False)
        
        self.label.setText(_translate("AnforderungUndSpezifikation", "Projektname"))
        self.label_4.setText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.label_5.setText(_translate("AnforderungUndSpezifikation", "Spezifikation/en"))
        self.label_6.setText(_translate("AnforderungUndSpezifikation", "User"))

        AnforderungUndSpezifikation.setWindowTitle("Requirement bearbeiten")

        
        self.lineEdit.setText(self.selectedProject)
        self.lineEdit_4.setText(self.currentuser)
        self.textEdit_2.setText(self.selectedreq)

        #Speichern --> Speichert alle Werte des Fensters + Schließt das Fenster + öffnet das Fenster2 neu mit der geupdateten Liste der Anforderungen
        self.pushButton.clicked.connect(self.UpdateProject)
        for aTuple in list(getSpecificationText(self.selectedreq)):     
            a = "".join(aTuple)
            self.textEdit.append(str(a))
        
        self.aaa = self.textEdit_2.toPlainText()


    # Thi 
    def UpdateProject(self):
        """Updated das Fenster "Anforderungliste"
            * löscht zunächste die ausgewählte Anforderung inkl. Spezifikation
            * übergibt die abgespeicherten Werte als "überarbeitete" Anforderung inkl. Spezifikation
            * Öffnet das Fenster der Klasse "Anforderungsliste" mit der aktuellen Anfoderungsliste

        Tests:
            * Überprüfung, ob während dem Prozess der Editierung eine gleichnamige Anforderung neu erstellt werden kann
            * Überprüfung, ob über den "Löschen"-Button die geöffnete zu bearbeitende Anforderung gelöscht werden kann
        """

        deleteRequirement(self.aaa)

        self.projectname = self.selectedProject
        self.reqname = self.textEdit_2.toPlainText()
        specText = self.textEdit.toPlainText()
        lines = specText.split("\n")

        #createRequirement(projectname,reqname, sepcText)
        #createRequirement(self.projectname, self.reqname)
        for eachSpec in lines:
            createRequirement(self.projectname, self.reqname, eachSpec)
        
        QtWidgets.QApplication.activeWindow().close()
        self.window = QtWidgets.QDialog()
        self.ui = Anforderungsliste(self.selectedProject, self.currentuser )
        self.ui.setupUi(self.window)
        self.window.hide()
        self.window.show()

##########################################################


def mmm():
    """Erzeugt ein Fehlerfenster, welches eine Fehlermeldung ausgibt, dass keine Anforderung zum Löschen ausgewählt wurde

        Test:
            * keine sinnvollen Tests möglich
    """
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Bitte wählen Sie eine Anforderung zum Löschen aus.")
    x = msg.exec_()


def mmm1():
    """Erzeugt ein Fehlerfenster, welches eine Fehlermeldung ausgibt, dass keine Anforderung zum Ändern ausgewählt wurde

        Test:
            * keine sinnvollen Tests möglich
    """
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Bitte wählen Sie eine Anforderung zum Ändern aus.")
    x = msg.exec_()

##########################################################

if __name__ == "__main__":
    """main Funktion: Über diese Funktioniert wird das Programm gestartet und in einigen Fällen beendet
    
        Tests:
            * keine sinnvollen Tests möglich    
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fenster2 = QtWidgets.QDialog()
    ui = Anforderungsliste()
    ui.setupUi(Fenster2)
    Fenster2.show()
    sys.exit(app.exec_())
