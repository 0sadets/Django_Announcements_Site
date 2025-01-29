from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    title = models.CharField(max_length=512)
    icon = models.CharField(max_length=2083)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    social_link = models.URLField(max_length=200, blank=True, null=True)
    
   # announcements = models.ManyToManyField('Announcement', related_name='creator', blank=True)
    
    favorite_announcements = models.ManyToManyField('Announcement', related_name='favorite_users', blank=True)
    
    def __str__(self):
        return self.username

class Announcement(models.Model):
    title = models.CharField(max_length=512)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=8)
    image = models.CharField(max_length=2083)
    price = models.IntegerField()
    location = models.CharField(max_length=512)
    desc = models.CharField(max_length=2083)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateField(default=datetime.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements')

    def __str__(self):
        return self.title
    
