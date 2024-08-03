from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

#키워드 
class UserAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['age']

class UserGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['gender']

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


CustomUser = get_user_model()

# 회원 가입
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(write_only=True) #이름 필드(닉네임으로 사용)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True, required=True) #비밀번호 확인 
    
    terms_accepted = serializers.BooleanField(write_only=True)  # 전체 이용약관 동의 필드
    terms_accepted_1 = serializers.BooleanField(write_only=True, required=False)  # 첫 번째 필수 이용약관 동의 필드
    terms_accepted_2 = serializers.BooleanField(write_only=True, required=False)  # 두 번째 필수 이용약관 동의 필드
    terms_accepted_optional = serializers.BooleanField(write_only=True, required=False)  # 선택 이용약관 동의 필드
       
    # 아이디 조건 검사
    def validate_username(self, value):
        if len(value) < 4 or len(value) > 16:
            raise serializers.ValidationError('아이디는 4자 이상 16자 이하로 입력해야 합니다.')
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('중복된 아이디가 있습니다.')
        return value

    """# 비밀번호 조건 검사
    def validate_password(self, value):
        errors = []

        # 비밀번호 길이 검사
        if len(value) < 8:
            errors.append('비밀번호는 8자 이상으로 입력해야 합니다.')

        # 숫자 포함 여부 검사
        if not any(char.isdigit() for char in value):
            errors.append('비밀번호에는 숫자가 포함되어야 합니다.')

        # 영문자 포함 여부 검사
        if not any(char.isalpha() for char in value):
            errors.append('비밀번호에는 영문자가 포함되어야 합니다.')

        # 특수문자 포함 여부 검사
        if not any(char in '!@#$%^&*()_+-=[]{},.<>?/~`' for char in value):
            errors.append('비밀번호에는 특수문자가 포함되어야 합니다.')

        # 오류가 있으면 모든 오류를 하나의 문자열로 결합하여 반환 >>  여기 수정함
        if errors:
            raise serializers.ValidationError(' '.join(errors))

        return value"""
    
    # 비밀번호 조건 검사 >> 디자인에 맞춰서 수정함
    def validate_password(self, value):
        if len(value) < 8 or not any(char.isdigit() for char in value) or not any(char.isalpha() for char in value) or not any(char in '!@#$%^&*()_+-=[]{},.<>?/~' for char in value):
            raise serializers.ValidationError('4~16자리 / 영문, 숫자, 특수문자 조합을 충족해 주세요.')
        return value
    
    # 이메일 조건 검사
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('중복된 이메일이 있습니다.')
        return value
   

    def validate(self, data):
        # 약관 조건 검사
        if data.get('terms_accepted', False):
            data['terms_accepted_1'] = True
            data['terms_accepted_2'] = True
            data['terms_accepted_optional'] = True

        if not data.get('terms_accepted_1') or not data.get('terms_accepted_2'):
            raise serializers.ValidationError('필수 약관에 동의하지 않을 경우, 회원 가입이 어렵습니다.')

        return data

    
    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirm']:
            raise serializers.ValidationError({'password': '비밀번호와 비밀번호 확인이 일치하지 않습니다. 다시 입력해주세요!'})

        
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],  # 이름 필드
            terms_accepted_1=validated_data['terms_accepted_1'],  # 첫 번째 이용약관 동의 여부 필드
            terms_accepted_2=validated_data['terms_accepted_2'],  # 두 번째 필수 이용약관 동의 여부 필드
            terms_accepted_optional=validated_data.get('terms_accepted_optional', False),  # 선택적 이용약관 동의 여부 필드
        
        )

        user.first_name = validated_data.pop('first_name')
        user.save()
        return user

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.terms_accepted_1 = validated_data.get('terms_accepted_1', instance.terms_accepted_1)  # 첫 번째 이용약관 동의 여부 필드
        instance.terms_accepted_2 = validated_data.get('terms_accepted_2', instance.terms_accepted_2)  # 두 번째 이용약관 동의 여부 필드
        instance.terms_accepted_optional = validated_data.get('terms_accepted_optional', instance.terms_accepted_optional)  # 선택적 이용약관 동의 여부 필드

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        return instance

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'password_confirm', 'first_name', 'email', 'terms_accepted', 'terms_accepted_1', 'terms_accepted_2', 'terms_accepted_optional']


