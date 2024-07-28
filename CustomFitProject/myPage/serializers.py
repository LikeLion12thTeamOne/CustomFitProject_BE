from rest_framework import serializers
from customFit.models import RecommendedProduct

class RecommendedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedProduct
        fields = ['recommendedProduct_id', 'user', 'product', 'GNB', 'review']
        read_only_fields = ['recommendedProduct_id', 'user', 'product']

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        validated_data.pop('product', None)
        return super().update(instance, validated_data)
