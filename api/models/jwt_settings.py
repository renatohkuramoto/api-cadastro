from pydantic import BaseModel
from api.config import get_secret_key


class Settings(BaseModel):
    authjwt_secret_key: str = get_secret_key()['SECRET_KEY']
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {'access', 'refresh'}
