from django.shortcuts import render
import string
import random

# Create your views here.

def home(request):
    return render(
        request,
        'generator/home.html',
        {"range": range(8,17)},
    )

def password(request):
    generatedPassword=""
    salt = list(string.ascii_lowercase)

    if request.GET.get("numbers"):
        salt.extend(list(string.digits))
    if request.GET.get("uppercase"):
        salt.extend(list(string.ascii_uppercase))
    if request.GET.get("special_chars"):
        salt.extend(list(string.punctuation))
    
    for _ in range(int(request.GET.get("length"))):
        generatedPassword += random.choice(salt)

    return render(
        request,
        "generator/password.html",
        {"generatedPassword": generatedPassword}
    )

def about(request):
    return render(
        request,
        "generator/about.html"
    )
