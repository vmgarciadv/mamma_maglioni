import sqlite3
from sqlite3 import Error

class DAO():
    #Crea la conexion con la base de datos
    def create_connection(self):
        try:
            conexion = sqlite3.connect('mamma_maglioni.db')
            print("Se ha establecido la conexion con la base de datos.")
            return conexion
        except Error:
            print(Error)
    #Cierra la conexion con la base de datos
    def cerrar_connection(self, conexion):
        try:
            conexion.close()
            print("Cerrada la conexion con la base de datos.")
        except:
            print("No se pudo cerrar la conexion con la base de datos.")

    #Inserta cliente en la base de datos por medio de los archivos
    def insert_cliente(self, conexion, cli):
        cursor = conexion.cursor()
        i = 0
        nombre = ""
        apellido = ""
        for x in cli:
            if i == 0 and x != " ":
                nombre += x
            if i==1 and x != " ":
                apellido += x
            if x == " ":
                i = 1
        try:
            cliente = (nombre, apellido)
            cursor.execute("insert into cliente(nombre, apellido) values (?, ?)", cliente)
            conexion.commit()
            id = cursor.lastrowid
            return (id)
            """cursor.execute("SELECT last_insert_rowid()")
            rows = cursor.fetchall()
            for row in rows:
                print(row)"""
        except: 
            print('def insert_cliente: Los datos no pudieron insertarse.')
    #Inserta los pedidos en la base de datos por medio de los archivos
    def insert_pedido(self, conexion, fecha, id_cli):
        cursor = conexion.cursor()
        try:
            pedido = (fecha, id_cli)
            cursor.execute("insert into pedido(fecha, fk_cliente) values (date(?), ?)", pedido)
            conexion.commit()
            id = cursor.lastrowid
            return (id)
        except: 
            print('def insert_pedido: Los datos no pudieron insertarse.')
            
    #Retorna el id de la pizza segun el tamano
    def buscar_pizza_size(self,conexion,pizza):
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT id from pizza where size = ?", (pizza,))
            records = cursor.fetchall()
            for row in records:
                return row[0]
        except: 
            print('def buscar_pizza_size: No se encontraron datos')

    #Retorna el tamano de la pizza por su id
    def buscar_pizza(self,conexion,id_pizza):
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT size from pizza where id = ?", (id_pizza,))
            records = cursor.fetchall()
            for row in records:
                return row[0]
        except: 
            print('def buscar_pizza: No se encontraron datos')
    
    #Retorna el nombre del cliente por el id del pedido
    def buscar_cliente(self,conexion,id_pedido):
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT nombre from cliente,pedido where fk_cliente = cliente.id and pedido.id = ?", (id_pedido,))
            records = cursor.fetchall()
            for row in records:
                return row[0]
        except: 
            print('def buscar_cliente: No se encontraron datos')

    #Retorna el nombre del ingrediente por el id del mismo
    def buscar_ingrediente(self,conexion,id_ing):
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT nombre from ingrediente where id = ?", (id_ing,))
            records = cursor.fetchall()
            for row in records:
                return row[0]
        except: 
            print('def buscar_ingrediente: No se encontraron datos')

    #Modifica el ingrediente para que se ingresen a la bd con un formato estandar sin caracteres especiales
    def modificar_ing(self,ingrediente):
        if ingrediente == 'champiñones': ingrediente = 'champinones'
        elif ingrediente == 'jamón': ingrediente = 'jamon'
        elif ingrediente == 'pimentón': ingrediente = 'pimenton'
        return ingrediente

    #Retorna una lista de las id de los ingredientes al registrar en un pedido
    def list_id_ingr(self,conexion,ingredientes,pizza):
        cursor = conexion.cursor()
        id_list_ingr = []
        if pizza=='personal': size = 'p_'
        elif pizza == 'mediana': size = 'm_'
        elif pizza == 'familiar': size = 'f_'
        try:
            for x in range(0,len(ingredientes)):
                ing = self.modificar_ing(ingredientes[x])
                ing = size + ing
                cursor.execute("SELECT id from ingrediente where nombre = ?", (ing,))
                records = cursor.fetchall()
                for row in records:
                    id_list_ingr.append(row[0])
        except: 
            print('def list_id_ingr: No se encontraron datos')
        return id_list_ingr

    #Inserta en la tabla pedi_pizza las foraneas respectivas que conforman un pedido.
    def insert_pedi_pizza(self,conexion,id_ped,pizza,ingredientes):
        i=0
        cursor = conexion.cursor()
        id_pizza = self.buscar_pizza_size(conexion,pizza)
        id_ing = self.list_id_ingr(conexion,ingredientes,pizza)
        """print("Pedido del cliente: ", self.buscar_cliente(conexion,id_ped))
        print("Pizza: ",self.buscar_pizza(conexion,id_pizza)) 
        for x in range(0,len(id_ing)):
            print(id_ing[x])
            print(self.buscar_ingrediente(conexion,id_ing[x]))
            input("")"""
        if (len(id_ing) == 0):
            try:
                pizzas = (id_pizza, id_ped)
                cursor.execute("insert into pedi_pizza(fk_pizza, fk_pedido) values (?, ?)", pizzas)
                conexion.commit()
            except: 
                print('def insert_pedi_pizza: Los datos no pudieron insertarse.')
        else:
            try:
                for x in range(0,len(id_ing)): 
                    pizzas = (id_ing[x], id_pizza, id_ped)
                    #print("Pizza: ",self.buscar_pizza(conexion,id_pizza)) 
                    #print("Pedido del cliente: ", self.buscar_cliente(conexion,id_ped))
                    #print("Ingredientes: ", self.buscar_ingrediente(conexion,id_ing[x]))
                    cursor.execute("insert into pedi_pizza(fk_ingrediente, fk_pizza, fk_pedido) values (?, ?, ?)", pizzas)
                    conexion.commit()
            except: 
                print('def insert_pedi_pizza: Los datos no pudieron insertarse.')
"""
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
"""