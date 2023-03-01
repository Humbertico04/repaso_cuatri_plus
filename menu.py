import os
import database1 as db1

def iniciar():
    while True:
        os.system('cls') # cls en Windows
        print("===================")
        print(" EJERCICIOS TEMA 1 ")
        print("===================")
        print("[1] Ejercicio 1 ")
        # print("[2] Ejercicio 2 ")
        # print("[3] Ejercicio 3 ")
        # print("[4] Ejercicio 4 ")
        # print("[5] Ejercicio 5 ")
        # print("[6] Ejercicio 6 ")
        # print("[7] Ejercicio 7 ")
        print("[8] Salir ")
        print("===================")
        opcion = input("> ")
        os.system('cls') # cls en Windows

        if opcion == '1':
            print("Entrando al ejercicio 1...\n")
            alumno = db1.obtener_datos(input("Porfavor introduzca el string corrupto: "))
            os.system('cls')
            print(alumno)

        if opcion == '2':
            print("Mostrando su nombre...\n")
            alumno = db1.obtener_datos(input("Introduce el string corrupto: "))
            os.system('cls')
            print("Nombre:", alumno.nombre)

        if opcion == '8':
            print("Saliendo...\n")

        break
    input("\nPresiona ENTER para salir...")