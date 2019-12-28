from django import forms
from .models import Images,Profile,comment,Like,Followers

class UploadImage(forms.ModelForm):
    class Meta:
        model=Images
         exclude=['like','comment','profile']
         
class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        

class Like(forms.ModelForm):
    class Meta:
        model=Images
        exclude=['likes','comments','pub_on','user','userId','profile','image','name','caption']

class Follow(forms.ModelForm):
    class Meta:
        model=Followers
        exclude=['user','insta']