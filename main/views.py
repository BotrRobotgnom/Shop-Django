from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

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
        try:
            user = User.objects.get(username=username)
            return render(request, 'registration.html', {'error': 'Користувач з таким іменем вже існує'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'main/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Невірне ім\'я користувача або пароль'})
    else:
        return render(request, 'main/login.html')
