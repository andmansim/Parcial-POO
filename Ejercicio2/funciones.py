class Animal:
    def __init__(self, especie):
        self.especie = especie
        
class Mamifero(Animal):
    def __init__(self, especie, tipo1):
        Animal.__init__(especie)
        self.tipo1 = tipo1

class Oviparo(Animal):
    def __init__(self, especie, tipo):
        Animal.__init__(especie)
        self.tipo = tipo
    
class Gato(Mamifero):
    def __init__(self, especie, tipo1, nombre):
        Mamifero.__init__(especie, tipo1)
        self.nombre = nombre
    def descripcion(self):
        print("Especie: " + self.especie)
        print("Clasificación: " + self.tipo)
        print("Nombre: " + self.nombre)

class Pollo (Oviparo):
    def __init__(self, especie, tipo, nombre):
        Oviparo.__init__(especie, tipo)
        self.nombre = nombre
    def descripcion(self):
        print("Especie: " + self.especie)
        print("Clasificación: " + self.tipo)
        print("Nombre: " + self.nombre)

class Ornitorrinco(Mamifero, Oviparo):
    def __init__(self, especie, tipo, tipo1, nombre):
        Mamifero.__init__(especie, tipo1)
        Oviparo.__init__(especie, tipo)
        self.nombre = nombre
    def descripcion(self):
        print("Especie: " + self.especie)
        print("Clasificación: " + self.tipo + " y " + self.tipo1)
        print("Nombre: " + self.nombre)
        
pollo = Pollo("animal", "oviparo", "pollo")
pollo.descripcion

gato = Gato("animal", "mamifero", "gato")
gato.descripcion

ornitorrinco = Ornitorrinco("animal", "oviparo", "mamifero", "ornitorrinco")
ornitorrinco.descripcion