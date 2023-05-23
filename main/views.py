from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse
from .models import User, Account


# Create your views here.
def index(request):
    return render(request, 'main/index.html')
    #return HttpResponse("Тест")

def shop(request):
    return render(request, 'main/shop.html')

def detail(request):
    return render(request, 'main/detail.html')

def cart(request):
    return render(request, 'main/cart.html')

def checkout(request):
    return render(request, 'main/checkout.html')

def contact(request):
    return render(request, 'main/contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.error(request, 'Користувач з таким іменем вже існує')
            return render(request, 'main/registration.html')
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'main/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Невірне ім\'я користувача або пароль')
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')
