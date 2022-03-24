class Animal:
    def __init__(self, especie):
        self.especie = especie
        
class Mamifero(Animal):
    def __init__(self, especie, tipo):
        Animal.__init__(especie)
        self.tipo = tipo

class Oviparo(Animal):
    def __init__(self, especie, tipo):
        Animal.__init__(especie)
        self.tipo = tipo
    
class Gato(Mamifero):
    def __init__(self, especie, tipo, nombre):
        Mamifero.__init__(especie, tipo)
        self.nombre = nombre
        