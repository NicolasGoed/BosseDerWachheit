from datetime import datetime
import sqlite3 as um
import UserManagement
from ProjectManagement import *

currentRequirement = None

um_connection = um.connect("Database.db")
c = um_connection.cursor()

c.execute('DROP TABLE Requirements')

createTable = """CREATE TABLE IF NOT EXISTS Requirements( 
    requirementid INTEGER UNIQUE PRIMARY KEY, 
    name TEXT , 
    creationdate TEXT, 
    modificationdate TEXT,
    projectid INTEGER NOT NULL REFERENCES Projects(projectid),   
    author TEXT NOT NULL REFERENCES user(username), 
    requirementtext text, 
    specificationtext text)"""
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
        , (requirementName, dateString, dateString, getcurrentProject()  ,UserManagement.currentUser, reqText, specText ))

    um_connection.commit()

def showRequirements():
    for data in c.execute('SELECT * FROM Requirements'):
        print(data)

createRequirement()
showRequirements()