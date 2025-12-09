# definicion de clase: ej Gato

class Gato:
    def __init__(self, nombre, edad = 5):
        self.nombre = nombre
        self.edad = edad
    def maullear(self):
        print (f"El gato {self.nombre} dice: Miau")
    def caminar(self):
        print(f"el gato {self.nombre} esta caminando")
    def info(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad}")


gato_1 = Gato("Nico")
gato_2 = Gato("Mica")
gato_3 = Gato("Jose")
gato_1.maullear("Ezequiel")
gato_3.info()
gato_2.caminar