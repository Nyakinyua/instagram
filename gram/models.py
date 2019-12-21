from django.db import models
import datetime as dt 

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    caption = models.CharField(max-length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes =models.IntegerField()