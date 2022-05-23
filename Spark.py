import json
import os
import glob
import warnings

from pyspark.ml.feature import Imputer, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

warnings.filterwarnings("ignore")

projectPath = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(projectPath, "input files/*")
outputFilesPath = os.path.join(projectPath, "output files")
inputFilesPath = os.path.join(projectPath, "input files/*")
tempFilePath = os.path.join(projectPath, "input files/tempFile.csv")


class Spark:
    def __init__(self, csv):
        self.csv = csv
        f = open(tempFilePath, "a")
        f.write(csv)
        f.close()

    def modifyDict(self, **kwargs):
        spark = SparkSession.builder.appName('Practice').getOrCreate()
        dfPyspark = spark.read.option('header', 'true').csv(tempFilePath, inferSchema=True)
        if kwargs['dropna']:
            dfPyspark = dfPyspark.na.drop(how='any')
        if kwargs['min_avgSpeed'] is not None:
            dfPyspark = dfPyspark.filter("avgSpeed>=" + str(kwargs['min_avgSpeed']))
        # dfPyspark.write.option("header", True).csv(os.path.join(outputFilesPath, inputFile.split('/')[-1]))
        # print(dfPyspark.show(5))
        return dfPyspark

    def removeTempFile(self):
        try:
            os.remove(tempFilePath)
        except:
            pass