from django.shortcuts import render

def home (request):
    return render (request, 'pages/home.html')

def dashboard (request):
    return render (request, 'pages/dashboard.html')

def learn (request):
    return render (request, 'pages/learn.html')

def about (request):
    return render (request, 'pages/about.html')

def blogs (request):
    return render (request, 'pages/blogs.html')

def forum (request):
    return render (request, 'pages/forum.html')

def mechlab (request):
    return render (request, 'pages/mechlab.html')

def ecosystem (request):
    return render (request, 'pages/ecosytem.html')

def groups (request):
    return render (request, 'pages/groups.html')

def members (request):
    return render (request, 'pages/members.html')