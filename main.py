from menu import Menu
import os

if __name__ == '__main__':
    listaViaje = []
    Menu = Menu()
    op = Menu.mostrarMenu()
    while op != 0 & op <=3:
        Menu.ManejadorMenu (op, listaViaje)
        op = Menu.mostrarMenu(listaViaje)
    print ('saliendo...')
    os.system('pause')
    os.system('exit')