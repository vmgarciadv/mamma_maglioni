from archivo import File

ejecucion = File()
ejecucion.start()


#precio = 0
#pedido = open ('../pedidos1.pz','r') #archivo almacenado en home

"""se encarga de buscar todas las pizzas personales
def Personal(precio): 

    palabra = 'personal'
    ocurrencias = []
 

    with open('/home/victor/pedidos1.pz') as lineas:
        for linea in lineas:
            if palabra in linea:
                ocurrencias.append(linea) #guarda todas las pizzas personales
    print("Pedidos pizzas personales: ", ocurrencias)

    for pedido in ocurrencias:
        if pedido == 'personal\n': #se encarga de despachar una pizza margarita si la hay
            pizza = PizzaPersonal()
            print(pizza.informacion() + "y cuesto " +str(pizza.get_precio()))

        if 'personal;' in pedido: #verifica que haya una pizza personal con mas de un ingrediente
            pizza = PizzaPersonal()
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
    print("Total venta personal  = ", precio)

def Mediana(precio): 

    print()
    palabra = 'mediana'
    ocurrencias = []
    with open('/home/victor/pedidos1.pz') as lineas:
        for linea in lineas:
            if palabra in linea:
                ocurrencias.append(linea) #guarda todas las pizzas medianas
    print("Pedidos pizzas medianas: ", ocurrencias)

    for pedido in ocurrencias:
        if pedido == 'mediana\n': #se encarga de despachar una pizza margarita mediana si la hay
            pizza = PizzaMediana()
            print(pizza.informacion() + "y cuesto " +str(pizza.get_precio())) 

        if 'mediana;' in pedido: #verifica que haya una pizza mediana con mas de un ingrediente
            pizza = PizzaMediana()
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
    print("Total venta mediana  = ", precio)


def Familiar(precio): 

    print()
    palabra = 'familiar'
    ocurrencias = []
    with open('/home/victor/pedidos1.pz') as lineas:
        for linea in lineas:
            if palabra in linea:
                ocurrencias.append(linea) #guarda todas las pizzas familiares
    print("Pedidos pizzas familiares: ", ocurrencias)

    for pedido in ocurrencias:
        if pedido == 'familiar\n': #se encarga de despachar una pizza margarita familiar si la hay
            pizza = PizzaFamiliar()
            print(pizza.informacion() + "y cuesto " +str(pizza.get_precio())) 

        if 'familiar;' in pedido: #verifica que haya una pizza familiar con mas de un ingrediente
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
    print("Total venta familiar  = ", precio)

Personal(precio)
Mediana(precio)
Familiar(precio)

#pizza = PizzaPersonal()
pizza = Jamon(pizza)
pizza = Champiñones(pizza)
pizza = Salchichon(pizza)
#print(pizza.informacion() + "y cuesto " +str(pizza.get_precio()))
"""