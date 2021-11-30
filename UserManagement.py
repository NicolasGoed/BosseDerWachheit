import sqlite3 as um
import getpass
from sqlite3.dbapi2 import connect
import sys
import hashlib
import os

currentUser = "a"
# currentUser = None
def setcurrentUser(currentUser1): 
    currentUser = currentUser1

# @Alf Hier wird dann bei dir eine neue Datenbank erstellt. Falls dies nicht gewünscht ist "UserDatabase.db" mit relativemPfad der existierenden DB austauschen.
# THI: Die Datei habe ich gelöscht, daher den obigen Kommentar löschen? Sonst funktioniert das Programm nicht 
um_connection = um.connect("Database.db")
c = um_connection.cursor()


# Hier wird der neue User erstellt. Zunächst Eingabe der Daten und dann Speichern in der Datenbank
def createUser(userR, passwordR):
    #userR = input('New User: ')
    #passwordR = getpass.getpass('New Password: ')
    passwordR = passwordR.encode('utf-8')
    c.execute('INSERT INTO users (username, password) VALUES (? , ? )', (userR, str(hashlib.sha1(passwordR).hexdigest())))
    # Hier wird mithilfe von hashlib das Passwort verschlüsselt. Dazu auch das Umwandeln in utf8 davor. Am Ende wird es erneut ein String zur Speicherung in der Datenbank
    # Quellen für diesen Prozess: https://docs.python.org/3/library/hashlib.html, https://www.codegrepper.com/code-examples/python/how+to+convert+hash+to+string+in+python
    um_connection.commit()

#createUser("a", "a")

def comparePassword(pw, pwWdh):
    return pw == pwWdh



def showUsers():
    for data in c.execute('SELECT * FROM users'):
        print(data)


# # THI: user, passwort als parameter ergänzt
def  checkUser(user, password):
# Get login details from user
    #user = input('User: ')
    #password = getpass.getpass('Password: ')

    
    # später als funtkion 
    # Execute sql statement and grab all records where the "usuario" and
    # "senha" are the same as "user" and "password"
    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, str(hashlib.sha1(password).hexdigest())))
    # If nothing was found then c.fetchall() would be an empty list, which
    # evaluates to False 
    if (c.fetchall()):
        global currentUser
        currentUser = user
        return True
    else:
        return False

def changePassword():
    # Get login details from user
    user = input('User: ')
    password = getpass.getpass('Old Password: ')
    npassword = getpass.getpass('New Pasword : ')
    npassword = npassword.encode('utf-8')

    # später als funtkion 
    # Execute sql statement and grab all records where the "usuario" and
    # "senha" are the same as "user" and "password"
    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, str(hashlib.sha1(password).hexdigest())))

    # If nothing was found then c.fetchall() would be an empty list, which
    # evaluates to False 
    if (c.fetchall()):
        c.execute('UPDATE users SET password = ? WHERE username = ?', ( str(hashlib.sha1(npassword).hexdigest()), user))
        print('Password of ' + user + ' was changed successfully')
        um_connection.commit()
    else:
        print('Wrong password')

# Möglichkeit Tabelle zu löschen (Testzwecke)
#c.execute('DROP TABLE users')

# Erstellen der Tabelle für die Benutzerdaten innerhalb der SQLite Datenbank
createTable = "CREATE TABLE IF NOT EXISTS users( username text UNIQUE PRIMARY KEY, password text)"
c.execute(createTable)

def deleteUser():
    showUsers()
    # Get login details from user
    user = input('User you want to delete: ')
    password = getpass.getpass('Are you sure? Password: ')
    

    # später als funtkion 
    # Execute sql statement and grab all records where the "usuario" and
    # "senha" are the same as "user" and "password" 
    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', ( user, str(hashlib.sha1(password).hexdigest())))

    # If nothing was found then c.fetchall() would be an empty list, which
    # evaluates to False 
    if (c.fetchall()):
        c.execute('DELETE FROM users WHERE username = ? AND password = ?', ( user,str(hashlib.sha1(password).hexdigest())))
        print('The user ' + user + ' was deleted successfully')
        um_connection.commit()
    else:
        print('Wrong password')







#createUser("Niklas", "Merkel")
#createUser(Fler, Test)
#createUser("Fler56", "Merkel")
#checkUser()
#print(currentUser)
# changePassword()
#deleteUser()
#showUsers()

#@Frontend einen Button wo alle User sichtbar
#@Frontedn Benutzerverwaltung Button, nicht alle iwo im GUI
#@Frontend #später Parameter übergeben mit Listener
#Ordentlich kommentieren, hexdigest ausm Internet