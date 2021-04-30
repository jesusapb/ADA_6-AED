class Seleccionar:

    def __init__(self,individuo):
        self.individuo = individuo
        self.res_sum = 0
        self.resultado = False
        self.pos_positivo = 0
        self.total_ideal = 19
        self.ruta_individuo = []


    def sacar_suma(self):
        self.res_sum = sum(self.individuo[1:])


    def Hacer_seleccion(self):
        self.sacar_suma()
        if self.res_sum == self.total_ideal:
            self.resultado = True
            #Nota es posible que sea mejor no agregar el  + 1
            self.pos_positivo = self.individuo[1:].index(1)
            self.ruta_individuo.append(self.individuo[0])
            self.ruta_individuo.append(self.pos_positivo)



    def imprimir_resultado(self):
        print("Es un candidado para ser unico")
        print(self.res_sum)
        print(self.resultado)
        print(self.pos_positivo)
        print(self.ruta_individuo)




#lista_1 = [4,2,2,2,2,2,2,2,2,2,1]
#lista_2 = [3,1,1,1,1,2,2,2,2,2,2]
#lista_2_inc = [3,1,1,1,1,2,2,2,2,2]
#lista_prueba = [20, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2]

#prueba = Seleccionar(lista_1)
#prueba.Hacer_seleccion()
#prueba.imprimir_resultado()

