import funciones
import vip
import random

if __name__ == "__main__":

    #Información del usuario       
    print("¿Cuál es su ID?")
    id = input()
 
    print("Nombre del titular:")
    nom = input()

    print("Fecha:")
    fe = random.randint()
    
    print("Número de la cuenta:")
    num = []
    while len(num) == 12:
        a = random.randint(0, 9)
        num.append(a)
     
    print("Saldo de la cuenta:")
    sal = input()
    sal = float(sal)
    
    print("¿Qué tipo de cuenta tiene? corriente/vip")
    cuenta = input()
    if cuenta == "corriente":
        cuenta = funciones.Cuenta (id, nom, fe, num, sal)
    
        #Operaciones en la cuenta
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
            raise Exception("Esa operación no está disponible")
    elif cuenta == "vip":

        #Cuenta Vip
        v = vip.Vip(id, nom, fe, num, sal,-1000)
        #Operaciones en la cuenta
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
            raise Exception("Esa operación no está disponible")
    else:
        raise Exception("Esa no es una opción válida")