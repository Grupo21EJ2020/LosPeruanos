class Curso_Tema():
    def __init__(self,idcurso_tema,idcurso,idtema):
        self.idcurso_tema = idcurso_tema
        self.__idcurso = idcurso
        self.__idtema = idtema
    @property
    def idcurso_tema(self):
        return self.__idcurso_tema
    @property 
    def idcurso_tema(self):
        return self.__idcurso_tema
    @property 
    def idtema(self):
        return self.__idtema
    @idcurso_tema.setter
    def idcurso_tema(self):
        self.__idcurso_tema = valor
    @idcurso.setter
    def idcurso(self):
        self.__idcurso = valor
    @idtema.setter
    def idtema(self):
        self.__idtema = valor
                



