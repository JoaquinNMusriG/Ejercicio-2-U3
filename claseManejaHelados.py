from claseHelado import Helado
from claseManejaSabores import ManejaSabores
import numpy as np

class ManejaHelados:
    __Helados = []

    def __init__ (self):
        self.__Helados = []

    def agregarHelado (self, gramos,sabores):
        unHelado = Helado(gramos)
        print('Ahora ingrese el numero de los sabores del helado (ingrese 0 para terminar), recuerde que el maximo es 4: ')
        i=0
        numero = -1
        while ((i<4) & (int(numero) != 0)):
            numero = input('Numero de sabor: ')
            if (numero.isdigit()):
                if (int(numero) != 0):
                    unSabor = sabores.buscarSabor(int(numero))
                    if (unSabor != None):
                        if (not unHelado.verificarSabor(int(numero))):
                            unHelado.agregarSabor(unSabor)
                            i += 1
                        else:
                            print('Sabor ya agregado.')
                    else:
                        print('No hay un sabor con ese numero.')
            else:
                numero = -1
                print('Valor inválido.')
        if unHelado.cantSabores() == 0:
            print('No se ingresaron sabores, se cancelará la venta.')
            del unHelado
        else:
            self.__Helados.append(unHelado)

    def mostrar5Sab(self,sabores):
        arreglo = np.zeros(sabores.getCantSabores())
        for helado in self.__Helados:
            helado.contarSabores(arreglo)
        sabores.mostrarNombre5(arreglo)

    def estimarGramosSabor(self,num):
        total = 0.0
        for helado in self.__Helados:
            if helado.verificarSabor(num):
                total += helado.getGramos() / helado.cantSabores()
        print('La cantidad estimadas de gramos del sabor es de: {:0.2f} gramos'.format(total))

    def mostrarSaboresporTipo(self, tipo, sabores):
        arreglo = np.zeros(sabores.getCantSabores())
        print('Los sabores de helado de ese tipo son: ')
        for helado in self.__Helados:
            if helado.getGramos() == tipo:
                helado.buscarSabores(arreglo)
        sabores.mostrarSabores(arreglo)
