from cmath import exp, log
import numpy as np



class DependenceFinder:

    def __init__(self, __maxRelativeError):
        self.__maxRelativeError = __maxRelativeError



    def expAproxMNK(self, param1, param2):
        if not self.__checkAriphmetics(1e-10, 1e+20, 1e-10, 1e+5, param1, param2, True):
            return [[0.0], 0.0, False]
        return self.__getAexp(param1, param2)

    def linearAproxMNK(self, param1, param2):
        if not self.__checkAriphmetics(1e-10, 1e+20, 1e-10, 1e+20, param1, param2, False):
            return [[0.0, 0.0], 0.0, False]
        return self.__getABlin(param1, param2)


    def quadAproxMNK(self, param1, param2):
        if not self.__checkAriphmetics(1e-10, 1e+20, 1e-10, 1e+10, param1, param2, False):
            return [[0.0], 0.0, False]
        return self.__getAquad(param1, param2)

    def __getAquad(self, param1, param2):
        maxRelError = -1
        n = len(param1)
        a = np.sum(list(map(lambda x, y: x * x * y, param2, param1))) / np.sum(list(map(lambda x: x ** 4, param2)))

        if abs(a) < 1e-10: return [[0], 0.0, False]
        for i in range(n):
            relError = -1
            if param2[i] != 0:
                relError = np.abs((a * param2[i] ** 2 - param1[i]) / (a * param2[i] ** 2))

            if relError > maxRelError:
                maxRelError = relError
        if maxRelError == -1 or maxRelError > self.__maxRelativeError:
            return [[0], 0.0, False]
        else:
            return [[a], maxRelError, True]

    def __getABlin(self, param1, param2):
        maxRelError = -1
        n=len(param1)

        a = (n * (np.sum(list(map(lambda x, y: x * y, param2, param1)))) - np.sum(param1) * np.sum(param2)) / (
                    n * np.sum(list(map(lambda x: x * x, param2))) - np.sum(param2) ** 2)
        b = (np.sum(param1) - a * np.sum(param2)) / n

        if a == 0.0: return [[a], 0.0, False]
        for i in range(n):
            if param2[i] != 0.0:
                relError = np.abs(((a * param2[i] + b) - param1[i]) / (a * param2[i] + b))
            else:
                relError = np.abs(param1[i])

            if relError > maxRelError:
                maxRelError = relError

        if maxRelError == -1 or maxRelError > self.__maxRelativeError:
            return [[0, 0], 0.0, False]
        else:
            return [[a, b], maxRelError, True]

    def __getAexp(self, param1, param2):
        maxRelError = -1
        n = len(param1)
        a = np.exp(np.sum(list(map(lambda x, y: (np.log(y) - x), param2, param1))) / n)

        for i in range(n):
            relError = np.abs((a * np.exp(param2[i]) - param1[i]) / (a * np.exp(param2[i])))
            if relError > maxRelError:
                maxRelError = relError
        if maxRelError == -1 or maxRelError > self.__maxRelativeError:
            return [[0], 0.0, False]
        else:
            return [[a], maxRelError, True]

    def __checkAriphmetics(self, minparam1, maxparam1, minparam2, maxparam2, param1, param2, checkNegativeNumber):
        n = len(param1)
        countzero1 = 0
        countzero2 = 0
        repeat = param2[0]
        countrepeat = 0

        for i in range(n):
            if i != 0 and param2[i] == repeat:
                countrepeat += 1
            repeat = param2[i]
            if abs(param1[i]) < minparam1 or abs(param2[i]) > maxparam1 or (checkNegativeNumber and param1[i] < 0.0):
                countzero1 += 1
            if abs(param2[i]) < minparam2 or abs(param2[i]) > maxparam2:
                countzero2 += 1
        if countzero1 != 0 or countzero2 != 0 or countrepeat != 0:
            return False
        else: return  True