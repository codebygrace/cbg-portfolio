from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='media/', blank=True)
    title = models.CharField(max_length=50)
    link = models.URLField()
    date = models.CharField(max_length=50)
    technologies = models.CharField(max_length=75)
    description = models.CharField(max_length=100)