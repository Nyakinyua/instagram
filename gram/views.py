from django.shortcuts import render
from django.http import HttpResponse ,Http404 
from .models import Images,Profile

# Create your views here.
def index(request):
    title = "Nyakinyua Gram Photos"
    images = Images.get_all_images()
    return render(request,"index.html",{"title":title,"images":images})

def profile(request,id):
    try:
        profile = Profile.objects.get(id=id)
        posts = 
    except DoesNotExist:
        raise Http404()
    return render(request,'profile.html',{'profile':profile})