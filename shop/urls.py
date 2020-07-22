from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
	path('category/', views.CategoryListAPIView.as_view(), name='CategoryListAPIView'),
	path('subcategory/', views.SubCategoryListAPIView.as_view(), name='SubCategoryListAPIView'),
	path('product/', views.ProductListAPIView.as_view(), name='ProductListAPIView'),
	path('category/<int:id>/', views.CategoryListAPIView.as_view(), name='CategoryListAPIView'),
	path('subcategory/<int:id>/', views.SubCategoryListAPIView.as_view(), name='SubCategoryListAPIView'),
	path('product/<int:id>/', views.ProductListAPIView.as_view(), name='ProductListAPIView'),
]