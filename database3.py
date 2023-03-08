# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

class listas:
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
    