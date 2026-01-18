from django.db import models
from django.contrib.auth.models import User


# Единицы измерения
class UnitMes(models.Model):
    name = models.CharField()


# Поставщики
class Providers(models.Model):
    name = models.CharField()


# Производители
class Producers(models.Model):
    name = models.CharField()


# Категории продуктов
class CategoryProduct(models.Model):
    name = models.CharField()


# Пункты выдачи
class PointPlace(models.Model):
    index = models.IntegerField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()


# Статусы заказов
class StatusOrder(models.Model):
    name = models.CharField()


# Данные заказа
class DataOrder(models.Model):
    date_order = models.DateField()
    date_delivery = models.DateField()
    id_PVZ = models.ForeignKey(PointPlace, on_delete=models.CASCADE)
    code = models.IntegerField()
    id_status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


# Товары
class Products(models.Model):
    article = models.CharField()
    name = models.CharField()
    id_unit_mes = models.ForeignKey(UnitMes, on_delete=models.CASCADE)
    price = models.IntegerField()
    id_provider = models.ForeignKey(Providers, on_delete=models.CASCADE)
    id_producer = models.ForeignKey(Producers, on_delete=models.CASCADE)
    id_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    photo = models.CharField()


# Заказ
class Order(models.Model):
    id_data = models.ForeignKey(DataOrder, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

