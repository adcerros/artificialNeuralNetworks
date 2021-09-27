from model import neurone
from dataAdmin import dataPreparator
import time


inicio = time.time()
print()
print()
myPreparator = dataPreparator()

trainingSet, validationSet, testSet = myPreparator.preparator("datos.txt")
trainingIn, trainingOut = myPreparator.getInOut(trainingSet)
validationIn, validationOut = myPreparator.getInOut(validationSet)
testIn, testOut = myPreparator.getInOut(testSet)
myNeurone = neurone(8)
myNeurone.train(trainingIn, trainingOut, validationIn, validationOut, 5000, 0.05)
fin = time.time()
print("Tiempo ejecucion: " + str(fin-inicio))