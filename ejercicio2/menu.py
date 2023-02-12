import os
import database as db

def iniciar():
    while True:
        os.system('cls') # cls en Windows
        print("===============")
        print(" NUMERO MÁGICO ")
        print("===============")
        print("[1] Funcionamiento ")
        print("[2] Ejecución ")
        print("[3] Cerrar ")
        print("===============")
        opcion = input("> ")
        os.system('cls') # cls en Windows

        if opcion == '1':
            # print("Mostrando el funcionamiento...\n")
            numeromag = db.numero_magico(0)
            os.system('cls')
            print(f"Este programa toma un número dado por el usuario comprendido entre el 1 y el 9 y usa el número magico {numeromag.numero_magico} y operaciones básicas para llegar a un resultado sorprendente")

        if opcion == '2':
            print("Entrando en el programa...\n")
            numeromag = db.numero_magico(db.comprobar_numero())
            os.system('cls')
            print(f"Tu número mágico resultante es el {numeromag.numero_final}")

        if opcion == '3':
            print("Saliendo...\n")

        break
    input("\nPresiona ENTER para salir...")