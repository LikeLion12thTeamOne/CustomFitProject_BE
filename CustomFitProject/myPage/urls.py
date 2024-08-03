from django.urls import path
from .views import (
    RecommendedProductListView, RecommendedProductEditView, 
    RecommendedProductDetailView
)
from .views import UserAgeUpdateView, UserDiseaseUpdateView, UserHeightUpdateView, UserWeightUpdateView
from .views import NoticeListView, NoticeDetailView
from .views import UserProfileView #myPage 회원정보 가져오기

urlpatterns = [
    # 추천상품 목록 보기
    path('recommended-products/', RecommendedProductListView.as_view(), name='recommended-product-list'),
    # 추천상품 목록 중 추천상품 리뷰 작성하기 및 수정하기
    path('recommended-products/<int:pk>/edit/', RecommendedProductEditView.as_view(), name='recommended-product-create-update'),
    # 추천상품 목록 중 추천상품 리뷰 자세히 보기
    path('recommended-products/<int:pk>/', RecommendedProductDetailView.as_view(), name='recommended-product-detail'),

    #키워드 변경 
    path('update/age/', UserAgeUpdateView.as_view(), name='update-age'), #age
    path('update/disease/', UserDiseaseUpdateView.as_view(), name='update-disease'), #disease
    path('update/height/', UserHeightUpdateView.as_view(), name='update-height'), #height
    path('update/weight/', UserWeightUpdateView.as_view(), name='update-weight'), #weight

    path('notices/', NoticeListView.as_view(), name='notice-list'), #전체 공지조회
    path('notices/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'), #개별 공지확인

    path('profile/', UserProfileView.as_view(), name='user-profile'), #myPage 회원정보 가져오기 
]
