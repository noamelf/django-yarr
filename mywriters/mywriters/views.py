from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={'message': 'Welcome!', 'feed_url': '/yarr'}
    return render(request, 'index.html', context)