from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_session_sql

async def con_sql() -> AsyncSession:
    Session = get_session_sql()
    async with Session() as session:
        yield session

