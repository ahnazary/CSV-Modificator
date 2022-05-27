FROM python:latest

WORKDIR /CSVModifier


EXPOSE 9000
EXPOSE 9092
EXPOSE 2181
COPY . .

RUN pip install -r requirements.txt

RUN ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic testTopic --replication-factor 1 --partitions 1
RUN ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic testTopic --describe


CMD [ "python", "Consumer.py" ]
