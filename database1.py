# Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

# Nombre Apellido ha sacado un Nota de nota.

# Ayuda

# Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

# cadena = "zeréP nauJ,01"

class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

    def __str__(self):
        return f"{self.nombre} {self.apellido} ha sacado un {self.nota} de nota."

    def to_dict(self):
        return {'nombre': self.nombre, 'apellido': self.apellido, 'nota': self.nota}


def obtener_datos(cadena):
    nota, nom_ape=cadena[::-1].split(",")
    nombre, apellido = nom_ape.split(" ")
    return Alumno(nombre, apellido, nota)
