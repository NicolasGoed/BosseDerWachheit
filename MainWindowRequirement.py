"""MainWindowRequirement Modul
    * beinhaltet eine Klasse mit einem GUI-Fenster und Buttons
    * eine Liste mit existierenden Projekten ist enthalten
    * neue Projekte können hinzufügt werden
    * vorhandene Projekte können geöffnet werden
    * vorhandene Projekte können gelöscht werden

authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
license: Public Domain
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from Fenster2 import Anforderungsliste
from ProjectManagement import *
from PyQt5.QtWidgets import QMessageBox



class MainFunction(object):
    """Eine Klasse in der Projekte in einem GUI-Fenster hinzugefügt, gelöscht oder geöffnet werden können 

    Args:
        object (class): beinhaltet ein Fenster mit Buttons

    Funktionen:
        * __init__()
        * openLogin()
        * setupUi()
        * retranslateUi():
        * addProjectDef()
        * deleteProjectDef()
        * open_button_click_requirement
    """

    def __init__(self, currentuser):
        """Konstruktor welcher den Parameter currentuser als self.currentuser festlegt

        Args:
            currentuser (str): eingeloggter User

        Test: 
            * keine sinnvollen Tests möglich
        """
        self.currentuser = currentuser
               
        
    def setupUi(self, MainWindow):
        """Setup und Initialisierung der verschiedenen GUI-Komponenten

        Args:
            MainWindow (Any): GUI-Fenster erhält den Objektnamen und die Größe

        Test:
            * Überprüfung, ob alle GUI-Komponenten in das Dialogfenster reinpassen
            * Überprüfung, ob das Fenster in der Größe veränderbar ist
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 781, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.CreateRequirement = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CreateRequirement.setObjectName("Projekt öffnen")
        self.verticalLayout.addWidget(self.CreateRequirement)
        
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("Projektliste")
        self.verticalLayout.addWidget(self.label)
        
        self.RequirementList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.RequirementList.setObjectName("RequirementList")
        self.verticalLayout.addWidget(self.RequirementList)

        self.AddProjectEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.AddProjectEdit.setObjectName("Projekt hinzufügen")
        self.verticalLayout.addWidget(self.AddProjectEdit)

        self.AddProject = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AddProject.setObjectName("Projekt hinzufügen")
        self.verticalLayout.addWidget(self.AddProject)

        self.DeleteProject = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DeleteProject.setObjectName("Projekt Löschen")
        self.verticalLayout.addWidget(self.DeleteProject)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adding projects from Database to QListObjects
        for aTuple in showProjectsName():
            self.RequirementList.addItems(aTuple)


    def retranslateUi(self, MainWindow):
        """Konkretisiert die sichtbaren Inhalte der verschiedenen GUI-Komponenten + schafft über Connections zu den Listener Funktionen

        Args:
            MainWindow (Any): Titel des Fensters

        Test:
            * Sind die GUI-Komponenten gross genug, sodass der Text vollständig sichtbar ist
            * Überprüfung, ob die durch die Listener erstellten Connections funktionieren.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CreateRequirement.setText(_translate("MainWindow", "Projekt öffnen"))
        self.AddProjectEdit.setPlaceholderText(_translate("MainWindow", "Projekt hinzufügen"))
        self.AddProject.setText(_translate("MainWindow", "Projekt hinzufügen"))
        self.DeleteProject.setText(_translate("MainWindow", "Projekt löschen"))
        self.label.setText(_translate("MainWindow", "Projektliste"))
        MainWindow.setWindowTitle("Projekte")
        
        self.CreateRequirement.clicked.connect(self.open_button_click_requirement)
        self.AddProject.clicked.connect(self.addProjectDef)
        self.DeleteProject.clicked.connect(self.deleteProjectDef)


    def addProjectDef(self):
        """Ein neues Projekt kann hinzugefügt werden
            * aktive Fenster schließt sich
            * danach öffnet sich das Fenster neu 

        Test:
            * Überprüfen: können in zwei verschiedenen Fenstern gleichzeitig gleichnamige Projekte erstellt werden
            * Überprüfen, ob ein neues Projekt in die Liste der Projekte des MainWindows übernommen wird
        """
        projectname = self.AddProjectEdit.text()
        createProject(projectname)
        QtWidgets.QApplication.activeWindow().close()
        self.window = QtWidgets.QDialog()
        self.ui = MainFunction(self.currentuser)
        self.ui.setupUi(self.window)
        self.window.show()


    def deleteProjectDef(self):
        """Ein ausgewähltes Projekt kann gelöscht werden
            * aktive Fenster schließt sich
            * danach öffnet sich das Fenster neu 

        Test:
            * Überprüfung: Kann das Projekt gerade gelöscht werden, während es editiert wird
            * Wird die Löschung auch auf das MainWindow übertragen
            * Überprüfen, ob das gelöschte Projekt in der Liste der Projekte des MainWindows nicht mehr erscheint

        """
        try:
            selectedProject = self.RequirementList.currentItem().text()
            deleteProject(selectedProject)
            QtWidgets.QApplication.activeWindow().close()
            self.window = QtWidgets.QDialog()
            self.ui = MainFunction(self.currentuser)
            self.ui.setupUi(self.window)
            self.window.show()

        except:
            mmmDelete()
            

    def open_button_click_requirement(self):
        """Öffnet ein ausgewähltes Projekt in einem neuen Fenster. Gibt eine Fehlermeldung aus, wenn kein Projekt ausgewählt wurde.

        Test:
            Überprüfung: Hat man weiterhin Zugriff auf das noch geöffnete Fenster "Projekte", wenn das neue Fenster "Anforderungsliste" geöffnet wird
            Überprüfung: können mehrere Projekte geöffnet werden
        """
        try:
            selectedProject = self.RequirementList.currentItem().text()
            currentuser = self.currentuser
            self.window = QtWidgets.QDialog()
            self.ui = Anforderungsliste(selectedProject, currentuser)
            self.ui.setupUi(self.window)
            self.window.show()
        
        except:
            mmm()

      
def mmm():
    """Erzeugt ein Fehlerfenster, welches eine Fehlermeldung ausgibt, dass kein Projekt ausgewählt wurde oder ein neues Projekt erstellt werden soll

    Test:
        * keine sinnvollen Tests möglich
    """
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Bitte Projekt auswählen oder ein neues Projekt erstellen.")
    x = msg.exec_()


def mmmDelete():
    """Erzeugt ein Fehlerfenster, welches eine Fehlermeldung ausgibt, dass kein Projekt zum Löschen ausgewählt wurde

    Test:
        * keine sinnvollen Tests möglich
    """
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Bitte Projekt zum Löschen auswählen.")
    x = msg.exec_()


if __name__ == "__main__":
    """main Funktion: Über diese Funktioniert wird das Programm gestartet und in einigen Fällen beendet
    
    Tests:
        * keine sinnvollen Tests möglich
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = MainFunction()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
