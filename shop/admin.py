from django.contrib import admin
from .models import Shop,Category,Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name','category']