import platform
import os
from dao import DAO
from archivo import File

def main():
    local = 'Mamma Maglioni'
    controlArchivos = File()
    sistema = platform.system()
    #controlArchivos.start('pedidos1.pz',sistema)
    clear()
    db = 'mamma_maglioni.db'
    bool_db = controlArchivos.search_db(db,sistema)
    conn = DAO()
    if (bool_db == 'false'): 
        conn.creando_db()
    conexion = conn.create_connection() #Llama a la funcion para crear la conexion con l
    menu_principal(local,controlArchivos,sistema,conexion)
    pass

def menu_principal(local,controlArchivos,sistema,conexion):
    conn = DAO()
    repetir = True
    while (repetir):
        clear()
        print(f'Bienvenido al sistema de control de la pizzeria\n')
        print('Por favor indique que desea realizar:')
        print('     1.-Procesar archivo de pedidos')
        print('     2.-Generar resumen de ventas')
        print('     3.-Ejemplo del formato del archivo de los pedidos.')
        print('     4.-Salir')
        print('\n')
        opcion = input('indique que desea realizar: ')
        if(opcion == '1'):
            procesar_archivo(controlArchivos,sistema, conexion)
            input("Presiona Enter para volver...")
        elif(opcion == '2'):
            generar_reporte(conexion)
        elif(opcion == '3'):
            ejemplo_archivo()
            input("Presiona Enter para volver...")
        elif(opcion == '4'):
            repetir = False
            conn.cerrar_connection(conexion)
        else:
            clear()
            print('Esa no es una opcion valida, por favor intentelo nuevamente')
            input("Presiona Enter para volver...")

def procesar_archivo(controlArchivos,sistema,conexion):
    clear()
    archivo = input('Por favor indique el nombre del archivo: ')
    if(".pz" in archivo):
        try:
            controlArchivos.start(archivo, sistema, conexion)
        except:
            print("\nEl archivo indicado no puede ser procesado.\n")
    else:
        print("\nLa extension del archivo no corresponde.\n")

    
