from models.gestor import Gestor
from helpers import ent
from os import system


gestor = Gestor("gestor.csv")
gestor.cabecera("nombre,apellido,dni")

while True:
    system("cls")
    
    print("Programa de gestión de alumnos")
    opcion=input("""
1. Mostrar alumnos
2. Editar alumno
3. Eliminar alumno
4. Cargar alumno
5. Salir
Opción: """)
    
   
    match opcion:
        case "1":
            system('cls')
            gestor.leer()
            input('enter para continuar...')
           
        case "2":
            gestor.editar()
        case "3":
            system('cls')
            gestor.leer()
            id = input("Ingrese el ID: ")
            gestor.eliminar(id)
            system('cls')
            gestor.leer()
            input("Alumno eliminado exitosamente..")
            
        case "4":
            system('cls')
            print('Cargando nuevo alumno..')
            nombre=ent("Nombre: ")
            apellido=ent("Apellido: ")
            dni=ent("Dni: ")
            gestor.escribir(f"{nombre},{apellido},{dni}")
            
            input("alumno creado exitosamente...")
            
        case "5":
            input("Saliendoo....")
            break
        case _:
            input("La opción seleccionada no es válida...")
            
    




