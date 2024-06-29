from faker import Faker
from kafka import KafkaProducer

fake = Faker()


def get_registered_data():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'created_at': fake.year()
    }


producer = KafkaProducer(
    bootstrap_servers='192.168.1.2:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
)
