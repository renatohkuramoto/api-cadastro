from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.models import Cadastro
from api.utils.encrypt import Encrypt
import logging


class CadastroController:
    async def get_cadastro(self, email, session: AsyncSession):
        try:
            sql_query = await session.execute(select(Cadastro).where(Cadastro.email == email))
            result = sql_query.scalars().first()
            sql_query.close()
            if (result):
                return {
                    'email': result.email,
                    'nome': result.nome,
                    'cep': result.cep,
                    'endereco': result.endereco,
                    'estado': result.estado,
                    'cidade': result.cidade,
                    'created_at': result.created_at,
                    'updated_at': result.updated_at
                }
            return None
        except Exception as error:
            logging.warning(error)
            await session.close()
    
    async def create_cadastro(self, data, session: AsyncSession):
        try:
            sql_query = await session.execute(select(Cadastro.email).where(Cadastro.email == data.email))
            exists = sql_query.first()
            if (not exists):
                data = {
                    'email': data.email.lower(),
                    'senha': Encrypt().hash_password(data.senha),
                    'nome': data.nome.upper(),
                    'endereco': data.endereco.upper(),
                    'cep': data.cep,
                    'estado': data.estado.upper(),
                    'cidade': data.cidade.upper(),
                    'created_at': datetime.now(),
                    'updated_at': None
                }
                new_cadastro = Cadastro(**data)
                session.add(new_cadastro)
                await session.commit()
                return True
            return False
        except Exception as error:
            logging.warning(error)
            await session.close()

    async def update_cadastro(self, email, data, session: AsyncSession):
        try:
            sql_query = await session.execute(select(Cadastro).where(Cadastro.email == email))
            register_db = sql_query.first()
            if (register_db):
                register_db[0].email = data.email
                register_db[0].senha = Encrypt().hash_password(data.senha)
                register_db[0].nome = data.nome.upper()
                register_db[0].endereco = data.endereco.upper()
                register_db[0].cep = data.cep
                register_db[0].estado = data.estado.upper()
                register_db[0].cidade = data.cidade.upper()
                register_db[0].updated_at = datetime.now()
                await session.commit()
                return True
            return None
        except Exception as error:
            logging.warning(error)
            await session.close()

    async def get_senha(self, email, session: AsyncSession):
        try:
            sql_query = await session.execute(select(Cadastro).where(Cadastro.email == email.email))
            result = sql_query.scalars().first()
            sql_query.close()
            if (result):
                return result.senha
            return None
        except Exception as error:
            logging.warning(error)
            session.close()
