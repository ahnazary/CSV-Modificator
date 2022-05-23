
import os
import shutil
import warnings

from pyspark.sql import SparkSession

warnings.filterwarnings("ignore")

projectPath = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(projectPath, "input files/*")
outputFilesPath = os.path.join(projectPath, "output files")
inputFilesPath = os.path.join(projectPath, "input files/*")
tempFilePath = os.path.join(projectPath, "input files/tempFile.csv")


class Spark:
    def __init__(self, csv, fileName):
        self.csv = csv
        self.fileName = fileName.split('.')[0] + '(modified).' + fileName.split('.')[-1]
        print('fine name is : {}'.format(self.fileName))
        f = open(tempFilePath, "a")
        f.write(csv)
        f.close()

    def deleteIfDirExists(self, dirPath):
        if os.path.exists(dirPath) and os.path.isdir(dirPath):
            shutil.rmtree(dirPath)

    def modifyDict(self, **kwargs):
        spark = SparkSession.builder.appName('Practice').getOrCreate()
        dfPyspark = spark.read.option('header', 'true').csv(tempFilePath, inferSchema=True)
        if kwargs['dropna']:
            dfPyspark = dfPyspark.na.drop(how='any')
        if kwargs['min_avgSpeed'] is not None:
            dfPyspark = dfPyspark.filter("avgSpeed>=" + str(kwargs['min_avgSpeed']))
        self.deleteIfDirExists(os.path.join(outputFilesPath, self.fileName))
        dfPyspark.write.option("header", True).csv(os.path.join(outputFilesPath, self.fileName))
        return dfPyspark

    def removeTempFile(self):
        if os.path.exists(tempFilePath):
            os.remove(tempFilePath)
