import json

from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer("registeredUser",
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             group_id='consumer-group-a')
    print("starting the consumer")
    for msg in consumer:
        print("Registered user = {}".format(json.loads(msg.value)))
