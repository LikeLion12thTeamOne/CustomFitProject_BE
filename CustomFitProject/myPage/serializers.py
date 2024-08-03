from rest_framework import serializers
from customFit.models import RecommendedProduct
from accounts.models import CustomUser
from .models import Notice

# 추천상품 직렬화
class RecommendedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedProduct
        fields = ['recommendedProduct_id', 'user', 'product','product_name', 'disease', 'GNB', 'review', 'rating']  # 별점 필드 추가
        read_only_fields = ['recommendedProduct_id', 'user', 'product', 'product_name','disease', 'rating']

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        validated_data.pop('product', None)
        return super().update(instance, validated_data)
    
#키워드 변경
class UserAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['age']

class UserDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['disease']

class UserHeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['height']

class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['weight']

#알림공지사항
class NoticeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title'] #list에는 제목만 보이게 / id는 글 구분

class NoticeDetailSerializer(serializers.ModelSerializer): #공지글 확인

    created_at = serializers.DateTimeField(format="%Y-%m-%d") #작성일-연도,월,일 만 보이게 

    class Meta:
        model = Notice
        fields = ['id', 'title', 'content',  'image', 'created_at']

class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'image']


#myPage 회원정보 가져오기 
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'first_name', 'age', 'gender', 
            'disease', 'height', 'weight', 'average_rating'
        ]
