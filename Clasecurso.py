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
    def Agregar(self):
        archivo = open("./archivos/curso.txt","a",encoding='utf8')
        archivo.write( str(self.__idcurso) + '|' + self.__descripcion + '|' + str(self.__idempleado))
        archivo.write("\n")    
        archivo.close()
        

         