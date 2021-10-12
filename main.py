from model import neurone
from dataAdmin import dataPreparator
import time
import matplotlib.pyplot as plt



inicio = time.time()
print()

# Parametros de la neurona
NUMBEROFCICLES = 10000
LEARNINGRATE = 0.025

# Preparacion de los conjuntos de datos
myPreparator = dataPreparator()
trainingSet, validationSet, testSet = myPreparator.preparator("concrete.dat")
trainingIn, trainingOut = myPreparator.getInOut(trainingSet)
validationIn, validationOut = myPreparator.getInOut(validationSet)
testIn, testExpectedOut = myPreparator.getInOut(testSet)

# Entrenamiento y obtencion del modelo
myNeurone = neurone(8)
trainingError , validationError = myNeurone.train(trainingIn, trainingOut, validationIn, validationOut, NUMBEROFCICLES, LEARNINGRATE)
model, modelRound, modelTrainingError, modelValidationError = myNeurone.getBestModel()

# Test
modelTestError, testExits = myNeurone.test(model[0], model[1], testIn, testExpectedOut)
myPreparator.getTestDocumentation(testExpectedOut, testExits)
print("/////////DATOS DEL MODELO FINAL////////////")
print("\nModelo final: " + str(model))
# Muestra de resultados
print("*** Se ha utilizado el error cuadratico medio ***")
print("\nRonda donde se consigue el modelo: " + str(modelRound + 1))
print("\nError de entrenamiento: " + str(modelTrainingError))
print("Error de validacion: " + str(modelValidationError))
print("Error de test: " + str(modelTestError))
print("Error medio: " + str((modelTrainingError + modelValidationError + modelTestError)/3))


fin = time.time()
print("\nTiempo ejecucion: " + str(fin-inicio))

# Grafico de errores
Errores, ax = plt.subplots()
ax.plot(trainingError, color = 'tab:blue', label = 'trainingError')
ax.plot(validationError, color = 'tab:red' , label = 'validationError')
ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
ax.legend(loc = 'upper right')
plt.show()