import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('test.db')
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE empleado(id integer PRIMARY KEY, name text)")
    conn.commit()

conn = sql_connection()
sql_table(conn)
