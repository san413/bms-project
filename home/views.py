from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def request_blood(request):
    return render(request, 'home/request.html')

def donate(request):
    return render(request, 'home/donate.html')

def about(request):
    return render(request, 'home/about.html')

def login_page(request):
    return render(request, 'home/login.html')

