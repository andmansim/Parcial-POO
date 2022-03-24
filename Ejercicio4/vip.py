import funciones
class Vip(funciones.Cuenta):
    def __init__(self, ID, nombre, fecha, numero, saldo, saldo_negativo):
        super().__init__(ID, nombre, fecha, numero, saldo)
        self.saldo_negarivo = saldo_negativo
        
        