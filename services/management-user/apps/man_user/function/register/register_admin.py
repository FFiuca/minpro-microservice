from django.forms.models import model_to_dict
from django.db import transaction
from .register_base import RegisterBase
from man_user.models import Admin
from master.models import Status

class RegisterAdmin(RegisterBase):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @transaction.atomic
    def register(self, data, *args, **kwargs):
        # print(super().test())
        user = super().register(**data)

        field= {
            'mobile_phone': data['mobile_phone'],
            'full_name': data['full_name'],
            'status': Status.objects.filter(status_name='Active').first(),
            'user': user
        }
        admin = Admin.objects.create(**field)

        if admin is None:
            raise Exception('create admin failed')

        print(user, admin)
        return {
            'user': model_to_dict(user),
            'admin': model_to_dict(admin)
        }



