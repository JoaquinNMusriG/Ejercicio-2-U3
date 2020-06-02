class Sabor:
    __Numero = 0
    __Nombre = ''
    __Descripcion = ''

    def __init__ (self,numero, nombre, descripcion):
        self.__Numero = numero
        self.__Nombre = nombre
        self.__Descripcion = descripcion

    def __str__(self):
        return 'Numero: '+str(self.__Numero)+' Nombre: '+ self.__Nombre+' Descripcion: '+self.__Descripcion

    def getNumero (self):
        return self.__Numero

    def getNombre (self):
        return self.__Nombre    
