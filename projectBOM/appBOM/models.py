from django.db import models
from django.contrib.auth.models import User


# Единицы измерения
class UnitMes(models.Model):
    id_unit_mes = models.IntegerField(primary_key=True)
    name = models.CharField()


# Поставщики
class Providers(models.Model):
    id_provider = models.IntegerField(primary_key=True)
    name = models.CharField()


# Производители
class Producers(models.Model):
    id_producer = models.IntegerField(primary_key=True)
    name = models.CharField()


# Категории продуктов
class CategoryProduct(models.Model):
    id_category = models.IntegerField(primary_key=True)
    name = models.CharField()


# Пункты выдачи
class PointPlace(models.Model):
    id_PVZ = models.IntegerField(primary_key=True)
    index = models.IntegerField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()

    def full_address(self):
        return f"{self.index}, {self.city}, {self.street}, {self.number}"


# Статусы заказов
class StatusOrder(models.Model):
    id_status = models.IntegerField(primary_key=True)
    name = models.CharField()


# Данные заказа
class DataOrder(models.Model):
    id_data = models.IntegerField(primary_key=True)
    date_order = models.DateField()
    date_delivery = models.DateField()
    id_PVZ = models.ForeignKey(PointPlace, on_delete=models.CASCADE)
    code = models.IntegerField()
    id_status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


# Товары
class Products(models.Model):
    id_product = models.IntegerField(primary_key=True)
    article = models.CharField()
    name = models.CharField()
    id_unit_mes = models.ForeignKey(UnitMes, on_delete=models.CASCADE)
    price = models.IntegerField()
    id_provider = models.ForeignKey(Providers, on_delete=models.CASCADE)
    id_producer = models.ForeignKey(Producers, on_delete=models.CASCADE)
    id_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField()
    description = models.TextField()
    photo = models.CharField()

    def get_discounted_price(self):
        """Возвращает цену со скидкой"""
        if self.discount > 0:
            discounted = self.price * (100 - self.discount) / 100
            return round(discounted, 2)
        return self.price

    def get_saving(self):
        """Возвращает сумму экономии"""
        if self.discount > 0:
            saving = self.price * self.discount / 100
            return round(saving, 2)
        return 0


# Заказ
class Order(models.Model):
    id_order = models.IntegerField(primary_key=True)
    id_data = models.ForeignKey(DataOrder, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()


# Роли
class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role_choices = (('admin', 'Администратор'), ('manager', 'Менеджер'), ('client', 'Клиент'))
    name = models.CharField(max_length=20, choices=role_choices, unique=True)


# Соединение пользователя с ролью
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True, blank=True)