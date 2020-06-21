import platform
import os
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
    repetir = True
    while (repetir):
        print(f'Bienvenido al sistema de control de la pizzeria', colored(local,'yellow'))
        print('Por favor indique que desea realizar:')
        print('     1.-Procesar archivo de pedidos')
        print('     2.-Generar resumen de ventas')
        print('     3.-Salir')
        print('\n')
        opcion = input('indique que desea realizar: ')
        if(opcion == '1'):
            procesar_archivo(controlArchivos,sistema)
        if(opcion == '2'):
            generar_reporte()
        if(opcion == '3'):
            repetir = False
        else:
            clear()
            print(colored('Esa no es una opcion valida, por favor intentelo nuevamente','red'))

def procesar_archivo(controlArchivos,sistema):
    clear()
    archivo = input('Por favor indique el nombre del archivo: ')
    controlArchivos.start(archivo, sistema)

def generar_reporte():
    print('No existo')

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()