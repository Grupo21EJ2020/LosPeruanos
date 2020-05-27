class Tema:
    def __init__(self,idtema,nombre):
        self.__idtema = idtema
        self.__nombre = nombre
    
    @property
    def idtema(self):
        return self.__idtema 
    @property
    def nombre(self):
        return self.__nombre