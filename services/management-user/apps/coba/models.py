from django.db import models

# Create your models here.

class Test2(models.Model):
    class Meta:
        permissions= [
            ('can_test2', 'just test description') # this will add new permission, not override the default instead. and when we delete model, permissions belongs to is still exist
        ]

    name = models.CharField(max_length=100, null=True)

