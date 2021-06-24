from django.db import models


# Create your models here.

class Transfer(models.Model):
    name = models.CharField(max_length=300)
    funds = models.IntegerField(default=0)
