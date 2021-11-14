from datetime import datetime
import sqlite3 as um
import UserManagement
from ProjectManagement import *

currentRequirement = None

um_connection = um.connect("Database.db")
c = um_connection.cursor()

def dropTable():
    c.execute('DROP TABLE Requirements')

createTable = """CREATE TABLE IF NOT EXISTS Requirements( 
    requirementid INTEGER UNIQUE PRIMARY KEY, 
    name TEXT , 
    creationdate TEXT, 
    modificationdate TEXT,
    projectid INTEGER NOT NULL REFERENCES Projects(projectid),   
    author TEXT NOT NULL REFERENCES user(username), 
    requirementtext text, 
    specificationtext text,
    requirementstatus INTEGER DEFAULT 1,
    specificationstatus INTEGER DEFAULT 0)"""
c.execute(createTable)

def createRequirement():
    requirementName = input('Requirement Name: ')
    reqText = input('Requirement Text: ')
    specText = input('Specification Text: ')


    projectdate = datetime.now()
    dateString = projectdate.strftime("%d/%m/%Y %H:%M:%S")


    c.execute("""INSERT INTO Requirements (
        name, 
        creationdate, 
        modificationdate, 
        projectid, 
        author, 
        requirementtext,
        specificationtext) 
        VALUES (?, ?, ?, ?, ?, ?, ? )"""
        , (requirementName, 
        dateString, dateString, 
        int(str(getcurrentProject())[0:-1])  ,
        UserManagement.currentUser, 
        reqText, specText ))

    um_connection.commit()

def getReqName(reqID:int):
    c.execute(""" SELECT name FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getCreationDate(reqID:int):
    c.execute(""" SELECT creationdate FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getModificationDate(reqID:int):
    c.execute(""" SELECT modificationdate FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getAuthor(reqID:int):
    c.execute(""" SELECT author FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    reqName = str(c.fetchall())
    reqName = reqName[3:-4]
    return reqName

def getRequirementText(reqID:int):
    c.execute(""" SELECT requirementtext FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    reqText = str(c.fetchall())
    reqText = reqText[3:-4]
    return reqText

def getSpecificationText(reqID:int):
    c.execute(""" SELECT specificationtext FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    specText = str(c.fetchall())
    specText = specText[3:-4]
    return specText

def getRequirementStatus(reqID:int):
    c.execute(""" SELECT requirementstatus FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    reqStatus = str(c.fetchall())
    reqStatus = int(reqStatus[2:-3])
    return reqStatus

def getSpecificationStatus(reqID:int):
    c.execute(""" SELECT specificationstatus FROM Requirements
    WHERE requirementid = ?
    """, 
    (reqID, ))

    specStatus = str(c.fetchall())
    specStatus = int(specStatus[2:-3])
    return specStatus

def getAllRequirements(ProjectID):
    c.execute("""SELECT requirementid FROM Requirements
    WHERE projectid = ?
    """,
    (ProjectID, ))

    allRequirements = c.fetchall()
    return allRequirements

def assignProject(reqID, projectID):
    c.execute("""
    UPDATE Requirements
    SET projectid = ? 
    WHERE requirementid = ?
    """, 
    (projectID, reqID)
    )

    um_connection.commit()

def setRequirementText(text:str, reqID:int):
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("""
    UPDATE Requirements
    SET requirementtext = ?,
    modificationdate = ?
    WHERE requirementid = ?
    """, 
    (text, modDate, reqID)
    )

    um_connection.commit()

def setSpecificationText(Spectext:str, reqID:int):
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("""
    UPDATE Requirements
    SET specificationtext = ?,
    modificationdate = ?
    WHERE requirementid = ?
    """, 
    (Spectext, modDate, reqID)
    )

    um_connection.commit()

def setRequirementStatus(RequStatus:int, reqID:int):
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("""
    UPDATE Requirements
    SET requirementstatus = ?,
    modificationdate = ?
    WHERE requirementid = ?
    """, 
    (RequStatus, modDate, reqID)
    )

    um_connection.commit()

def setSpecificationStatus(SpecStatus:int, reqID:int):
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("""
    UPDATE Requirements
    SET specificationstatus = ?,
    modificationdate = ?
    WHERE requirementid = ?
    """, 
    (SpecStatus, modDate, reqID)
    )

    um_connection.commit()

# Es fehlen noch Methoden für die Übergabe der Lasten-, bzw. Pflichtenheft Daten 


def showRequirements():
    for data in c.execute('SELECT * FROM Requirements'):
        print(data)


#dropTable()
#createRequirement()
#assignProject(1, 1)
#showRequirements()
#print(getReqName(2))
#print(getCreationDate(2))
#print(getModificationDate(2))
#print(getAuthor(2))
#print(getRequirementText(2))
#print(getSpecificationText(1))
#print(getRequirementStatus(2))
#print(getSpecificationStatus(1))
#AllRequirements = getAllRequirements(1)
#print(AllRequirements[0])
showRequirements()
setRequirementText("Karbonat Erol sagt ", 2)
setSpecificationStatus(1, 3)
showRequirements()