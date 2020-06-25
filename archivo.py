import os
from dao import DAO
from datetime import datetime
from pizza.pizzas import PizzaPersonal, PizzaMediana, PizzaFamiliar
from pizza.decoradores import Jamon, Champiñones, Pimenton, DobleQueso, Aceitunas, Pepperoni, Salchichon

"""
Clase File que se encarga de hacer operaciones sobre los archivos
"""

class File():
    def __init__(self):
        self.ruta = None
        self.pizzas = []

    """Funcion para verificar si ya existe la BD"""
    def search_db(self, name, os):
        if(os == 'Windows'):
            db = self.specific_os_search_db(name,'../') #Colocar ruta del proyecto, ahi deberia estar el archivo de la BD al ser creada
        elif(os == 'Linux'):
            db = self.specific_os_search_db(name,'../')#Colocar ruta del proyecto, ahi deberia estar el archivo de la BD al ser creada
        else:
            db = self.specific_os_search_db(name,'')
        if db == None:
            db = 'false'
        return db

    """Funcion para verificar si ya existe la BD"""       
    def specific_os_search_db(self,name,dir):
        for root, dirs, files in os.walk(dir):
            if name in files:
                print('encontrado')
                self.ruta = root + "/" + name
                return 'true'
    
    """Funcion para buscar el archivo de entrada con los pedidos"""
    def search(self, name, os):
        if(os == 'Windows'):
            self.specific_os_search(name,'C:/Users')
        elif(os == 'Linux'):
            self.specific_os_search(name,'/home/')
        else:
            self.specific_os_search(name,'')
    
    """Funcion que retorna la ruta donde se encuentra el archivo con los pedidos"""
    def specific_os_search(self,name,dir):
        for root, dirs, files in os.walk(dir):
            if name in files:
                self.ruta = root + "/" + name
                break
     
    """Guarda en un array todas las lineas del documento"""
    def set_wordlist(self):
        word_list = []
        with open(self.ruta) as lineas:
            for linea in lineas:
                word_list.append(linea)
        return(word_list)

    """Funcion para obtener la pizza y el cliente de las lineas que se extrajeron del documento"""
    def obtener_cliente_pizza(self, cli_fech):
        cliente = ""
        for x in cli_fech:
            if x != ";" and x != "\n":
                cliente += x
            if x == ";": break
        return cliente

    """Funcion para obtener la fecha de las lineas que se extrajeron del documento"""
    def obtener_fecha(self, cli_fech):
        i=0
        fecha = ""
        for x in cli_fech:
            if (i == 1 and x != "\n"):
                fecha += x
            if x == ";": i=1
        try:
            date_time_str = fecha
            date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y')
            return (str(date_time_obj))
        except:
            fecha = ""
            return fecha    
        
    """Funcion para obtener los ingredientes de las lineas que se extrajeron del documento"""
    def obtener_ingredientes(self, pizz_ing):
        i=0
        ing = ""
        ingredientes = []
        for x in pizz_ing:
            if (i == 1 and (x != "\n" and x != ";")):
                ing += x
            elif (i == 1 and (x == "\n" or x == ";")):
                ingredientes.append(ing)
                ing = ""
            if x == ";": i=1
        return ingredientes

    """Funcion para insertar cada pedido del archivo en la base de datos"""
    def insert_pedidos(self, word_list, conexion):
        i, error = 0, 0
        ing = []
        db = DAO()
        if ('COMIENZO_PEDIDO\n' in word_list and 'FIN_PEDIDO\n' in word_list):
            for r in word_list:
                if (i==1):
                    cli_fech = r
                    cli = self.obtener_cliente_pizza(cli_fech)
                    fech = self.obtener_fecha(cli_fech)
                    if (";" in cli_fech) and (cli != "") and (fech != ""): 
                        id_cli = db.insert_cliente(conexion,cli)
                        id_ped = db.insert_pedido(conexion,fech,id_cli)
                    else:
                        print("El formato de los pedidos es incorrecto.")
                        error = 1
                        break
                if 'personal' in r or 'mediana' in r or 'familiar' in r:
                    pizz_ing = r
                    pizz = self.obtener_cliente_pizza(pizz_ing)
                    ing = self.obtener_ingredientes(pizz_ing)
                    db.insert_pedi_pizza(conexion,id_ped,pizz,ing)
                if(r == 'COMIENZO_PEDIDO\n'): i=1
                else: i=0
        else:
            print("Este documento no posee pedidos o su formato es incorrecto.")

        if error != 1:
                    print("¡Archivo de pedidos procesado con éxito!")

    """Funcion que inicia las operaciones"""
    def start(self,arc,os,conn):
        self.search(arc,os)
        wl = self.set_wordlist()
        self.insert_pedidos(wl,conn)
