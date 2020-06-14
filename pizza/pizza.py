from abc import ABC, abstractmethod #modulo ABC para clases abstractas

def overrides(interface_class): #esto es para que funcione el @override en python
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

"""Super clase Pizza"""

class Pizza(ABC):

    def __init__(self, size, precio):
        self.size = size
        self.precio = precio

    def get_size(self):
        return self.size

    def get_precio(self):
        return self.precio

    def informacion(self):
        return "Soy una pizza " + self.get_size()

"""Hijas concretas"""

class PizzaPersonal(Pizza):

    def __init__(self):
        size = "Personal"
        precio = 10
        Pizza.__init__(self, size, precio)
        

class PizzaMediana(Pizza):

    def __init__(self):
        size = "Mediana"
        precio = 15
        Pizza.__init__(self, size, precio)



class PizzaFamiliar(Pizza):

    def __init__(self):
        size = "Familiar"
        precio = 20
        Pizza.__init__(self, size, precio)


