class OutputFileWriter:
    def __init__(self, filenameOut):
        self.__filenameOut = filenameOut
        self.__file = open(self.__filenameOut, "w")

    def writeResult(self, NumberParam1, NumberParam2, type):
        self.__file.write("Параметр " + str(NumberParam1) + " связан с параметром " + str(NumberParam2) +": Зависимость "+ type + "\n")