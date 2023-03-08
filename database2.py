# Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

# Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
# Multiplica el numero_usuario por 9 en sí mismo
# Multiplica el numero_magico por el numero_usuario en sí mismo
# Finalmente muestra el valor final del numero_magico por pantalla

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

