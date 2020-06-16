from abc import ABC, abstractmethod #modulo ABC para clases abstractas
from pizza import Pizza

def overrides(interface_class): #esto es para que funcione el @override en python
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

"""clase AdicionalesDecorador. Decoradora principal del cual implementaran
los decoradores concretos"""

class IngredientesDecorator(Pizza):
    @abstractmethod
    def get_precio(self):
        pass

    @abstractmethod
    def informacion(self):
        pass

class Jamon(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza
    
    def get_precio(self):
        if self.size == "Personal":
            return 1.5 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 1.75 + self.pizza.get_precio()
        else:
            return 2.00 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Jamon, "  

class Champiñones(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        if self.size == "Personal":
            return 1.75 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 2.05 + self.pizza.get_precio()
        else:
            return 2.50 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Champiñones, "

class Pimenton(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        if self.size == "Personal":
            return 1.5 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 1.75 + self.pizza.get_precio()
        else:
            return 2.00 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Pimenton, "

class DobleQueso(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        if self.size == "Personal":
            return 0.80 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 1.30 + self.pizza.get_precio()
        else:
            return 1.70 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Doble Queso, "

class Aceitunas(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        if self.size == "Personal":
            return 1.80 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 2.15 + self.pizza.get_precio()
        else:
            return 2.60 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Aceitunas, "

class Pepperoni(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        if self.size == "Personal":
            return 1.25 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 1.70 + self.pizza.get_precio()
        else:
            return 1.90 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Pepperoni, "

class Salchichon(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        if self.size == "Personal":
            return 1.60 + self.pizza.get_precio()
        elif self.size == "Mediana":
            return 1.85 + self.pizza.get_precio()
        else:
            return 2.10 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Salchichon, "