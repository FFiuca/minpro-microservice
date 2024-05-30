import requests
from config.kong import URL_MAPPING
from man_user.models import Kong_JWT
import logging
import json
from . import kong
import datetime

logger = logging.getLogger(__name__)

class ConsumerBase(kong.KongBase):

    def create(self):
        pass
    def update(self):
        pass
    def list(self):
        pass
    def detail(self):
        pass
    def delete(self):
        pass

class ConsumerAPI(ConsumerBase):
    def create(self, data, *args, **kwargs):
        url = self.url+ URL_MAPPING['consumer']['create']

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'custom_id': data['user'].user_proxy.pk,
            'username': data['username'],
            'tags' : ['man_user_app']
        }

        response = requests.post(url, data=data)
        print('create', response.json(), data)
        if response.status_code not in [200, 201]:
            return {
                'status': False,
                'data': response.json()
            }

        return {
            'status': True,
            'data': response.json()
        }

    def detail(self, data, *args, **kwargs):
        url = self.url+ URL_MAPPING['consumer']['detail']
        url = url.format(consumer_username_or_id=data['username'])

        response = requests.get(url)
        if response.status_code not in [200, 201]:
            return {
                'status': False,
                'data': response.json()
            }

        return {
            'status': True,
            'data': response.json()
        }

class ConsumerAction:
    def create(self, data, *args, **kwargs):
        cons = ConsumerAPI()

        is_exist = cons.detail(data=data)
        if is_exist['status']:
            return is_exist['data']

        create = cons.create(data=data)
        print('kong',create)

        if create['status'] is False:
            logger.error('[kong api] '+json.dumps(create))
            raise Exception('[kong api] create consumer failed.')

        create= create['data']
        Kong_JWT.objects.update_or_create(
            user= data['user'],
            defaults={
                'kong_consumer_id': create['id'],
                'request_body': create
            }
        )
        print('aah', create)
        return create
