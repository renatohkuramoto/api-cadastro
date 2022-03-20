import time
import uuid
import jwt
from api.config import get_secret_key


JWT_SECRET = get_secret_key()['SECRET_KEY']
JWT_ALGORITHM = get_secret_key()['ALGO']


def token_response(token):
    return {
        'access_token': token
    }


def sing_in(email):
    payload = {
        'email': email,
        'type': 'access',
        'jti': str(uuid.uuid4()),
        'expires': time.time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded if decoded['expires'] >= time.time() else None
    except Exception:
        return None
