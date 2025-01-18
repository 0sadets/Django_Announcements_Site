from django.db import models
from datetime import datetime

class Category(models.Model):
    title = models.CharField(max_length=512)
    icon = models.CharField(max_length=2083)

    def __str__(self):
        return self.title
    
class Announcement(models.Model):
    title = models.CharField(max_length=512)
    category_id = models.IntegerField()
    image = models.CharField(max_length=2083)
    price = models.IntegerField()
    location = models.CharField(max_length=512)
    desc = models.CharField(max_length=2083)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title