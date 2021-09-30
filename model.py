import random
import matplotlib.pyplot as plt
import copy


# Adaline model
class neurone:

    def __init__(self, varNumber):
        # Se crean las listas
        self.models = []
        self.trainingErrors = []
        self.validationErrors =[]
        self.weights = []
        self.varNumber = varNumber
        # Se inicializa el umbral
        self.threshold = random.uniform(-1,1)
        # Se inicializan los pesos
        for i in range(varNumber):
            self.weights.append(random.uniform(-1,1))
    
    def train(self, trainingIn, trainingOut, validationIn, validationOut, numberOfRounds, learningRate):
        trainingPatternsNumber = len(trainingIn)
        # Bucle de entrenamiento
        for round in range(numberOfRounds):
            for i in range (trainingPatternsNumber):
                exit = 0
                currentPattern = trainingIn[i]
                # Se calcula la salida
                for j in range(self.varNumber):
                    exit += currentPattern[j] * self.weights[j]
                exit += self.threshold
                # Si la salida no es la deseada se modifican los pesos y el umbral
                desiredExit = trainingOut[i]
                if exit != desiredExit:
                    for j in range(self.varNumber):
                        self.weights[j] = self.weights[j] + (learningRate * (desiredExit-exit) * currentPattern[j])
                    self.threshold = self.threshold + (learningRate * (desiredExit-exit))
            self.setModelAndErrors(trainingIn, trainingOut, validationIn, validationOut)
            # Deteccion de estabilizacion del error a partir de la ronda 100 cada 5 rondas
            if round > 100:
                if (round % 5) == 0:
                    if abs(self.validationErrors[round]-self.validationErrors[round-50]) < 0.000001:
                        print("\n!!!!Se ha detectado una estabilizcion del error en la ronda: " + str(round + 1) + " !!!!\n")
                        return self.trainingErrors, self.validationErrors 
        return self.trainingErrors, self.validationErrors 

    def setModelAndErrors(self, trainingIn, trainingOut, validationIn, validationOut):
        model = []
        model.append(copy.deepcopy(self.weights))
        model.append(self.threshold)
        self.models.append(model)
        # Calculo del errores
        self.trainingErrors.append(self.errorCalculator(trainingIn, trainingOut))
        self.validationErrors.append(self.errorCalculator(validationIn, validationOut))
        
    def getAllModels(self):
        return self.models

    def getBestModel(self):
        numberOfRows = len(self.validationErrors)
        minValue = 1
        roundNumber = 0
        for i in range(numberOfRows):
            if self.validationErrors[i] < minValue:
                minValue = self.validationErrors[i]
                roundNumber = i
        return self.models[roundNumber], roundNumber, self.trainingErrors[roundNumber], self.validationErrors[roundNumber]

    def test(self, newWeights, newThreshold, testIn, testOut):
        self.weights = newWeights
        self.threshold = newThreshold
        return self.errorCalculator(testIn, testOut)
    
    def errorCalculator(self, dataIn, dataOut): 
        error = 0   
        patternNumber = len(dataIn)
        for i in range(patternNumber):
            exit = 0
            currentData = dataIn[i]
            # Se calcula la salida
            for j in range(self.varNumber):
                exit += currentData[j] * self.weights[j]
            exit += self.threshold
            error += (dataOut[i] - exit)**2
        return(error/patternNumber)       





        






