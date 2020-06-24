import platform
import os
from dao import DAO
from archivo import File
from database.connection import *

def main():
    local = 'Mamma Maglioni'
    controlArchivos = File()
    sistema = platform.system()
    #controlArchivos.start('pedidos1.pz',sistema)
    clear()
    menu_principal(local,controlArchivos,sistema)
    pass

def menu_principal(local,controlArchivos,sistema):
    conn = DAO()
    conexion = conn.create_connection() #Llama a la funcion para crear la conexion con la BD
    repetir = True
    while (repetir):
        clear()
        print(f'Bienvenido al sistema de control de la pizzeria')
        print('Por favor indique que desea realizar:')
        print('     1.-Procesar archivo de pedidos')
        print('     2.-Generar resumen de ventas')
        print('     3.-Salir')
        print('\n')
        opcion = input('indique que desea realizar: ')
        if(opcion == '1'):
            procesar_archivo(controlArchivos,sistema, conexion)
            input("Presiona Enter para continuar...")
        elif(opcion == '2'):
            generar_reporte()
        elif(opcion == '3'):
            repetir = False
            conn.cerrar_connection(conexion)
        else:
            clear()
            print('Esa no es una opcion valida, por favor intentelo nuevamente')
            input("Presiona Enter para continuar...")

def procesar_archivo(controlArchivos,sistema,conexion):
    clear()
    archivo = input('Por favor indique el nombre del archivo: ')
    controlArchivos.start(archivo, sistema, conexion)

    
def generar_reporte():
    clear()
    conexion = sqlite3.connect('mamma_maglioni.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(distinct fecha) FROM pedido")
    fecha = cursor.fetchone()
    contador =  1
    while contador <= fecha[0]:     
        reporte = open("../mamma_maglioni/reporte.txt", "w")
        cursor.execute("SELECT distinct fecha FROM pedido")
        fechas = cursor.fetchall()
        for fechita in fechas:
            reporte.write("Fecha " + ''.join(fechita) + os.linesep)
            reporte.write("Venta total" + os.linesep)
            reporte.write("Ventas por pizza (sin incluir adicionales):" + os.linesep)
        contador  = 3
        reporte.close()


    input("Presiona Enter para continuar...")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()