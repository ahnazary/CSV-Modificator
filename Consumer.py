import json
import re

import pandas as pd

from kafka import KafkaConsumer
from MySpark import Spark


if __name__ == "__main__":
    consumer = KafkaConsumer("testTopic",
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             group_id='testTopic')
    print("starting the consumer ...")
    for msg in consumer:
        if re.match('.*tempFile.csv', str(json.loads(msg.value)['fileName'])):
            continue
        print("message received, file {}".format(json.loads(msg.value)['fileName']))
        mySpark = Spark(json.loads(msg.value)['csvStr'], json.loads(msg.value)['fileName'])
        print(mySpark.modifyDict(dropna=True, min_avgSpeed=80, max_avgSpeed=100).show())
        mySpark.writeToDB(mySpark.modifyDict(dropna=True, min_avgSpeed=80, max_avgSpeed=100))
        mySpark.removeTempFile()
