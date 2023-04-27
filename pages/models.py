from django.db import models
from django.conf import settings

# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=True , null=False , max_length=64 )
    author =  models.CharField(blank=True , null=False ,max_length=64)
    genre =  models.CharField(blank=True , null=False ,max_length=64)
    length = models.IntegerField()
    publisher = models.CharField(blank=True , null=False ,max_length=64)
    
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="books")
    
    def __str__(self):
        return self.title
