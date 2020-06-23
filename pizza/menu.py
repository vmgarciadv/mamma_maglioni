import platform
import os
from dao import DAO
from archivo import File
from termcolor import colored, cprint

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
    conexion = conn.create_connection()
    repetir = True
    while (repetir):
        clear()
        print(f'Bienvenido al sistema de control de la pizzeria', colored(local,'yellow'))
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
            print(colored('Esa no es una opcion valida, por favor intentelo nuevamente','red'))
            input("Presiona Enter para continuar...")

def procesar_archivo(controlArchivos,sistema,conexion):
    clear()
    archivo = input('Por favor indique el nombre del archivo: ')
    controlArchivos.start(archivo, sistema, conexion)

def generar_reporte():
    print('No existo')

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()