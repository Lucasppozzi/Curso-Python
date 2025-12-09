
#            Conjuntos (set) en Python       #
##############################################
# ¿Qué es un conjunto?
# Un conjunto es una colección de elementos:
# - No tiene orden
# - No permite duplicados
# - Es útil para operaciones como unión, intersección, etc.

numeros = {1, 0, 2, 3, 4, -1}
vacio = {} #  ESTO ES UN DICT vacio
conj_vacio = set()
numeros.add(10)
print(numeros)
numeros.remove(10) # Elimina un elemento que le paso entre (). Si no existe ERROR
print(numeros)
numeros.discard(1) # Lo mismo que remove, pero no da ERROR si no existe el elem.
print(numeros)
elem = numeros.pop()
print(elem, numeros)
numeros.clear()
print(numeros)
lista = [1, 2, 3, 3, 3, 5, 10, "hola", "hola", "que"]
#print(list(set(lista))) Elimina los elementos repetidos de una lista y la vuelvo a convertir en lista.
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # Union, {1, 2, 3, 4, 5}
print(a & b) # interseccion: {3}
print(a - b) # Diferencia: {1, 2}
print(a ^ b) # Diferencia simetrica: {1, 2, 4, 5}