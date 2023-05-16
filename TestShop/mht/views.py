from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'mht/index.html')
    #return HttpResponse("Тест")

def shop(request):
    return render(request, 'mht/shop.html')

def detail(request):
    return render(request, 'mht/detail.html')

def cart(request):
    return render(request, 'mht/cart.html')

def checkout(request):
    return render(request, 'mht/checkout.html')

def contact(request):
    return render(request, 'mht/contact.html')