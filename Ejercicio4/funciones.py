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
    
    def transferir(self, trans1):
        if trans1 >= self.saldo:
            print("No puede transferir esta cantidad de dinero")
        else:

            print("Has transferido esta cantidad de dinero " + str(trans1) + " el día " + str(self.fecha))
            self.saldo = self.saldo - trans1
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
print("¿Quieres hacer alguna operación? transferir/retirar")
usuario = input()
if usuario == "retirar":
    print("¿Cuánto dinero quiere retirar?")
    ret = float(input())
    print(cuenta.retirar(ret))
elif usuario == "transferir":
    print("¿Cuánto dinero quiere transferir?")
    trans = float(input())
    print("¿A quién lo quiere transferir?")
    usuario = input()
    print(cuenta.transferir(trans))
else:
    raise Exception("esa operación no está disponible")


