from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api.auth.auth_handler import decode_token
from fastapi_jwt_auth import AuthJWT
from api.models import Settings

denylist = set()

@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in denylist

@AuthJWT.load_config
def get_config():
    return Settings()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
      super(JWTBearer, self).__init__(auto_error=auto_error)
      
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication schema")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken):
        isTokenValid: bool = False
        try:
            payload = decode_token(jwtoken)
            in_deny_list = payload['jti'] in denylist
            if in_deny_list:
                payload = None
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
