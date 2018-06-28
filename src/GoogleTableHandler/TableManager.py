import gspread
import re

from numpy.core import float128


class TableManager:

    def __init__(self, __client, __tablename):
        self.__countParameters = 0
        self.__countMetrics = 0
        self.__tablename = __tablename
        self.__client = __client
        self.__table = self.__openTable()

    def __getTableListfromEdit(self):
        tableList = self.__table.get_all_values()
        return tableList

    def __openTable(self):
        try:
            if re.match("http", self.__tablename) :
                table=self.__client.open_by_url(self.__tablename).sheet1
            else:
                table = self.__client.open(self.__tablename).sheet1
        except gspread.exceptions.SpreadsheetNotFound:
            print("[ERROR]: You can not open this GoogleSheets!")
            exit(5)
        return table

    def getParamList(self):
        tableList= self.__getTableListfromEdit()
        paramList = []
        countMetrics = 0
        for parameter in tableList:
            if re.match("Parameter", parameter[0]):
                if (countMetrics != 0) and (len(parameter[1:]) != countMetrics):
                    print("Count parameter error!")
                    # TODO: ErrorHandler
                    exit(6)
                paramList.append(list(map(float128, parameter[1:])))
                countMetrics = len(paramList[0])
        return paramList

    def setParamList(self, list):
        self.__table.clear()
        for i in range(len(list)):
            self.__table.delete_row(i+1)
            self.__table.insert_row((["Parameter " + str(i+1)] + list[i]), i+1)