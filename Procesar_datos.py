from Leer_csv import *
from division import *
from Seleccionar import *

''' Esta clase es para extraer los datos, crear la tabla y llenarla con los datos '''
class Procesar_datos:

    def __init__(self):
        #self.tipo = tipo
        self.contenido = []
        self.tabla = []
        self.nueva_lista = []
        self.lista_claves = []
        self.archivo = 'C:\\Users\\japb1\\OneDrive - Universidad Autonoma de Yucatan\\facultad\Análisis exploratorio de datos\\ADA 3- V2\\ada 3-codigo -v1\\210323COVID19MEXICO.csv'
        self.numero_estados= 32
        ##se ajusto el rango de edad de 125 por el tipo de enfermedades 10
        #self.rango_edades = 125
        self.tipos_enfermedades = 10


    # la tabla funciona como una lista de listas de contadores
    def construir_tabla(self):
        lista_listas = []
        i =0
        while i < self.numero_estados:
            lista_temporal = []
            j= 0
            while j < self.tipos_enfermedades:
                lista_temporal.append(0)
                j = j + 1
            i = i + 1
            lista_listas.append(lista_temporal)
        self.tabla = lista_listas


    def incrementar_contadores(self, a, b):
        var_incre = self.tabla[a][b]
        var_incre = var_incre + 1
        self.tabla[a][b] = var_incre


    # Este metodo funciona para la tabla de personas confirmadas
    def construir_proceso(self):
        self.construir_tabla()
        informacion = Leer_csv(self.archivo)
        self.contenido = informacion.contenido
        print("paso 1 completo")
        elemento_primero =self.contenido.pop(0)
        primer_elemento = division(elemento_primero)
        primer_elemento.proceso()
        self.lista_claves = primer_elemento.lista_cadena
        for i in self.contenido:
            casteo = division(i)
            casteo.proceso()
                #casteo.hacer_ajuste_2()
            casteo.hacer_ajuste_3()
                # print(casteo.lista_cadena)

            clasificar = Seleccionar(casteo.lista_cadena)
            clasificar.Hacer_seleccion()

            if clasificar.resultado == True:
                self.incrementar_contadores(clasificar.ruta_individuo[0]-1, clasificar.ruta_individuo[1])
                #self.incrementar_contadores(casteo.lista_cadena[0] - 1, casteo.lista_cadena[2])
                # print(casteo.lista_cadena)


    def imprimir_resultados(self):
        #print(self.lista_claves)
        #for i in self.tabla:
        #    print(i)
        print(self.tabla)



# proceso de extraccion de los datos
procesar= Procesar_datos()
procesar.construir_proceso()
procesar.imprimir_resultados()

