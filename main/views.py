from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import User


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
        if User.objects.filter(username=username).exists():
            # Обробка помилки, якщо користувач вже існує
            messages.error(request, 'Такий користувач уже існує')
            return render(request, 'main/registration.html')
        
        # Створення нового користувача
        user = User(username=username)
        user.set_password(password)
        user.save()
        # Логін користувача після реєстрації
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
            user.save()
            return redirect('/')
        else:
            messages.error(request, 'Невірне ім\'я користувача або пароль')
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')
