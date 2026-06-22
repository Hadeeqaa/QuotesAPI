from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20 )
    class Count(models.IntegerChoices):
        ONE=1,('One')
        TWO=2,('two')
        THREE=3,('three')
        FOUR=4,('four')
        FIVE=5,('five')
    count = models.IntegerField(
        choices=Count.choices,
        default=Count.ONE)
    
# Create your models here.
class Quote(models.Model):
    text = models.CharField(max_length=50)



