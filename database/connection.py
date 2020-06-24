import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('mamma_maglioni.db')
        print(conn)
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE cliente(id integer PRIMARY KEY,nombre text NOT NULL, apellido text NOT NULL)")
        cursor.execute("CREATE TABLE pizza(id integer PRIMARY KEY,size text NOT NULL UNIQUE,precio real NOT NULL)")
        cursor.execute("CREATE TABLE ingrediente(id integer PRIMARY KEY,nombre text NOT NULL, precio real NOT NULL)")
        cursor.execute("CREATE TABLE pedido(id integer NOT NULL,fecha date NOT NULL,fk_cliente integer NOT NULL,PRIMARY KEY (id),FOREIGN KEY (fk_cliente) REFERENCES cliente(id))")
        cursor.execute("CREATE TABLE pedi_pizza(id integer NOT NULL, fk_ingrediente integer, fk_pizza integer NOT NULL, fk_pedido integer NOT NULL, PRIMARY KEY (id), FOREIGN KEY (fk_ingrediente) REFERENCES ingrediente(id), FOREIGN KEY (fk_pizza) REFERENCES pizza(id), FOREIGN KEY (fk_pedido) REFERENCES pedido(id))")
        conn.commit()
    except:
        print('Las tablas ya han sido creadas.')

def sql_insert(conn):
    cursor = conn.cursor()
    try:
        ingredientes = [("p_jamon",1.5,),("m_jamon",1.75,),("f_jamon",2.00,), 
                        ("p_champinones",1.75,),("m_champinones",2.05,),("f_champinones",2.50,), 
                        ("p_pimenton",1.5,),("m_pimenton",1.75,),("f_pimenton",2.00,), 
                        ("p_doble queso",0.80,),("m_doble queso",1.30,),("f_doble queso",1.70,),
                        ("p_aceitunas",1.80,),("m_aceitunas",2.15,),("f_aceitunas",2.60,), 
                        ("p_pepperoni",1.25,),("m_pepperoni",1.70,),("f_pepperoni",1.90,), 
                        ("p_salchichon",1.60,),("m_salchichon",1.85,),("f_salchichon",2.10),]
        cursor.executemany("insert into ingrediente(nombre,precio) values (?,?)", ingredientes)
        pizzas = [("personal", 10,), 
                ("mediana", 15,), 
                ("familiar", 20,),]
        cursor.executemany("insert into pizza(size, precio) values (?, ?)", pizzas)
        conn.commit()
    except: 
         print('Los datos ya han sido insertados.')

conn = sql_connection()
sql_table(conn)
sql_insert(conn)