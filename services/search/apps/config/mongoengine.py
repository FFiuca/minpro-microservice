import mongoengine
import importlib

def connect():
    from django.conf import settings # use delayed import to prevent cyclic import
    # print('a', settings.MONGODB_SETTINGS)

    mongoengine.connect(
        db=settings.MONGODB_SETTINGS['db'],
        host=settings.MONGODB_SETTINGS['host'],
        username=settings.MONGODB_SETTINGS['username'],
        password=settings.MONGODB_SETTINGS['password']
    )
