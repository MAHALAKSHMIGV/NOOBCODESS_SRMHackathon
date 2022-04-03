import sqlite3
connection=sqlite3.connect("facebase.db")
cursor=connection.cursor()
cursor.execute("create table people(id integer primary key, name text, vaccdet, text, faceID, text)");