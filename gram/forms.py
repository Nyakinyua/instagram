from django import forms
from .models import Images,Profile,comment,Like,Followers

class postImage(forms.ModelForm):
    class Meta:
        model=postImage
         exclude=['likes','comments','date','user','profile']
         
class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['user','images']

class Likes(forms.ModelForm):
    class Meta:
        model=Images
        exclude=['likes','comments','date','user','userId','profile','image','name','caption']

class FormFollow(forms.ModelForm):
    class Meta:
        model=Followers
        exclude=['user','insta','user_id']