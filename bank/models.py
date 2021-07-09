from django.db import models


# Create your models here.

class Transfer(models.Model):
    name = models.CharField(max_length=300)
    funds = models.IntegerField(default=0)


class TransferHistory(models.Model):
    sender = models.CharField(max_length=300)
    receiver = models.CharField(max_length=300)
    funds = models.IntegerField(default=0)
