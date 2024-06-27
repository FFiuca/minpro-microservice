from pymongo import MongoClient
from django.conf import settings


client = MongoClient(
    host=settings.MONGODB_SETTINGS['host'],
    port=settings.MONGODB_SETTINGS['port'],
    username=settings.MONGODB_SETTINGS.get('username'),
    password=settings.MONGODB_SETTINGS.get('password'),
    maxPoolSize=50  # Adjust pool size as needed
)

def get_db_handle():
    db = client[settings.MONGODB_SETTINGS['db']]
    return db
