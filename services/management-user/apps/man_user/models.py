from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from django.contrib.auth.models import User as AuthUser, AbstractUser
from master.models import Status
from django.utils.translation import gettext_lazy as _

# Custom User
# this is swap for from django.contrib.auth.models import User model. Default user model will be use this
# class User(AbstractUser):
#     email = models.EmailField(unique=True, blank=False)
#     first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
#     last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)

#     def __str__(self):
#         return self.email

# Clinic Owner
class Customer(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ['created_at']

    mobile_phone = models.CharField(max_length=25, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='customer_user')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1, related_name='customer_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    test = models.DateTimeField(auto_now_add=True, blank=True, null=True)

# Admin Apps
class Admin(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ['created_at']

    mobile_phone = models.CharField(max_length=25, blank=True)
    full_name = models.CharField(max_length=100, blank=False)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE,  related_name='admin_user')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='admin_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

# Kong Proxy
class Kong_JWT(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['kong_consumer_id'])
        ]

    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    jwt_id = models.CharField(max_length=255, null=True, blank=True)
    jwt_key = models.CharField(max_length=255, null=True, blank=True)
    jwt_secret = models.CharField(max_length=255, null=True)
    rsa_public_key = models.TextField(null=True)
    kong_consumer_id = models.CharField(max_length=255, null=True)
    algorithm = models.CharField(max_length=50, null=True)
    request_body = models.JSONField(null=True)
    response_body = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

class Kong_JWT_Token(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['token'])
        ]

    kong_jwt = models.ForeignKey(Kong_JWT, on_delete=models.CASCADE)
    token = models.CharField(max_length=500,blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)

class User_Proxy(models.Model):
    uuid = models.CharField(primary_key=True, max_length=200, blank=False, null=False)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
