from base.es import es as es_base
from base.mongo import mongo
from django.utils import timezone
from django.conf import settings
from elasticsearch.client import IndicesClient
from bson import ObjectId

class CRUD:
    client_mongo = None
    client_es = None
    collection = None
    index = None

    def __init__(self, collection:str) -> None:
        self.client_es = es_base.ESBase().client
        self.client_mongo = mongo.MongoBase(collection=collection).collection
        self.collection = collection

        if settings.TESTING:
            self.index = 'test_'+ collection

    def get(self, data: dict, *args, **kwargs):
        pass

    def add(self, data: dict, *args, **kwargs):
        pass

    def add_bulk(self, data: list, *args, **kwargs):
        pass

    def update(self, id, data, *args, **kwargs):
        pass

    def delete(self, id: str, data, *args, **kwargs):
        pass

    def soft_delete(self, id, *args, **kwargs):
        pass

    def delete_bulk(self, id: list, *args, **kwargs):
        pass

    def drop(self, collection: str, *args, **kwargs):
        pass

# this is v1, maybe will be update further
class CRUD1(CRUD):

    def get(self, query: dict, soft_delete=True, *args, **kwargs):
        # check authorization here
        # pass

        term = {'term': {'__meta.status_delete': 0}}
        if soft_delete is True:
            idx = query['query'].get('bool') if isinstance(query['query'], dict) else None
            if idx is not None:
                idx = idx.get('filter')
                if idx is not None:
                    if isinstance(idx, list):
                        query['query']['bool']['filter'].append(term)
                    else:
                        query['query']['bool']['filter'] = [ idx, term ]
                else:
                    query['query']['bool']['filter'] = [term]
            else:
                if isinstance(query['query'], dict):
                    query['query']['bool'] = { 'filter': [term] }
                else:
                    query['query'] = {'bool': { 'filter': [term] }}


        print(query)
        result = self.client_es.search(
            index=self.index,
            query=query['query']
        )

        return result

    def add(self, data, *args, **kwargs):
        # check authorization here
        # pass

        data['__meta'] = {
            'deleted_at': None,
            'created_at': timezone.now().isoformat(),
            'status_delete': 0,
        }
        print(data)
        zz = data
        id_mongo = self.client_mongo.insert_one(data).inserted_id
        id_mongo = str(id_mongo)
        print( data, 'hah', zz)

        # idk, _id automatically added when inser_one perform
        data.pop('_id')

        indices = IndicesClient(self.client_es)

        index_is_exist = bool(indices.exists(index=self.index))
        print('index', index_is_exist, isinstance(bool(index_is_exist), bool))
        if index_is_exist is False:
            # add = indices.create(index=self.index, body=es_base.ESBase().default['body']) # can
            add = self.client_es.indices.create(index=self.index, body=es_base.ESBase().default['body']) # can
            print('index2', add)

        add_es = self.client_es.index(
            index=self.index,
            id=str(id_mongo),
            document=data
        )

        return {
            'mongo': id_mongo,
            'es': add_es
        }

    def update(self, id: str, data: dict, *args, **kwargs):
        # check authorization here
        # pass

        update_mongo = self.client_mongo.update_one(
            filter={'_id': ObjectId(id)},
            update={'$set': data}
        )
        print(update_mongo)
        update_es = self.client_es.update(
            index=self.index,
            id=id,
            doc=data
        )

        return update_es

    def delete(self, id: str, *args, **kwargs):
        delete_mongo = self.client_mongo.delete_one(filter={'_id': ObjectId(id)})

        delete_es = self.client_es.delete(
            index=self.index,
            id=id
        )

        return delete_es

    def soft_delete(self, id, *args, **kwargs):
        data = {
            '__meta': {
                'deleted_at': timezone.now().isoformat(),
                'status_delete': 1,
            }
        }

        update_mongo = self.client_mongo.update_one(
            filter={'_id': ObjectId(id)},
            update={'$set': {
                '__meta.deleted_at': data['__meta']['deleted_at'],
                '__meta.status_delete': data['__meta']['status_delete'],
            }}
        )

        update_es = self.client_es.update(
            index=self.index,
            id=id,
            doc=data
        )


        return update_es

