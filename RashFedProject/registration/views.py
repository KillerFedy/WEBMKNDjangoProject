from django.shortcuts import render

def index(request):
    return render(request, 'registration/registration.html')

def authorization(request):
    return render(request, 'registration/login.html')
