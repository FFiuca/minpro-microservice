from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class Status(SafeDeleteModel, models.Model):
    _safedelete_policy= SOFT_DELETE

    status_name = models.TextField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
