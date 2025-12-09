class Alumno:
 
    def __init__(self, nombre, nota):
        self.nombre = nombre  
        self.nota = nota

    
    def imprimir(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

  
    def resultado(self):
        if self.nota < 5:
            print("Materia desaprobada.")
        else:
           
            print(f"Materia aprobada, felicitaciones {self.nombre}.")


if __name__ == "__main__":
    print("--- Ingrese datos del Alumno ---")
    nombre1 = input("Ingrese el nombre: ")
    nota1 = float(input("Ingrese la nota: "))
    
    alumno1 = Alumno(nombre1, nota1)
    

    print("\n--- Resultados del Alumno  ---")
    alumno1.imprimir()
    alumno1.resultado()
