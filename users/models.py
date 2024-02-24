from django.db import models

# Create your models here.

class User(models.Model):

    _id = models.UUIDField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=16)

    role=models.CharField(max_length=10, default="write")



