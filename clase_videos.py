
class Video:
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
    