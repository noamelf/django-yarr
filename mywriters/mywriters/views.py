from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

import logging

logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            logger.info('Signup form valid')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        logger.info('Signup form invalid')

    return render(request, 'mywriters/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'mywriters/login.html')

def user_logout(request):
    logout(request)      
    return redirect('/')
