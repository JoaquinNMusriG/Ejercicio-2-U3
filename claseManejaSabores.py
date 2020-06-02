from claseSabor import Sabor
import csv
import numpy as np

class ManejaSabores:
    __sabores = []

    def __init__ (self):
        self.__sabores = []

    def cargarDatos (self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for sabor in reader:
            unSabor = Sabor(int(sabor[0]),sabor[1],sabor[2])
            self.__sabores.append(unSabor)

    def buscarSabor (self, num):
        band = False
        indice = 0
        while (indice < len(self.__sabores)) & (not band):
            if (self.__sabores[indice].getNumero() == num):
                band = True
            else:
                indice += 1
        if indice < len(self.__sabores):
            resultado = self.__sabores[indice]
        else:
            resultado = None
        return resultado

    def getCantSabores(self):
        return len(self.__sabores)

    def mostrarNombre5(self,arreglo):
        for i in range(5):
            indice = np.where(arreglo == np.amax(arreglo))
            print(self.__sabores[indice[0][0]].getNombre())
            arreglo[indice[0][0]] = -1
            #arreglo = np.delete(arreglo, indice[0][0])

    def mostrarSabores(self, arreglo):
        for i in range(self.getCantSabores()):
            if arreglo[i]:
                print(self.__sabores[i])
