from django.db import models

# Create your models here.
# sitter Model
class Sitter(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sitterNum = models.IntegerField(default=0)
    # dob = models.DateField(auto_now_add=False, default=0, blank=False)
    NIN = models.CharField(max_length=15, default=None)
    contact = models.CharField(max_length=13,  default=None)
    recoName = models.CharField(max_length=100, default=0, blank=False)
    NoK = models.CharField(max_length=100,default=None)
    education = models.CharField(max_length=255, default=0)

    # babys Model
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    babyNum = models.IntegerField()
    babyTimeIn = models.DateTimeField(auto_now_add=True, blank=False)
    babyBringer = models.CharField(max_length=100)
    parentName = models.CharField(max_length=100)
