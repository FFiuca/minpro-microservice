from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from man_user.function.kong.consumer import ConsumerAction
import logging
import json
# from .models import

log = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_consumer_kong(sender, instance, created, *args, **kwargs):
    print('signals consumer kong', sender, instance, args, kwargs)
    if created:
        consumer = ConsumerAction().create({
            'username': instance.username,
            'user': instance
        })

        log.info('[signals user: create_consumer_kong] consumer created '+json.dumps(consumer))
