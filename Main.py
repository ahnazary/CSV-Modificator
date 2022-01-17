import glob
import os

from ReadContent import ReadContent

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input files/*")


for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "txt":
        readContent = ReadContent(file)

for file in glob.glob(path):
    print("file is: ", file, "\n")
    readContent = ReadContent(file)

    if ReadContent.getFileFormat(file) == "csv":
        # readContent.removeDuplicateRowsFromCSV()
        readContent.checkVehicleCount()
        print("first row is : ", readContent.getFirstRow())
        print("last row is : ", readContent.getLastRow())
        print("headers are : ", readContent.getHeaders())
        print("number of rows is : ", readContent.getSize(), "\n")


