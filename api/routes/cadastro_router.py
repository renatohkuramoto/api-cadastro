import logging
from fastapi import APIRouter, Request
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from api.models.cadastro_model import CadastroIn
from api.utils import response_success, extract_token
from api.dependencies import con_sql
from api.controller import CadastroController
from api.auth import JWTBearer, JWTHandler

router = APIRouter()

@router.get('/get-cadastro', dependencies=[Depends(JWTBearer())])
async def get_cadastro(request: Request, session: AsyncSession = Depends(con_sql)):
    try:
        token = extract_token(request.headers['authorization'])
        data_token = JWTHandler.decode_token(token)
        if (data_token):
            response = await CadastroController().get_cadastro(data_token['email'], session)
            if response:
                return response_success(response)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'status': False, 'message': 'Cadastro não localizado.'})
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'status': False, 'message': 'Token inválido ou expirado.'})
    except Exception as error:
        logging.warning(error)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'status': False, 'message': 'Token inválido ou expirado.'})

@router.post('/create-cadastro')
async def create_cadastro(cadastro: CadastroIn, session: AsyncSession = Depends(con_sql)):
    response = await CadastroController().create_cadastro(cadastro, session)
    if (response is True):
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail={'status': True, 'message': 'Registro salvo.'})
    elif (response is False):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': False, 'message': 'Registro já existe.'})
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'status': False, 'message': 'Server Error'})

@router.put('/update-cadastro', dependencies=[Depends(JWTBearer())])
async def update_cadastro(cadastro: CadastroIn, request: Request, session: AsyncSession = Depends(con_sql)):
    try:
        token = extract_token(request.headers['authorization'])
        data_token = JWTHandler.decode_token(token)
        if (data_token):
            response = await CadastroController().update_cadastro(data_token['email'], cadastro, session)
            if (response):
                return response_success(response)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': False, 'message': 'Erro ao atualizar.'})
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'status': False, 'message': 'Token inválido ou expirado.'})
    except Exception as error:
        logging.warning(error)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={'status': False, 'message': 'Token inválido ou expirado.'})