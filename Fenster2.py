# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fenster22.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from RequirementManagement import *
from Lastenheft import LastenheftFenster
from Pflichtenheft import PflichtenheftFenster
from PyQt5.QtWidgets import QMessageBox

#https://stackoverflow.com/questions/37837682/python-class-input-argument
#passing variable to different script
#if running this function on its own there is no selected Project passed in. so it won't run
#


############################################################################################################
### 1. Klasse - Fenster - Anfoderungsliste

class Anforderungsliste(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    # Thi Dok
    def __init__(self, selectedProject, currentuser):
        self.selectedProject = selectedProject
        self.currentuser = currentuser

    # Thi dok
    def openCreateRequirement(self):
       QtWidgets.QApplication.activeWindow().close()
       self.window = QtWidgets.QDialog()
       self.ui = Ui_AnforderungUndSpezifikation(self.selectedProject, self.currentuser)
       self.ui.setupUi(self.window)
       #Fenster2.hide()
       self.window.show()
    
       # Thi dok
    def openUpdateRequirement(self):
        try:
            selectedreq = self.LastenUndPflichtenheft.currentItem().text()
            QtWidgets.QApplication.activeWindow().close()
            self.window = QtWidgets.QDialog()
            self.ui = Ui_UpdateAnforderungUndSpezifikation(self.selectedProject, self.currentuser, selectedreq)
            self.ui.setupUi(self.window)
            self.window.show()   
        except:
            mmm1()

   # Thi dok
    def openLastenheft(self):
       self.window = QtWidgets.QDialog()
       self.ui = LastenheftFenster(self.selectedProject)
       self.ui.setupUi(self.window)
       self.window.show()

       # Thi dok
    def openPflichtenheft(self):
       self.window = QtWidgets.QDialog()
       self.ui = PflichtenheftFenster(self.selectedProject)
       self.ui.setupUi(self.window)
       self.window.show()

   # Thi dok
    def deleteAnforderung(self):
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
        
   # Niki dok
    def setupUi(self, Fenster2):
        Fenster2.setObjectName("Übersicht Lasten und Pflichten")
        Fenster2.resize(420, 400)
        self.pushButton = QtWidgets.QPushButton(Fenster2)
        self.pushButton.setGeometry(QtCore.QRect(40, 320, 101, 28))
        self.pushButton.setObjectName("pushButton Lastenheft")
        self.pushButton_2 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton Pflichtenheft")
        self.pushButton_3 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 40, 93, 28))
        self.pushButton_3.setObjectName("pushButton Erstellen")
        self.pushButton_4 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 40, 93, 28))
        self.pushButton_4.setObjectName("pushButton Bearbeiten")
        self.pushButton_5 = QtWidgets.QPushButton(Fenster2)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 40, 93, 28))
        self.pushButton_5.setObjectName("pushButton Löschen")
        self.label = QtWidgets.QLabel(Fenster2)
        self.label.setGeometry(QtCore.QRect(40, 100, 251, 16))
        self.label.setObjectName("label Anforderungsliste")
        self.LastenUndPflichtenheft = QtWidgets.QListWidget(Fenster2)

        # Adding requirements to QListWidget with ProjectName = SelectedProject 
        # (ProjectId zu kompliziert, da ich bis jetzt nur das mit dem ProjectName habe // Thi )
        # Adding projects from Database to QListObjects
        #for aTuple in getAllRequirements(self.selectedProject):
        for aTuple in getAllRequirements(self.selectedProject):
            self.LastenUndPflichtenheft.addItems(aTuple)

        

        self.LastenUndPflichtenheft.setGeometry(QtCore.QRect(40, 120, 331, 141))
        self.LastenUndPflichtenheft.setObjectName("LastenUndPflichtenheft")
        self.label_2 = QtWidgets.QLabel(Fenster2)
        self.label_2.setGeometry(QtCore.QRect(40, 300, 141, 16))
        self.label_2.setObjectName("label Lastenheft erstellen:")
        self.label_3 = QtWidgets.QLabel(Fenster2)
        self.label_3.setGeometry(QtCore.QRect(270, 300, 141, 16))
        self.label_3.setObjectName("label Pflichtenheft erstellen:")
        self.label_4 = QtWidgets.QLabel(Fenster2)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 400, 16))
        self.label_4.setObjectName("label Anforderung und Spezifikation erstellen")

        self.retranslateUi(Fenster2)
        QtCore.QMetaObject.connectSlotsByName(Fenster2)

    # Niki Dok
    def retranslateUi(self, Fenster2):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Fenster2", "Lastenheft"))
        self.pushButton_2.setText(_translate("Fenster2", "Pflichtenheft"))
        self.pushButton_3.setText(_translate("Fenster2", "Erstellen"))
        self.pushButton_4.setText(_translate("Fenster2", "Bearbeiten"))
        self.pushButton_5.setText(_translate("Fenster2", "Löschen"))
        self.label.setText(_translate("Fenster2", "Anforderungsliste"))
        self.label_2.setText(_translate("Fenster2", "Lastenheft erstellen"))
        self.label_3.setText(_translate("Fenster2", "Pflichtenheft erstellen"))
        self.label_4.setText(_translate("Fenster2", "Anforderung und Spezifikation erstellen"))
        Fenster2.setWindowTitle("Übersicht Lasten und Pflichten")

        self.pushButton_3.clicked.connect(self.openCreateRequirement)
        self.pushButton_4.clicked.connect(self.openUpdateRequirement)
        
        self.pushButton.clicked.connect(self.openLastenheft)
        self.pushButton_2.clicked.connect(self.openPflichtenheft)
        self.pushButton_5.clicked.connect(self.deleteAnforderung)
        
        
