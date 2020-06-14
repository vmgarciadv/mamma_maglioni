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
    cursor.execute("create table piz_ing(id integer primary key, precio real not null, fk_pizza integer, fk_ingrediente integer)")

    conn.commit()

def sql_insert(conn):
    cursor = conn.cursor()
    
    ingredientes = [("Jamon",), ("Champinones",), ("Pimenton",), ("Doble queso",), ("Aceitunas",), ("Pepperoni",), ("Salchichon",),]
    cursor.executemany("insert into ingrediente(nombre) values (?)", ingredientes)

    pizzas = [("Personal", 10,), ("Mediana", 15,), ("Familiar", 20,),]
    cursor.executemany("insert into pizza(size, precio) values (?, ?)", pizzas)

    piz_ing = [(1.5, 1, 1), (1.75, 1, 2), (1.5, 1, 3), (0.80, 1, 4), (1.80, 1, 5), (1.25, 1, 6), (1.60, 1, 7), 
               (1.75, 2, 1), (2.05, 2, 2), (1.75, 2, 3), (1.30, 2, 4), (2.15, 2, 5), (1.70, 2, 6), (1.85, 2, 7),
               (2.00, 3, 1), (2.50, 3, 2), (2.00, 3, 3), (1.70, 3, 4), (2.60, 3, 5), (1.90, 3, 6), (2.10, 3, 7),]
    cursor.executemany("insert into piz_ing(precio, fk_pizza, fk_ingrediente) values (?, ?, ?)", piz_ing)

    conn.commit()

conn = sql_connection()
sql_table(conn)
sql_insert(conn)