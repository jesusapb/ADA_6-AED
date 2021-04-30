import csv

''' Este metodo es fundamental para optener el contenido de un CSV'''
class Leer_csv:
    # Al constructor se le pasa el nombre del archivo y se extrae el contenido
    def __init__(self,archivo):
        self.fechas = []
        self.contenido = []
        with open(archivo) as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                self.contenido.append(row)


    # Metodo para pruebas locales, NO USAR en el programa global
    def imprimir_csv(self):
        for i in self.contenido:
            print(i)
            #print(self.contenido)


    # Metodo para pruebas locales, NO USAR en el programa global
    def imprimir_completo(self):
        print("Fechas",self.fechas)
        print(self.contenido)
        print(len(self.contenido))
        print(len(self.contenido[0]))


#ruta ='C:\\Users\\japb1\\OneDrive - Universidad Autonoma de Yucatan\\facultad\Análisis exploratorio de datos\\ADA 3- V2\\ada 3-codigo -v1\\210323COVID19MEXICO.csv'
#prueba = Leer_csv(ruta)
#prueba.imprimir_csv()





