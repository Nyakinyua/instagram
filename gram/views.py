from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404 
from .models import Images,Profile,Comment,Followers,Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UploadImage,EditProfile,UpdateProfile,CommentForm,Like,Follow



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title = "Nyakinyua Gram Photos"
    images = Images.get_all_images()
    return render(request,"index.html",{"title":title,"images":images})

@login_required(login_url="/accounts/login/")
def logout_request(request):
  '''
  view function renders home page once logout
  '''
  logout(request)
  return redirect('login/')

@login_required(login_url='/accounts/login/')
def profile(request,id):
    try:
        current_user = request.user.id
        profile = Profile.objects.get(id=id)
        
    except Exception as e:
        raise Http404()
    return render(request,'profile.html',{'profile':profile})

@login_required(login_url='accounts/login/')
def upload_pic(request):
    title='NewPost'
    current_user = request.user
    current_user_id= request.user.id
    
    if request.method == 'POST':
        form = UploadImage(request.POST,request.FILES)
        if form.is_valid():
          image=form.save(commit=False) 
          image.save()
          
          return redirect('index')
    else:
        form = upload_pic()
    return render(request,'upload.html',{'title':title,'form':form})
            

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        search_images = Images.search_by_image_name(search_term)
        
        message = f"{search_term}"
        return render(request,"search.html",{"message":message,"images":search_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})  
    
