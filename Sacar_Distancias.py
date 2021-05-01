from Distancias import *

class Sacar_Distancias:


    def __init__(self,lista_listas):
        self.lista_listas = lista_listas
        self.lista_dis_euclidianas = []
        self.lista_dis_normales = []
        self.lista_dis_Wasserstein = []


    def hacer_calculo(self):
        pass


    def imprimir_resultados(self):
        print(self.lista_dis_euclidianas)
        print(self.lista_dis_normales)
        print(self.lista_dis_Wasserstein)