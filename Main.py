import glob
import os

from ReadFile import ReadFile

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input files/*")

for file in glob.glob(path):
    readFile = ReadFile(file)
    print(readFile.getFirstRow())
    print(readFile.getLastRow())
    print(readFile.getHeaders())
    print(readFile.getSize())

