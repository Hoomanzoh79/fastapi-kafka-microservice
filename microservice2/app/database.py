from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker)
from sqlalchemy.orm import DeclarativeBase

DB_CONNECTION_STRING = "postgresql+asyncpg://postgres:1234@database:5432/cart-db"

engine = create_async_engine(
    DB_CONNECTION_STRING,
    pool_size=20,
    max_overflow=10,
)
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False,
    expire_on_commit=False,bind=engine
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
