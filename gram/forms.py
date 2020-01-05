from django import forms
from .models import Images,Profile,Comment,Like,Followers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadImage(forms.ModelForm):
    class Meta:
        model=Images
        exclude = ['']
         
class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['user','images']

        

class Like(forms.ModelForm):
    class Meta:
        model=Images
        exclude=['likes','comments','pub_on','user','userId','profile','image','name','caption']

class Follow(forms.ModelForm):
    class Meta:
        model=Followers
        exclude=['user','insta']
        
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')