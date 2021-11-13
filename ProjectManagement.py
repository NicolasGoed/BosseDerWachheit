from datetime import datetime
import sqlite3 as um
import UserManagement

Pnow = ''

um_connection = um.connect("Database.db")
c = um_connection.cursor()

c.execute('DROP TABLE Projects')

createTable = "CREATE TABLE IF NOT EXISTS Projects( projectid INTEGER UNIQUE PRIMARY KEY, projectname TEXT NOT NULL, creationdate TEXT, user TEXT NOT NULL REFERENCES user(username))"
c.execute(createTable)


def createProject():
    projectname = input('Projectname: ')
    projectdate = datetime.now()
    dateString = projectdate.strftime("%d/%m/%Y %H:%M:%S")
    c.execute('INSERT INTO Projects (projectname, creationdate, user) VALUES (?, ?, ? )', (projectname, dateString, UserManagement.currentUser ))
    global Pnow 
    for Pnow in c.execute(' SELECT projectid FROM projects WHERE projectname = ? AND creationdate = ? AND user = ?',(projectname, dateString, UserManagement.currentUser )):
        Pnow = Pnow
        
    um_connection.commit()


def deleteProject():
    c.execute('DELETE FROM Projects WHERE projectid = ? ', (Pnow))




def showProjects():
    for data in c.execute('SELECT * FROM Projects'):
        print(data)



#UserManagement.showUsers()
createProject()
createProject()
showProjects()
deleteProject()
print("------------")
showProjects()

