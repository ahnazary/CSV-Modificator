import csv
import json
import os


class ReadContent():
    def __init__(self, fileAddress):
        self.fileAddress = fileAddress
        self.header = []
        self.rows = []
        self.newHeader = []
        self.newRows = []

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
            self.newHeader.append("TIMESTAMP")
            self.newHeader.append("Output")

            # rows of the new CSV file that is going to be generated from JSON objects
            for obj in JSONObjects:
                for item in obj:
                    tempList = [item, obj[item]]
                    self.newRows.append(tempList)

            # creating address for the new CSV file to be written
            my_path = os.path.abspath(os.path.dirname(__file__)) + "/input files/"
            temp = self.fileAddress.split("/")[-1].split(".")[0] + ".csv"
            pathToWriteCSV = os.path.join(my_path, temp)
            with open(pathToWriteCSV, 'w') as file:
                write = csv.writer(file)
                write.writerow(self.newHeader)
                write.writerows(self.newRows)
            file.close()

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

    def removeDuplicateRowsFromCSV(self):
        newRows = []
        for elem in self.rows:
            if elem not in newRows:
                newRows.append(elem)
        self.newRows = newRows
        my_path = os.path.abspath(os.path.dirname(__file__)) + "/input files/"
        temp =  self.fileAddress.split("/")[-1].split(".")[0] + ".csv"
        pathToWriteCSV = os.path.join(my_path, temp)
        with open(pathToWriteCSV, 'w') as file:
            write = csv.writer(file)
            write.writerow(self.newHeader)
            write.writerows(self.newRows)
        file.close()