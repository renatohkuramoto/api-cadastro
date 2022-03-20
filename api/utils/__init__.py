import logging
import unicodedata
import re


def response_error(status_code):
    return {
        'status': False,
        'status_code': status_code
    }


def response_success(body):
    return {
        'data': body,
        'status': True,
        'status_code': 200
    }


def remove_characters(string):
    try:
        normalized = unicodedata.normalize('NFKD', string)
        normalized = u''.join([c for c in normalized if not unicodedata.combining(c)])
        return re.sub('[^a-zA-Z0-9 \\\]', '', normalized).replace(' ', '').upper()
    except Exception as error:
        logging.warning(error)
        return string


def encode_utf(string: str) -> str:
    return string.encode('utf-8')


def extract_token(bearer_token):
    try:
        return bearer_token.split(' ')[1]
    except Exception as error:
        logging.warning(error)