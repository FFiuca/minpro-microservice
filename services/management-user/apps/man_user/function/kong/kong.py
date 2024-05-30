from config.kong import (
    HOST,
    PORT,
    LISTENER_HOST,
    LISTENER_PORT,
    PATH_GUEST,
    PATH_USER,
    URL_MAPPING
)
from urllib.parse import urljoin

class KongBase:
    def __init__(self) -> None:
        self.url = '{}:{}'.format(HOST, PORT)
        self.listener_url = '{}:{}'.format(LISTENER_HOST, LISTENER_PORT)


