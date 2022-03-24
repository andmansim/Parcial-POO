class Cuenta:
    def __init__(self, ID, nombre, fecha, numero, saldo):
        self.ID = ID
        self.nombre = nombre
        self.fecha = fecha
        self.numero = numero
        self.saldo = saldo
        
    def retirar(self, ret1):

        if ret1 >= self.saldo:
            print("No puede retirar esta cantidad de dinero")
        else:
            print("Has retirado esta cantidad de dinero " + str(ret1) + " el día " + str(self.fecha))
            self.saldo = self.saldo - ret1
            return self.saldo
print("¿Cuál es su ID?")
id = input()
print("Nombre del titular:")
nom = input()
print("Fecha:")
fe = input()
print("Número de la cuenta:")
num = input()
print("Saldo de la cuenta:")
sal = float(input())

cuenta = Cuenta (id, nom, fe, num, sal)
print("¿Cuánto dinero quiere retirar?")
ret = float(input())
print(cuenta.retirar(ret))


