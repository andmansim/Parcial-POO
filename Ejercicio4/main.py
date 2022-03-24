import funciones

if __name__ == "__main__":
    #Información del usuario       
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
    sal = float(sal)
    cuenta = funciones.Cuenta (id, nom, fe, num, sal)