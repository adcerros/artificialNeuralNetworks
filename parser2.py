import sys;


class parser:

    def __init__(self, path):
        # Se leen las lineas y se limpian los saltos de linea
        filePointer = open(path, "r")
        textLines = filePointer.readlines()
        numberOfLines = len(textLines)
        for i in range(numberOfLines):
            textLines[i] = textLines[i].strip('\n')

        # Construccion matriz de datos
        data = []
        for i in range(numberOfLines):
            floatLine = []
            line = (textLines[i].split(", "))
            numberOfColumns = len(line) 
            for j in range(numberOfColumns):
                # Se hace un cast a float
                floatLine.append(float(line[j]))
            data.append(floatLine)
            # El siguiente print es solo para comprobaciones
            print(floatLine)

parser("datos.txt")