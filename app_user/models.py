from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class AppUser(models.Model):
    USER_TYPES = (
    ('C', 'Customer'), 
    ('S', 'Seller')
    )
    GENDER_CHOICES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appusers')
    user_type = models.CharField(max_length=1,choices=USER_TYPES, default='C')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    mobile = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    zipcode = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.user.username
'gender' 'mobile' 'address' 'city' 'zipcode'
