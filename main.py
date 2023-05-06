from menu import Menu
import os

if __name__ == '__main__':
    listaViajero = []
    Menu = Menu()
    op = Menu.mostrarMenu()
    while op != 0 & op <=3:
        Menu.ManejadorMenu (op, listaViajero)
        op = Menu.mostrarMenu(listaViajero)
    print ('saliendo...')
    os.system('pause')
    os.system('exit')