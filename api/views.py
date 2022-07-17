import json
from django.http import JsonResponse
from shop.models import Category,Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
# Create your views here.


@api_view(['GET','POST'])
def home(request,*args,**kwargs):
    instance = Product.objects.all().first()
    data = {}
    if instance:
        data = ProductSerializers(instance).data

    return Response(data)