# Normalizador de datos universal
def numberNormalizer(self, data):
    numberOfRows = len(data)
    numberOfColumns = len(data[0])
    listOfMax = []
    listOfMin = []
    # Busqueda de maximos y minimos recorriendo la matriz por columnas
    for j in range(numberOfColumns):
        # Se inicializan los valores con el primer elemento de la columna en cada iteraccion
        max = data[0][j]
        min = data[0][j]
        for i in range(numberOfRows):
            currentElement = data[i][j]
            if currentElement > max:
                max = currentElement
            if currentElement < min:
                min = currentElement
        # Cada elemento de la lista representa el min/max de cada columna de la lista global
        listOfMax.append(max)
        listOfMin.append(min)
    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            data[i][j] = (data[i][j] - listOfMin[j])/(listOfMax[j]-listOfMin[j])
    return data