from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.URLField()
    video = models.FileField()

    def __str__(self):
        return self.name