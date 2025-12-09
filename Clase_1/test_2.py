

# print("Hola mundo")
# print('Hola mundo') # Control + S

# un_numero = 14 
# otro_numero = 50
# otro_numero_2 = 690
# numero = 1  # int

# numero_flotantes = 1.70 # float
# numero_flotantes_2 = 2.50
# pepe = 5.6 # float

# cadenas = "es una cadena" # str
# cadenas_2 = 'es otra cadena'

# print( type(cadenas), numero, int(numero_flotantes))

# edad = 29
# numero_2 = 90

# print("Suma: ", numero + otro_numero)
# print("Resta: ", otro_numero_2 - numero)
# print("Multiplicacion: ", 10 * 2)
# print("Potencia: ", 5 ** 2)
# print("Division :", 10 / 2)
# print("Division entera: ", 10 // 2)
# print("Modulo: ", 10 % 2)

# dato = input("Ingrese un dato: ") # Python lo transforma a string

# #print("Un dato: ", dato)

# resultado = ((10 + 5) * 2 - 10) * 0

# print(resultado)
 
# # un_numero_entero = input("ingrese un numero: ")
# # otro_numero_entero = input("ingrese un numero: ")

# # print(int(un_numero_entero) + int(otro_numero_entero))

# print( "5hol" *10)

# Slicing

una_cadena = "Hola Mundo"
#             0123456789
print(una_cadena[9])
print(una_cadena[0:7:2]) # [inicio: fin: salto]
print(una_cadena[-1])
# print(una_cadena[50]) Error
print(len(una_cadena))
print(una_cadena[::-1])


lista_1 = ["una", 13, 2.5, [1,2,3,[1]], "hola mundo"]
print(lista_1[1:3])
print(lista_1[3][3][0])

tuplas_1 = ("una", 13, ())
print(tuplas_1[0])