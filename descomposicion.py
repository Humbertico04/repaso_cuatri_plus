# Crea un script llamado descomposicion.py que realice las siguientes tareas:
# 
# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:
# 
# python descomposicion.py 3647
# 
# El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
# 
# 0007
# 
# 0040
# 
# 0600
# 
# 3000
# 
# Pista
# 
# Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

def descomposicion(numero):
    numero = str(numero)[: : -1]
    long = len(numero)
    cadena = ""
    for i in range(long):
        cadena += f"\n{numero[i]:0>{long-i}}{'':0<{i}}"
    return cadena
        