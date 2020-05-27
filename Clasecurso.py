class Curso():
    def __init__(self,idcurso,descripcion,idempleado):
        self.__idcurso = idcurso
        self.__descripcion = descripcion
        self.__idempleado = idempleado
    @property 
    def idcurso(self):
        return self.__idcurso
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def idempleado(self):
        return self.__idempleado  
    @idcurso.setter
    def idcurso(self):
        self.__idcurso = valor
    @descripcion.setter 
    def descripcion(self):
        self.__descripcion = valor
    @idempleado.setter   
    def idempleado(self):
        self.__idempleado = valor

    def Agregar(self):
        archivo = open("./archivos/curso.txt","a",encoding='utf8')
        archivo.write( str(self.__idcurso) + '|' + self.__descripcion + '|' + str(self.__idempleado))
        archivo.write("\n")    
        archivo.close()
    def Eliminar(self,idcurso):
        f = open("./archivos/curso.txt")
        Lista = []
        for line in f:
            linea = line.split("\n")
            self.__idcurso = linea[0]
            self.__descripcion = linea[1]
            self.__idempleado = linea[2]
            if self.__idcurso != self.__idcurso:
                Lista += line
        f.close()

        f =open("./archivos/curso.txt","w")  
        f.write(Lista)  
        f.close()    
        
        


        

         


        

                
            

         