from rest_framework import serializers
from .models import FoodCategory, Product, CartItem, RecommendedProduct

# 제품 정보를 직렬화
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 카테고리와 관련된 제품 정보를 직렬화
class FoodsCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)     #category:product = 1:n

    class Meta:
        model = FoodCategory
        fields = '__all__'

# 카트 항목을 직렬화
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['product']


# 추천상품 목록 직렬화
class RecommendedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedProduct
        fields = ['recommendedProduct_id', 'user', 'product', 'disease', 'GNB', 'review']  # 필드 추가
        read_only_fields = ['recommendedProduct_id', 'user', 'product', 'disease']
