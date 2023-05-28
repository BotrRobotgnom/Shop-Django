from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop.html', views.shop),
    path('detail.html', views.detail),
    path('cart.html', views.cart),
    path('checkout.html', views.checkout),
    path('contact.html', views.contact),
    path('registration.html', views.register),
    path('login.html', views.login),
    path('logout/', views.logout_user, name='logout'),
]
