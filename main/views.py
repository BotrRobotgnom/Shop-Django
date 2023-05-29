from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from .models import User, Product, Order

def index(request):
    return render(request, 'main/index.html')

def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main/shop.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'main/detail.html', context)

def cart(request):
    return render(request, 'main/cart.html')

def checkout(request):
    if request.user.is_authenticated:
        # Get the user's cart or create a new one
        cart, created = Order.objects.get_or_create(user=request.user, status=Order.CART)
        context = {
            'cart': cart
        }
        return render(request, 'main/checkout.html', context)
    else:
        messages.error(request, 'You need to be logged in to proceed to checkout.')
        return redirect('login')

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
