from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from man_user.models import User_Proxy
from man_user.function.kong.consumer import ConsumerAction
import logging
import json
import uuid
from datetime import datetime
from django.forms import model_to_dict
# from .models import

log = logging.getLogger(__name__)

# signals apply sequence depends on first definition

@receiver(post_save, sender=User)
def create_user_proxy(sender, instance, created, *args, **kwargs):
    print('signal user proxy', instance)
    if created:
        proxy= User_Proxy.objects.create(uuid=str(uuid.uuid4()), user=instance)

        log.info('[signals user: create user proxy] proxy created '+json.dumps(model_to_dict(proxy)))

@receiver(post_save, sender=User)
def create_consumer_kong(sender, instance, created, *args, **kwargs):
    print('signals consumer kong', sender, instance, args, kwargs)
    if created:
        consumer = ConsumerAction().create({
            'username': instance.username,
            'user': instance
        })

        log.info('[signals user: create_consumer_kong] consumer created '+json.dumps(consumer))
