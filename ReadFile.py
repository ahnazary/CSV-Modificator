import csv

class ReadFile():
    def __init__(self, fileAddress):
        self.fileAddress = fileAddress
        self.header = []
        self.rows = []
        file = open(self.fileAddress)
        csvReader = csv.reader(file)
        self.header = next(csvReader)

        for row in csvReader:
            self.rows.append(row)

        file.close()

    def getFirstRow(self):
        return self.rows[0]

    def getLastRow(self):
        return self.rows[-1]

    def getHeaders(self):
        return self.header

    #returns number of rows in CSV formatted file
    def getSize(self):
        return len(self.rows)