from django.contrib import admin
from .models import Category, Customer, Worker, Product, Order

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Worker)
admin.site.register(Product)
admin.site.register(Order)
