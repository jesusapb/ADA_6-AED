#from scipy.stats import wasserstein_distance
''' Esta clase resuelve el inciso uno del ejercicio'''

class Distancias:

    def __init__(self,lista_A,lista_B):
        self.lista_A = lista_A
        self.lista_B = lista_B
        # atributos de valores
        self.dis_euclidiana = 0
        self.dis_normal = 0
        self.dis_wasserstein = 0


    def distancia_Euclideana(self):
        diferencias = 0
        for i,j in zip(self.lista_A,self.lista_B):
            #print(abs(i -j))
            diferencias = abs(i - j) + diferencias
        self.dis_euclidiana = diferencias


    def distancia_Normal(self):


        pass


    def distancia_Wasserstein(self):
        #self.dis_wasserstein= wasserstein_distance(self.lista_A,self.lista_B)
        pass
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html



    def calcular_distancia(self):
        self.distancia_Euclideana()
        self.distancia_Normal()
        self.distancia_Wasserstein()



    def imprimir_distancias(self):
        print("Distancias:")
        print("Euclidiana:",self.dis_euclidiana)
        print(self.dis_wasserstein)
        print(self.dis_normal)




#lista_1 = [4,2,2,2,2,2,2,2,2,2,1]
#lista_2 = [3,1,1,1,1,2,2,2,2,2,2]
#prueba_3 = Distancias(lista_1[1:],lista_2[1:])
#prueba_3.distancia_Euclideana()
#prueba_3.imprimir_distancias()






    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html

