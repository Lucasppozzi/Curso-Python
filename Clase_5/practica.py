def es_numero(dato):
    if dato.isdigit():
        return True
    return False

def anio_bisiesto(anio):
    while not es_numero(anio):
        anio = input("Ingrese un año: ")
    anio = int(anio)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El anio {anio} es bisiesto!")
        return None
    print(f"El anio {anio} no es bisiesto")
anio_bisiesto(input("Ingrese un anio: "))