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

''' cualquiera es valida '''

ganado = 3
empatados = 1
perdidos = 0
partidos_totales = 20



# print("El promedio total es: ", resultado)



# Nico C
# perdidos = int(input("Indicar partidos Perdidos: "))
# ganados = int(input("Indicar partidos Ganados: "))
# empatados = (20 - ganados) - perdidos
# puntos_totales = perdidos * 0 + ganados * 3 + empatados * 1
# promedio = puntos_totales / 20
# print("El promedio total es: ", promedio)


# Mario T
# partidos_ganados = int(input("Bienvenido, ingrese el numero de partido que han ganado: "))
# partidos_empatados = int(input("Genial!, ahora indiqueme cuantos partidos han empatado: "))
# partidos_perdidos = int(input("finalmente, indiqueme cuantos partidos perdieron: "))
# promedio_de_puntos = ((partidos_ganados * 3)+(partidos_empatados * 1)+(partidos_perdidos * 0))/20
# print("el promedio de puntos de su equipo fue: ", promedio_de_puntos)


# Nahu

# perdidos = int(input("Indicar partidos Perdidos: "))
# ganados = int(input("Indicar partidos Ganados: "))
# empatados = int(input("Indicar partidos empatados: "))
# puntos_totales = int(perdidos) * 0 + int(ganados) * 3 + int(empatados) * 1
# promedio = puntos_totales / 20
# print("El promedio total es: ", promedio)



ganado = int(input(("Partidos ganados: "))) * 3
empatado = int(input(("Partidos empatados: "))) * 1
perdido = int(input(("Partidos perdidos: "))) * 0
print(ganado, empatado, perdido)
partidos_totales = 20
print("Promedio total es: ", ((ganado + empatado + perdido) / partidos_totales))

