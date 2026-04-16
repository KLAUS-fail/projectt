from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Order, Product, PickupPoint

admin.site.register(Order)
admin.site.register(PickupPoint)
admin.site.register(Product)

admin.site.unregister(Group)
