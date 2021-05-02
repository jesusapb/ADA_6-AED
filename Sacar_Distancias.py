from Distancias import *


class Sacar_Distancias:


    def __init__(self,lista_listas):
        self.lista_listas = lista_listas
        self.rango_establecido = 32
        self.lista_dis_euclidianas = []
        self.lista_dis_normales = []
        self.lista_dis_Wasserstein = []


    def hacer_calculo(self):
        lista_A = list(range(self.rango_establecido))
        lista_B = list(range(self.rango_establecido))

        for i in lista_A:
            for j in lista_B:
                # Se puede poner un if para los casos donde los valores sean iguales
                if i != j:
                    #print(i,":",j)
                    variable = Distancias(self.lista_listas[i],self.lista_listas[j])
                    variable.distancia_Euclideana()
                    #variable.distancia_Normal()
                    #variable.distancia_Wasserstein()
                    #variable.calcular_distancia()
                    self.lista_dis_euclidianas.append([variable.dis_euclidiana,i,j])
                    #self.lista_dis_normales.append([variable.dis_normal,i,j])
                    #self.lista_dis_Wasserstein.append([variable.dis_wasserstein,i,j])


            lista_B.pop(0)


    def imprimir_resultados(self):
        print("Resultados: ")
        print(self.lista_dis_euclidianas)
        print(self.lista_dis_normales)
        print(self.lista_dis_Wasserstein)





#tabla = [[1734, 99, 1340, 332, 3723, 1193, 256, 5209, 254, 4123], [3565, 195, 2331, 332, 8047, 1865, 318, 9642, 183, 4371], [1754, 56, 1302, 130, 3650, 429, 188, 5589, 107, 2903], [1191, 77, 551, 71, 1885, 166, 97, 3353, 71, 1017], [5084, 218, 1784, 378, 8277, 1188, 414, 6626, 269, 5705], [754, 48, 438, 67, 1118, 369, 70, 2336, 79, 1011], [2324, 148, 918, 194, 3100, 445, 227, 3403, 160, 1378], [2673, 178, 1447, 328, 5725, 1066, 335, 4952, 222, 3986], [67838, 3227, 29544, 6986, 106481, 10523, 7024, 109184, 4092, 172489], [1595, 158, 1087, 156, 3293, 613, 181, 3848, 118, 2741], [8496, 595, 3319, 638, 13503, 1710, 677, 20242, 626, 10185], [3500, 196, 1071, 205, 4618, 455, 251, 5199, 221, 1939], [2758, 228, 663, 180, 3599, 831, 264, 6070, 223, 3097], [5679, 566, 3863, 646, 9767, 3143, 707, 11069, 705, 8206], [12039, 772, 2862, 914, 15554, 3650, 927, 18982, 997, 14385], [3359, 333, 1474, 367, 5545, 724, 396, 7367, 298, 4089], [4911, 236, 1565, 271, 6307, 527, 409, 7579, 319, 5600], [785, 83, 568, 95, 1458, 540, 125, 1986, 78, 957], [9113, 308, 3559, 709, 12194, 2996, 694, 15213, 459, 12036], [2473, 160, 676, 261, 3792, 1026, 180, 6421, 127, 943], [7099, 422, 1500, 618, 8737, 2270, 725, 11385, 501, 7826], [4012, 222, 1149, 417, 6746, 713, 341, 8039, 283, 8117], [1730, 109, 1056, 161, 2428, 604, 155, 4016, 91, 1387], [4911, 423, 2287, 551, 7798, 1327, 445, 11065, 343, 5948], [2101, 188, 1140, 261, 5332, 1358, 313, 6668, 193, 2378], [3590, 168, 2500, 292, 8542, 939, 406, 10606, 170, 3870], [7184, 230, 3968, 480, 12548, 758, 450, 12612, 385, 2146], [5227, 298, 2079, 485, 8595, 1027, 404, 8952, 353, 3573], [2150, 138, 322, 156, 2286, 485, 140, 2897, 255, 1101], [5480, 292, 1942, 292, 7323, 1529, 271, 8385, 273, 3381], [2463, 186, 1977, 210, 4692, 911, 280, 5619, 176, 2032], [1622, 153, 825, 248, 3296, 847, 190, 3795, 106, 2845]]
#prueba_dis = Sacar_Distancias(tabla)
#prueba_dis.hacer_calculo()
#prueba_dis.imprimir_resultados()


