from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RecommendedProductSerializer
from customFit.models import RecommendedProduct
from accounts.models import CustomUser
from accounts.serializers import UserAgeSerializer, UserDiseaseSerializer, UserHeightSerializer, UserWeightSerializer
from .models import Notice
from .serializers import NoticeListSerializer, NoticeDetailSerializer
from .serializers import UserProfileSerializer #myPage 회원정보 가져오기

# 추천상품 목록 보기
class RecommendedProductListView(generics.ListAPIView):
    serializer_class = RecommendedProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RecommendedProduct.objects.filter(user=self.request.user)

# 추천상품 목록 중 추천상품 리뷰 작성하기 및 수정하기
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


#키워드 업데이트
class UserAgeUpdateView(generics.UpdateAPIView):
    serializer_class = UserAgeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserDiseaseUpdateView(generics.UpdateAPIView):
    serializer_class = UserDiseaseSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserHeightUpdateView(generics.UpdateAPIView):
    serializer_class = UserHeightSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserWeightUpdateView(generics.UpdateAPIView):
    serializer_class = UserWeightSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

#공지사항   
class NoticeListView(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeListSerializer

class NoticeDetailView(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeDetailSerializer


#myPage 회원정보 가져오기 
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user