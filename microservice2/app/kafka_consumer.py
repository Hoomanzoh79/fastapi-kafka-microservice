# consumer.py
from aiokafka import AIOKafkaConsumer
import asyncio
from .kafka_config import KAFKA_BOOKER, TOPIC_NAME, GROUP_ID

async def consume_messages():
    # Create a Kafka consumer instance
    consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BOOKER,
        group_id=GROUP_ID,
        auto_offset_reset="earliest"  
    )
    # Start the consumer
    await consumer.start()
    try:
        # Continuously poll for new messages
        async for msg in consumer:
            print(f"Received message: {msg.value.decode('utf-8')}")
    finally:
        # Stop the consumer
        await consumer.stop()

# Run the consumer
if __name__ == "__main__":
    asyncio.run(consume_messages())