############################################################################################################
### 2. Klasse - Fenster - Anforderung erstellen

class Ui_AnforderungUndSpezifikation(object):

    # Thi
    def __init__(self, selectedProject, currentuser):
        self.selectedProject = selectedProject
        self.currentuser = currentuser

    # Niki Dok
    def setupUi(self, AnforderungUndSpezifikation):
        AnforderungUndSpezifikation.setObjectName("AnforderungUndSpezifikation")
        AnforderungUndSpezifikation.resize(450, 567)
        self.pushButton = QtWidgets.QPushButton(AnforderungUndSpezifikation)
        self.pushButton.setGeometry(QtCore.QRect(180, 490, 93, 28))
        self.pushButton.setObjectName("pushButton Speichern")
        self.label_2 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_2.setGeometry(QtCore.QRect(10, 525, 411, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 220, 361, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit Anforderung")
        self.lineEdit_4 = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 60, 361, 22))
        self.lineEdit_4.setObjectName("lineEdit User")
        self.textEdit = QtWidgets.QTextEdit(AnforderungUndSpezifikation)
        self.textEdit.setGeometry(QtCore.QRect(40, 310, 361, 131))
        self.textEdit.setObjectName("textEdit Spezifikation")
        self.lineEdit = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit.setGeometry(QtCore.QRect(40, 140, 361, 22))
        self.lineEdit.setObjectName("lineEdit Projektname")
        self.label = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label.setGeometry(QtCore.QRect(40, 120, 500, 16))
        self.label.setObjectName("Überschrift Projektname")
        self.label_4 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 100, 20))
        self.label_4.setObjectName("Überschrift Anforderung")
        self.label_5 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_5.setGeometry(QtCore.QRect(40, 290, 100, 20))
        self.label_5.setObjectName("Überschrift Spezifikation/en")
        self.label_6 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 100, 20))
        self.label_6.setObjectName("Überschrift User")



        self.retranslateUi(AnforderungUndSpezifikation)
        QtCore.QMetaObject.connectSlotsByName(AnforderungUndSpezifikation)

    # Niki Dok
    def retranslateUi(self, AnforderungUndSpezifikation):
        _translate = QtCore.QCoreApplication.translate
        AnforderungUndSpezifikation.setWindowTitle(_translate("AnforderungUndSpezifikation", "Anforderung und Spezifikation"))
        self.pushButton.setText(_translate("AnforderungUndSpezifikation", "Speichern"))
        self.lineEdit_2.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.lineEdit_4.setPlaceholderText(_translate("AnforderungUndSpezifikation", "User"))
        
        # User ist nicht änderbar! // Thi
        self.lineEdit_4.setEnabled(False)

        self.textEdit.setHtml(_translate("AnforderungUndSpezifikation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        
        self.textEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Spezifikation"))
        self.lineEdit.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Projektname"))

        # Projektname ist nicht änderbar!
        self.lineEdit.setEnabled(False)

        self.label.setText(_translate("AnforderungUndSpezifikation", "Projektname"))
        self.label_4.setText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.label_5.setText(_translate("AnforderungUndSpezifikation", "Spezifikation/en"))
        self.label_6.setText(_translate("AnforderungUndSpezifikation", "User"))

        AnforderungUndSpezifikation.setWindowTitle("Requirement erstellen")

        
        self.lineEdit.setText(self.selectedProject)
        self.lineEdit_4.setText(self.currentuser)

        #Speichern --> Speichert alle Werte des Fensters + Schließt das Fenster + Kehrt zum Fenster2 zurück + Updated die Liste der Anforderungen
        self.pushButton.clicked.connect(self.openFensterAfterSaving)
    
    # Thi Dok
    def openFensterAfterSaving(self):

       self.projectname = self.selectedProject
       self.reqname = self.lineEdit_2.text()
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
### 2. Klasse - Fenster - Anforderung bearbeiten

class Ui_UpdateAnforderungUndSpezifikation(object):

    # Thi Dok
    def __init__(self, selectedProject, currentuser, selectedreq):
        """[summary]

        Args:
            selectedProject ([type]): [description]
            currentuser ([type]): [description]
            selectedreq ([type]): [description]
        """
        self.selectedProject = selectedProject
        self.currentuser = currentuser
        self.selectedreq = selectedreq




    # Niki
    def setupUi(self, AnforderungUndSpezifikation):
        AnforderungUndSpezifikation.setObjectName("AnforderungUndSpezifikation")
        AnforderungUndSpezifikation.resize(450, 567)
        self.pushButton = QtWidgets.QPushButton(AnforderungUndSpezifikation)
        self.pushButton.setGeometry(QtCore.QRect(180, 490, 93, 28))
        self.pushButton.setObjectName("pushButton Speichern")
        self.label_2 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_2.setGeometry(QtCore.QRect(10, 525, 411, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 220, 361, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit Anforderung")
        self.lineEdit_4 = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 60, 361, 22))
        self.lineEdit_4.setObjectName("lineEdit User")
        self.textEdit = QtWidgets.QTextEdit(AnforderungUndSpezifikation)
        self.textEdit.setGeometry(QtCore.QRect(40, 310, 361, 131))
        self.textEdit.setObjectName("textEdit Spezifikation")
        self.lineEdit = QtWidgets.QLineEdit(AnforderungUndSpezifikation)
        self.lineEdit.setGeometry(QtCore.QRect(40, 140, 361, 22))
        self.lineEdit.setObjectName("lineEdit Projektname")
        self.label = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label.setGeometry(QtCore.QRect(40, 120, 500, 16))
        self.label.setObjectName("Überschrift Projektname")
        self.label_4 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 100, 20))
        self.label_4.setObjectName("Überschrift Anforderung")
        self.label_5 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_5.setGeometry(QtCore.QRect(40, 290, 100, 20))
        self.label_5.setObjectName("Überschrift Spezifikation/en")
        self.label_6 = QtWidgets.QLabel(AnforderungUndSpezifikation)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 100, 20))
        self.label_6.setObjectName("Überschrift User")



        self.retranslateUi(AnforderungUndSpezifikation)
        QtCore.QMetaObject.connectSlotsByName(AnforderungUndSpezifikation)

    # Niki Dok
    def retranslateUi(self, AnforderungUndSpezifikation):
        _translate = QtCore.QCoreApplication.translate
        AnforderungUndSpezifikation.setWindowTitle(_translate("AnforderungUndSpezifikation", "Anforderung und Spezifikation"))
        self.pushButton.setText(_translate("AnforderungUndSpezifikation", "Speichern"))
        self.lineEdit_2.setPlaceholderText(_translate("AnforderungUndSpezifikation", "Anforderung"))
        self.lineEdit_4.setPlaceholderText(_translate("AnforderungUndSpezifikation", "User"))
        
        # User ist nicht änderbar!
        self.lineEdit_4.setEnabled(False)

        self.textEdit.setHtml(_translate("AnforderungUndSpezifikation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        
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
        self.lineEdit_2.setText(self.selectedreq)

        #Speichern --> Speichert alle Werte des Fensters + Schließt das Fenster + öffnet das Fenster2 neu mit der geupdateten Liste der Anforderungen
        self.pushButton.clicked.connect(self.UpdateProject)
        for aTuple in list(getSpecificationText(self.selectedreq)):     
            a = "".join(aTuple)
            self.textEdit.append(str(a))
        
        self.aaa = self.lineEdit_2.text()


    # Thi 
    def UpdateProject(self):
        

       deleteRequirement(self.aaa)
       self.projectname = self.selectedProject
       self.reqname = self.lineEdit_2.text()
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

# Niki Dok
def mmm():
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Bitte wählen Sie eine Anforderung zum Löschen aus.")
    x = msg.exec_()

# Niki Dok
def mmm1():
    msg = QMessageBox()
    msg.setWindowTitle("Fehler")
    msg.setText("Bitte wählen Sie eine Anforderung zum Änderung aus.")
    x = msg.exec_()

##########################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fenster2 = QtWidgets.QDialog()
    ui = Anforderungsliste()
    ui.setupUi(Fenster2)
    Fenster2.show()
    sys.exit(app.exec_())
