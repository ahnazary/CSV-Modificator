from ReadContent import ReadContent


class RulesAndFilters(ReadContent):
    def __init__(self, fileAddress):
        super().__init__(fileAddress)

    def checkVehicleCount(self):

        def removeInvalids():
            rowsToBeDeleted = 0
            if 'vehicleCount' in self.header:
                index = self.header.index("vehicleCount")
                for row in self.rows:
                    if int(row[index]) == 0:
                        print("Invalid Vehicle Count : ", row)
                        rowsToBeDeleted += 1
                        self.rows.remove(row)
                return rowsToBeDeleted

        print("rows to be deleted :", removeInvalids())
        while removeInvalids() != 0 and removeInvalids() is not None:
            removeInvalids()

        ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def removeDuplicateRowsFromCSV(self):
        newRows = []
        for row in self.rows:
            repeats = 1
            if row not in newRows:
                newRows.append(row)
            elif row in newRows:
                repeats += 1
                print("Duplicate Row : ", row, "repeats: ", repeats)
        self.rows = newRows

        self.writeNewCSVFile(self.header, self.rows)

    def removeInvalidTimeStamps(self):
        for item in self.header:
            if 'timestamp' in item.lower():
                index = self.header.index(item)

                for row in self.rows:
                    if not ReadContent.isValidDate(row[index]):
                        print("Invalid TimeStamp : ", row)
                        self.rows.remove(row)

        ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def removeTimeStampsNotDividableBy5(self):
        for item in self.header:
            if 'timestamp' in item.lower():
                index = self.header.index(item)

                for row in self.rows:
                    if ReadContent.isValidDate(row[index]) and ':' in row[index]:
                        tempList = row[index].split(':')
                        if len(tempList) == 3:
                            if int(tempList[1]) % 5 == 0 and int(tempList[2] == 0):
                                continue
                        elif len(tempList) == 2 and int(tempList[1]) % 5 == 0:
                            continue
                        else:
                            print("Invalid TimeStamp (not dividable by 5): ", row)
                            self.rows.remove(row)

        ReadContent.writeNewCSVFile(self, self.header, self.rows)
