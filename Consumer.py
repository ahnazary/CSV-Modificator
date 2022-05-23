import json

from kafka import KafkaConsumer
from Spark import Spark

if __name__ == "__main__":
    consumer = KafkaConsumer("testTopic",
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='latest',
                             group_id='testTopic1')
    print("starting the consumer ...")
    for msg in consumer:
        spark = Spark(json.loads(msg.value)['csvStr'], json.loads(msg.value)['fileName'])
        print(spark.modifyDict(dropna=True, min_avgSpeed=80).show(20))
        spark.removeTempFile()
