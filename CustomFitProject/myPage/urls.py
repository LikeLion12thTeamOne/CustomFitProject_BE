from django.urls import path
from .views import (
    RecommendedProductListView, RecommendedProductEditView, 
    RecommendedProductDetailView
)

urlpatterns = [
    # 추천상품 목록 보기
    path('recommended-products/', RecommendedProductListView.as_view(), name='recommended-product-list'),

    # 추천상품 목록 중 추천상품 리뷰 작성하기 및 수정하기
    path('recommended-products/<int:pk>/edit/', RecommendedProductEditView.as_view(), name='recommended-product-create-update'),

    # 추천상품 목록 중 추천상품 리뷰 자세히 보기
    path('recommended-products/<int:pk>/', RecommendedProductDetailView.as_view(), name='recommended-product-detail'),
]
