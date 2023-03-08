# Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

# Sugerencia

# Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.

class tareas:
    def __init__(self, tarea, prioridad):
        self.tarea = tarea
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.tarea}"

    @staticmethod
    def ordenar_tareas(lista_tareas):
        # lista_tareas.sort(key=lambda tarea: tarea.prioridad)
        lista_tareas.sort()
        for tarea in lista_tareas:
            print(tarea[1])
        return lista_tareas

tarea = [
    (1, 'Hacer compras'),
    (3, 'Ir al gimnasio'),
    (2, 'Llamar al médico'),
    (4, 'Limpiar la casa')
]

print(tareas.ordenar_tareas(tarea))


