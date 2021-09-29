from model import neurone
from dataAdmin import dataPreparator
import time
import matplotlib.pyplot as plt



inicio = time.time()
print()


NUMBEROFCICLES = 10000
LEARNINGRATE = 0.001
# Preparacion de los conjuntos de datos
myPreparator = dataPreparator()
trainingSet, validationSet, testSet = myPreparator.preparator("datos.txt")
trainingIn, trainingOut = myPreparator.getInOut(trainingSet)
validationIn, validationOut = myPreparator.getInOut(validationSet)
testIn, testOut = myPreparator.getInOut(testSet)

# Entrenamiento y obtencion del modelo
myNeurone = neurone(8)
trainingError , validationError = myNeurone.train(trainingIn, trainingOut, validationIn, validationOut, NUMBEROFCICLES, LEARNINGRATE)
model, modelRound, modelTrainingError, modelValidationError = myNeurone.getBestModel()

# Test
modelTestError = myNeurone.test(model[0], model[1], testIn, testOut)
print("/////////DATOS DEL MODELO FINAL////////////")
print("\nModelo final: " + str(model))


# Denormalizacion de los datos
trainingErrorsDenormalized = myPreparator.denormalizeErrors(trainingError)
validationErrorsDenormalized = myPreparator.denormalizeErrors(validationError)
denormalizedModelTrainingError = myPreparator.denormalizeSingleError(modelTrainingError)
denormalizedModelValidationError = myPreparator.denormalizeSingleError(modelValidationError)
denormalizedModelTestError = myPreparator.denormalizeSingleError(modelTestError)

# Muestra de resultados
print("\nRonda donde se consigue el modelo: " + str(modelRound + 1))
print("\nError de entrenamiento: " + str(denormalizedModelTrainingError))
print("Error de validacion: " + str(denormalizedModelValidationError))
print("Diferencia entre el error de entrenamiento y de validacion: " + str(abs(denormalizedModelTrainingError - denormalizedModelValidationError)))
print("Error de test: " + str(denormalizedModelTestError))
print("Error medio: " + str((denormalizedModelTrainingError + denormalizedModelValidationError)/3))


fin = time.time()
print("\nTiempo ejecucion: " + str(fin-inicio))

# Grafico de errores
Errores, ax = plt.subplots()
ax.plot(trainingErrorsDenormalized, color = 'tab:blue', label = 'trainingError')
ax.plot(validationErrorsDenormalized, color = 'tab:red' , label = 'validationError')
ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
ax.legend(loc = 'upper right')

# Grafico de pesos y umbral
weight1, weight2, weight3, weight4, weight5, weight6, weight7, weight8 , threshold = ([] for i in range(9))
models = (myNeurone.getAllModels())
for i in range(len(models)):
    model = models[i]
    weights = model[0]
    threshold.append(model[1])
    weight1.append(weights[0])
    weight2.append(weights[1])
    weight3.append(weights[2])
    weight4.append(weights[3])
    weight5.append(weights[4])
    weight6.append(weights[5])
    weight7.append(weights[6])
    weight8.append(weights[7])

Peso1, ax = plt.subplots()
ax.plot(weight1, label = 'weight1')
ax.plot(weight2, label = 'weight2')
ax.plot(weight3, label = 'weight3')
ax.plot(weight4, label = 'weight4')
ax.plot(weight5, label = 'weight5')
ax.plot(weight6, label = 'weight6')
ax.plot(weight7, label = 'weight7')
ax.plot(weight8, label = 'weight8')
ax.plot(threshold, label = 'threshold')
ax.legend(loc = 'upper right')
plt.show()