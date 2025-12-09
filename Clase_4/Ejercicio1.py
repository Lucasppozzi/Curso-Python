"""
Consigna:
Para aprobar un crédito, el cliente debe ser mayor de edad.
Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.
En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito
"""
edad = int(input("ingrese su edad"))
antiguedad = int(input("ingrese su antiguedad"))
ingresos = float(input("sus ingresos por favor"))

if edad >= 18:
    if antiguedad >= 3:
        if ingresos >= 2500:
         print("CREDITO APROBADO")
    elif ingresos >= 4000:
        print("credito aprobado")
    else: 
        print("CREDITO NO APROBADO")
else:
     print("CREDITO NO APROBADO")
 