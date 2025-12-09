

a = int(input("ingrese un numero: "))
b = int(input("ingrese un numero: "))






def dividir(a, b):
    if b == 0:
        return None
    return a / b
def dividir_excep(a, b):
    try:
       return a / b
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    return none

