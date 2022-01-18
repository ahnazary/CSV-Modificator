from ReadContent import ReadContent


class RulesAndFilters(ReadContent):
    def __init__(self, fileAddress):
        super().__init__(fileAddress)

    def setValueRange(self, columnName, condition, value):

        if condition.lower() == "not equal":
            def removeInvalids():
                rowsToBeDeleted = 0
                if columnName in self.header:
                    index = self.header.index(columnName)
                    for row in self.rows:
                        if self.checkTypeOfVariable(row[index], int):
                            if int(row[index]) == value:
                                print("Invalid value : ", row)
                                rowsToBeDeleted += 1
                                self.rows.remove(row)
                    return rowsToBeDeleted

            while removeInvalids() != 0 and removeInvalids() is not None:
                removeInvalids()
            ReadContent.writeNewCSVFile(self, self.header, self.rows)

        elif condition.lower() == "greater than":
            def removeInvalids():
                rowsToBeDeleted = 0
                if columnName in self.header:
                    index = self.header.index(columnName)
                    for row in self.rows:
                        if self.checkTypeOfVariable(row[index], int):
                            if int(row[index]) < value:
                                print("Invalid value : ", row)
                                rowsToBeDeleted += 1
                                self.rows.remove(row)
                    return rowsToBeDeleted

            while removeInvalids() != 0 and removeInvalids() is not None:
                removeInvalids()
            ReadContent.writeNewCSVFile(self, self.header, self.rows)

        elif condition.lower() == "lower than" or condition.lower() == "smaller than":
            def removeInvalids():
                rowsToBeDeleted = 0
                if columnName in self.header:
                    index = self.header.index(columnName)
                    for row in self.rows:
                        if self.checkTypeOfVariable(row[index], int):
                            if int(row[index]) > value:
                                print("Invalid value : ", row)
                                rowsToBeDeleted += 1
                                self.rows.remove(row)
                    return rowsToBeDeleted

            while removeInvalids() != 0 and removeInvalids() is not None:
                removeInvalids()
            ReadContent.writeNewCSVFile(self, self.header, self.rows)

    def removeDuplicateRowsFromCSV(self):
        newRows = []
        for row in self.rows:
            if row not in newRows:
                newRows.append(row)
            elif row in newRows:
                print("Duplicate Row : ", row)
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
        
    def checkTypeOfValue(self, columnName, typeOfValue):
        for item in self.header:
            if columnName in item.lower():
                index = self.header.index(item)

                for row in self.rows:
                    if not self.checkTypeOfVariable(row[index], typeOfValue):
                        print("Invalid value type : ", row)
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

    @staticmethod
    def checkTypeOfVariable(var, typeOfVar):
        try:
            if isinstance(var, typeOfVar):
                return True
        except:
            return False