import logging
import bcrypt
from api.utils import encode_utf


class Encrypt:
    def verify_password(self, password_send, password_db):
        try:
            if bcrypt.checkpw(encode_utf(password_send), password_db):
                return True
            return None
        except Exception as error:
            logging.warning(error)

    def hash_password(self, password):
        return bcrypt.hashpw(encode_utf(password), bcrypt.gensalt(rounds=8))
