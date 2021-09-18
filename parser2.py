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

    def numberNormalizer(self, data):
        numberOfRows = len(data)
        numberOfColumns = len(data[0])
        # Se inicializan los valores
        listOfMax = list(data[0])
        listOfMin = list(data[0])
        # Busqueda de maximos y minimos
        for i in range(numberOfRows):
            for j in range(numberOfColumns):
                currentElement = data[i][j]
                if currentElement > listOfMax[j]:
                    listOfMax[j] = currentElement
                if currentElement < listOfMin[j]:
                    listOfMin[j] = currentElement
        # Normalizacion
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
