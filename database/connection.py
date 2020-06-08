import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('mamma_maglioni.db')
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cursor = conn.cursor()

    cursor.execute("create table pizza(id integer not null primary key, size text not null, precio real not null, fk_pedido integer)")
    cursor.execute("create table ingrediente(id integer primary key, nombre text not null)")
    cursor.execute("create table pedido(id integer primary key, nombre_cliente text not null, fecha text not null)")
    cursor.execute("create table piz_ing(id integer primary key, precio real not null, fk_pizza integer, fk_pedido integer)")

    conn.commit()

def sql_insert(conn):
    cursor = conn.cursor()
    
    ingredientes = [("Jamon",), ("Champinones",), ("Pimenton",), ("Doble queso",), ("Aceitunas",), ("Pepperoni",), ("Salchichon",),]
    cursor.executemany("insert into ingrediente(nombre) values (?)", ingredientes)

    pizzas = [("Personal", 10,), ("Mediana", 15,), ("Familiar", 20,),]
    cursor.executemany("insert into pizza(size, precio) values (?, ?)", pizzas)

    conn.commit()

conn = sql_connection()
sql_table(conn)
sql_insert(conn)