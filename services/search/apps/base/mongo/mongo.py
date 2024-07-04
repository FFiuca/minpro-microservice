from config import pymongo, mongoengine

class MongoBase():

    def __init__(self, collection= None,*args, **kwargs):
        self.collection = pymongo.db[collection]

        # print(self.collection)


