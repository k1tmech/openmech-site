from django.shortcuts import render

def home (request):
    return render (request, 'pages/home.html')

def dashboard (request):
    return render (request, 'pages/dashboard.html')

def learn (request):
    return render (request, 'pages/learn.html')





