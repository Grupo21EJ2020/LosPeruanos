class Tema():
    def __init__(self,idtema,nombre):
        self.__idtema = idtema
        self.__nombre = nombre
    
    @property
    def idtema(self):
        return self.__idtema 
    @property
    def nombre(self):
        return self.__nombre
    
    #para modificar datos
    @idtema.setter
    def idtema(self, idtema):
        self.__idtema = idtema
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    #Apartado para los archivos
    def Agregar(self):
        archivo_tema = open("./archivos/tema.txt","a",encoding='utf8')
        archivo_tema.write( str(self.__idtema) + '|' + self.__nombre)
        archivo_tema.write("\n")    
        archivo_tema.close()
    
    def Eliminar(self):
        archivo_tema = open("./archivos/tema.txt","r",encoding ='utf8')

        lista = []
        for x in archivo_tema:
            datos = x.split("\n")
            if datos[0] != (self.__idtema + "|" + self.__nombre):
                lista.append(datos[0])
                archivo_temas_2 = open("./archivos/curso.txt","w",encoding = "utf8")
                for i in lista:
                    archivo_tema_2.write(i + "\n")
                    archivo_tema_2.close()
        archivo_tema.close()