from rest_framework import serializers
from .models import CustomUser

# 이 단계별로 등록 (과정)

# 1단계) 회원 정보, 약관  >> 여기 코드 추가해야함
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(write_only=True) #이름 필드(닉네임으로 사용)
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True, required=True) #비밀번호 확인 
    
    terms_accepted = serializers.BooleanField(write_only=True)  # 전체 이용약관 동의 필드
    terms_accepted_1 = serializers.BooleanField(write_only=True, required=False)  # 첫 번째 필수 이용약관 동의 필드
    terms_accepted_2 = serializers.BooleanField(write_only=True, required=False)  # 두 번째 필수 이용약관 동의 필드
    terms_accepted_optional = serializers.BooleanField(write_only=True, required=False)  # 선택 이용약관 동의 필드
       

    def validate(self, data):
        # 전체 동의가 체크된 경우
        if data.get('terms_accepted', False):
            data['terms_accepted_1'] = True
            data['terms_accepted_2'] = True
            data['terms_accepted_optional'] = True
        
        # 필수 동의 체크
        if not data.get('terms_accepted_1'):
            raise serializers.ValidationError({'terms_accepted_1': '첫 번째 필수 이용약관에 동의해야 합니다.'})
        if not data.get('terms_accepted_2'):
            raise serializers.ValidationError({'terms_accepted_2': '두 번째 필수 이용약관에 동의해야 합니다.'})
        
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