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
 

class Vip(Cuenta):
    def __init__(self, ID, nombre, fecha, numero, saldo, saldo_negativo):
        super().__init__(ID, nombre, fecha, numero, saldo)
        self.saldo_negarivo = saldo_negativo
        
        