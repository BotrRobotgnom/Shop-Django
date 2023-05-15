from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop.html', views.shop),
    path('detail.html', views.detail),
    path('cart.html', views.cart),
    path('checkout.html', views.checkout),
    path('contact.html', views.contact)
]
