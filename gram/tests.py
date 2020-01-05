from django.test import TestCase
from .models import Profile, Like, Comment, Images
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestCase(TestCase):
    # setup method
    def setUp(self):
        """
        class that creates new profile
        """
        self.maya = User(username="Maya", email="maya123@gmail.com")
        self.maya = Profile(user=self.maya, user_id=1, bio="You're cute to think its about you", profile_photo="my.jpg")

        # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.maya, Profile))

    # Testing save method

    def test_save_profile(self):
        self.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    # Testing delete method
    def test_delete_profile(self):
        self.maya.delete_profile()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles), 0)


class ImagePostTestCase(TestCase):

    def setUp(self):
        """
        creating new instances of the image
        """
        self.new_image = Images(image="image.jpg", image_name="roses", caption="live",
                                user_id=1, user='Joy', likes=0, posted_on="111-2019")

    def test_save_image(self):
        """
        test case that saves the new image created
        """
        self.roses.save_image()
        image = Images.objects.all()
        self.assertEqual(len(image), 1)

    def test_delete_image(self):
        self.roses.save_image()
        self.roses.delete_image()
        image=Images.objects.all()
        self.assertTrue(len(image)==0)
        
    def test_update_caption(self):
        '''
        testcase that tests on updating a post's caption
        '''
        self.roses.save_post()
        new_image=Images.update_caption(self.roses.id,'flowers bloom life and soul')        
        self.assertTrue(result.caption,'flowers bloom life and soul')

    def get_all_images(self):
        """
        Test case that gets all images in a post
        """
        self.roses.save_image()
        all_images = Images.get_all_images()
        self.assertTrue(len(all_images)<1)
        
    def test_get_image_id(self):
        """
        Test case that gets the id of one image
        """
        self.roses.save_image()
        image_id=Images.get_image_id(self.roses.id)
        self.assertTrue(image_id.id==self.roses.id)
        
    def test_get_one_post(self):
        '''
        testcase that gets a single image
        '''
        self.bmw.save_post()
        one=Images.get_one_image(self.roses.id)  
        self.assertTrue(one.image_name==self.roses.image_name)
    
    def test_search_user(self):
        """
        testcase that tests the search user function
        """
        self.maya.save_profile()
        user = Profile.search_users(self.maya.username)
        self.assertTrue(user.username=="Maya")
    

class CommentTestCase(TestCase):
    def setUp(self):
        self.comment=Comment(body="I like it",image_id=self.bmw.id,posted_by=self.pyra,posted_on='09-12-2019')    

        

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_instance_follow(self):
        self.assertTrue(isinstance(self.follow,Followers))

    def test_save(self):
        self.follow.save_followers()
        prof=Followers.objects.all()
        self.assertTrue(len(prof)>0)
