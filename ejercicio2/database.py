import os

class NumeroMagico:
        def __init__(self, numero_magico, numero_usuario, numero_final):
            self.numero_magico = numero_magico
            self.numero_usuario = numero_usuario
            self.numero_final = numero_final
    
        def __str__(self):
            return f"El numero magico es: {self.numero_final}"

def numero_magico(numero_usuario):
    numero_magico = 12345679
    numero_final = 9*numero_usuario*numero_magico
    return NumeroMagico(numero_magico, numero_usuario, numero_final)

def comprobar_numero():
    while True:
        try:
            numero_usuario = int(pedir_numero("Introduce un numero entre 1 y 9: "))
            if numero_usuario >= 1 and numero_usuario <= 9:
                return numero_usuario
            else:
                os.system('cls')
                print("El numero introducido no es correcto")
        except ValueError:
            os.system('cls')
            print("Porfavor asegurese de que cumpla con las condiciones")

def pedir_numero(string):
    return input(string)
