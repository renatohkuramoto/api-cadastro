import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from api.config import get_database


def get_session_sql():
    try:
        engine = create_async_engine(get_database()['SQL_LITE'])
        return sessionmaker(engine, expire_on_commit=False,
                            class_=AsyncSession)
    except Exception as error:
        logging.warning(error)
        raise Exception('Database Error')
