from django.db import models

from accounts.models import ProfileUser
from phones.models import Phone
# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField()
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    posted_data = models.DateTimeField(auto_now_add=True)