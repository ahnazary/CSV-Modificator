import csv
import glob
import json
import os
import re
import time

from kafka import KafkaProducer

projectPath = os.path.abspath(os.path.dirname(__file__))
inputFilesPath = os.path.join(projectPath, "input files/*")
outputFilesPath = os.path.join(projectPath, "output files")


def jsonSerializer(data):
    return json.dumps(data).encode('utf-8')


def csvToStr(filePath):
    csvStr = ''
    with open(filePath, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                csvStr = csvStr + str(cell) + ','
            csvStr = csvStr + '\n'
    return {'csvStr': re.sub(',\n', '\n', csvStr), 'fileName': filePath.split('/')[-1]}


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=jsonSerializer)

if __name__ == "__main__":
    for inputFile in glob.glob(inputFilesPath):
        print(csvToStr(inputFile))
        producer.send('testTopic', csvToStr(inputFile))
        time.sleep(4)
