from rest_framework import serializers
from .models import CustomUser

# 이 단계별로 등록 (과정)

# 1단계) 회원 정보, 약관  >> 여기 코드 추가해야함
class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password_confirm', 'first_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            # last_name 제외
        )
        return user


# 2단계) 나이
class UserAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['age']

# 3단계) 성별
class UserGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['gender']

# 4단계) 질병
class UserDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['disease']

# 5단계) 키
class UserHeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['height']

# 6단계) 몸무게
class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['weight']