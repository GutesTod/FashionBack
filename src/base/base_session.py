from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from ..config import settings

engine = create_engine(settings.POSTGRES_URL)


async def get_session():
    session = sessionmaker(engine, expire_on_commit=False)
    return session