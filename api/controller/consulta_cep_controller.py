import logging
from api.utils.requests import get
from api.utils import remove_characters
from api.config import get_viacep


class ConsultaCEP:
    async def search_cep(self, cep):
        try:
            cep = remove_characters(cep)
            url = get_viacep()['url'] + f'{cep}/json/'
            response = await get(url)
            if (response['status_code'] == 200):
                return response
            return None
        except Exception as error:
            logging.warning(error)
            return None