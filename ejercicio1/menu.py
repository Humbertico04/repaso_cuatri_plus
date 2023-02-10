import os
import database as db

def iniciar():
    while True:
        os.system('cls') # cls en Windows
        print("============================")
        print(" BIENVENIDO AL DESCORRUPTOR ")
        print("============================")
        print("[1] Mostrar la calificación del alumno ")
        print("[2] Mostrar solo el nombre del alumno ")
        print("[3] Mostrar solo el apellido del alumno ")
        print("[4] Cerrar el descorruptor ")
        print("============================")
        opcion = input("> ")
        os.system('cls') # cls en Windows

        if opcion == '1':
            print("Mostrando su calificación...\n")
            alumno = db.obtener_datos(input("Introduce el string corrupto: "))
            os.system('cls')
            print(alumno)

        if opcion == '2':
            print("Mostrando su nombre...\n")
            alumno = db.obtener_datos(input("Introduce el string corrupto: "))
            os.system('cls')
            print("Nombre:", alumno.nombre)

        if opcion == '3':
            print("Mostrando su apellido...\n")
            alumno = db.obtener_datos(input("Introduce el string corrupto: "))
            os.system('cls')
            print("Apellido:", alumno.apellido)

        if opcion == '4':
            print("Saliendo...\n")

        break
    input("\nPresiona ENTER para salir...")