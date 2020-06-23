import os
from dao import DAO
from datetime import datetime
from pizzas import Pizza, PizzaPersonal, PizzaMediana, PizzaFamiliar
from decoradores import IngredientesDecorator, Jamon, Champiñones, Pimenton, DobleQueso, Aceitunas, Pepperoni, Salchichon

class File():
    def __init__(self):
        self.ruta = None
        self.pizzas = []
    
    def search(self, name, os):
        if(os == 'Windows'):
            self.specific_os_search(name,'C:/Users/Daren/Documents')
        elif(os == 'Linux'):
            self.specific_os_search(name,'/home/')
        else:
            self.specific_os_search(name,'')
    
    def specific_os_search(self,name,dir):
        for root, dirs, files in os.walk(dir):
            if name in files:
                self.ruta = root + "/" + name
                break
     
    #Cuarda en un array todas las lineas del documento.
    def set_wordlist(self):
        word_list = []
        with open(self.ruta) as lineas:
            for linea in lineas:
                word_list.append(linea)
        return(word_list)
    #Funciona para obtener la pizza y el cliente de las lineas que se extrajeron del documento
    def obtener_cliente_pizza(self, cli_fech):
        cliente = ""
        for x in cli_fech:
            if x != ";" and x != "\n":
                cliente += x
            if x == ";": break
        return cliente

    def obtener_fecha(self, cli_fech):
        i=0
        fecha = ""
        for x in cli_fech:
            if (i == 1 and x != "\n"):
                fecha += x
            if x == ";": i=1
        date_time_str = fecha
        date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y')
        return (str(date_time_obj))

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

    #Para insertar cada pedido del archivo en la base de datos.
    def insert_pedidos(self, word_list, conexion):
        i=0
        ing = []
        db = DAO()
        for r in word_list:
            if (i==1):
                cli_fech = r
                cli = self.obtener_cliente_pizza(cli_fech)
                fech = self.obtener_fecha(cli_fech)
                id_cli = db.insert_cliente(conexion,cli)
                id_ped = db.insert_pedido(conexion,fech,id_cli)
            if 'personal' in r or 'mediana' in r or 'familiar' in r:
                pizz_ing = r
                pizz = self.obtener_cliente_pizza(pizz_ing)
                ing = self.obtener_ingredientes(pizz_ing)
                db.insert_pedi_pizza(conexion,id_ped,pizz,ing)
            if(r == 'COMIENZO_PEDIDO\n'): i=1
            else: i=0
        print("\nRegistrado los pedidos en la base de datos.\n")
        
    def set_pizzas(self):
        with open(self.ruta) as lineas:
            for linea in lineas:
                if 'personal' in linea or 'mediana' in linea or 'familiar' in linea:
                    self.pizzas.append(linea)
        print('Pedidos pizzas personales: ', self.pizzas)

    def get_pizzas(self):
        precio = 0

        for pedido in self.pizzas:
            if pedido == 'personal\n' or 'personal;' in pedido:
                pizza = PizzaPersonal()
            elif pedido == 'mediana\n' or 'mediana;' in pedido:
                pizza = PizzaMediana()
            else:
                pizza = PizzaFamiliar()

            if 'jamón' in pedido or 'jamon' in pedido:
                pizza = Jamon(pizza)
            if 'champiñones' in pedido:
                pizza = Champiñones(pizza)
            if 'pimentón' in pedido or 'pimenton' in pedido:
                pizza = Pimenton(pizza)
            if 'doble queso' in pedido:
                pizza = DobleQueso(pizza)
            if 'aceitunas' in pedido:
                pizza = Aceitunas(pizza)
            if 'pepperoni' in pedido:
                pizza = Pepperoni(pizza)
            if 'salchichon' in pedido:
                pizza = Salchichon(pizza)
            
            print(pizza.informacion() + "y cuesto " +str(pizza.get_precio())) #esto al final no tiene porque mostrarse
            precio += pizza.get_precio()
        print("Total ventas  = ", precio)

    def start(self,arc,os,conn):
        #arc = input("Nombre del archivo de pedidos: ")
        self.search(arc,os)
        wl = self.set_wordlist()
        self.insert_pedidos(wl,conn)
        self.set_pizzas()
        self.get_pizzas()