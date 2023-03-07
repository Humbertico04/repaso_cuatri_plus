import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def pedir_numero(string):
    return input(string)

def comprobar_numero():
    while True:
        try:
            numero_usuario = int(pedir_numero("Introduce un numero entre 1 y 9: "))
            if numero_usuario >= 1 and numero_usuario <= 9:
                return numero_usuario
            else:
                limpiar_pantalla()
                print("El numero introducido no es correcto")
        except ValueError:
            limpiar_pantalla()
            print("Porfavor asegurese de que cumpla con las condiciones")