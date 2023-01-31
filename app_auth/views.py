from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import LoginForm
# Create your views here.
def login_naj(request):
    if request.method =="POST":
        form= LoginForm(request.POST)
    else:
        form= LoginForm()
        return render (request, "login.html", {"form":form})

