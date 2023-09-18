from django.db import models
from authentication.models import CustomUser

# Create your models here.

class PersonalInformation(models.Model):
    HOME = 'home'
    OFFICE = 'office'
    ADDRESS_CHOICES = (
        (HOME, 'Home'),
        (OFFICE, 'Office'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    address_type = models.CharField(max_length=100, choices=ADDRESS_CHOICES)

    def __str__(self) -> str:
        return self.user.email
    