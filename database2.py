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

