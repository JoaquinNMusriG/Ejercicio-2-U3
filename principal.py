from claseManejaSabores import ManejaSabores
from claseManejaHelados import ManejaHelados
from claseMenu import Menu

if __name__ == '__main__':
    sabores = ManejaSabores()
    sabores.cargarDatos()
    helados = ManejaHelados()

    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Registrar un HELADO vendido
              2 Mostrar el nombre de los 5 sabores de helado más pedidos
              3 Ingresar un número de sabor y estimar el total de gramos vendidos
              4 Ingresar tipo de helado y mostrar sabores vendidos""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op,sabores,helados)
        salir = op == 0
