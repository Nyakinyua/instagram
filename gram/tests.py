from django.test import TestCase
from .models import Profile,Like,Comment,Images
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.maya = Profile(user="Maya",email=maya@gmail.com,bio="Too much juice",profile_photo="my.jpg")
    
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.maya,Profile))
        
    # Testing save method
    def test_save_profile(self):
        self.save_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profile)>0)
        
    # Testing delete method
    def test_delete_profile(self):
        self.maya.delete_profile()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles),0)
        
    def test_search_user(self):
        

class TestImage(TestCase):
    def setUp(self):
        self.comment=Comment(images=1,comment='this is dope')
        self.follow=Followers(user="collo",insta='like',user_id=1)
        self.new_image=Images(image="image",name="sexy",caption="live",likes=0,userId=10)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_instance_follow(self):
        self.assertTrue(isinstance(self.follow,Followers))

    def test_save(self):
        self.follow.save_followers()
        prof=Followers.objects.all()
        self.assertTrue(len(prof)>0)

