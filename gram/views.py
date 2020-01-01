from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404 
from .models import Images,Profile,Comment,Followers,Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UploadImage,EditProfile,UpdateProfile,CommentForm,Like,Follow
from django.contrib.auth import logout



# Create your views here.
def home(request):
    title = "Nyakinyua Gram Photos"
    
    return render(request,"index.html",{"title":title})

@login_required(login_url="/accounts/login/")
def news_feed(request):
    try:
        current_user = request.user.id
        images = Images.objects.all()
        prof_pic = Profile.objects.filter(userId=current_user)
        profile = prof_pic.reverse()[0:1]
        users = User.objects.all().exclude(id=request.user.id)
        comments = Comment.objects.all()
    except Exception as e:
        raise Http404
    return render(request,'all_pics.html',{"images":images,"profile":profile,"users":users,"comments":comments})


@login_required(login_url="/accounts/login/")
def logout_user(request):
    '''
    view function renders home page once logout
    '''
    
    logout(request)
    return redirect('home/')

@login_required(login_url="/accounts/login/")
def profile(request):
    try:
        current_user=request.user.id
        profile_photos=Images.objects.filter(userId=current_user)
        profile_image=Profile.objects.filter(userId=current_user).all()
        profile=profile_image.reverse()[0:1]

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile_photos,"pic":profile})

@login_required(login_url='accounts/login/')
def uploads(request):
    title='NewPost'
    current_user = request.user
    current_user_id= request.user.id
    
    if request.method == 'POST':
        form = UploadImage(request.POST,request.FILES)
        if form.is_valid():
          image=form.save(commit=False) 
          image.user=current_user
          image.userId=current_user_id
          image.profile=current_user_id
          image.save()
          
          return redirect('profile')
    else:
        form = UploadImage()
    
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


@login_required(login_url='/accounts/login/')
def edit(request):
    current_user_id=request.user.id
    profile=Profile.objects.filter(userId=current_user_id)
    if len(profile)<1:

        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.userId=current_user_id
                profile.save()
            return redirect("profile")
        else:
            form=EditProfile()
            return render(request,"edit.html",{"form":form})
    else:
        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES )
            if form.is_valid():
                profile=form.save(commit=False)
                bio=form.cleaned_data['bio']
                profile_photo=form.cleaned_data['profile_photo']
                update=Profile.objects.filter(userId=current_user_id).update(bio=bio,pic=profile_photo)
                profile.userId=current_user_id
                profile.save(update)
            return redirect("profile")
        else:

            form=EditProfile()

            return render(request,"edit.html",{"form":form})

@login_required(login_url="/accounts/login/")
def one_post(request,id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            image = Images.objects.get(id=id)
            comment.save()
        return redirect("one_pic") 
    else:
        form = CommentForm()
    
            
        return render(request,"one_pic.html",{"form":form})   
     
     
