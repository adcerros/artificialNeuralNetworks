import sys
import time
import random
import matplotlib.pyplot as plt
import math


class dataPreparator:

    def __init__(self):
        pass
 
    def preparator(self, path):
        parsedData = self.parser(path)
        normalizedData = self.numberNormalizer(parsedData)
        scrambledData = self.dataScrambler(normalizedData)
        trainingSet, validationSet, testSet = self.dataPartitioner(scrambledData)
        # El file creator es mas bien para pruebas
        self.dataFileCreator(trainingSet, validationSet, testSet)
        return trainingSet, validationSet, testSet

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
        return data

    # Normalizador de datos universal
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

    # Desordenador de datos universal
    def dataScrambler(self, data):
        random.shuffle(data)
        return data
    
    # Particionador de datos ad-hoc
    def dataPartitioner(self, data):
        numberOfRows = len(data)
        trainingSet = data[:math.floor(numberOfRows * 0.7)]
        validationSet = data[math.floor(numberOfRows * 0.7) : math.floor(numberOfRows * 0.85)]
        testSet = data[math.floor(numberOfRows * 0.85) :]
        return trainingSet, validationSet, testSet 

    # Crea y escribe los ficheros de datos que contienen los distintos set 
    def dataFileCreator(self, trainingSet, validationSet, testSet):
        # Set de entrenamiento
        trainingSetFile = open("trainingSet.txt", "w+")
        for i in range(len(trainingSet)):
            trainingSetFile.write(str(trainingSet[i]) + "\n")
        trainingSetFile.write("@Numero de datos: " + str(len(trainingSet)))
        # Set de validacion
        validationSetFile = open("validationSet.txt", "w+")
        for i in range(len(validationSet)):
            validationSetFile.write(str(validationSet[i]) + "\n")
        validationSetFile.write("@Numero de datos: " + str(len(validationSet)))
        # Set de test
        testSetFile = open("testSet.txt", "w+")
        for i in range(len(testSet)):
            testSetFile.write(str(testSet[i])+ "\n")
        testSetFile.write("@Numero de datos: " + str(len(testSet)))

    

inicio = time.time()
mypreparator = dataPreparator()
trainingSet, validationSet, testSet = mypreparator.preparator("datos.txt")
fin = time.time()
print("Tiempo ejecucion: " + str(fin-inicio))
