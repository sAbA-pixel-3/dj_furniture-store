from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page - Home',
        'list': ['kot', 'ok'],
        'dict': {'first': 'kot', 'second': 'ok'},
        'is_auth': True
    }
    return render(request, 'main/index.html', context)  

def about(request):
    return HttpResponse('About Page')