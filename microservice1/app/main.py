# main.py (FastAPI Producer)
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from aiokafka import AIOKafkaProducer

from .kafka_config import KAFKA_BOOKER, TOPIC_NAME

app = FastAPI()

# Kafka producer instance
producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOKER)

@asynccontextmanager
async def lifespan(app: FastAPI):
    consuming_task = asyncio.create_task(producer.start())
    yield
    consuming_task.cancel()

app.router.lifespan_context = lifespan

@app.post("/send-message")
async def send_message(message: str):
    await producer.send_and_wait(TOPIC_NAME, message.encode("utf-8"))
    return {"status": "Message sent"}
