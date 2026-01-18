from django.db import models
from django.contrib.auth.models import User


# Единицы измерения
class UnitMes(models.Model):
    name = models.CharField()


# Поставщик
class Provider(models.Model):
    name = models.CharField()


# Производитель
class Producer(models.Model):
    name = models.CharField()


# Категория продукта
class CategoryProduct(models.Model):
    name = models.CharField()


# Пункт выдачи
class PointPlace(models.Model):
    index = models.IntegerField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()


# Статусы заказа
class StatusOrder(models.Model):
    name = models.CharField()


# Заказ
class Order(models.Model):
    date_order = models.DateField()
    date_delivery = models.DateField()
    point_place = models.ForeignKey(PointPlace, on_delete=models.CASCADE)
    code_order = models.IntegerField()
    status_order = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    client_order = models.ForeignKey(User, on_delete=models.CASCADE)


# Товары
class Product(models.Model):
    artickle = models.CharField()
    name = models.CharField()
    unit_mes = models.ForeignKey(UnitMes, on_delete=models.CASCADE)
    price = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    discount = models.IntegerField()
    count_store = models.IntegerField()
    description = models.TextField()
    photo_name = models.CharField()


# Товар в заказе
class ProductOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count_product = models.IntegerField()

