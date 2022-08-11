from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.URLField()
   
    def __str__(self):
        return self.url

class Face(models.Model):
    name = models.CharField(max_length=255)
    img = models.FileField()
    suspeito = models.BinaryField()     

    def __str__(self):
        return self.name   