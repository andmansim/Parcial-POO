class Cuenta:
    def __init__(self, ID, nombre, fecha, numero, saldo):
        self.ID = ID
        self.nombre = nombre
        self.fecha = fecha
        self.numero = numero
        self.saldo = saldo
        
print("¿Cuál es su ID?")
id = input()
print("Nombre del titular:")
nom = input()
print("Fecha:")
fe = input()
print("Número de la cuenta:")
num = input()
print("Saldo de la cuenta:")
sal = input()

cuenta = Cuenta (id, nom, fe, num, sal)


