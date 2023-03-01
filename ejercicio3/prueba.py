import timeit

def elementos_repetidos(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento in lista_nueva:
            continue
        else:
            lista_nueva.append(elemento)
    return lista_nueva

def comparar_listas(lista_1, lista_2):
    lista_nueva = []
    for elemento in lista_1:
        if elemento in lista_2:
            lista_nueva.append(elemento)
    return lista_nueva

def lista_3(lista_1, lista_2):
    lista_nueva = []
    for elemento in lista_1:
        if elemento in lista_2:
            lista_nueva.append(elemento)
    return lista_nueva

def lista_4(lista_1, lista_2):
    lista_nueva = []
    for elemento in lista_1:
        if elemento not in lista_nueva and elemento in lista_2:
            lista_nueva.append(elemento)
    return lista_nueva

def lista_5(lista_1, lista_2):
    lista_nueva = []
    for elemento in lista_1:
        if elemento in lista_2 and elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a','o']

t1 = timeit.timeit(lambda: comparar_listas(elementos_repetidos(lista_1), elementos_repetidos(lista_2)), number=1000)
t2 = timeit.timeit(lambda: elementos_repetidos(comparar_listas(lista_1, lista_2)), number=1000)

if t1 < t2:
    print("La función 1 es más eficiente que la función 2")
else:
    print("La función 2 es más eficiente que la función 1")

t3 = timeit.timeit(lambda: lista_3(lista_1, lista_2), number=10000000)
t4 = timeit.timeit(lambda: lista_4(lista_1, lista_2), number=10000000)
t5 = timeit.timeit(lambda: lista_5(lista_1, lista_2), number=10000000)

print(t1, t2, t3, t4, t5)