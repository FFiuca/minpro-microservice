from urllib.parse import urljoin
from django.conf import settings

HOST = settings.KONG_HOST_API
PORT = settings.KONG_HOST_PORT

LISTENER_HOST = 'http://localhost'
LISTENER_PORT = '8000'

PATH_GUEST = 'guest'
PATH_USER = 'user'

ALGORITHM= "HS256"
KEY_CLAIM_NAME = 'kid'
CLAIM_TO_VERIFY = 'exp'
EXPIRATION = 172800 # seconds

class KongBase:
    def __init__(self) -> None:
        self.url = '{}:{}'.format(HOST, PORT)
        self.listener_url = '{}:{}'.format(LISTENER_HOST, LISTENER_PORT)


