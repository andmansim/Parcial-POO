import funciones

if __name__ == "__main__":
    #Información del usuario       
    print("¿Cuál es su ID?")
    id = input()
    if id == str:
        pass
    else: 
        raise Exception("Ese no es un ID válido")
    print("Nombre del titular:")
    
    nom = input()
    if nom == str:
        pass
    else: 
        raise Exception("Ese no es un nombre válido")
    
    print("Fecha:")
    fe = input()
    if fe == str:
        pass
    else: 
        raise Exception("Ese no es un fecha válida")
    
    print("Número de la cuenta:")
    num = input()
    if num == int:
        pass
    else: 
        raise Exception("Ese no es un número válido")
    
    print("Saldo de la cuenta:")
    sal = input()
    if sal == int:
        sal = float(sal)
    else: 
        raise Exception("Ese no es un saldo válido")

    cuenta = funciones.Cuenta (id, nom, fe, num, sal)