FROM python:latest

WORKDIR /CSVModifier


EXPOSE 9000
EXPOSE 9092
EXPOSE 2181
COPY . .

RUN pip install -r requirements.txt


CMD [ "python", "Consumer.py" ]
