from abc import ABC, abstractmethod #modulo ABC para clases abstractas
from pizza import Pizza

def overrides(interface_class): #esto es para que funcione el @override en python
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

"""clase AdicionalesDecorador. Decoradora principal del cual implementaran
los decoradores concretos"""

class AdicionalesDecorator(Pizza):
    
    def get_size(self):
        return self.size

class Jamon(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.5
        elif self.size == "Mediana":
            return self.precio + 1.75
        else:
            return self.precio + 2.00
    
    """
    def set_precio(self):
        if self.size == "Personal":
            self.precio += 1.5
    """
          
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con Jamon y cuesto " + str(self.get_precio())

class Champiñones(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.75
        elif self.size == "Mediana":
            return self.precio + 2.05
        else:
            return self.precio + 2.50
    
      
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con Champiñón y cuesto " + str(self.get_precio())

class Pimenton(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.5
        elif self.size == "Mediana":
            return self.precio + 1.75
        else:
            return self.precio + 2.00
    
      
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con Pimentón y cuesto " + str(self.get_precio())

class DobleQueso(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 0.80
        elif self.size == "Mediana":
            return self.precio + 1.30
        else:
            return self.precio + 1.70
    
      
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con doble queso y cuesto " + str(self.get_precio())

class Aceitunas(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.80
        elif self.size == "Mediana":
            return self.precio + 2.15
        else:
            return self.precio + 2.60
    
      
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con Aceitunas y cuesto " + str(self.get_precio())

class Pepperoni(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.25
        elif self.size == "Mediana":
            return self.precio + 1.70
        else:
            return self.precio + 1.90
    
      
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con Aceitunas y cuesto " + str(self.get_precio())

class Salchichon(AdicionalesDecorator):

    def __init__(self, pizza):
        Pizza.__init__(self, pizza.size, pizza.precio)

    def get_size(self):
        return self.size

    @overrides(AdicionalesDecorator)
    def get_precio(self):      
        if self.size == "Personal":
            return self.precio + 1.60
        elif self.size == "Mediana":
            return self.precio + 1.85
        else:
            return self.precio + 2.10
    
      
    @overrides(AdicionalesDecorator)
    def informacion(self):
        return self.get_size() + " con Salchichón y cuesto " + str(self.get_precio())