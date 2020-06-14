from pizza import Pizza, PizzaPersonal, PizzaMediana, PizzaFamiliar
from decoradores import AdicionalesDecorator, Jamon, Champiñones, Pimenton, DobleQueso, Aceitunas, Pepperoni, Salchichon

pizza = PizzaPersonal()
extra = Jamon(pizza)

print(extra.informacion())

pizza = PizzaMediana()
extra = Champiñones(pizza)

print(extra.informacion())

pizza = PizzaFamiliar()
extra = Aceitunas(pizza)

print(extra.informacion())