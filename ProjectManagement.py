"""Project Management Modul
        * Erzeugt in der Datenbank die Tabelle für Projekte
        * Bietet alle Funktionen um mit der Projektdatenbank zu interagieren 
        * Bietet Funktionen zum auslesen der Projektdatenbank


authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
license: Public Domain
"""

from datetime import datetime
import sqlite3 as um
import UserManagement

currentProject = ''

def getcurrentProject():
    """Eine Methode die das aktuelle Projekt,ausgewählt anhand der ID, übergibt 

    Returns:
        int: die ID des aktuellen Projekts 
    """
    return currentProject

#Connection zur Datenbank herstellen und Cursor definieren und setzen
um_connection = um.connect("Database.db")
c = um_connection.cursor()

# DROP löscht jedes Mal alle Projekte bzw die Tabelle (Nur für Testzwecke!)
# c.execute('DROP TABLE Projects')

# Wenn nicht schon existent, wird die Tabelle für die Projekte in der Datenbank erstellt
createTable = "CREATE TABLE IF NOT EXISTS Projects( projectid INTEGER UNIQUE PRIMARY KEY, projectname TEXT NOT NULL, creationdate TEXT, user TEXT NOT NULL REFERENCES user(username))"
c.execute(createTable)


def createProject(projectname):
    """Methode zum Erstellen eines Projekts in der Datenbank. 
       Mit den Daten die der Benutzer im GUI eingibt
       Mit dem Projektnamen wird dann die ID des Prjekts Selected und für die Methode currentProjekt gespeichert 

    Args:
        projectname (String): Den Projektnamen den der Benutzer im GUI in das Textefeld eingibt wird dieser Methode übergeben und in der Datenbank eingesetzt

    Tests:
        *Prüfen, ob das Projekt korrekt in die Datenbank eingefügt wurde mit den passenden Werten.
        *Versuchen zwei Projekte mit dem gleichen Namen zu erstellen
    """

    projectdate = datetime.now()
    dateString = projectdate.strftime("%d/%m/%Y %H:%M:%S")
    c.execute('INSERT INTO Projects (projectname, creationdate, user) VALUES (?, ?, ? )', (projectname, dateString, UserManagement.currentUser ))
    global currentProject 
    for currentProject in c.execute(' SELECT projectid FROM projects WHERE projectname = ? AND creationdate = ? AND user = ?',(projectname, dateString, UserManagement.currentUser )):
        currentProject = currentProject
        
    um_connection.commit()




def deleteProject(currentProject):
    """Möglichkeit ein Projekt löschen zu können

    Args:
        currentProject (String): Das aktuelle Projekt anhand des Projektnamens (Sollte erst ID sein aber wurde später aufgrund von Problemen im Frontend geändert)

    Tests:
        *Prüfen, ob das Projekt korrekt gelöscht wurde 
        *Prüfen ob nach Löschug wieder möglich ist ein Projekt mit diesem Namen zu erstellen
    """
    c.execute('DELETE FROM Projects WHERE projectname = ? ', (currentProject, )) 
    um_connection.commit()




def showProjects():
    """Methode um alle vorhandenen Projekte anzuzeigen

    Returns:
        list: eine Liste aller in der Datenbank per SELECT Abfrage gefundenen Projekte 

    Tests:
        *Sind alle Projekte korrekt vorhanden? 
        *Wird die Liste korrekt erstellt und enthält sie alle Einträge und Werte zu den Projekten der Datenbank
    """
    data = list(c.execute('SELECT * FROM Projects'))
    return data



def showProjectsName():
    """Methode um nur die Namen aller Projekte auszulesen

    Returns:
        list: eine Liste aller Projektnamen die per SELECT Abfrage ausgelsen werden

    Tests:
        *Werden insgesamt alle Namen ausgegben
        *Sind die Namen korrekt zu den Einträgen und fehlen nicht einzeln aber dafür andere doppelt 
        *Werden die Daten korrekt in die Liste durch SQL übergeben 
    """
    data = c.execute('SELECT DISTINCT projectname FROM Projects')
    array = list(data)
    return array

