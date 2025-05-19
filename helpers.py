from os import system


# ENTRADA
def ent(mensaje):
    valor=""
    while valor == "":
        system("cls")
        valor=input(mensaje)
        valor=valor.strip()
        
        if valor=="":
            input("Debe ingresar un valor")
    
    return valor
    
    
    