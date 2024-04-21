from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy import create_engine

from v1.config import settings

# Each base gets its own metadata
SyncBase = declarative_base()
AsyncBase = declarative_base()


class PostgresManager:
    _engines = {}

    @classmethod
    def get_engine(cls, is_async):
        key = is_async
        if key not in cls._engines:
            if is_async:
                engine = create_async_engine(
                    settings.db_url,
                    # echo=True,
                )
                AsyncBase.metadata.bind = engine
            else:
                engine = create_engine(
                    settings.db_url,
                    # echo=True,
                )
                SyncBase.metadata.bind = engine
            cls._engines[key] = engine
        return cls._engines[key]


class PostgresSession:
    def __init__(self, is_async=False):
        self.is_async = is_async
        self.engine = PostgresManager.get_engine(is_async)
        self.session = None

        if is_async:
            self.session_factory = sessionmaker(
                bind=self.engine, expire_on_commit=False, class_=AsyncSession
            )
        else:
            self.session_factory = sessionmaker(
                bind=self.engine, expire_on_commit=False
            )

    def __enter__(self):
        if self.is_async:
            raise RuntimeError("Use 'async with' for async mode")
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.close()

    async def __aenter__(self):
        if not self.is_async:
            raise RuntimeError("Session must be async for 'async with'")
        self.session = self.session_factory()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.commit()
        await self.session.close()
