# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

def lista_3(lista_1: list, lista_2: list) -> list:
    lista_nueva: list = []
    for elemento in lista_1:
        if elemento not in lista_nueva and elemento in lista_2:
            lista_nueva.append(elemento)
    return lista_nueva

print(lista_3(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a','o']))