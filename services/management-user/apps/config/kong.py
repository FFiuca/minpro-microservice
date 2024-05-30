from django.conf import settings

HOST = settings.KONG_HOST_API
PORT = settings.KONG_HOST_PORT

LISTENER_HOST = 'http://localhost'
LISTENER_PORT = '8000'

PATH_GUEST = 'guest'
PATH_USER = 'user'

URL_MAPPING = {
    'consumer' : {
        'list': '/consumers',
        'create': '/consumers',
        'update': '/consumers/{consumer_username_or_id}',
        'delete': '/consumers/{consumer_username_or_id}',
        'detail': '/consumers/{consumer_username_or_id}',
    },
    'jwt': {
        'list': '/consumers/{consumer}/jwt',
        'create': '/consumers/{consumer}/jwt',
        'delete': '/consumers/{consumer}/jwt/{jwt-id}',
    }
}

ALGORITHM= "HS256"
KEY_CLAIM_NAME = 'kid'
CLAIM_TO_VERIFY = 'exp'
EXPIRATION = 172800 # seconds
