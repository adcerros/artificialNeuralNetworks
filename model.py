import random
import numpy as np
from numpy.random.mtrand import permutation

#Adaline model
class neurone:

    def __init__(self, varNumber):
        self.weights = []
        self.varNumber = varNumber
        self.threshold = random.randrange(-1,1)
        # Se inicializan los pesos
        for i in range(varNumber):
            self.weights.append(random.randrange(-1,1))
    
    def train(self, trainingIn, trainingOut, validationIn, validationOut, numberOfRounds, learningRate):
        # Se crean las listas de modelos y sus correspondientes errores
        models = []
        trainingErrors = []
        # Se inicializan los pesos
        numberOfRows = len(trainingIn)
        # Bucle de entrenamiento
        for i in range(numberOfRounds):
            for j in range (numberOfRows):
                exit = 0
                error = 0
                # Se calcula la salida
                for k in range(self.varNumber):
                    exit += trainingIn[j][k] * self.weights[k]
                exit += self.threshold
                error += abs(trainingOut[j] - exit)
                # Si la salida no es la deseada se modifican los pesos y el umbral
                if exit != trainingOut[j]:
                    for k in range(self.varNumber):
                        self.weights[k] = self.weights[k] + (learningRate * (trainingOut[j]-exit) * trainingIn[j][k])
                    self.threshold = self.threshold + (learningRate * (trainingOut[j]-exit))
            trainingErrors.append(error/numberOfRows)
            models.append(self.weights)
        print(trainingErrors[0])
        print(trainingErrors[len(trainingErrors)-1])
    print()

                










