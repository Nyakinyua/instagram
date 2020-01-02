from django.db import models
import datetime as dt 
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) 
    userId = models.IntegerField(default=None)
    bio = models.TextField(max_length=200)
    profile_photo = models.ImageField(upload_to = 'profile/',blank=True)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        return self.save()
    
    def delete_profile(self):
        profile=Profile.objects.all().delete()
        return profile
    
    def search_user(cls,user):
        return User.objects.filter(username__icontains=user)
    
class Like(models.Model):
    like = models.IntegerField(blank=True,default= 0)
    


class Images(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    image_name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    userId=models.IntegerField(default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    like = models.ForeignKey(Like,on_delete=models.CASCADE,default=0)
    posted_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['posted_on']
        
    def save_image(self):
        return self.save()
    
    def delete_image(self):
        image=Image.objects.all().delete()
        return image
    
    def update_caption(self,caption):
        return self.update
       
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_by_image_name(cls,search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image
    
    @classmethod
    def get_user_posts(cls,user_id):
        """
        Function that gets all posts by a user
        """
        posts = cls.objects.filter(posted_by__id__contains=user_id)
        return posts
    
class Comment(models.Model):
    comment = models.TextField(max_length=45,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    images=models.IntegerField(default=None)
    image_id = models.ForeignKey(Images,on_delete=models.CASCADE,default=None)
    
    def save_comment(self):
        return self.save()

    def delete_comment(self):
        return self.delete()
    

    def __str__(self):
        return self.comment
    
    @classmethod
    def get_comments(self):
        comments = cls.objects.filter(image_id__in=id)
        return comments
    
class Followers(models.Model):
    user=models.CharField(max_length=30)
    insta=models.CharField(default='',max_length=50)
    
    def save_followers(self):
        self.save()