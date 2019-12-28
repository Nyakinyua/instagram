from django.shortcuts import render
from django.http import HttpResponse,Http404 
from .models import Images,Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    title = "Nyakinyua Gram Photos"
    images = Images.get_all_images()
    return render(request,"index.html",{"title":title,"images":images})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    posts = Images.get_user_posts(request.user.id)
    try:
        profile = Profile.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    return render(request,'profile.html',{'profile':profile,'posts':posts})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        search_images = Images.search_by_image_name(search_term)
        
        message = f"{search_term}"
        return render(request,"search.html",{"message":message,"images":search_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})  
    
def logout(request):
    return render(request, 'registration/logout.html')

def login(request):
    return render(request, 'registration/login.html')