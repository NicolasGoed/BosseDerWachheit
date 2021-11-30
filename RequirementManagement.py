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
    projectname TEXT REFERENCES Projects(projectname),   
    author TEXT NOT NULL REFERENCES user(username), 
    requirementtext text, 
    specificationtext text,
    requirementstatus INTEGER DEFAULT 1,
    specificationstatus INTEGER DEFAULT 0)"""
c.execute(createTable)


def createRequirement(projectname,reqname, specText):
    requirementName = reqname
    projectname = projectname
    #reqText = ""
    specText = specText
    

    projectdate = datetime.now()
    dateString = projectdate.strftime("%d/%m/%Y %H:%M:%S")

    c.execute("""INSERT INTO Requirements (
        name, 
        creationdate, 
        modificationdate, 
        projectname,
        specificationtext,
        author) 
        VALUES (?, ?, ?, ?, ?, ?)"""
        , (requirementName, 
        dateString, dateString, 
        projectname,
        specText,
        UserManagement.currentUser, 
        ))



    um_connection.commit()
#createRequirement("a","req16")


def getSpecificationText(reqname):
    dataspectext = c.execute(""" SELECT specificationtext FROM Requirements
    WHERE name = ?
    """, 
    (reqname, ))
    dataspectextarray = list(dataspectext)
    print(dataspectextarray)
    return dataspectextarray
#getSpecificationText("req24")


def getAllRequirements(projectname):
    data = c.execute("""SELECT DISTINCT name FROM Requirements
    WHERE projectname = ?
    """,
    (projectname, ))
 
    array = list(data)
    
    return array


#print (getAllRequirements("a"))


def setSpecificationText(Spectext, reqname):
    modDate = datetime.now()
    modDate = modDate.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("""
    UPDATE Requirements
    SET specificationtext = ?,
    modificationdate = ?
    WHERE name = ?
    """, 
    (Spectext, modDate, reqname)
    )
      #  WHERE requirementid = ?


    um_connection.commit()
#setSpecificationText("aa", "req18")

def showRequirements():
    for data in c.execute('SELECT * FROM Requirements'):
        print(data)

# Dokumentation mache ich // Thi
def deleteRequirement(requirementname):
    c.execute('DELETE FROM Requirements WHERE name = ?', (requirementname, ))
    um_connection.commit()
    

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

def assignProject(reqID, projectname):
    c.execute("""
    UPDATE Requirements
    SET projectname = ? 
    WHERE requirementid = ?
    """, 
    (projectname, reqID)
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
#showRequirements()
#setRequirementText("Karbonat Erol sagt ", 2)
#setSpecificationStatus(1, 3)
#showRequirements()