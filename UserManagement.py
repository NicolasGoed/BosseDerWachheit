import sqlite3 as um
import getpass
from sqlite3.dbapi2 import connect
import sys
import hashlib
import os


# Hier wird eine neue Datenbank erstellt. Falls dies nicht gewünscht ist "UserDatabase.db" mit relativemPfad der existierenden DB austauschen.
um_connection = um.connect("UserDatabase.db")
c = um_connection.cursor()

#c.execute('DROP TABLE users')

createTable = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username text UNIQUE, password text)"
c.execute(createTable)

#später Parameter übergeben mit Listener 
def createUser():
    userR = input('New User: ')
    passwordR = getpass.getpass('New Password: ')
    passwordR = passwordR.encode('utf-8')
    c.execute('INSERT INTO users (username, password) VALUES (? , ? )', (userR, str(hashlib.sha1(passwordR).hexdigest())))
    um_connection.commit()

#createUser()

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


checkUser()