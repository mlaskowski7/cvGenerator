from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    summary = models.TextField(max_length = 2000)
    university = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255)
    high_school = models.CharField(max_length = 255, default = 'Not finished')
    previous_work = models.TextField(max_length = 1000)
    skills = models.TextField(max_length = 1000)
    
    def __str__(self):
        return self.name
    