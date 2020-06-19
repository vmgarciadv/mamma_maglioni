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
    cursor.execute("CREATE TABLE cliente(id integer PRIMARY KEY,nombre text NOT NULL, apellido text NOT NULL)")
    cursor.execute("CREATE TABLE pizza(id integer PRIMARY KEY,size text NOT NULL,precio real NOT NULL)")
    cursor.execute("CREATE TABLE ingrediente(id integer PRIMARY KEY,nombre text NOT NULL, precio real NOT NULL)")
    cursor.execute("CREATE TABLE pedido(id integer NOT NULL,fecha date NOT NULL,fk_cliente integer NOT NULL,PRIMARY KEY (id,fk_cliente),FOREIGN KEY (fk_cliente) REFERENCES cliente (id))")
    cursor.execute("CREATE TABLE pedi_piz(fk_pizza integer NOT NULL, fk_pedido integer NOT NULL, fk_cliente integer NOT NULL,PRIMARY KEY (fk_pizza,fk_pedido,fk_cliente),FOREIGN KEY (fk_pizza) REFERENCES pizza (id),FOREIGN KEY (fk_pedido,fk_cliente) REFERENCES pedido (id,fk_cliente))")
    cursor.execute("CREATE TABLE pedi_ing(fk_ingrediente integer NOT NULL, fk_pedido integer NOT NULL, fk_cliente integer NOT NULL, fk_pizza integer NOT NULL, fk_pedido1 integer NOT NULL, fk_cliente1 integer NOT NULL, PRIMARY KEY (fk_ingrediente, fk_pedido, fk_cliente, fk_pizza, fk_pedido1, fk_cliente1), FOREIGN KEY (fk_ingrediente) REFERENCES ingrediente(id), FOREIGN KEY (fk_pedido,fk_cliente) REFERENCES pedido(id,fk_cliente), FOREIGN KEY (fk_pizza,fk_pedido1,fk_cliente1) REFERENCES pedi_piz (fk_pizza, fk_pedido1, fk_cliente1))")
    conn.commit()

def sql_insert(conn):
    cursor = conn.cursor()
    ingredientes = [("p_Jamon",1.5,),("m_Jamon",1.75,),("f_Jamon",2.00,), 
                    ("p_Champinones",1.75,),("m_Champinones",2.05,),("f_Champinones",2.50,), 
                    ("p_Pimenton",1.5,),("m_Pimenton",1.75,),("g_Pimenton",2.00,), 
                    ("Doble queso",0.80,),("Doble queso",1.30,),("Doble queso",1.70,),
                    ("Aceitunas",1.80,),("Aceitunas",2.15,),("Aceitunas",2.60,), 
                    ("Pepperoni",1.25,),("Pepperoni",1.70,),("Pepperoni",1.90,), 
                    ("Salchichon",1.60,),("Salchichon",1.85,),("Salchichon",2.10),]
    cursor.executemany("insert into ingrediente(nombre,precio) values (?,?)", ingredientes)
    pizzas = [("Personal", 10,), 
              ("Mediana", 15,), 
              ("Familiar", 20,),]
    cursor.executemany("insert into pizza(size, precio) values (?, ?)", pizzas)
    conn.commit()

conn = sql_connection()
sql_table(conn)
sql_insert(conn)