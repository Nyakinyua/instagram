from django.db import models
import datetime as dt 

# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=40)
    bio = models.TextField(max_length=200)
    profile_photo = models.ImageField(upload_to = 'profile/',blank=True)
    
    def __str__(self):
        return self.user_name
    
    def save_profile(self):
        return self.save()
    
    def delete_profile(self):
        return self.delete()

class Images(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    image_name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['pub_date']
        
    def save_image(self):
        return self.save()
    
    def delete_image(self):
        return self.delete()
       
   