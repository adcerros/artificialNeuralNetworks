import random
import numpy as np
from numpy.random.mtrand import permutation

#Adaline model
class neurone:

    def __init__(self, varNumber):
        self.weights = []
        self.threshold = random.randrange(-1,1)
        # Se inicializan los pesos
        for i in range(varNumber):
            self.weights.append(random.randrange(-1,1))
    
    def train(self, trainingData, validationData, numberOfRounds, learningRate):
        # Se crean las listas de modelos y sus correspondientes errores
        models = []
        trainingErrors = []
        # Se inicializan los pesos
        numberOfRows = len(trainingData)
        numberOfColumns = len(trainingData[0])
        # Se dividen los datos en entradas y salidas deseadas
        entries = []
        desiredExits = []
        varNumber = len(trainingData[0])-1
        for i in range(numberOfRows):
            entries.append(trainingData[i][:numberOfColumns-1])
            desiredExits.append(trainingData[i][numberOfColumns-1])
        # Bucle de entrenamiento
        for i in range(numberOfRounds):
            for j in range (numberOfRows):
                exit = 0
                error = 0
                # Se calcula la salida
                for k in range(varNumber):
                    exit += entries[j][k] * self.weights[k]
                exit += self.threshold
                error += abs(desiredExits[j] - exit)

                # Si la salida no es la deseada se modifican los pesos y el umbral
                if exit != desiredExits[j]:
                    for k in range(varNumber):
                        self.weights[k] = float(self.weights[k]) + (learningRate * (desiredExits[j]-exit) * entries[j][k])
                    self.threshold = self.threshold + (learningRate * (desiredExits[j]-exit))
            trainingErrors.append(error/numberOfRows)
            models.append(self.weights)
        print(trainingErrors[0])
        print(trainingErrors[len(trainingErrors)-1])
    print()

                










