from django.contrib import admin
from .models import Profile,Images,Like,Comment

# Register your models here.

admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)