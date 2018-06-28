import time
from click._unicodefun import click

from src.DependenceSolver.TestGenerator import RandomDependGenerator
from src.GoogleTableHandler.AutManager import *
from src.GoogleTableHandler.TableManager import *
from src.DependenceSolver.DependenceFinder import *
from src.Output.ConsoleProgressBar import *
from src.Output.OutputFileWriter import *


class GlobalSolver():

    def __init__(self):
        self.__accesDependList = ["Линейная", "Экспоненциальная", "Квадратичная", "Отсутствует"]
        self.__open()
        self.__countParameters = len(self.__parameters)

    def __open(self):
        self.__client = authorized()
        self.__tablename = input("Введите название гугл таблицы на вашем аккаунте или url адрес доступной таблицы: ")
        self.__tableMan = TableManager(self.__client, self.__tablename)
        #self.__gen = RandomDependGenerator(20, 1, 50)
        #self.__tableMan.setParamList(self.__gen.randomGeneratedDepend())
        self.__tableMan.getParamList()
        self.__parameters = self.__tableMan.getParamList()
        self.__outfilename = input("Введите имя файла для сохранения результатов: ")
        self.__fileWriter = OutputFileWriter(self.__outfilename)
        self.__maxRelError = float(input("Введите максимальное относительное отклонение в процентах от зависимости: "))/100.0
        self.__finder = DependenceFinder(self.__maxRelError)

    def solv(self):
        progressBar = ConsoleProgressBar(50, self.__countParameters*(self.__countParameters-1))
        progressBar.startProcess()
        countdep=0

        for p1 in range(len(self.__parameters)):
            for p2 in range(len(self.__parameters)):
                if p1 != p2:
                    #print(str(p1)+" "+str(p2))
                    dep = 3
                    minError = 1000000
                    resultL = self.__finder.linearAproxMNK(self.__parameters[p1], self.__parameters[p2])
                    resultE = self.__finder.expAproxMNK(self.__parameters[p1], self.__parameters[p2])
                    resultQ = self.__finder.quadAproxMNK(self.__parameters[p1], self.__parameters[p2])
                    rel=[resultL[2], resultE[2], resultQ[2]]
                    commonResultError = [resultL[1], resultE[1], resultQ[1]]


                    for i in range(len(commonResultError)):
                        if commonResultError[i] < minError and commonResultError[i] < self.__maxRelError and rel[i]:
                            minError = commonResultError[i]
                            dep = i
                    if dep != 3:
                        self.__fileWriter.writeResult(p1, p2, self.__accesDependList[dep])
                        countdep+=1
                    progressBar.updateProgress(countdep)