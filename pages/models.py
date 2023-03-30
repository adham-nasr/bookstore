from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=True , null=False , max_length=64 )
    author =  models.CharField(blank=True , null=False ,max_length=64)
    genre =  models.CharField(blank=True , null=False ,max_length=64)
    length = models.IntegerField()
    publisher = models.CharField(blank=True , null=False ,max_length=64)
    
    def __str__(self):
        return self.title

