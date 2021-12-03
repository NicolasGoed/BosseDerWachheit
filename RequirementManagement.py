from datetime import datetime
import sqlite3 as um
import UserManagement
from ProjectManagement import *

currentRequirement = None

um_connection = um.connect("Database.db")
c = um_connection.cursor()

def dropRequirementTable():
    """Funktion, um die Requirement Tabelle vollständig zu löschen.
       Nur für Testzwecke!
    """
    c.execute('DROP TABLE Requirements')


def createTable(): 
    """Erstellt die Tabelle für die Anforderungsdatenbank mit folgenden Spalten 
        * RequirementID = Eindeutige ID einer Anforderung 
        * Name = Name der Anforderung 
        * Creationdate = Datetime der Erstellung
        * ModificationDate = Datetime der letzten Bearbeitung
        * ProjectName = Projekt, dem das Requirement zugeordnet wurde
        * Author = User, der die Anforderung erstellt hat 
        * RequirementText = Anforderungstext
        * specificationText = Spezifikationstext
        * RequirementStatus = Status, ob es sich um ein Requirement handelt (0 = nein, 1 = ja)
        * SpecificationStatus = Status, ob eine Spezifikation zur Anforderung existiert (0 = nein, 1 = ja)
    """
    createTable = "CREATE TABLE IF NOT EXISTS Requirements(requirementid INTEGER UNIQUE PRIMARY KEY, name TEXT , creationdate TEXT, modificationdate TEXT, projectname TEXT REFERENCES Projects(projectname), author TEXT NOT NULL REFERENCES user(username), requirementtext text, specificationtext text, requirementstatus INTEGER DEFAULT 1, specificationstatus INTEGER DEFAULT 0)"

    c.execute(createTable)


def createRequirement(projectname,reqname, specText):
    """Erstellt eine Anforderung in der Anforderungsdatenbank. Dafür werden Projektname, 
       Anforderungsname und der Spezifikationstext genutzt. Die restlichen Daten werden 
       automatisch generiert.

    Args:
        projectname (String): Name des Projekts, dem das Requirement zugeordnet werden soll 
        reqname (String): Name der Anforderung
        specText (String): Spezifikationstext, welcher zu der Anforderung gehört

    Test:
        * Projektname einfügen, der bereits vorhanden ist 
        * Einen sehr großen Spezifikationstext einfügen 
    """
    requirementName = reqname
    projectname = projectname
    specText = specText
    

    projectdate = datetime.now()
    dateString = projectdate.strftime("%d/%m/%Y %H:%M:%S")

    c.execute("INSERT INTO Requirements (name, creationdate, modificationdate, projectname, specificationtext,author) VALUES (?, ?, ?, ?, ?, ?)", (requirementName, dateString, dateString, projectname, specText,UserManagement.currentUser,))



    um_connection.commit()


def getSpecificationText(reqname):
    """Benutzt den Anforderungsnamen, um alle Spezfikationstexte, welche einer
       Anforderung zugeordnet sind, aus der Anforderungsdatenbank zu ziehen.

    Args:
        reqname (String): Name der Anforderung

    Returns:
        list: Liste aller Spezifikationstexte zu einer Anforderung

    Tests:
        * Eingeben eines Anforderungsnamen, welcher nicht existiert
        * Eigabe der Requirementnummer, statt des Anforderungsnamen
    """


    dataspectext = c.execute(" SELECT specificationtext FROM Requirements WHERE name = ?", (reqname, ))
    dataspectextarray = list(dataspectext)
    #print(dataspectextarray)
    return dataspectextarray



def getAllRequirements(projectname):
    """Gibt alle Anforderungen eines Projektes in einer Liste zurück. Dafür erfolgt der Zugriff
       auf die Anforderungsdatenbank über den Projektnamen.

    Args:
        projectname (String): Name des Projekts, dessen Anforderungen zurückgegeben werden sollen

    Returns:
        list: Liste aller Anforderungen, welche mit dem Projekt verknüpft sind

    Tests:
        * Eingabe eines anderen Datentypen als String
        * Eingabe der Projektnummer statt des Projektnamen
    """
    data = c.execute("SELECT DISTINCT name FROM Requirements WHERE projectname = ?",  (projectname, ))
 
    array = list(data)
    
    return array



