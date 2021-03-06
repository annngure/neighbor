from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import auth,messages
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')


def registerView(request):
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration sucessful.")
            return redirect('login')   
    else:
        messages.error(request,"Invalid Information")
        form = NewUserForm()
    context={
        "form":form}
    return render(request,'registration/register.html',context)


def loginPage(request):
    if request.user.is_authenticated():
        return redirect('index')

    if request.method == "POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
                auth.login(request,user)
                messages.info(request,"You are now logged in.")
                return redirect('index')
            
        else:
            messages.error(request,"Invalid username or password.")

    return render(request,'registration/login.html')

def profileView(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit = False)
            profile.save()
        return redirect ('occupant')

    else:
        form = UpdateProfileForm()
    context={
        "form":form
    }
    return render(request, 'profile.html',context)


def logout(request):
    auth.logout(request)
    return redirect('login')

def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"
        context={
        "message":message,
        "business": searched_business
        }
        return render(request, 'search.html',context)

    else:
        message = "You haven't searched yet"
        return render(request, 'search.html')

def post(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Post sucessful.")
            return redirect('business_post')   
    else:
        messages.error(request,"Invalid Information")
        form = PostForm()
    context={
        "form":form}
    return render(request,'post.html',context)

def business_post(request):
    business=Business.objects.all()
    post =Posts.objects.all()
    context ={
        "business":business,
        "post":post
    }
    return render(request,'Bussiness_Post.html',context)

def occupants(request):
    profiles= Profile.objects.all()
    context={
        "profiles":profiles
    }
    return render(request,'occupant.html',context)