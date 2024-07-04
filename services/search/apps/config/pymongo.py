from pymongo import MongoClient
from django.conf import settings


db = None
client = MongoClient(
            host=settings.MONGODB_SETTINGS['host'],
            port=settings.MONGODB_SETTINGS['port'],
            username=settings.MONGODB_SETTINGS.get('username'),
            password=settings.MONGODB_SETTINGS.get('password'),
            maxPoolSize=50
        )

def get_db_handle():
    global db
    db = client[settings.MONGODB_SETTINGS['db']]
    return db

def get_db_test_handle():
    global db
    db = client[settings.MONGODB_SETTINGS['test']['db']]
    return db

if settings.TESTING is False:
    get_db_handle()
else:
    get_db_test_handle()

