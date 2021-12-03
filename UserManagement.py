"""Project Management Modul
        * Erzeugt in der Datenbank die Tabelle für User
        * Bietet alle Funktionen um mit der Userdatenbank zu interagieren 
        * Bietet Funktionen zum Auslesen der Userdatenbank


authors: Thi Tran, Niklas Schenk, Nicolas Gödeke, Niklas Langer (Bosse der Wachheit)
date: 05.12.2021
version: 0.0.1
license: Public Domain
"""

import sqlite3 as um
import getpass
from sqlite3.dbapi2 import connect
import sys
import hashlib
import os

currentUser = "a"

def setcurrentUser(currentUser1): 
    """Setzt den sich angemeldeten User als aktuellen User

    Args:
        currentUser1 (String): der Benutzer der im Moment angemeldet ist

    Tests: 
        *Überprüfen, ob der User wirklich der aktuelle ist 
        *Übergabe eines Users der nicht angemeldet ist 
    """

    currentUser = currentUser1

#Connection zur Datenbank herstellen und den cursor definieren und setzen
um_connection = um.connect("Database.db")
c = um_connection.cursor()



def createUser(userR, passwordR):
    """Erzeugt einen neuen User. Bekommt von der GUI im Eingabefeld die Daten übergeben.
       Um das Paswort nicht in Klartext in der Datenbank zu speichern, wird es zu einem Hash gewandelt
       Da das die Python eigene Hash-Funktion ein Datum einsetzt, enstehen immer unterschiedliche Hashes pro Datensatz, deshalb die verwenung von hashlib

    Args:
        userR (String): der Username der in der GUI vom Benutzer eingegeben wird
        passwordR (String): das Passwort, welches in der GUI von Benutzer eingegeben wird

    Tests:
        *Da der User UNIQUE sein muss, die Eingabe eines bereits existierenden Usernames
        *Überprüfung ob der Hash bei diesem Passwort immer gleichbleiben ist, da sonst ein Login nicht möglich ist 


    Source:
        https://docs.python.org/3/library/hashlib.html, https://www.codegrepper.com/code-examples/python/how+to+convert+hash+to+string+in+python
    """
    passwordR = passwordR.encode('utf-8')
    c.execute('INSERT INTO users (username, password) VALUES (? , ? )', (userR, str(hashlib.sha1(passwordR).hexdigest())))
    
    um_connection.commit()



def comparePassword(pw, pwWdh):
    """Wir fordern den User auf, das Passwort bei der Erstellung eines Accounts zweimal einzugeben. 
       Diese Methode überprüft ob diese auch übereinstimmen.

    Args:
        pw (String): Passwort das der Benutzer in das erste Eingabefeld einträgt
        pwWdh (String): Passwort das der Benutzer zur Überprüfung in das zweite Eingabefeld einträgt

    Returns:
        String: Wenn die beiden Passwörter übereinstimmen wird dies übergeben

    Tests: 
        *Zwei nicht übereinstimmende Passwörter eingeben 
        *Prüfen, ob es korrekt übergeben wird und nicht doch bei nicht übereinstimmenden Passwörtern ein User in der Datenbank erstellt wird (mit ggf. falschem Passwort oder einem der Beiden)
    """
    return pw == pwWdh



def showUsers():
    """Zeigt alle in der Datenbank gespeicherten User an

    Tests:
        *Überprüfen ob es wirklich alle User sind und alle gespeichert werden
        *Daten der einzelnen User Prüfen und ob diese stimmen und korrekte Werte besitzen
    """
    for data in c.execute('SELECT * FROM users'):
        print(data)



def  checkUser(user, password):
    """
      *Wenn der Benutzer sich einloggen will, werden hier die Daten die er eingibt überprüft 
       Auch hier muss wie bei der CreateUser das Passwort gehashed werden. Jetzt ist es wichtig das beide übereinstimmen, 
       da sonst ein einloggen nicht möglich ist 
      *Sollte fetchall nichts finden entsteht eine leere Liste und es wird False übergeben

    Args:
        user (String): Username des Benutzers den er zum einloggen in der GUI eingibt 
        password (String): Passwort des Benutzers den er zum einloggen in der GUI eingibt

    Returns:
        Boolean: Wenn keine passender Datensatz gefunden wird ist die Liste leer und es wird False übergeben

    Tests:
        *Falsches Passwort zu dem Benutzernamen eingeben 
        *Falschen Benutzernamen eingeben, der nicht existiert 
        *Überprüfen ob hashlib den korrekten Hash erzeugt um sie vergleichbar zu machen
    """

    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, str(hashlib.sha1(password).hexdigest())))
    

    if (c.fetchall()):
        global currentUser
        currentUser = user
        return True
    else:
        return False




def changePassword():
    """Methode wurde letzendlich im Frontend nicht Benutzt, deshalb keine Args sondern einfache Konsoleneingabe!
       Hier hat der Benutzer die Möglichkeit sein Passwort zu ändern
       Dafür muss er seinen User und sein altes sowie gewünschtes neues passwort eingeben
       Das neue Passwort wird dann erneut gehashed und in die Datenbank per UPDATE an der Stelle des alten Passworts verändert 

       Tests:
        *Wurde das Passwort in der Datenbank erfolgreich geändert 
        *Eingabe eines falschen alten Passworts 
    """
    
    user = input('User: ')
    password = getpass.getpass('Old Password: ')
    npassword = getpass.getpass('New Pasword : ')
    npassword = npassword.encode('utf-8')

    
    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, str(hashlib.sha1(password).hexdigest())))

    
    if (c.fetchall()):
        c.execute('UPDATE users SET password = ? WHERE username = ?', ( str(hashlib.sha1(npassword).hexdigest()), user))
        print('Password of ' + user + ' was changed successfully')
        um_connection.commit()
    else:
        print('Wrong password')

#Möglichkeit Tabelle zu löschen(Testzwecke!)
#c.execute('DROP TABLE users')

# Erstellen der Tabelle für die Benutzerdaten innerhalb der SQLite Datenbank, wenn sie noch nicht existiert 
createTable = "CREATE TABLE IF NOT EXISTS users( username text UNIQUE PRIMARY KEY, password text)"
c.execute(createTable)

def deleteUser():
    """Methode wurde letzendlich im Frontend nicht Benutzt, deshalb keine Args sondern einfache Konsoleneingabe!
       Hier hat der Benutzer die Möglichkeit seinen Benutzer zu löschen
       Dafür muss er seinen User und sein Passwort eingeben
       Der richtige Dateneintrag wird dann per SELECT abgefragt und daraufhin per DELETE aus der Datenbank gelöscht 

       Tests:
        *Überprüfen ob der User wirklich gelöscht ist 
        *Versuch eines User ohne das korrekte Passwort zu löschen

    """
    showUsers()
    user = input('User you want to delete: ')
    password = getpass.getpass('Are you sure? Password: ')
    

    
    password = password.encode('utf-8')
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', ( user, str(hashlib.sha1(password).hexdigest())))

    
    if (c.fetchall()):
        c.execute('DELETE FROM users WHERE username = ? AND password = ?', ( user,str(hashlib.sha1(password).hexdigest())))
        print('The user ' + user + ' was deleted successfully')
        um_connection.commit()
    else:
        print('Wrong password')


