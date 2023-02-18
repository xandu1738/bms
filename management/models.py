from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Position(models.Model):
    position = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.position
    
    def get_absolute_url(self):
        return reverse("position")
    
class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    #profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("employees")
