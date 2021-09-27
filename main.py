from model import neurone
from dataAdmin import dataPreparator
import time


inicio = time.time()
print()
print()
myPreparator = dataPreparator()

trainingSet, validationSet, testSet = myPreparator.preparator("datos.txt")
myNeurone = neurone(8)
myNeurone.train(trainingSet, validationSet, 5000,0.05)

fin = time.time()
print("Tiempo ejecucion: " + str(fin-inicio))