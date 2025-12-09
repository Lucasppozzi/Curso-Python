"""
En Tech Connect se va a realizar un torneo de fútbol interno de la compañía. Como
parte del equipo de desarrollo, te solicitan desarrollar un programa que permita calcular
el promedio final de los equipos de fútbol del torneo.
Para ello, debes considerar tres aspectos:
✓ Jugaron 20 partidos durante el torneo.
✓ Los partidos poseen diferente puntaje según el resultado:
○ Ganado: 3 puntos
○ Empatado: 1 punto
○ Perdido 0 puntos
✓ El promedio final resulta de la cantidad de puntos totales divididos la cantidad de
partidos.
Cada una de las cantidades de partidos ganados, empatados o perdidos debe
solicitarse al usuario utilizando la función input().
✓ partidos_ganados 8
✓ partido_empatados 7
✓ partido_perdidos 5
"""

# ganado_puntos = 3
# empatados_puntos = 1
# perdidos_puntos  = 0
# partidos_totales = 20


# ganados = int(input("ingrese los partidos ganados"))
# perdidos = int(input("ingrese los perdidos "))
# empatados = int(input("ingrese los empatados"))
# resultado = ((ganados * ganado_puntos) + (perdidos * empatados_puntos) + (empatados * perdidos_puntos)) / partidos_totales
# print("el promedio total es: ", resultado)


# slicing


una_cadena = "hola mundo"

print(una_cadena[0:4])
print(len(una_cadena))
print(una_cadena[:-1])


#listas y tuplas 




lista_1 = ["una", 13, 2.5, [], "hola mundo"]

print(lista_1[1:3])
tuplas_1 = {"una", 13, ()}
print(tuplas_1[0])
