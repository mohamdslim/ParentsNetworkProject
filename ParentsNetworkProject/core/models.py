from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    profile_pic = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    bio = models.TextField(null=True , blank=True ,max_length=500,default="")

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']

    
