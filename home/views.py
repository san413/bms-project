from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Donor

def index(request):
    return render(request, 'home/index.html')

def request_blood(request):
    return render(request, 'home/request.html')

def donate(request):
    return render(request, 'home/donate.html')

def about(request):
    return render(request, 'home/about.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'home/login.html', {"error": "Invalid username or password"})

    return render(request, 'home/login.html')

def register_page(request):
    return render(request, 'home/register.html')

def register_donor(request):
    return render(request, 'home/register_donor.html')

def profile(request):
    return render(request, 'home/profile.html')

from django.shortcuts import render

def blood_availability(request):
    return render(request, 'home/blood_availability.html')

def blood_types(request):
    return render(request, 'home/blood_types.html')

def search_donor(request):
    return render(request, 'home/search_donor.html')

def register_volunteer(request):
    return render(request, 'home/register_volunteer.html')

def register_donor(request):
    if request.method == "POST":
        Donor.objects.create(
            name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            age=request.POST.get("age"),
            dob=request.POST.get("dob"),
            mobile=request.POST.get("mobile"),
            blood_group=request.POST.get("blood_group"),
            address=request.POST.get("address"),
        )

        return render(request, "home/register_donor.html", {"success": True})

    return render(request, "home/register_donor.html")
