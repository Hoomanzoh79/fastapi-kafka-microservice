# main.py (FastAPI Consumer)
from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio

from .kafka_consumer import consume_messages

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    consuming_task = asyncio.create_task(consume_messages())
    yield
    consuming_task.cancel()

app.router.lifespan_context = lifespan