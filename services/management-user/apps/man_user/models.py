from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from django.contrib.auth.models import User as AuthUser, AbstractUser
from master.models import Status
from django.utils.translation import gettext_lazy as _

# Custom User
# this is swap for from django.contrib.auth.models import User model. Default user model will be use this
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.email

# Clinic Owner
class Customer(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    mobile_phone = models.CharField(max_length=25, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_user')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1, related_name='customer_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

# Admin Apps
class Admin(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    mobile_phone = models.CharField(max_length=25, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='admin_user')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1, related_name='admin_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
