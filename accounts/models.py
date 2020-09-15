from django.db import models

# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    passsword=models.CharField(max_length=20)