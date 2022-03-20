from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.database import engine
from api.database import Base
from api.routes import (ConsultaCepRouter, CadastroRouter, AuthRouter)


app = FastAPI(
    title='API Cadastro',
    version='1.0.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(CadastroRouter, prefix='/cadastro', tags=['Cadastro'])
app.include_router(AuthRouter, prefix='/auth', tags=['Login'])
app.include_router(ConsultaCepRouter, prefix='/viacep', tags=['Consulta CEP'])