import json

from kafka import KafkaConsumer
from Spark import Spark

if __name__ == "__main__":
    consumer = KafkaConsumer("testTopic",
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='latest',
                             group_id='testTopic1')
    print("starting the consumer ...")
    # spark = Spark(csvStr)
    # print(spark.modifyDict(dropna=True, min_avgSpeed=104).show())
    # spark.removeTempFile()
    for msg in consumer:
        # print(json.loads(msg.value))
        spark = Spark(json.loads(msg.value)['csvStr'])
        print(spark.modifyDict(dropna=True, min_avgSpeed=70).show(20))
        spark.removeTempFile()
