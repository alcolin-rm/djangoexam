from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('dishes/', views.dish_list, name='dishes'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='foodshop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/', views.my_orders, name='my_orders'),
]