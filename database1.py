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
