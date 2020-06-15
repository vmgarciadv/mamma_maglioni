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
        return 1.5 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Jamon, "  

class Champiñones(IngredientesDecorator):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size)
        self.pizza = pizza

    def get_precio(self):
        return 1.75 + self.pizza.get_precio()

    def informacion(self):
        return self.pizza.informacion() + "Champiñones, "

"""
class Pimenton(IngredientesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(IngredientesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.5
        elif self.size == "Mediana":
            return self.precio + 1.75
        else:
            return self.precio + 2.00
    
      
    @overrides(IngredientesDecorator)
    def informacion(self):
        return self.get_size() + " con Pimentón y cuesto " + str(self.get_precio())

class DobleQueso(IngredientesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(IngredientesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 0.80
        elif self.size == "Mediana":
            return self.precio + 1.30
        else:
            return self.precio + 1.70
    
      
    @overrides(IngredientesDecorator)
    def informacion(self):
        return self.get_size() + " con doble queso y cuesto " + str(self.get_precio())

class Aceitunas(IngredientesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(IngredientesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.80
        elif self.size == "Mediana":
            return self.precio + 2.15
        else:
            return self.precio + 2.60
    
      
    @overrides(IngredientesDecorator)
    def informacion(self):
        return self.get_size() + " con Aceitunas y cuesto " + str(self.get_precio())

class Pepperoni(IngredientesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(IngredientesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.25
        elif self.size == "Mediana":
            return self.precio + 1.70
        else:
            return self.precio + 1.90
    
      
    @overrides(IngredientesDecorator)
    def informacion(self):
        return self.get_size() + " con Aceitunas y cuesto " + str(self.get_precio())

class Salchichon(IngredientesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(IngredientesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.60
        elif self.size == "Mediana":
            return self.precio + 1.85
        else:
            return self.precio + 2.10
    
      
    @overrides(IngredientesDecorator)
    def informacion(self):
        return self.get_size() + " con Salchichón y cuesto " + str(self.get_precio())
        """