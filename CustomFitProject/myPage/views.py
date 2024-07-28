from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RecommendedProductSerializer
from customFit.models import RecommendedProduct

# 추천상품 목록 보기
class RecommendedProductListView(generics.ListAPIView):
    serializer_class = RecommendedProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RecommendedProduct.objects.filter(user=self.request.user)

# 추천상품 목록 중 추천상품 리뷰 작성하기 및 수정하기 edit
class RecommendedProductEditView(generics.RetrieveUpdateAPIView):
    serializer_class = RecommendedProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RecommendedProduct.objects.filter(user=self.request.user)

# 추천상품 목록 중 추천상품 리뷰 자세히 보기
class RecommendedProductDetailView(generics.RetrieveAPIView):
    serializer_class = RecommendedProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RecommendedProduct.objects.filter(user=self.request.user)
