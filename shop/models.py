from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    category = models.ForeignKey(Category, related_name='shops', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)