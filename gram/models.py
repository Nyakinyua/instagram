from django.db import models
import datetime as dt 

# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=40)
    bio = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to = 'profile/')
    
    def __str__(self):
        return self.user_name
    
    def save_user(self):
        return self.save()

class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
   