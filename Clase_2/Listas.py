# una lista es una estructura que guarda varios elementos juntos, en un orden



lista = []
lista_1 = list()
lista_str = ["manzana", "uva", "silla", "mesa"]
#                0        1        2      3
print(lista_str[1], lista_str[0], lista_str[3],lista_str[2])
print(lista_str[0:2])
lista_2 = lista_str[0:2]
# print(lista_str)
# print(lista_2 + ["naranja"])
print(lista_str[: :-1])
print(lista_str[-1])
lista_copia = lista_str[:] # ESTO NO MODIFICA LA LISTA_STR
print(lista_copia, "----------", lista_str)
lista_str.append("pc") # agrega un elemento al final de la lista
print(lista_str)
lista_str.insert(0, "teclado") # agrega un elemento en el indice que pongamos
print(lista_str)
lista_str.remove("teclado")  # elimina el elemento cuando lo encuentra, si hay repetidos elimina el 
dato = lista_str.pop # elimina el uiltimo elemento y LO DEVUELVE
dato_2 = lista_str.pop(1)
print(lista_str, dato, dato_2)
print(len(lista_str)) # devuelve el largo de la lista
lista_int = [1, 3, 5, 6, 10]
print(sum(lista_int)) # suma todos los elementos de una lista 
print(f"sorted: {sorted(lista_int)}")
print(f"sorted: {sorted(lista_str)}")
lista_str.sort()
print(lista_str)
lista_str.reverse() # da vuelta la lista
print(lista_str)
print(lista_int.count(1)) # devuelve la cantidad de veces que aparece en la lista
print(lista_int.index(10)) #devuelve el indice del elemento en la lista
lista_elementos = [1, "hola", none, True, [], 4.5]


"""
Partirás de:
matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
list(list(int()))
Debes llegar a:
matriz = [
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]
"""