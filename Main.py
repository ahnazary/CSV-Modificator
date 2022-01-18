import glob
import os

from ReadContent import ReadContent
from RulesAndFilters import RulesAndFilters

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input files/*")


for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "txt":
        readContent = ReadContent(file)

for file in glob.glob(path):
    readContent = ReadContent(file)

    if ReadContent.getFileFormat(file) == "csv":
        print("file is: ", file)

        rulesAndFilters = RulesAndFilters(file)

        # rulesAndFilters.removeDuplicateRowsFromCSV()
        rulesAndFilters.setValueRange("vehicleCount", "not equal", 0)
        rulesAndFilters.setValueRange("avgSpeed", "smaller than", 60)
        rulesAndFilters.checkTypeOfValue("avgSpeed", int)
        rulesAndFilters.removeInvalidTimeStamps()
        rulesAndFilters.removeTimeStampsNotDividableBy5()

        print("first row is : ", readContent.getFirstRow())
        print("last row is : ", readContent.getLastRow())
        print("headers are : ", readContent.getHeaders())
        print("number of rows is : ", readContent.getSize(), "\n")




