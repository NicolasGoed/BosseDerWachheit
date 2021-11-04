import sqlite3 as um
import getpass
from sqlite3.dbapi2 import connect
import sys
import hashlib
import os


# @Alf Hier wird dann bei dir eine neue Datenbank erstellt. Falls dies nicht gewünscht ist "UserDatabase.db" mit relativemPfad der existierenden DB austauschen.
um_connection = um.connect("UserDatabase.db")
c = um_connection.cursor()

# Möglichkeit Tabelle zu löschen (Testzwecke)
#c.execute('DROP TABLE users')

# Erstellen der Tabelle für die Benutzerdaten innerhalb der SQLite Datenbank
createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username text UNIQUE, password text)"
c.execute(createTable)

# Hier wird der neue User erstellt. Zunächst Eingabe der Daten und dann Speichern in der Datenbank
def createUser():
    userR = input('New User: ')
    passwordR = getpass.getpass('New Password: ')
    passwordR = passwordR.encode('utf-8')
    c.execute('INSERT INTO users (username, password) VALUES (? , ? )', (userR, str(hashlib.sha1(passwordR).hexdigest())))
    # Hier wird mithilfe von hashlib das Passwort verschlüsselt. Dazu auch das Umwandeln in utf8 davor. Am Ende wird es erneut ein String zur Speicherung in der Datenbank
    # Quellen für diesen Prozess: https://docs.python.org/3/library/hashlib.html, https://www.codegrepper.com/code-examples/python/how+to+convert+hash+to+string+in+python
    um_connection.commit()




def showUsers():
    for data in c.execute('SELECT * FROM users'):
        print(data)

showUsers()


def checkUser():
# Get login details from user
    user = input('User: ')
    password = getpass.getpass('Password: ')


    # später als funtkion 
    # Execute sql statement and grab all records where the "usuario" and
    # "senha" are the same as "user" and "password"
    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, str(hashlib.sha1(password).hexdigest())))

    # If nothing was found then c.fetchall() would be an empty list, which
    # evaluates to False 
    if (c.fetchall()):
        print('Welcome ' + user)
    else:
        print('Login failed')

#createUser()
checkUser()


#DeleteUser
#ChangeUser (Passwort und Benitzername verändern) (optinal)
#@Frontend einen Button wo alle User sichtbar 
#@Frontedn Benutzerverwaltung Button, nicht alle iwo im GUI 
#@Frontend #später Parameter übergeben mit Listener 
#Ordentlich kommentieren, hexdigest ausm Internet