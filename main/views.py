from django.shortcuts import render
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