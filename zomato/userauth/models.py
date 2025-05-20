from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=10)
    phon = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='profile_pics',default='default.jpg')
    email = models.EmailField(max_length=100,unique=True)
    
    def __str__(self):
        return self.username 