def setSpecificationText(Spectext, reqname):
    """Setzt den Spezifikationstext in der Anforderungsdatenbank für eine Anforderung. Dafür wird der 
       Name der Anforderung übergeben, für welche der Spezifikationstext gesetzt werden soll. Außerdem wird der 
       Spezifikationstext übergeben, welcher in der Datenbank eingefügt werden soll.

    Args:
        Spectext (String): Spezifikationstext für die Anforderung
        reqname (String): Name der zu bearbeitenden Anforderung

    Test:
        * Übergabe eines leeren Spezifikationstext
        * Übergabe der Requirementnummer statt dem Anforderungsnamen
    """
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("UPDATE Requirements SET specificationtext = ?, modificationdate = ? WHERE name = ?",  (Spectext, modDate, reqname))
      #  WHERE requirementid = ?


    um_connection.commit()


def showRequirements():
    """Gibt alle Requirements, welche in der Datenbank vorhanden sind, auf der Konsole aus
    """
    for data in c.execute('SELECT * FROM Requirements'):
        print(data)


def deleteRequirement(requirementname):
    """Löscht die Anforderung mit dem übergebenen Anforderungsnamen aus der 
       Anforderungsdatenbank

    Args:
        requirementname (String): Name der Anforderung, welche gelöscht werden soll

    Tests:
        * Übergabe eines nicht vorhandenen Anforderungsnamen
        * Übergabe des Parameter 'name', um eine SQL-Injection zu versuchen
    """
    c.execute('DELETE FROM Requirements WHERE name = ?', (requirementname, ))
    um_connection.commit()
    

def getRequirementStatus(reqID:int):
    """Fragt den Anforderungsstatus von der Anforderung anhand der Anforderungs-ID ab.

    Args:
        reqID (int): ID der Anforderung

    Returns:
        int: Status der Anforderung

    Tests:
        * Eingabe des Anforderungsnamen
        * Versuch einer SQL-Injection
    """
    c.execute("SELECT requirementstatus FROM Requirements WHERE requirementid = ?", (reqID, ))

    reqStatus = str(c.fetchall())
    reqStatus = int(reqStatus[2:-3])
    return reqStatus

