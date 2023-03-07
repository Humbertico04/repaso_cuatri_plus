import os
import database1 as db1
import database2 as db2
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("===================")
        print(" EJERCICIOS TEMA 1 ")
        print("===================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2 ")
        # print("[3] Ejercicio 3 ")
        # print("[4] Ejercicio 4 ")
        # print("[5] Ejercicio 5 ")
        # print("[6] Ejercicio 6 ")
        # print("[7] Ejercicio 7 ")
        print("[8] Cerrar ")
        print("===================")
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Entrando al ejercicio 1...\n")
            alumno = db1.obtener_datos(input("Porfavor introduzca el string corrupto: "))
            helpers.limpiar_pantalla()
            print(alumno)

        if opcion == '2':
            print("Entrando en el programa...\n")
            numeromag = db2.numero_magico(helpers.comprobar_numero())
            helpers.limpiar_pantalla()
            print(f"Tu número mágico resultante es el {numeromag.numero_final}")

        if opcion == '8':
            print("Saliendo...")
            break

        input("\nPresiona ENTER para salir...")