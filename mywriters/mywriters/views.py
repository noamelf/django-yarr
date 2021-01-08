import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from yarr.models import Feed

from mywriters.models import UserFeeds

from .forms import AddFeedForm

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            logger.info("Signup form valid")
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
        logger.info("Signup form invalid")

    return render(request, "mywriters/signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "mywriters/login.html")


def user_logout(request):
    logout(request)
    return redirect("/")

@login_required
def catalogue(request):
    if request.method == "GET":
        return render(request, "mywriters/catalogue.html", {"form": AddFeedForm()})

    elif request.method == "POST":
        form = AddFeedForm(request.POST, instance=UserFeeds(user=request.user))
        if form.is_valid():
            form.save()
            feeds = Feed.objects.all()
            feeds.check_feed()
        return redirect("/")
