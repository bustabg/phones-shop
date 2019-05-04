from django.db import models
from accounts.models import ProfileUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Brand(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return f"Phone manufacturer is  {self.brand}"


class Phone(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    phone_model = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image_url = models.URLField()
    screen_size = models.FloatField(validators=[MinValueValidator(2), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.user} is selling {self.phone_model}"
