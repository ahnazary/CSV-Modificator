import csv
import json
import os

import numpy
from dateutil.parser import parse


class ReadContent():
    def __init__(self, fileAddress):
        self.fileAddress = fileAddress
        self.header = []
        self.rows = []
        self.fileName = self.fileAddress.split('/')[-1].split('.')[0]

        # checks if the format is CSV
        if fileAddress.split('.')[-1].lower() == "csv":
            file = open(self.fileAddress)
            csvReader = csv.reader(file)

            # generates headers and rows lists
            self.header = next(csvReader)
            for row in csvReader:
                self.rows.append(row)
            file.close()

        # if format is not CSV, creates a new CSV file
        elif fileAddress.split('.')[-1].lower() == "txt":

            JSONObjects = []
            with open(self.fileAddress) as f:
                for jsonObj in f:
                    tempDict = json.loads(jsonObj)
                    JSONObjects.append(tempDict)

            # headers of the new CSV file that is going to be generated from JSON objects
            self.header.append("TIMESTAMP")
            self.header.append(self.fileName)

            # rows of the new CSV file that is going to be generated from JSON objects
            for obj in JSONObjects:
                for item in obj:
                    tempList = [item, obj[item]]
                    self.rows.append(tempList)

            # creating address for the new CSV file to be written
            self.writeNewCSVFile(self.header, self.rows)

    def getFirstRow(self):
        return self.rows[0]

    def getLastRow(self):
        return self.rows[-1]

    def getHeaders(self):
        return self.header

    # returns number of rows in CSV formatted file
    def getSize(self):
        return len(self.rows)

    @staticmethod
    def getFileFormat(fileAddress):
        return fileAddress.split('.')[-1].lower()

    def writeNewCSVFile(self, headers, rows):
        if self.getFileFormat(self.fileAddress) == 'csv':
            pathToWriteCSV = self.fileAddress
        else:
            my_path = os.path.abspath(os.path.dirname(__file__)) + "/input files/"
            temp = self.fileAddress.split("/")[-1].split(".")[0] + ".csv"
            pathToWriteCSV = os.path.join(my_path, temp)
        with open(pathToWriteCSV, 'w') as file:
            write = csv.writer(file)
            write.writerow(headers)
            write.writerows(rows)
        file.close()

    @staticmethod
    def isValidDate(string, fuzzy=False):
        try:
            parse(string, fuzzy=fuzzy)
            return True
        except ValueError:
            return False

    def getMaxValueOfColumn(self, columnName):
        if columnName in self.header:
            tempList = []
            max([], default="EMPTY")
            index = self.header.index(columnName)
            for row in self.rows:
                try:
                    tempList.append(int(row[index]))
                except:
                    continue
            return max(tempList)

    def getMinValueOfColumn(self, columnName):
        if columnName in self.header:
            tempList = []
            min([], default="EMPTY")
            index = self.header.index(columnName)
            for row in self.rows:
                try:
                    tempList.append(int(row[index]))
                except:
                    continue
            return min(tempList)

    def getAvgValueOfColumn(self, columnName):
        if columnName in self.header:
            tempList = []
            index = self.header.index(columnName)
            for row in self.rows:
                try:
                    tempList.append(int(row[index]))
                except:
                    continue

            npArr = numpy.array(tempList)
            return numpy.mean(npArr)

    @staticmethod
    def checkTypeOfVariable(var, typeOfVar):
        try:
            if isinstance(var, typeOfVar):
                return True
        except:
            return False