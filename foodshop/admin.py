from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Dish, Order


@admin.register(Client)
class ClientAdmin(UserAdmin):
    list_display = ('username', 'email', 'bonus_balance', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Бонусная программа', {'fields': ('bonus_balance',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Бонусная программа', {'fields': ('bonus_balance',)}),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'dish', 'created_at')