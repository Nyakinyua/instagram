from django.contrib import admin
from .models import Profile,Images,Like


# Register your models here.

admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Like)