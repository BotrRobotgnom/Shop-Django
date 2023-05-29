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

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'main/detail.html', context)

def add_to_cart(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=pk)
        # Створити новий об'єкт Order
        order = Order(user=request.user, product=product)
        # Зберегти об'єкт Order
        order.save()
        return redirect('cart')  
    else:
        messages.error(request, 'Авторизуйтесь')
        return redirect('login')


def cart(request):
    # Перевірка, чи користувач аутентифікований
    if request.user.is_authenticated:
        # Отримати замовлення, пов'язані з користувачем
        orders = Order.objects.filter(user=request.user)
        total_price = sum(order.product.price for order in orders)

        context = {
            'orders': orders,
            'total_price': total_price,
        }
    else:
        # Якщо користувач неаутентифікований, повернути порожній список замовлень
        orders = []

        context = {
            'orders': orders
        }
    return render(request, 'main/cart.html', context)

def remove_from_cart(request, order_id):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            order.delete()
        except Order.DoesNotExist:
            pass

    return redirect('cart')

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        messages.error(request, 'Авторизуйтесь')
        return redirect('login')

    cart = Order.objects.filter(user=user)

    # Очищення кошика
    for order in cart:
        order.delete()

    # Перенаправлення на головну сторінку
    return redirect('/')


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
