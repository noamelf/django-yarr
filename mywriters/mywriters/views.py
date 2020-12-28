from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Catalogue

from yarr.forms import AddFeedForm
from yarr.models import Feed

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

def catalogue(request):
    if request.method == 'GET':
        logger.info('GET')
        items = Catalogue.objects.all()
        return render(request, 'mywriters/catalogue.html', context={'catalogue': items})
    
    elif request.method == 'POST':
        feed = Feed()
        feed_form = AddFeedForm(request.POST, instance=feed)

        if feed_form.is_valid():
            # Save feed
            # ++ Really we would like to get the feed at this point, to
            # ++ fill out the name and other feed details, and grab initial
            # ++ entries. However, feedparser isn't thread-safe yet, so for
            # ++ now we just have to wait for the next scheduled check
            feed = feed_form.save(commit=False)
            feed.title = feed.feed_url
            feed.user = request.user
            feed.save()

        return redirect('/')
