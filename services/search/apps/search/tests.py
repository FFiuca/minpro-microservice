from rest_framework.test import APITestCase
from search.functions.crud.crud import CRUD1
from faker import Faker
from django.urls import reverse


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

    def test_get(self):
        data = {
            'collection': 'test2',
            'data' : {}
        }
        query = {
            'query': {
                'bool': {
                    'must': [
                        {'match': {'name': 'smith'}}
                    ]
                }
            }
        }

        data['data']= query
        resp = self.client.post(
            reverse('search|search.get'),
            data,
            format='json',
            # content_type='application/json'
        )

        print(resp.status_text, resp.json())
        # self.assertEqual(resp.status_code, 200)

        resp= resp.json()

        self.assertTrue(isinstance(resp['data'], dict))

    def test_create(self):
        header = {
            'X-Consumer-Custom-Id': '9854b3b8-90ba-46ad-8b3c-4e0b99d03c98'
        }
        data = {
            'collection': 'test2',
            'data' : {
                'name': fake.name()+' test'
            }
        }

        resp = self.client.post(
            reverse('search|search.create'),
            data,
            format='json',
            headers=header
            # content_type='application/json'
        )

        print(resp.status_text, resp.json())
        # self.assertEqual(resp.status_code, 200)

        resp= resp.json()

        self.assertTrue(isinstance(resp['data'], dict))


    def test_update(self):
        header = {
            'X-Consumer-Custom-Id': '9854b3b8-90ba-46ad-8b3c-4e0b99d03c98'
        }
        data = {
            'collection': 'test2',
            'data' : {
                'name': fake.name()+' test'
            }
        }

        resp = self.client.put(
            reverse('search|search.update', args=['668f93ca874c2653c4b4c856']),
            data,
            format='json',
            headers=header
            # content_type='application/json'
        )

        print(resp.status_text, resp.json())
        self.assertEqual(resp.status_code, 200)

        resp= resp.json()

        self.assertTrue(isinstance(resp['data'], dict))

    def test_soft_delete(self):
        header = {
            'X-Consumer-Custom-Id': '9854b3b8-90ba-46ad-8b3c-4e0b99d03c98'
        }
        data = {
            'collection': 'test2'
        }

        resp = self.client.delete(
            reverse('search|search.soft_delete', args=['668f93ca874c2653c4b4c856']),
            data,
            headers=header
        )

        print(resp.status_text, resp.json())
        self.assertEqual(resp.status_code, 200)

        resp= resp.json()
        self.assertTrue(isinstance(resp['data'], dict))

    def test_destroy(self):
        header = {
            'X-Consumer-Custom-Id': '9854b3b8-90ba-46ad-8b3c-4e0b99d03c98'
        }
        data = {
            'collection': 'test2'
        }

        resp = self.client.delete(
            reverse('search|search.destroy', args=['668f93ca874c2653c4b4c856']),
            data,
            headers=header
        )

        print(resp.status_text, resp.json())
        self.assertEqual(resp.status_code, 200)

        resp= resp.json()
        self.assertTrue(isinstance(resp['data'], dict))

    def test_seed_data(self):
        cls = CRUD1('test2')
        data = []
        result = []

        for r in range(0, 10000):
            data.append({'name': fake.name()})
            result.append(cls.add(data[r]))

        print(len(data))
        print(len(result))

        self.assertEqual(len(data), len(result))
