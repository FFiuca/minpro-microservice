import factory
from factory import django
from faker import Faker
from faker.providers import address
from search.mongo_docs import Manga

fake = Faker(['id_ID'])
fake.add_provider(address)

class MangaFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Manga

    title = factory.Sequence(lambda obj: fake.name())
