from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
import uuid

class Files(SafeDeleteModel, models.Model):
    _safedelete_policy= SOFT_DELETE

    # @classmethod
    def generate_id(self):
        return str(uuid.uuid4())

    id = models.UUIDField(
        primary_key=True,
        max_length=200,
        blank=False,
        null=False,
        default= generate_id
    )
    user_id = models.CharField(max_length=100, blank=True, null=True, default=None)
    filename = models.CharField(max_length=100, blank=False, default=None)
    type= models.CharField(max_length=20, blank=True, null=True)
    path= models.TextField(blank=False, default=None)
    url= models.TextField(blank=False, default=None)
    size = models.FloatField(blank=True, default=None)
    created_at= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at= models.DateTimeField(auto_now=True, blank=True, null=True)

