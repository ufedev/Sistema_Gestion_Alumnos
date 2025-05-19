from os import system

class Gestor:
    
    def __init__(self,ruta):
        self.ruta=ruta
       
    def __abrir(self,modo="r"):
        # r =read(lectura) w=write(escritura) a=append(agregar)
        try:
            archivo=open(self.ruta,modo)
            return archivo
        except:
            archivo=open(self.ruta,'w')
            archivo.close()
            archivo=open(self.ruta,modo)
            return archivo
            
          
    
    def leer(self):
        archivo=self.__abrir()
        lectura:list[str]=archivo.readlines()
        
        anchos_col=[0]*(len(lectura[0].strip().split(','))+1)
        
        # [0]*3+1 = [0,0,0,0]
        
        for indice,linea in enumerate(lectura):
            if indice==0:
                nueva_linea=f"ID,{linea}".strip().split(',')
            else:
                nueva_linea=f"{indice},{linea}".strip().split(',')
          
            for i,v in enumerate(nueva_linea):
                v=len(str(v))
                if anchos_col[i] < v:
                    anchos_col[i]=v
            
        for indice,linea in enumerate(lectura):
            if indice==0:
                linea_completa=f"ID,{linea}".strip().split(',')
            else:
                linea_completa=f"{indice},{linea}".strip().split(',')
                
            nueva_linea=""
            if indice==0:
                print(f"+{"-"*((sum(anchos_col)+((3*len(anchos_col))-1)))}+")
            for i,valor in enumerate(linea_completa):
                ancho=len(valor)
                diferencia=anchos_col[i]-ancho
                if i == 0:
                    valor=f"| {valor}"+" "*(diferencia)
                else:
                    valor=f" | {valor}"+" "*(diferencia)
                    
                if i == len(linea_completa)-1:
                    valor+=" |"                
                nueva_linea+=valor

            print(nueva_linea)
            
            if indice==0 or indice == len(lectura)-1:
                print(f"+{"-"*(sum(anchos_col)+(3*len(anchos_col)-1))}+")
                
        archivo.close()
        
        
    def escribir(self,texto):
        archivo=self.__abrir("a")
        archivo.write(f"{texto}\n")
        archivo.close()
        
   
    def cabecera(self,cb):
        archivo = self.__abrir()
            # [
            #     "nombre,apellido,dni",
            #     "federico,malfasi, 12345678",
            #     "federico,malfasi,12345678"
            # ]
            #! readlines devuelve ⬆️
        if len(archivo.readlines())<=1:
            archivo_cabecera=self.__abrir('w')
            archivo_cabecera.write(f"{cb}\n")
            archivo_cabecera.close()
        archivo.close()
        
        
    def insertar(self):
        pass

    def editar(self):
        system('cls')
        self.leer()
        
        id=input("Seleccione el ID del alumno: ")
        archivo=self.__abrir()
        nueva_lista=[]
        for indice,linea in enumerate(archivo.readlines()):
            
            if int(id)==indice and indice>0:
                system('cls')
                print('Editando alumno.. En caso de no querer modificar dejar vacio..')
                nombre,apellido,dni=linea.strip().split(',')
                
                
                nuevo_nombre=input(f"Actual '{nombre}' Nuevo Nombre: ")
                nuevo_apellido=input(f"Actual '{apellido}' Nuevo Apellido: ")
                nuevo_dni=input(f"Actual '{dni}' Nuevo DNI: ")
                print(nombre,apellido,dni)
                input('...')
                
                nueva_linea=""
                
                if nuevo_nombre=="":
                    
                    nueva_linea+=f"{nombre},"
                else:
                    
                    nueva_linea+=f"{nuevo_nombre},"
                
                if nuevo_apellido=="":
                    
                    nueva_linea+=f"{apellido},"
                else:
                    
                    nueva_linea+=f"{nuevo_apellido},"
                
                if nuevo_dni=="":
                   
                    nueva_linea+=dni
                else:
                  
                    nueva_linea+=nuevo_dni
                
                nueva_linea+="\n"
                nueva_lista.append(nueva_linea)
                continue
            
            nueva_lista.append(linea)
        
        archivo.close()
        
        nuevo_archivo=self.__abrir("w")
        for linea in nueva_lista:
            nuevo_archivo.write(linea)
        
        nuevo_archivo.close()
        system('cls')
        self.leer()
        
        input('..Alumno editado correctamente..')
        
        
        
    
    def eliminar(self,id):
        
        archivo = self.__abrir()
        
        nueva_lista=[]
        
        for indice,linea in enumerate(archivo.readlines()):
          
            
            if indice==int(id):
                if id=="0":
                    nueva_lista.append(linea)
                continue
            nueva_lista.append(linea)
            
        archivo.close()
        
        archivo=self.__abrir('w')
        
        for linea in nueva_lista:
            archivo.write(linea)
        
        archivo.close()
        
        
        
        