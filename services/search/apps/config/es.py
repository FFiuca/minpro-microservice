from elasticsearch import Elasticsearch
from django.conf import settings
from elasticsearch.client import SslClient

host = settings.ELASTICSEARCH_SETTINGS['host']
port = settings.ELASTICSEARCH_SETTINGS['port']
api_key= settings.ELASTICSEARCH_SETTINGS['key']['api_key']

client = Elasticsearch(
    '{host}:{port}'.format(host=host, port=port),
    api_key=api_key,
    verify_certs=False,
    # scheme='https',
    # basic_auth=('elastic', 'es-password'),
)

class Certificates():
    client = SslClient(client)

    def get_certificates(self):
        return self.client.certificates()
