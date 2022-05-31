import re

import psycopg2
import os
import shutil
import warnings

from ReadContent import ReadContent
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
        self.dbFileName = fileName.split('.')[0]
        self.fileName = fileName.split('.')[0] + '(modified).' + fileName.split('.')[-1]
        print('file name is : {}'.format(self.fileName))
        self.removeTempFile()
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
            try:
                dfPyspark = dfPyspark.na.drop(how='any')
            except:
                raise Exception('dropna is not supported for this data type')
        if kwargs['min_avgSpeed'] is not None:
            try:
                dfPyspark = dfPyspark.filter("avgSpeed>=" + str(kwargs['min_avgSpeed']))
            except:
                raise Exception('min_avgSpeed does not exist in this data frame')
        if kwargs['max_avgSpeed'] is not None:
            try:
                dfPyspark = dfPyspark.filter("avgSpeed<=" + str(kwargs['max_avgSpeed']))
            except:
                raise Exception('max_avgSpeed does not exist in this data frame')

        self.deleteIfDirExists(os.path.join(outputFilesPath, self.fileName))
        dfPyspark.write.option("header", True).csv(os.path.join(outputFilesPath, self.fileName))
        return dfPyspark

    def removeTempFile(self):
        if os.path.exists(tempFilePath):
            os.remove(tempFilePath)

    def writeToDB(self, sparkDF):
        con = psycopg2.connect(
            host="172.18.0.4",
            database="SparkConsumer",
            user="user",
            password="admin")
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS {};'.format(self.dbFileName))

        queryStr = 'CREATE TABLE {} ('.format(self.dbFileName)
        for i in range(len(sparkDF.schema.names)):
            typeStr = 'timestamp' if re.match('.*timestamp.*', sparkDF.schema.names[i].lower()) else 'TEXT'
            if i == len(sparkDF.schema.names) - 1:
                queryStr = queryStr + sparkDF.schema.names[i] + ' ' + typeStr + ');'
            else:
                queryStr = queryStr + sparkDF.schema.names[i] + ' ' + typeStr + ', '
        # print(queryStr)
        cur.execute(queryStr)
        queryStr = 'INSERT INTO {}'.format(self.dbFileName)
        for i in range(len(sparkDF.schema.names)):
            if i == 0:
                queryStr += '({}, '.format(sparkDF.schema.names[i])
            elif i == len(sparkDF.schema.names) - 1:
                queryStr += '{})'.format(sparkDF.schema.names[i])
            else:
                queryStr += '{}, '.format(sparkDF.schema.names[i])
        queryStr += ' VALUES '
        checkPointStr = queryStr
        for row in sparkDF.collect():
            iNum = 0
            for j in row:
                if not isinstance(j, int) and not isinstance(j, float):
                    j = '\'' + str(j) + '\''
                if iNum == 0:
                    queryStr += '({}, '.format(j)
                if iNum == len(row) - 1:
                    queryStr += '{})'.format(j)
                if iNum != len(row) - 1 and iNum != 0:
                    queryStr += '{}, '.format(j)
                iNum += 1
            # print(queryStr)
            cur.execute(queryStr)
            queryStr = checkPointStr

        con.commit()
        cur.close()
