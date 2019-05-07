from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png')
    phone_number = PhoneNumberField(null=False, unique=True)

    def __str__(self):
        return f"{self.user}"