def generar_reporte(conexion):
    clear()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(distinct fecha) FROM pedido") #busco cuántas fechas hay en el archivo, de esa forma sabré hasta donde el archivo debe leer 
    fecha = cursor.fetchone()##2
    cursor.execute("SELECT p.size, COUNT(pp.fk_pizza), SUM(p.precio) FROM pizza p, pedi_pizza pp, pedido pe where pp.fk_pizza = p.id and pp.fk_pedido = pe.id GROUP BY pp.fk_pizza;")
    resultado = cursor.fetchall()
    contador =  1
    ##while contador <= fecha[0]:   #contador debe ser menor que el numero de fechas  en caso de pedidos1.pz menor a 2 (5/06 y 6/06)
    reporte = open("../mamma_maglioni/reporte.txt", "w")
    cursor.execute("SELECT distinct fecha FROM pedido")
    fechas = cursor.fetchall()
    for fechita in fechas: #por cada fecha escribo en el archivo su pedido
        reporte.write("=======================================================\n")
        reporte.write("Fecha " + ''.join(fechita) + "\n") #os.linesep es para saltar de linea
        reporte.write("\n")
        cursor_f = conexion.cursor()
        cursor_f.execute(f"""select SUM(i.precio) 
                             from pedi_ing pi, ingrediente i, (select id from pedido where fecha = '{fechita[0]}') as x 
                             where pi.fk_pedido = x.id and pi.fk_ingrediente = i.id""")
        valor1 = cursor_f.fetchone()
        cursor_f.execute(f"""select SUM(p.precio) 
                            from pedi_pizza pp, pizza p, (select id from pedido where fecha = '{fechita[0]}') as x
                            where pp.fk_pedido = x.id and pp.fk_pizza = p.id""")
        valor2 = cursor_f.fetchone()
        if (valor1[0] is not None):
            valor_total = valor1[0] + valor2[0]
            reporte.write(f"Venta total: {valor_total} UMs \n")
        else:
            reporte.write(f"Venta total: {valor2[0]} UMs \n")
        reporte.write("\n")
        reporte.write("Ventas por pizza (sin incluir adicionales):" + "\n")
        reporte.write("\n")
        reporte.write("Tamaño               Unidades                Monto UMs" + "\n")
        reporte.write("\n")
        cursor_f.execute(f"""select p.size, pe.fecha, count(p.size), p.precio
                            from pizza p, pedi_pizza pepi, pedido pe
                            where p.id = pepi.fk_pizza and pepi.fk_pedido = pe.id and pe.fecha = '{fechita[0]}'
                            group by p.size, pe.fecha;""")
        valores = cursor_f.fetchall()

        for valor in valores:
            if valor[0] != "mediana":
                reporte.write(f"{valor[0]}             ||{valor[2]}                     ||{valor[3]}\n")
            else:
                reporte.write(f"{valor[0]}              ||{valor[2]}                     ||{valor[3]}\n")
                
        reporte.write(os.linesep)
        cursor_f.execute(f"""select i.nombre, pe.fecha, count(i.nombre), i.precio*count(i.nombre)
                             from ingrediente i, pedi_ing pepi, pedido pe
                             where i.id = pepi.fk_ingrediente and pepi.fk_pedido = pe.id and pe.fecha = '{fechita[0]}'
                             group by i.nombre, pe.fecha;""")
        valores = cursor_f.fetchall()
        if(valores):
            reporte.write("Ventas por Ingredientes:\n")
            reporte.write("\n")
            reporte.write("Ingredientes               Unidades                Monto UMs" + "\n")
            reporte.write("\n")
            ingredientes = normalizar_ingredientes(valores)
            for ingrediente in ingredientes:
                if(ingrediente[0] > 0):
                    reporte.write(f"{ingrediente[2]}                ||{ingrediente[0]}       ||{ingrediente[1]}\n")
        else:
            reporte.write("No se registraron ventas con ingredientes \n")
            reporte.write("\n")
        #aqui van todas las consultas por fecha
        reporte.write(os.linesep)
        #contador  += 1
    reporte.close()
    input("Presiona Enter para continuar...")

def normalizar_ingredientes(lista):
    jamon = [0,0,'jamon']
    champinones = [0,0,'champinones']
    pimenton = [0,0,'pimenton']
    doble = [0,0,'doble queso']
    aceitunas = [0,0,'aceitunas']
    pepperoni = [0,0,'pepperoni']
    salchichon = [0,0,'salchichon']
    for elemento in lista:
        if('jamon' in elemento[0]):
            jamon[0] += elemento[2]
            jamon[1] += elemento[3]
        elif('champinones' in elemento[0]):
            champinones[0] += elemento[2]
            champinones[1] += elemento[3]
        elif('pimenton' in elemento[0]):
            pimenton[0] += elemento[2]
            pimenton[1] += elemento[3]
        elif('doble queso' in elemento[0]):
            doble[0] += elemento[2]
            doble[1] += elemento[3]
        elif('aceitunas' in elemento[0]):
            aceitunas[0] += elemento[2]
            aceitunas[1] += elemento[3]
        elif('pepperoni' in elemento[0]):
            pepperoni[0] += elemento[2]
            pepperoni[1] += elemento[3]
        else:#salchichon 
            salchichon[0] += elemento[2]
            salchichon[1] +=elemento[3]  
    return [jamon,champinones,pimenton,doble,aceitunas,pepperoni,salchichon]              
    

def ejemplo_archivo():
    clear()
    print("""COMIENZO_PEDIDO
                Rosa Quiñones;05/06/2020
                personal
                FIN_PEDIDO
                COMIENZO_PEDIDO
                Luis Gómez;06/06/2020
                personal;champiñones
                FIN_PEDIDO
                COMIENZO_PEDIDO
                María Valdéz;06/06/2020
                mediana;champiñones;jamón;pimentón
                familiar;doble queso;aceitunas;pepperoni
                familiar;champiñones;pimentón;aceitunas
                FIN_PEDIDO\n""")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()