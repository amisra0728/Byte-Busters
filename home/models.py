from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileType(models.Model):
    name = models.CharField(max_length=20)

# class Unit(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField( max_length=50)
#     size = models.CharField(max_length=50)
#     info = models.JSONField()


# class Requirements(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     rent_type = models.CharField(max_length=50)
#     requirement_type = models.CharField(max_length=50)
#     rent = models.IntegerField()
#     other_charges = models.IntegerField()
#     available_from = models.DateField()
#     preferred_tenant = models.CharField(max_length=50)


# class SiteVisit(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     date_time = models.DateTimeField()
#     status = models.CharField( max_length=50)


class Flat(models.Model):
    location = models.CharField(max_length=255)
    bhk_type = models.IntegerField()
    gender_preference = models.CharField(max_length=255)
    rental_type = models.CharField(max_length=255)
    furnish = models.CharField(max_length=255)
    mobile_number = models.BigIntegerField()
    mobile_post = models.BooleanField(default=False)
    budget_range = models.BigIntegerField()

class Flatmate(models.Model):
    location = models.CharField(max_length=255)
    bhk_type = models.IntegerField()
    gender_preference = models.CharField(max_length=255)
    rental_type = models.CharField(max_length=255)
    furnish = models.CharField(max_length=255)
    rent=models.BigIntegerField()
    mobile_number = models.BigIntegerField()
    mobile_post = models.BooleanField(default=False)
    amenities=models.CharField(max_length=255)
    

