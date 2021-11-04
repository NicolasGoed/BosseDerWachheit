import sqlite3 as um
import getpass
from sqlite3.dbapi2 import connect
import sys

um_connection = um.connect("UserDatabase.db")
c = um_connection.cursor()

createTable = "CREATE TABLE IF NOT EXISTS users(id int, username text, password text)"

c.execute(createTable)

# Get login details from user
user = input('User: ')
password = getpass.getpass('Password: ')



# Execute sql statement and grab all records where the "usuario" and
# "senha" are the same as "user" and "password"
c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, password))

# If nothing was found then c.fetchall() would be an empty list, which
# evaluates to False 
if (len(list(c)) > 0):
    print('Welcome')
else:
    print('Login failed')