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
    if (bool_db == 'false'): conn.creando_db()
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
        print('     3.-Ejemplo del formato de los archivos de los pedidos.')
        print('     4.-Salir')
        print('\n')
        opcion = input('indique que desea realizar: ')
        if(opcion == '1'):
            procesar_archivo(controlArchivos,sistema, conexion)
            input("Presiona Enter para volver...")
        elif(opcion == '2'):
            generar_reporte()
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
    try:
        controlArchivos.start(archivo, sistema, conexion)
    except:
        print("\nEl archivo indicado no puede ser procesado.\n")

    
def generar_reporte():
    clear()
    conexion = sqlite3.connect('mamma_maglioni.db') #me conecto a la BD
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(distinct fecha) FROM pedido") #busco cuántas fechas hay en el archivo, de esa forma sabré hasta donde el archivo debe leer 
    fecha = cursor.fetchone()
    cursor.execute("SELECT p.size, COUNT(pp.fk_pizza), SUM(p.precio) FROM pizza p, pedi_pizza pp, pedido pe where pp.fk_pizza = p.id and pp.fk_pedido = pe.id GROUP BY pp.fk_pizza;")
    resultado = cursor.fetchall()
    contador =  1
    while contador <= fecha[0]:   #contador debe ser menor que el numero de fechas  en caso de pedidos1.pz menor a 2 (5/06 y 6/06)
        reporte = open("../mamma_maglioni/reporte.txt", "w")
        cursor.execute("SELECT distinct fecha FROM pedido")
        fechas = cursor.fetchall()

        for fechita in fechas: #por cada fecha escribo en el archivo su pedido
            reporte.write("Fecha " + ''.join(fechita) + os.linesep) #os.linesep es para saltar de linea
            reporte.write(os.linesep)
            reporte.write("Venta total " + os.linesep)
            reporte.write(os.linesep)
            reporte.write("Ventas por pizza (sin incluir adicionales):" + os.linesep)
            reporte.write("Tamaño               Unidades                Monto UMs" + os.linesep)

            #aqui van todas las consultas por fecha

            reporte.write(os.linesep)
        contador  += 1
        reporte.close()


    input("Presiona Enter para continuar...")

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