from django.contrib import admin
from .models import FoodCategory, Product, RecommendedProduct

admin.site.register(FoodCategory)
admin.site.register(Product)
admin.site.register(RecommendedProduct)
