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
    fe = random.randint(1, 100)
    
    print("Número de la cuenta:")
    num = []
    while len(num) < 12:
        a = random.randint(0, 9)
        num.append(a)
    
    print(num)
    print("Saldo de la cuenta:")
    sal = 10000
    sal = float(sal)
    
    print("¿Qué tipo de cuenta tiene? corriente/vip")
    cuenta = input()
    if cuenta == "corriente":
        cuenta = funciones.Cuenta (id, nom, fe, num, sal)
    
        #Operaciones en la cuenta
        print("¿Quieres hacer alguna operación? transferir/retirar/ingresar")
        usuario = input()
        if usuario == "retirar":
            print("Va a retirar una cantidad de: ")
            ret = float(78)
            print(cuenta.retirar(ret))
        elif usuario == "transferir":
            print("Su transferencia es de:")
            trans = float(2000)
            print("¿A quién lo quiere transferir?")
            usuario = input()
            print(cuenta.transferir(trans))
        elif usuario == "ingresar":
            ing = 575
            print(cuenta.ingresar(ing))
        else:
            raise Exception("Esa operación no está disponible")
    elif cuenta == "vip":

        #Cuenta Vip
        v = vip.Vip(id, nom, fe, num, sal,-1000)
        #Operaciones en la cuenta
        print("¿Quieres hacer alguna operación? transferir/retirar")
        usuario = input()
        if usuario == "retirar":
            print("Va a retirar una cantidad de: ")
            ret = float(78)
            print(cuenta.retirar(ret))
        elif usuario == "transferir":
            print("Su transferencia es de:")
            trans = float(2000)
            print("¿A quién lo quiere transferir?")
            usuario = input()
            print(cuenta.transferir(trans))
        elif usuario == "ingresar":
            ing = 575
            print(v.ingresar(ing))
        else:
            raise Exception("Esa operación no está disponible")
           
    else:
        raise Exception("Esa no es una opción válida")