from claseManejaSabores import ManejaSabores
from claseManejaHelados import ManejaHelados

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.registrarHelado,
                            2:self.cincoSabores,
                            3:self.gramosEstimados,
                            4:self.saboresVendidos,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,sabores,helados):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(sabores,helados)
    def salir(self,sabores,helados):
        print('Salir')
    def registrarHelado(self,sabores,helados):
        gramos = input('Ingrese la cantidad de gramos del helado vendido: ')
        if gramos.isdigit():
            gramos = int(gramos)
            if (gramos == 100) or (gramos == 150) or (gramos == 250) or (gramos == 500) or (gramos == 1000):
                helados.agregarHelado(gramos,sabores)
            else:
                print('Esa no es una cantidad aceptable de gramos para un helado.')
        else:
            print('Valor ingresado inválido.')

    def cincoSabores(self,sabores,helados):
        print('Los 5 sabores de helados mas pedidos son: ')
        helados.mostrar5Sab(sabores)

    def gramosEstimados(self,sabores,helados):
        numero = input('Ingrese el numero de sabor para estimar gramos: ')
        if numero.isdigit():
            if sabores.buscarSabor(int(numero)) != None:
                helados.estimarGramosSabor(int(numero))
            else:
                print('No hay un sabor con ese numero.')
        else:
            print('Valor ingresado inválido.')

    def saboresVendidos(self,sabores,helados):
        tipo = input('Ingrese el tipo de helado para mostrar sabores vendidos: ')
        if tipo.isdigit():
            tipo = int(tipo)
            if (tipo == 100) or (tipo == 150) or (tipo == 250) or (tipo == 500) or (tipo == 1000):
                helados.mostrarSaboresporTipo(tipo,sabores)
            else:
                print('No hay un tipo de helado con esa cantidad de gramos.')
        else:
            print('Valor ingresado inválido.')
