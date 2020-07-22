from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class CategoryListAPIView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	
class SubCategoryListAPIView(ListAPIView):
	queryset = SubCategory.objects.all()
	serializer_class = SubCategorySerializer

class ProductListAPIView(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
