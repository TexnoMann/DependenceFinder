import  sys
class ConsoleProgressBar:
    def __init__(self, sizeLine, countIteration):
        self.__currentSizeBar = 0
        self.__currentProgress = 0
        self.__sizeLine = sizeLine
        self.__countIteration = countIteration
        self.__sizeIterable = self.__sizeLine / self.__countIteration

    def startProcess(self):
        print("[DependFinder] Solver Progress:")

    def updateProgress(self, countDepend):
        self.__currentProgress += 1
        self.__currentSizeBar = round(1.0*self.__currentProgress * self.__sizeIterable)

        self.__bar = u'🐱' * self.__currentSizeBar + ' ' * (self.__sizeLine - self.__currentSizeBar)

        percents = round(100.0 * self.__currentProgress / float(self.__countIteration), 1)
        sys.stdout.write('[%s] %s%s ...%s\r' % (self.__bar, percents, '%', " Найдено зависимостей: "+str(countDepend)+" из "+ str(self.__currentProgress) + " проверенных. "))
        sys.stdout.flush()