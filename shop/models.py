from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	
	class Meta:
		ordering = ('name', )
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		
	def __str__(self):
		return self.name
		
class SubCategory(models.Model):
	category = models.ForeignKey(Category, related_name='sub_category', on_delete=models.PROTECT)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	
	class Meta:
		ordering = ('name', )
		verbose_name = 'sub category'
		verbose_name_plural = 'sub categories'
		
	def __str__(self):
		return self.name

class Product(models.Model):
	sub_category = models.ForeignKey(SubCategory, related_name='product', on_delete=models.PROTECT)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	
	class Meta:
		ordering = ('name', )
		index_together = (('id', 'slug'))
		
	def __str__(self):
		return self.name
