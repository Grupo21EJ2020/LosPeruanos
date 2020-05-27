class empleado():
    def __init__(self,idempleado,nombre,direccion):
        self.__idempleado= idempleado
        self.__nombre= nombre
        self.__direccion= direccion
    @property
    def idempleado(self):
        return self.__idempleado
    @property
    def nombre(self):
        return self.__nombre
    @property 
    def direccion():
        return self.__direccion
        
    @idempleado.setter
    def idempleado(self):
        self.__idcempleado = valor
    @nombre.setter 
    def nombre(self):
        self.__nombre = valor
    @direccion.setter   
    def direccion(self):
        self.__direccion = valor

    def Agregar(self):
        archivo = open("./archivos/empleados.txt","a",encoding='utf8')
        archivo.write( str(self.__idempleado) + '|' + self.__nombre + '|' + str(self.__direccion))
        archivo.write("\n")    
        archivo.close()
    def Eliminar(self):
        f = open("./archivos/empleados.txt")
        Lista = []
        for line in f:
            linea = line.split("|")
            self.__idempleado = linea[0]
            self.__nombre = linea[1]
            self.__direccion = linea[2]
            if self.__idempleado != self.__idempleado:
                Lista += line
        f.close()

        f =open("./archivos/empleados.txt","w")  
        f.write(Lista)  
        f.close()    
        
    def Modificar(self):
         f = open("./archivos/empleados.txt")
         
         cam = []
         for line in f:
             linea = line.split("|")
             self.__idempleado = linea[0]
             self.__nombre = linea[1]
             self.__direccion = linea[2]
             if self.__idempleado != self.__idempleado:
                 cam += line
         f.close()
         for renglon in cam:
            datos = renglon.split("|")
            if datos[0] == (self.__idempleado,):
                self.__idempleado = int(input("ingrese el empleado modificado"))
                self.__nombre = input("ingrese el nombre modicado")
                self.__direccion = (input("ingrese la direccion modificada"))
                datosNuevos = datos[1].replace(datos[1], self.__nombre + "|" + self.__direccion + "\n")
                datosCambiados = (datos[0] + "|" + datosNuevos)
                cam.append(datosCambiados)
         f =open("./archivos/empleados.txt","w")  
         f.write(cam)  
         f.close()
    
    def borrarInfoclear(self):

        archivo = open("./archivos/empleados.txt","r",encoding ='utf8')

        lista = []
        for x in archivo:
            datos = x.split("\n")
            if datos[0] != (self.__idempleado + "|" + self.__nombre + "|" + self.__direccion):
                lista.append(datos[0])
                archivo2 = open("./archivos/empleados.txt","w",encoding = "utf8")
                for i in lista:
                    archivo2.write(i + "\n")
                    archivo2.close()
        archivo.close()

            

