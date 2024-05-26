import requests
from man_user.models import Kong_JWT, Kong_JWT_Token
from . import kong
from config.kong import URL_MAPPING, ALGORITHM, KEY_CLAIM_NAME, CLAIM_TO_VERIFY, EXPIRATION
import logging
import json
import jwt as jwt_lib
from datetime import datetime, tzinfo
from django.utils import timezone

logger = logging.getLogger(__name__)

class JWTBase(kong.KongBase):
    def create(self, data):
        pass

    def list(self, data):
        pass

    def delete(self, data):
        pass


class JWTApi(JWTBase):
    def create(self, data):
        url = self.url+ URL_MAPPING['jwt']['create']
        url = url.format(consumer=data['kong_consumer_id'])

        response = requests.post(url)
        if response.status_code not in [200, 201]:
            return {
                'status': False,
                'data': response.json()
            }

        response = response.json()
        return {
            'status': True,
            'data': response
        }

class JWTAction:
    def create(self, data):
        user = Kong_JWT.objects.filter(user=data['user']).first()
        print('aaa',data)
        clss = JWTApi()
        jwt = clss.create(data={'kong_consumer_id': user.kong_consumer_id})
        if jwt['status'] is False:
            logger.error('[kong api] '+ json.dumps(jwt))
            raise Exception('[kong api] create jwt failed')

        jwt = jwt['data']

        user.jwt_id= jwt['id']
        user.jwt_key= jwt['key']
        user.jwt_secret= jwt['secret']
        user.rsa_public_key= jwt['rsa_public_key']
        user.algorithm= jwt['algorithm']
        user.response_body = jwt

        user.save()
        return user

    def generate_token(self, user):
        kong = Kong_JWT.objects.filter(user=user).first()
        jwt = kong.response_body

        payload = {}
        header={}

        header[KEY_CLAIM_NAME]= jwt['key']
        header["alg"]= ALGORITHM
        header['typ']= 'JWT'

        expired_at= jwt['created_at']+ EXPIRATION

        payload['email']= kong.user.email
        payload['kong_consumer_id'] = kong.kong_consumer_id
        payload[CLAIM_TO_VERIFY]= expired_at

        token= jwt_lib.encode(payload=payload, headers=header, key=jwt['secret'], algorithm=ALGORITHM)
        token= Kong_JWT_Token.objects.create(
            kong_jwt= kong,
            token= token,
            expired_at= datetime.fromtimestamp(expired_at)
        )

        return token
