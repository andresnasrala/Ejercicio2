import os
import csv
from claseViajeroFrecuente import ViajeroFrecuente as viajero_frecuente

class Menu:

    def mostrarMenu(self, ListaViajeros=None):
        os.system('cls')
        op = int (input ('''
    -------->Menu<--------
    Seleccione una opcion:
    1. Item 1: Leer archivo y crear lista 
    2. Item 2: Ingresar numero de viajero 
    3. Item 3: 
    0. Salir
    Su opcion: '''))
        return op

    def ManejadorMenu (self, op, ListaViajeros):    
        if op == 1:
            self.opcion1(ListaViajeros)
        elif op == 2:
            self.opcion2(ListaViajeros)
        elif op == 3:
            self.opcion3()

    def opcion1 (self, ListaViajeros):
        total = 0
        bandera = True
        path = './archivo_Viajeros.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter =',')
        for fila in reader:
            if bandera:
                bandera = False
            else:
                num_viajero = fila[0]
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas_acum = fila[4]
                viajero = viajero_frecuente(num_viajero, dni, nombre, apellido, millas_acum)
                ListaViajeros.append(viajero)
                total += 1
        if total > 0:
            print (f'Lista cargada correctamente, se cargaron {total} viajeros')
            os.system('pause')
        else:
            print ('Error en la carga')
            os.system('pause')


    def opcion2 (self, ListaViajeros):
        os.system('cls')
        i = 0
        num_viajero = int (input ('ingrese numero del viajero: '))
        xViajero = ListaViajeros[i].getNumero()
        print (f'Primer numero: {xViajero}')
        while (i <= len(ListaViajeros) -1) and (num_viajero != xViajero):
            print (f'i antes: {i}')
            i += 1
            print (f'i despues: {i}')
            if i < len(ListaViajeros):
                print ('si')
                xViajero = int (ListaViajeros[i].getNumero())
                print (f'iffffff numero: {xViajero}') 
        print (f'iiiiii: {i}')
        print (f'ultimo numero: {ListaViajeros[i].getNumero()}')
        if num_viajero != xViajero:
            print ('Error, numero de viajero invalido')
        else:
            print(f'Viajero encontrado con el numero {num_viajero} y {xViajero}, indice = {i}, numero de viajero: {ListaViajeros[i].getNumero()}')
        os.system('pause')

    def opcion3 (self):
        print ('opc 3')
        os.system('pause')