from fastapi import APIRouter, HTTPException, status
from api.controller import ConsultaCEP


router = APIRouter()

@router.get('/search-cep/<string:cep>')
async def search_cep(cep: str):
    data = await ConsultaCEP().search_cep(cep)
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'status': False, 'message': 'CEP não localizado.'})