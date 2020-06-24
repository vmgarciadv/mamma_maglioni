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
    print('No existo')

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