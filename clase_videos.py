
class Video():
    def __init__(self,idvideo,nombre,url,fecha_publicacion):
        self.__idvideo = idvideo
        self.__nombre = nombre
        self.__url = url
        self.__fecha_publicacion

    #Propiedades 
    @property
    def idvideo(self):
        return self.__idvideo 
    @property
    def nombre(self):
        return self.__nombre
    @property
    def url(self):
        return self.__url
    @property
    def fecha_publicacion(self):
        return self.__fecha_publicacion
    
    #para modificar datos
    @idvideo.setter
    def idvideo(self,idvideo):
        self.__idvideo = idvideo
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @url.setter
    def url(self,url):
        self.__url = url
    @fecha_publicacion
    def fecha_publicacion(self,fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion
    
    #Apartado para los archivos
    def Agregar(self):
        archivo_videos = open("./archivos/videos.txt","a",encoding='utf8')
        archivo_videos.write( str(self.idvideo) + '|' + self.__nombre + '|' + str(self.__url) + '|' + str(self.fecha_publicacion))
        archivo_videos.write("\n")    
        archivo_videos.close()
    
    def Eliminar(self):
        archivo_videos = open("./archivos/videos.txt","r",encoding ='utf8')

        lista = []
        for x in archivo_videos:
            datos = x.split("\n")
            if datos[0] != (self.__idvideo + "|" + self.__nombre + "|" + self.__url + "|" + self.__fecha_publicacion):
                lista.append(datos[0])
                archivo_videos_2 = open("./archivos/videos.txt","w",encoding = "utf8")
                for i in lista:
                    archivo_videos_2.write(i + "\n")
                    archivo_videos_2.close()
        archivo_videos.close()