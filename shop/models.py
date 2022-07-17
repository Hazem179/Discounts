from django.db import models

STATUS = (('active', 'Active'),
          ('pending', 'Pending'),
          ('stopped', 'Stopped'))


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
    address = models.CharField(max_length=1024)
    status = models.CharField(max_length=32, choices=STATUS)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    available = models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = ('name','slug')


    def __str__(self):
        return self.name
