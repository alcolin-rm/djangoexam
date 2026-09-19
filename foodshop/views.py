from decimal import Decimal, ROUND_HALF_UP

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm, OrderForm
from .models import Dish, Order


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dish_list')
    else:
        form = RegisterForm()

    return render(request, 'shop/register.html', {'form': form})


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'shop/dish_list.html', {'dishes': dishes})


@login_required
def order_create(request):
    initial = {}

    dish_id = request.GET.get('dish')
    if dish_id:
        initial['dish'] = dish_id

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user

            user = request.user

            if form.cleaned_data.get('use_bonuses'):
                user.bonus_balance = Decimal('0.00')

            bonus = (
                order.dish.price * Decimal('0.05')
            ).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            user.bonus_balance += bonus
            user.save()

            order.save()
            return redirect('my_orders')
    else:
        form = OrderForm(initial=initial)

    return render(request, 'shop/order_create.html', {'form': form})


@login_required
def my_orders(request):
    orders = Order.objects.filter(client=request.user).select_related('dish')
    return render(request, 'shop/my_orders.html', {'orders': orders})