def getSpecificationStatus(reqID:int):
    """Fragt den Spezifikationsstatus von der Anforderung anhand der Anforderungs-ID ab.

    Args:
        reqID (int): ID der Anforderung

    Returns:
        int: Status der Spezifikation

    Tests:
        * Eingabe einer nicht existenten Anforderungs-ID
        * Versuch einer SQL-Injection
    """


    c.execute(""" SELECT specificationstatus FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    specStatus = str(c.fetchall())
    specStatus = int(specStatus[2:-3])
    return specStatus

def assignProject(reqID, projectname):
    """Teilt anhand des Projektnamens und der Anforderungs-ID dem Requirement ein Projekt in der Anforderungsdatenbank 
       zu.

    Args:
        reqID (int): ID der zu ändernden Anforderung
        projectname (str): Projekt, welchem die Anforderung zugeordet werden soll

    Tests:
        * Eingabe eines Strings als reqID
        * Eingabe eines nicht vorhanden Projekts
    """

    c.execute("UPDATE Requirements SET projectname = ?  WHERE requirementid = ?", (projectname, reqID))

    um_connection.commit()

def setRequirementText(text:str, reqID:int):
    """Setzt oder aktualisiert den Anforderungstext einer Anforderung in der Anforderungsdatenbank. Dazu wird auch das Datum + Uhrzeit 
       der letzten Bearbeitung aktualisiert.

    Args:
        text (str): Anforderungstext
        reqID (int): ID der Anforderung

    Tests:
        * Eingabe einer leeren RequirementID 
        * Eingabe eines extrem langen RequirementText
    """

    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("UPDATE Requirements SET requirementtext = ?, modificationdate = ? WHERE requirementid = ?",  (text, modDate, reqID))

    um_connection.commit()


def setRequirementStatus(RequStatus:int, reqID:int):
    """ Aktualisiert den Anforderungsstatus in der Anforderungsdatenbank anhand der Anforderungs-ID.

    Args:
        RequStatus (int): Neuer Anforderungsstatus
        reqID (int): ID der zu ändernden Anforderung

    Test: 
        * Übergabe eines leeren Anforderungsstatus
        * Übergabe eines Anforderungsstatus der nicht 0 oder 1 ist 
    """
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("UPDATE Requirements SET requirementstatus = ?, modificationdate = ? WHERE requirementid = ?", (RequStatus, modDate, reqID))

    um_connection.commit()

def setSpecificationStatus(SpecStatus:int, reqID:int):
    """ Aktualisiert den Spezifikationsstatus in der Anforderungsdatenbank anhand der Anforderungs-ID.

        Args:
            RequStatus (int): Neuer Spezifikationsstatus
            reqID (int): ID der zu ändernden Anforderung

        Test: 
            * Übergabe einer nicht vorhandenen Anforderungs-ID
            * Übergabe eines Anforderungsstatus der nicht 0 oder 1 ist 
        """

    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("UPDATE Requirements SET specificationstatus = ?, modificationdate = ? WHERE requirementid = ?",  (SpecStatus, modDate, reqID))

    um_connection.commit()

def getReqName(reqID:int):
    """Abfrage und Rückgabe des Anforderungsname anhand der Anforderungs-ID aus der Anforderungsdatenbank

    Args:
        reqID (int): ID der Anforderung

    Returns:
        str: Name der Anforderung

    Tests:
        * Anforderungs-ID übergeben, welche nicht existiert
        * Auswahl Anforderung mit leerem Anforderunsnamen
    """

    c.execute("SELECT name FROM Requirements WHERE requirementid = ?", (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getCreationDate(reqID:int):
    """Abfrage der Erstellungszeit (Datum + Zeit) aus der Anforderungsdatenbank. DDie daraus erhaltene 
       Liste wird als String zugeschnitten, sodass die Zeit als String zurückgegebn wird, nicht als DateTime.

    Args:
        reqID (int): Anforderungs-ID

    Returns:
        str: Erstellungszeit (Datum + Zeit)

    Tests:
        * Versuch einer SQL-Injection 
        * Übergabe von keiner Anforderungs-ID
    """
    c.execute(" SELECT creationdate FROM Requirements WHERE requirementid = ?", (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getModificationDate(reqID:int):
    """Abfrage der Zeit der letzten Bearbeitung (Datum + Zeit) aus der Anforderungsdatenbank. Die daraus erhaltene 
       Liste wird als String zugeschnitten, sodass die Zeit als String zurückgegebn wird, nicht als DateTime.

    Args:
        reqID (int): Anforderungs-ID

    Returns:
        str: Zeit der letzten Bearbeitung (Datum + Zeit)
    
    Tests:
        * Abfrage der Funktion, ohne vorher den Table erstellt zu  haben
        * Übergabe von 0 als Anforderungs-ID
    """
    c.execute("SELECT modificationdate FROM Requirements WHERE requirementid = ?", (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getAuthor(reqID:int):
    """Abfrage des Autors aus der Anforderungsdatenbank anhand der Anforderungs-ID. Schneidet die abgefragte Liste zu einem
    klaren String zusammen. Der Autor wird als String übergeben.

    Args:
        reqID (int): ID der Anforderung

    Returns:
        str: Autor der Anforderung

    Tests:
        * Es existiert kein Autor in der Anforderung
        * Die Anforderungs-ID wird extrem hoch gewählt (Overflow)
    """
    c.execute("SELECT author FROM Requirements WHERE requirementid = ?",  (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName


