import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def string_contiene(string, caracter):
    if caracter in string:
        return string
    else:
        print("Formato incorrecto")
        string_contiene(leer_texto(), caracter)

def comprobar_numero(min=0, max=100):
    while True:
        try:
            numero_usuario = int(input("Introduce un numero entre {} y {}: \n>".format(min, max)))
            if numero_usuario >= min and numero_usuario <= max:
                return numero_usuario
            else:
                limpiar_pantalla()
                print("El numero introducido no es correcto")
        except ValueError:
            limpiar_pantalla()
            print("Porfavor asegurese de que cumpla con las condiciones")

def comprobar_lista(mensaje=None):
    print(mensaje) if mensaje else None
    try:
        lista = eval(input("Introduce una lista: \n>"))
        if not isinstance(lista, list):
            limpiar_pantalla()
            print("Formato incorrecto")
            comprobar_lista()
        else:
            return lista
    except (SyntaxError, ValueError, NameError):
        limpiar_pantalla()
        print("Formato incorrecto\n")
        comprobar_lista()

def pedir_entrada_si_o_no(invite):
    SI = ("s", "si", "y", "yes", "1")
    """Por defecto, toda respuesta no comprendida será NO"""
    try:
        return input(invite).lower() in SI
    except:
        return False
    