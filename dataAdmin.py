import random
import math

from numpy import number


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
        filePointer.close()
        return data

    # Normalizador de datos universal
    def numberNormalizer(self, data):
        numberOfRows = len(data)
        numberOfColumns = len(data[0])
        # Se inicializan los valores
        self.listOfMax = list(data[0])
        self.listOfMin = list(data[0])
        # Busqueda de maximos y minimos
        for i in range(numberOfRows):
            currentPattern = data[i]
            for j in range(numberOfColumns):
                currentElement = currentPattern[j]
                if currentElement > self.listOfMax[j]:
                    self.listOfMax[j] = currentElement
                if currentElement < self.listOfMin[j]:
                    self.listOfMin[j] = currentElement
        # Normalizacion
        for i in range(numberOfRows):
            currentPattern = data[i]
            for j in range(numberOfColumns):
                currentPattern[j] = (currentPattern[j] - self.listOfMin[j])/(self.listOfMax[j]-self.listOfMin[j])
        return data
    
    # Denormalizador de los errores
    def denormalizeErrors(self, listOfErrors):
        denormalizedErrors = []
        # Posicion de la lista donde se encuentran los resultados
        resultsPosition = len(self.listOfMin)-1
        minError = self.listOfMin[resultsPosition]
        maxError = self.listOfMax[resultsPosition]
        errorsRows = len(listOfErrors)
        for i in range(errorsRows):
            currentError = (listOfErrors[i] * (maxError - minError)) + minError 
            denormalizedErrors.append(currentError)
        return denormalizedErrors

    def denormalizeSingleError(self, error):
        resultsPosition = len(self.listOfMin)-1
        minError = self.listOfMin[resultsPosition]
        maxError = self.listOfMax[resultsPosition]
        return (error * (maxError - minError)) + minError 

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

    # Se dividen los datos en entradas y salidas deseadas
    def getInOut(self, data):
        numberOfRows = len(data)
        numberOfColumns = len(data[0])
        entries = []
        desiredExits = []
        for i in range(numberOfRows):
            entries.append(data[i][:numberOfColumns-1])
            desiredExits.append(data[i][numberOfColumns-1])
        return entries, desiredExits


    

