from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from api.database import Base


class Cadastro(Base):
    __tablename__ = 'cadastro'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100))
    senha = Column(String(100))
    nome = Column(String(100))
    endereco = Column(String(100))
    cep = Column(String(100))
    estado = Column(String(100))
    cidade = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class CadastroIn(BaseModel):
    email: str
    senha: str
    nome: str
    endereco: str
    cep: str
    estado: str
    cidade: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'email@gmail.com',
                'senha': '4589665555',
                'nome': 'Pessoa Teste',
                'endereco': 'Av. Paulista',
                'cep': '000000000',
                'estado': 'São Paulo',
                'cidade': 'São Paulo'
            }
        }


class EmailSearch(BaseModel):
    email: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'email@gmail.com'
            }
        }


class Auth(BaseModel):
    email: str
    senha: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'email@gmail.com',
                'senha': '4589665555'
            }
        }