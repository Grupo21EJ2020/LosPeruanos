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
            
