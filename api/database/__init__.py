import databases
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from api.config import get_database
from api.database.sessions import *

Base = declarative_base()

database = databases.Database(get_database()['SQL_LITE'])
engine = create_async_engine(get_database()['SQL_LITE'])