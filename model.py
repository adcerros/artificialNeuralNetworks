import random
import numpy as np
import matplotlib.pyplot as plt

# Adaline model
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
        validationErrors =[]
        # Se inicializan los pesos
        trainingPatternsNumber = len(trainingIn)
        # Bucle de entrenamiento
        for round in range(numberOfRounds):
            for i in range (trainingPatternsNumber):
                exit = 0
                # Se calcula la salida
                for j in range(self.varNumber):
                    exit += trainingIn[i][j] * self.weights[j]
                exit += self.threshold
                # Si la salida no es la deseada se modifican los pesos y el umbral
                if exit != trainingOut[i]:
                    for j in range(self.varNumber):
                        self.weights[j] = self.weights[j] + (learningRate * (trainingOut[i]-exit) * trainingIn[i][j])
                    self.threshold = self.threshold + (learningRate * (trainingOut[i]-exit))
            models.append(self.weights)          
            # Calculo del error de entrenamiento
            trainingErrors.append(self.errorCalculator(trainingIn, trainingOut))
            # Calculo error validacion
            validationErrors.append(self.errorCalculator(validationIn, validationOut))
        
        
        fig, ax = plt.subplots()
        ax.plot(trainingErrors)
        ax.plot(validationErrors)
        plt.show()
    
    def errorCalculator(self, dataIn, dataOut): 
        error = 0   
        patternNumber = len(dataIn)
        for i in range(patternNumber):
            exit = 0
            # Se calcula la salida
            for j in range(self.varNumber):
                exit += dataIn[i][j] * self.weights[j]
            exit += self.threshold
            error += abs(dataOut[i] - exit)
        return(error/patternNumber)       

                










