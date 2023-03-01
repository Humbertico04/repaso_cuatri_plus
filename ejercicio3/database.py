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
            lista_2.pop(lista_2.index(elemento))
            print(lista_2)
    return lista_nueva

print(comparar_listas(elementos_repetidos(["h",'o','l','a',' ', 'm','u','n','d','o']), elementos_repetidos(["h",'o','l','a',' ', 'l','u','n','a']))) #1
elementos_repetidos(comparar_listas(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a'])) #2
