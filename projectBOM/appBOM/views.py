from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import *


# Обработка входа пользователя в систему
def login_view(request):
    if request.method == 'POST':

        # Получение логина и пароля из формы
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Проверка существования пользователя с такими данными
        if user is not None:

            # Вход в систему, в случае, если данные есть в системе
            login(request, user)
            return redirect('home')

        # В случае неудачи - вывод ошибки
        else:
            return render(request, 'appBOM/login.html', {'error': 'Неверный логин или пароль (｡•́︿•̀｡)'})

    # Демонстрация страницы авторизации
    return render(request, 'appBOM/login.html')



# Обработка выхода из системы
def logout_view(request):
    logout(request)
    return redirect('login')



# Проверка роли: Администратор
def is_administrator(user):
    profile = Profile.objects.get(user=user)
    return profile.role.name == 'admin'



# Проверка роли: Менеджер
def is_manager(user):
    profile = Profile.objects.get(user=user)
    return profile.role.name == 'manager'



# Проверка роли: Клиент
def is_client(user):
    profile = Profile.objects.get(user=user)
    return profile.role.name == 'client'



# Проверка роли: Администратор ИЛИ Менеджер
def administrator_or_manager(user):
    profile = Profile.objects.get(user=user)
    return profile.role.name in ['admin', 'manager']



# Главная страница
@login_required
def home(request):

    # Получение роли пользователя
    profile = Profile.objects.get(user=request.user)
    role = profile.role.name

    # Формирование ФИО
    full_name = ""
    if request.user.first_name and request.user.last_name:
        full_name = f"{request.user.first_name} {request.user.last_name}"
    elif request.user.first_name:
        full_name = request.user.first_name

    return render(request, 'appBOM/home.html', {'role': role, 'full_name': full_name})



# Страница "Товары"
def view_products(request):
    products = Products.objects.all()

    # Получение полного имени пользователя, если авторизован
    if request.user.is_authenticated:
        full_name = request.user.get_full_name()
    else:
        full_name = "Гость"

    return render(request, 'appBOM/product_list.html', {'products': products, 'full_name': full_name, 'user': request.user})



# Страница "Заказы"
@login_required
@user_passes_test(administrator_or_manager)
def view_orders(request):
    orders = Order.objects.all().select_related('id_data', 'id_product')

    # Получение полного имени пользователя
    full_name = request.user.get_full_name()

    return render(request, 'appBOM/order_list.html', {'orders': orders, 'full_name': full_name})