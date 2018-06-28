import random
from cmath import *

import numpy as np


class RandomDependGenerator:
    def __init__(self, __countGenParameters, __maxvalue, __randomError):
        self.__maxvalue=__maxvalue
        self.__randomError=__randomError
        self.__currentGenParameters = [[1.0, 2.0, 3.0]]
        self.__countGenParameters = __countGenParameters


    def randomGeneratedDepend(self):
        for i in range(self.__countGenParameters-1):
            fun = random.randint(0, 2)
            if fun == 0:
                p = self.__expGen()
            elif fun == 1:
                p = self.__linGen()
            else: p = self.__quadGen()
            self.__currentGenParameters.append(p)
        return self.__currentGenParameters

    def __expGen(self):
        a = random.randint(-self.__maxvalue*4, self.__maxvalue*4)/2.0
        error = random.randint(-self.__randomError, self.__randomError)/100.0
        numberparam1 = random.randint(0, len(self.__currentGenParameters)-1)
        param1 = np.array(self.__currentGenParameters[numberparam1], dtype=np.float128)
        param2 = list(map(lambda x: float(np.round(((a*np.exp(x)).real + (a*np.exp(x)*error).real), 3)), param1))
        return param2

    def __linGen(self):
        a = random.randint(-self.__maxvalue*4, self.__maxvalue * 4) / 2.0
        b = random.randint(-self.__maxvalue*4, self.__maxvalue * 4) / 2.0
        error = random.randint(-self.__randomError, self.__randomError) / 100.0
        numberparam1 = random.randint(0, len(self.__currentGenParameters) - 1)
        param1 = np.array(self.__currentGenParameters[numberparam1], dtype=np.float128)
        param2 = list(map(lambda x: float(np.round(((a * x + b) + (a * x +b) * error), 3)), param1))
        return param2


    def __quadGen(self):
        a = random.randint(-self.__maxvalue*4, self.__maxvalue * 4) / 2.0
        error = random.randint(-self.__randomError, self.__randomError) / 100.0
        numberparam1 = random.randint(0, len(self.__currentGenParameters) - 1)
        param1 = np.array(self.__currentGenParameters[numberparam1], dtype=np.float128)
        param2 = list(map(lambda x: float(np.round((a*x*x + a*x*x*error), 3)), param1))
        return param2