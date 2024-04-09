from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def post(request):
    return render(request, 'core/detail.html')

def category(request):
    return render(request, 'core/home.html')

def author(request):
    return render(request, 'core/home.html')

def dates(request):
    return render(request, 'core/home.html')