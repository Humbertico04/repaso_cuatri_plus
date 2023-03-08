# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

# Por ejemplo:

# pares, impares = separar([6,5,2,1,7])

# print(pares)

# print(impares)

# [2, 6]

# [1, 5, 7]

# Sugerencia

# Para ordenar una lista automáticamente puedes utilizar el método .sort().

def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares

print(separar([6,5,2,1,7]))