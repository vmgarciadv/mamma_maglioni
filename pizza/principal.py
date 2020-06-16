from pizza import Pizza, PizzaPersonal, PizzaMediana, PizzaFamiliar
from decoradores import IngredientesDecorator, Jamon, Champiñones #, Pimenton, DobleQueso, Aceitunas, Pepperoni, Salchichon



pizza = PizzaFamiliar()
pizza = Jamon(pizza)
pizza = Champiñones(pizza)
print(pizza.informacion() + "y cuesto " +str(pizza.get_precio()))