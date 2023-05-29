from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop.html', views.shop),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('contact.html', views.contact),
    path('registration.html', views.register),
    path('login.html', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:order_id>/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:order_id>/', views.update_quantity, name='update_quantity'),

]
