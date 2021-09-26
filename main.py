import adaline
from dataAdmin import dataPreparator
import time


inicio = time.time()
mypreparator = dataPreparator()

trainingSet, validationSet, testSet = mypreparator.preparator("datos.txt")
fin = time.time()
print("Tiempo ejecucion: " + str(fin-inicio))