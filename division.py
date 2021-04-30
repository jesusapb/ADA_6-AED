
''' Cambiar  nombre a Castear'''
class division:


    def __init__(self,cadena):
        self.cadena = cadena.pop()
        self.lista_cadena = []
        self.nueva_lista = []



    def proceso(self):
        self.lista_cadena = self.cadena.split()
        #print(self.lista_cadena)


    def hacer_ajuste(self):
        i = 0
        while i < 17:
            if i != 0 and i != 1 and i != 10 and i != 11 and i != 12 and i != 37:
                self.nueva_lista.append(float(self.lista_cadena[i]))
            else:
                self.nueva_lista.append(self.lista_cadena[i])
            i = i + 1

        self.lista_cadena = self.nueva_lista


    def hacer_ajuste_2(self):
        ## Estado
        self.nueva_lista.append(int(self.lista_cadena[4]))
        ##fecha de defuncion
        self.nueva_lista.append((self.lista_cadena[12]))
        ##edad
        self.nueva_lista.append(int(self.lista_cadena[15]))
        self.lista_cadena= self.nueva_lista


    def hacer_ajuste_3(self):
        ##Estado
        #self.nueva_lista.append(int(self.lista_cadena[4]))
        # Diabetes
        #self.nueva_lista.append(int(self.lista_cadena[20]))
        #EPOC
        #self.nueva_lista.append(int(self.lista_cadena[21]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[22]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[23]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[24]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[25]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[26]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[27]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[28]))
        #
        #self.nueva_lista.append(int(self.lista_cadena[29]))

        self.nueva_lista.append(int(self.lista_cadena[4]))
        for i in range(20,30):
            self.nueva_lista.append(int(self.lista_cadena[i]))
            #print(i)
        self.lista_cadena = self.nueva_lista







    # Metodo para pruebas locales, NO USAR en el programa global
    def imprimir_cadena(self):
        print(self.lista_cadena)
        print(len(self.lista_cadena))
        #print(self.nueva_lista)
        #for i in self.lista_cadena:
        #    print(i)

        #print(float(self.lista_cadena[2]))


##pruebas del nuevo metodo
#lista_a = ['2021-03-23\tc1baa1\t1\t12\t20\t2\t20\t20\t067\t2\t2021-01-19\t2021-01-15\t9999-99-99\t2\t1\t38\t1\t97\t2\t2\t1\t2\t2\t2\t1\t2\t2\t1\t2\t2\t2\t1\t4\t2\t97\t5\t99\tMÃ©xico\t97\t2']

#prueba2 = division(lista_a)
#prueba2.proceso()
#prueba2.hacer_ajuste_3()
#prueba2.imprimir_cadena()