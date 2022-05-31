from django.db import models

# Create your models here.

class Client(models.Model):

    company = models.CharField(max_length=100)

    description = models.TextField()

    budget = models.IntegerField()

    expiration_date = models.DateField()

    image = models.FilePathField(path="/img")
