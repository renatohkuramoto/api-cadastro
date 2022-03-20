import logging
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_jwt_auth import AuthJWT
from api.auth import JWTBearer
from api.models import Auth
from api.controller import CadastroController
from api.auth import JWTHandler, denylist
from api.dependencies import con_sql
from api.utils.encrypt import Encrypt


router = APIRouter()


@router.post('/login', response_description='Obter token de acesso', name='Autenticação')
async def login(auth: Auth, session: AsyncSession = Depends(con_sql)):
    password_db = await CadastroController().get_senha(auth, session)
    if password_db:
        if (Encrypt().verify_password(auth.senha, password_db)):
            return JWTHandler.sing_in(auth.email)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={'status': False, 'message': 'Credenciais inválidas.'})


@router.get('/logoff', dependencies=[Depends(JWTBearer())])
async def logoff(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        jti = Authorize.get_raw_jwt()['jti']
        denylist.add(jti)
        return {'detail': 'Token de acesso foi revogado.'}
    except Exception as error:
        logging.warning(error)