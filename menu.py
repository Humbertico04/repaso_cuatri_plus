import database1 as db1
import database2 as db2
import database3 as db3
import database4 as db4
import descomposicion as db5
import database6 as db6
import database7 as db7
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("===================")
        print(" EJERCICIOS TEMA 1 ")
        print("===================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2 ")
        print("[3] Ejercicio 3 ")
        print("[4] Ejercicio 4 ")
        print("[5] Ejercicio 5 ")
        print("[6] Ejercicio 6 ")
        print("[7] Ejercicio 7 ")
        print("[8] Cerrar ")
        print("===================")
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Entrando al ejercicio 1...\n")
            alumno = db1.obtener_datos(helpers.string_contiene(helpers.leer_texto(mensaje="Porfavor introduzca el string corrupto: "), "," and " "))
            helpers.limpiar_pantalla()
            print(alumno)

        elif opcion == '2':
            print("Entrando al ejercicio 2...\n")
            numeromag = db2.numero_magico(helpers.comprobar_numero(1, 9))
            helpers.limpiar_pantalla()
            print(f"Tu número mágico resultante es el {numeromag.numero_final}")

        elif opcion == '3':
            print("Entrando al ejercicio 3...\n")
            lista_1 = helpers.comprobar_lista("Lista 1")
            print("Lista 1 creada correctamente\n")
            lista_2 = helpers.comprobar_lista("Lista 2")
            print(lista_1, lista_2)
            input("Lista 2 creada correctamente\n>")
            print(lista_1, lista_2)
            lista_nueva = db3.listas.comparar_listas(lista_1, lista_2)
            lista_final = db3.listas.elementos_repetidos(lista_nueva)
            helpers.limpiar_pantalla()
            print(f"Tu lista final resultante: {lista_final}")

        elif opcion == '4':
            print("Entrando al ejercicio 4...\n")
            tareas = []
            tarea = db4.tareas(helpers.leer_texto(mensaje="Porfavor introduzca la tarea que desea realizar"),
                               helpers.comprobar_numero(mensaje="Introduce la prioridad de la tarea:\n>"))
            tareas.append((tarea.prioridad, tarea.tarea.capitalize()))
            helpers.limpiar_pantalla()
            while helpers.pedir_entrada_si_o_no("Desea añadir una tarea?: \n>") == True:
                tarea = db4.tareas(helpers.leer_texto(mensaje="Porfavor introduzca la tarea que desea realizar"),
                               helpers.comprobar_numero(mensaje="Introduce la prioridad de la tarea:\n>"))
                tareas.append((tarea.prioridad, tarea.tarea.capitalize()))
                helpers.limpiar_pantalla()
            helpers.limpiar_pantalla()
            print("Tareas ordenadas por prioridad: \n")
            db4.tareas.ordenar_tareas(tareas)


        elif opcion == '5':
            print("Entrando al ejercicio 5...\n")
            desc = db5.descomposicion(helpers.comprobar_numero(max=float('inf')))
            helpers.limpiar_pantalla()
            print(f"Su descomposicion es: {desc}")

        elif opcion == '6':
            print("Entrando al ejercicio 6...\n")
            pares, impares = db6.separar(helpers.comprobar_lista())
            helpers.limpiar_pantalla()
            print("Lista de los pares: {}\nLista de los impares: {}".format(pares, impares))

        elif opcion == '7':
            print("Entrando al ejercicio 7...\n")
            lista = db7.agregar_una_vez(helpers.comprobar_lista(), input("\nIntroduce el elemento que desee añadir: \n>"))
            while helpers.pedir_entrada_si_o_no("Desea añadir otro elemento?: \n>") == True:
                lista = db7.agregar_una_vez(lista, input("\nIntroduce el elemento que desee añadir: \n>"))
            helpers.limpiar_pantalla()
            print("Lista final: {}".format(lista))

        if opcion == '8':
            print("Saliendo...")
            break

        input("\nPresiona ENTER para salir...")