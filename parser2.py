import sys
import time
import random
import matplotlib.pyplot as plt

class dataPreparator:

    def __init__(self, path):
        parsedData = self.parser(path)
        normalizedData = self.numberNormalizer(parsedData)
        self.finalData = self.dataScrambler(normalizedData)


    # Parser de datos universal
    def parser(self, path):
        # Se leen las lineas y se limpian los saltos de linea
        filePointer = open(path, "r")
        textLines = filePointer.readlines()
        numberOfLines = len(textLines)
        for i in range(numberOfLines):
            textLines[i] = textLines[i].strip('\n')
        # Construccion matriz de datos
        data = []
        for i in range(numberOfLines):
            floatLine = []
            line = (textLines[i].split(", "))
            numberOfColumns = len(line)
            for j in range(numberOfColumns):
                # Se hace un cast a float
                floatLine.append(float(line[j]))
            data.append(floatLine)
            # # El siguiente print es solo para comprobaciones
            # print(floatLine)
        return data


    # Normalizador de datos universal
    def numberNormalizer(self, data):
        numberOfRows = len(data)
        numberOfColumns = len(data[0])
        listOfMax = []
        listOfMin = []
        # Busqueda de maximos y minimos recorriendo la matriz por columnas
        for j in range(numberOfColumns):
            # Se inicializan los valores con el primer elemento de la columna en cada iteraccion
            max = data[0][j]
            min = data[0][j]
            for i in range(numberOfRows):
                currentElement = data[i][j]
                if currentElement > max:
                    max = currentElement
                if currentElement < min:
                    min = currentElement
            # Cada elemento de la lista representa el min/max de cada columna de la lista global
            listOfMax.append(max)
            listOfMin.append(min)
        for i in range(numberOfRows):
            for j in range(numberOfColumns):
                data[i][j] = (data[i][j] - listOfMin[j])/(listOfMax[j]-listOfMin[j])
        return data

    # Desordenador de datos
    def dataScrambler(self, data):
        random.shuffle(data)
        for i in range(len(data)):
            print(data[i])
        return data
    




inicio = time.time()
dataPreparator("datos.txt")
fin = time.time()
print("Tiempo ejecucion: " + str(fin-inicio))
