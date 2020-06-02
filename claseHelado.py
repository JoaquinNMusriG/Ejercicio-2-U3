from claseSabor import Sabor
import numpy as np

class Helado:
    __Gramos = 0
    __Sabor = []

    def __init__ (self, gramos):
        self.__Gramos = gramos
        self.__Sabor = []

    def __str__ (self):
        for sab in self.__Sabor:
            print(sab)
        return 'Gramos del helado: ' + str(self.__Gramos)

    def agregarSabor(self, sabor):
        self.__Sabor.append(sabor)

    def cantSabores(self):
        return len(self.__Sabor)

    def verificarSabor(self,numSabor):
        indice = 0
        resultado = False
        while (indice < len(self.__Sabor)) & (not resultado):
            if (self.__Sabor[indice].getNumero() == numSabor):
                resultado = True
            indice += 1
        return resultado

    def contarSabores(self, arreglo):
        for sabor in self.__Sabor:
            arreglo[sabor.getNumero() -1] += 1    

    def getGramos(self):
        return self.__Gramos

    def buscarSabores(self, arreglo):
        for sabor in self.__Sabor:
            arreglo[sabor.getNumero() -1] = 1
