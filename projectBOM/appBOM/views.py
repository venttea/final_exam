from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        else:

            # В случае неудачи - вывод ошибки
            return render(request, 'appBOM/login.html', {'error': 'Неверный логин или пароль'})

    # Демонстрация страницы авторизации
    return render(request, 'appBOM/login.html')


# Обработка выхода из системы
def logout_view(request):
    logout(request)
    return redirect('login')


# Главная страница после авторизации
@login_required
def home(request):
    return render(request, 'appBOM/home.html')