from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from .forms import *
from django.contrib import auth,messages
from .models import *
# Create your views here.
def index(request):

    return render(request,'index.html')