from django.db import models

class Valute(models.Model):
    date=models.DateTimeField()
    USD = models.IntegerField()
    EUR = models.IntegerField()