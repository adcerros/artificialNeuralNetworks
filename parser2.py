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
            for j in range(9):
                # Se hace un cast a float
                floatLine.append(float(line[j]))
            data.append(floatLine)
        print(data)



parser("datos.txt")