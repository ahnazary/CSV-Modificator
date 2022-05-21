import json
import time

from kafka import KafkaProducer

from Data import get_registered_user


def jsonSerializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=jsonSerializer)

if __name__ == "__main__":
    while True:
        registeredUser = get_registered_user()
        print(registeredUser)
        producer.send('registeredUser', registeredUser)
        time.sleep(4)

