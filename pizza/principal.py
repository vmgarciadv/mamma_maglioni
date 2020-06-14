from pizza import Pizza, PizzaPersonal, PizzaMediana, PizzaFamiliar
from decoradores import AdicionalesDecorator, Jamon

pizza = PizzaPersonal()
extra = Jamon(pizza)

print(extra.informacion())