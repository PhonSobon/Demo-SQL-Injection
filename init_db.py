import sqlite3

connection = sqlite3.connect('demo.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('admin', 'password123'))

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('user', 'mypassword'))

connection.commit()
connection.close()