# backend/app/database.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import get_settings

settings = get_settings()

# Define Base here so models can import it without triggering engine creation
Base = declarative_base()

# Engine and session factory will be created on demand
_engine = None
_async_session_maker = None

def get_engine():
    """Lazy creation of async engine."""
    global _engine
    if _engine is None:
        _engine = create_async_engine(
            settings.database_url.replace("postgresql://", "postgresql+asyncpg://"),
            echo=True,
            future=True
        )
    return _engine

def get_session_maker():
    """Lazy creation of async session maker."""
    global _async_session_maker
    if _async_session_maker is None:
        _async_session_maker = sessionmaker(
            get_engine(), class_=AsyncSession, expire_on_commit=False
        )
    return _async_session_maker

async def get_db():
    """FastAPI dependency that provides a database session."""
    async with get_session_maker()() as session:
        yield session