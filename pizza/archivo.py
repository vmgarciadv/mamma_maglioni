import os
from pizzas import Pizza, PizzaPersonal, PizzaMediana, PizzaFamiliar
from decoradores import IngredientesDecorator, Jamon, Champiñones, Pimenton, DobleQueso, Aceitunas, Pepperoni, Salchichon

class File():
    def __init__(self):
        self.ruta = None
        self.pizzas = []
    
    def search(self, name):
        for root, dirs, files in os.walk('/home/'):
            if name in files:
                self.ruta = root + "/" + name

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

    def start(self):
        arc = input("Nombre del archivo de pedidos: ")
        self.search(arc)
        self.set_pizzas()
        self.get_pizzas()