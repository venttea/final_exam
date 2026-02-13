from django.contrib import admin
from django.urls import path
from appBOM import views

urlpatterns = [

    # Панель администратора
    path('admin/', admin.site.urls),

    # Вход в систему
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),

    # Выход из системы
    path('logout/', views.logout_view, name='logout'),

    # Главная страница (после авторизации)
    path('home/', views.home, name='home'),

    # Список товаров доступный всем
    path('products/', views.view_products, name='product_list'),

    # Список заказов для администраторов и менеджеров
    path('orders/', views.view_orders, name='order_list'),
]