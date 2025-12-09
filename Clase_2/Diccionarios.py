diccionario = {}
diccionario_1 = dict()
diccionario = {"hola" : "Que tal", "frutas" : ["manzana", " uva"], "numeros " : [1, 4, 57]}
diccionario_2 = {
    "usuarios": {
        "user": "nicolas12",
        "password": "1234",
        "dni": 123321312
    }
}
persona = {
    "Nombre": "Ana",
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Córdoba"
}

print(persona)
# acceder a los valores
print(persona ["Nombre"])
print(persona.get("nombree", "esta key no existe en el dict"))
persona["Nombre"] = "Ezequiel"
persona ["Nombre2"] = "Ruben"
print(persona)
del persona["nombre2"]
print(persona)
nombre = persona.pop("nombre")
print(persona, nombre)
# perona.clear elimina todo el dict
print(persona)

print(persona.keys()) # devuelve las keys
print(persona.values()) # devuelve los valores
print(persona.items()) # devuelve valor y key
print("edad " in persona)


"""
Deberás crear un diccionario que almacene a los 
ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2018.
Y mostrarlo por pantalla.
Datos para la resolución:
1990: 'Alemania',
1994: 'Brasil',
1998: 'Francia',
2002: 'Brasil',
2006: 'Italia',
2010: 'España',
2014: 'Alemania'
2018: 'Francia'
"""
diccionario_mundial_FIFA = {
1990: 'Alemania',
1994: 'Brasil',
1998: 'Francia',
2002: 'Brasil',
2006: 'Italia',
2010: 'España',
2014: 'Alemania',
2018: 'Francia'

}