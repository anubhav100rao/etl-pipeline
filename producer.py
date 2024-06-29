from faker import Faker
from kafka import KafkaProducer
import json
from time import sleep

fake = Faker()


def get_registered_data():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'created_at': fake.year()
    }


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['192.168.1.2:9092'],
    value_serializer=json_serializer
)


if __name__ == '__main__':
    while True:
        data = get_registered_data()
        producer.send('registered_user', value=data)
        print(data)
        sleep(3)
