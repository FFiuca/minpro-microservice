import factory
from factory import django
from man_user import models
from master import models as MasterModel
from faker import Faker
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from main.common_helper import extract_digits
from man_user.function.kong.consumer import ConsumerAction

fake = Faker(['id_ID'])

class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ['email']

    @staticmethod
    def create_password1(obj):
        # print('obj fact', obj, dir(obj))
        return make_password(obj.username)

    username= factory.Sequence(lambda obj: fake.user_name()) # to deal with unique field. here, lambda must declare one params due factory_boy will inject in back end
    password= factory.LazyAttribute(lambda obj: make_password(obj.username)) # to deal with field who have depends on
    # password= factory.LazyAttribute(create_password1)
    email= factory.Sequence(lambda obj: fake.email()) # when use lambda function here, cannot combine with factory.Faker like factory.Sequence(lambda obj: extract_digits(factory.Faker('phone_number', locale='id_ID')))
    is_superuser= factory.LazyFunction(lambda: fake.random_element(elements=(0,1))) # to deal with small func
    is_staff= factory.LazyFunction(lambda: fake.random_element(elements=(0,1)))

class AdminFactory(django.DjangoModelFactory):
    class Meta:
        model = models.Admin
        django_get_or_create= ['user']

    mobile_phone= factory.Sequence(lambda obj: extract_digits(fake.phone_number()))
    full_name= factory.Faker('name', locale='id_ID')
    status= MasterModel.Status.objects.order_by('?').first() # to get randomly
    print('statusa', status.pk)
    # status= MasterModel.Status.objects.first()
    user= factory.SubFactory(UserFactory) # to deal with 1-1 or 1-many relationship

class Kong_JWTFactory(django.DjangoModelFactory):
    class Meta:
        model= models.Kong_JWT
        django_get_or_create= ['user']

    @staticmethod
    def generete_kong_consumer_id(obj):
        data = ConsumerAction().create({'username': obj.user.username, 'user': obj.user})
        print('data_kong', data)
        return data['id']

    user = factory.SubFactory(UserFactory)
    kong_consumer_id = factory.LazyAttribute(generete_kong_consumer_id)
