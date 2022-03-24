class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Mamifero(Animal):
    def __init__(self, nombre, tipo):
        Animal.__init__(nombre)
        self.tipo = tipo

class Oviparo(Animal):
    def __init__(self, nombre, tipo):
        Animal.__init__(nombre)
        self.tipo = tipo