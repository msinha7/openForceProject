from django.db import models

# Create your models here.
class ratings(models.Model):
    quote = models.TextField()
    session= models.TextField()
    username = models.TextField()
    rating = models.IntegerField()