# producer.py

from aiokafka import AIOKafkaProducer
import asyncio
from .kafka_config import KAFKA_BOOKER, TOPIC_NAME

async def send_message():
    # Create a Kafka producer instance
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOKER
    )
    # Start the producer
    await producer.start()
    try:
        # Send a message to the Kafka topic
        message = "Hello, Kafka!"
        await producer.send_and_wait(TOPIC_NAME, message.encode("utf-8"))
        print(f"Message sent: {message}")
    finally:
        # Stop the producer
        await producer.stop()

# Run the producer
if __name__ == "__main__":
    asyncio.run(send_message())
