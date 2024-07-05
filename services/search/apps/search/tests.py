from rest_framework.test import APITestCase
from search.functions.crud.crud import CRUD1
from faker import Faker


fake = Faker()
class SearchTest(APITestCase):

    def test_unit_add(self):
        cls = CRUD1('test2')
        data = {
            'name': fake.name()
        }
        print('data')
        add = cls.add(data)
        print(add)

        self.assertIsNot(add, None)

    def test_unit_search(self):
        cls = CRUD1('test2')
        query = {
            # 'query': {
            #     # 'wildcard': {
            #     #     'name' : { 'value': 'kat*'}
            #     # }
            # }
            'query': None
        }
        print('test_unit_search', query)
        data = cls.get(query)
        print(data)

        self.assertIsNot(data, None)

    def test_unit_update(self):
        cls = CRUD1('test2')
        data = {
            'name': 'helmi',
            'collage': 'unair'
        }
        id = '6687f7586c8bcc01d7178d1e'

        update = cls.update(id, data)

        self.assertIsNot(update, None)

    def test_unit_soft_delete(self):
        cls = CRUD1('test2')
        id = '6687f7586c8bcc01d7178d1e'

        soft_delete = cls.soft_delete(id)

        self.assertIsNot(soft_delete, None)

    def test_unit_delete(self):
        cls = CRUD1('test2')
        id = '6687f7586c8bcc01d7178d1e'

        delete = cls.delete(id)

        self.assertIsNot(delete, None)

