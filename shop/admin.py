from django.contrib import admin
from .models import Shop, Category, Product


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','shop','price','available']
    list_filter = ['available', 'category','shop']
    list_editable = ['price','available']
    prepopulated_fields = {'slug': ('name',)}

