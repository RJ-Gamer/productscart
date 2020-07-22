from rest_framework.serializers import ModelSerializer
from .models import (Category, SubCategory, Product)

class CategorySerializer(ModelSerializer):
	def __init__(self, *args, **kwargs):
		super(CategorySerializer, self).__init__(*args, **kwargs)
		
	class Meta:
		model = Category
		fields = '__all__'
	

class SubCategorySerializer(ModelSerializer):
	def __init__(self, *args, **kwargs):
		super(SubCategorySerializer, self).__init__(*args, **kwargs)
		
	class Meta:
		model = SubCategory
		fields = '__all__' 


class ProductSerializer(ModelSerializer):
	def __init__(self, *args, **kwargs):
		super(ProductSerializer, self).__init__(*args, **kwargs)
		
	class Meta:
		model = Product
		fields = '__all__'
