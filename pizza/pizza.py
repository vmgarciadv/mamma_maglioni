from abc import ABC, abstractmethod #modulo ABC para clases abstractas

def overrides(interface_class): #esto es para que funcione el @override en python
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

"""Super clase Pizza"""

class Pizza(ABC):

    def __init__(self, size):
        self.size = size
        super().__init__()

    @abstractmethod
    def get_precio(self):
        pass

    def informacion(self):
        return "Soy una pizza " + self.size + " con: "

"""Hijas concretas"""

class PizzaPersonal(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Personal")

    def get_precio(self):
        return 10

class PizzaMediana(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Mediana")

    def get_precio(self):
        return 15

class PizzaFamiliar(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Familiar")

    def get_precio(self):
        return 20