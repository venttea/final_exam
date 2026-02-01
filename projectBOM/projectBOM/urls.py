from django.contrib import admin
from django.urls import path
from appBOM import views

urlpatterns = [

    # Админка
    path('admin/', admin.site.urls),

    # Вход в систему
    path('', views.login_view, name='login'),

    # Вход в систему
    path('login/', views.login_view, name='login'),

    # Выход из системы
    path('logout/', views.logout_view, name='logout'),

    # Главная страница (после авторизации)
    path('home/', views.home, name='home'),
]