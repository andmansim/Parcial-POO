class Cuenta:
    def __init__(self, ID, nombre, fecha, numero, saldo):
        self.ID = ID
        self.nombre = nombre
        self.fecha = fecha
        self.numero = numero
        self.saldo = saldo
    def retirar(self):
        print("¿Cuánto dinero quiere retirar?")
        ret = float(input())
        if ret >= self.saldo:
            print("No puede retirar esta cantidad de dinero")
        else:
            print("Has retirado esta cantidad de dinero " + ret + " este día " + self.fecha)
            self.saldo = self.saldo - ret
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
sal = input()

cuenta = Cuenta (id, nom, fe, num, sal)
cuenta.retirar

