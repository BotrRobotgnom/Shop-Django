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
        user = request.user
        order, created = Order.objects.get_or_create(user=user, status=Order.AWAIT)
        product = get_object_or_404(Product, pk=pk)
        order.add_item(product)
        return redirect('cart')
    else:
        messages.error(request, 'Авторизуйтесь')
        return redirect('login')

def update_quantity(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id, status=Order.AWAIT)
        keys = list(order.items.keys())  # Create a copy of the keys
        for product in keys:
            quantity = int(request.POST.get(f'quantity{product.id}', 0))
            if quantity > 0:
                order.items[product] = quantity
            else:
                order.remove_item(product)
    return redirect('cart')

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        orders = Order.objects.filter(user=user, status=Order.AWAIT)
    else:
        orders = []
    context = {
        'orders': orders
    }
    return render(request, 'main/cart.html', context)

def remove_from_cart(request, order_id, product_id):
    if request.user.is_authenticated:
        user = request.user
        order = get_object_or_404(Order, id=order_id, user=user, status=Order.AWAIT)
        product = get_object_or_404(Product, id=product_id)
        order.remove_item(product)
    return redirect('cart')

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        orders = Order.objects.filter(user=user, status=Order.AWAIT)
        for order in orders:
            order.status = Order.COMPLETED
            order.save()
    else:
        messages.error(request, 'Авторизуйтесь')
        return redirect('login')
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
