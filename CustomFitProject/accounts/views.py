from django.views import View  
from django.shortcuts import redirect, render  
from django.urls import reverse  
from django.core.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework.permissions import AllowAny
#키워드 입력부분 
from .serializers import (
    UserRegistrationSerializer, UserAgeSerializer, UserGenderSerializer, 
    UserDiseaseSerializer, UserHeightSerializer, UserWeightSerializer
)
from .models import CustomUser

# 이 단계별로 회원가입

# 1단계) 회원 정보, 약관  >> 여기 코드 추가해야함
class UserRegistrationStep1View(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]     # 모든 사용자가 접근

    def perform_create(self, serializer):   # 사용자가 등록될 때 호출
        user = serializer.save()    # 새로운 사용자 객체를 저장

        # 세션에 사용자 이름과 비밀번호를 저장
        self.request.session['registration_data'] = {
            'username': user.username,
            'password': serializer.validated_data['password']
        }
        self.request.session.save()     # 세션 데이터를 저장


# 2단계) 나이
class UserRegistrationStep2View(generics.UpdateAPIView):
    serializer_class = UserAgeSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        # 세션에서 사용자 이름을 가져와 해당 사용자 객체를 반환
        username = self.request.session.get('registration_data', {}).get('username')
        
        # 세션에 사용자 이름이 없으면 PermissionDenied 예외를 발생
        if not username:
            raise PermissionDenied("No registration data found in session.")
        return CustomUser.objects.get(username=username)

    # 사용자가 나이를 업데이트할 때 호출
    def perform_update(self, serializer):
        # 세션에 저장된 데이터에 새로운 나이 데이터를 추가
        self.request.session['registration_data'].update(serializer.validated_data)
        self.request.session.save()     # 세션 데이터를 저장
        serializer.save()   # 사용자 객체를 저장

# 3단계) 성별
class UserRegistrationStep3View(generics.UpdateAPIView):
    serializer_class = UserGenderSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        username = self.request.session.get('registration_data', {}).get('username')
        if not username:
            raise PermissionDenied("No registration data found in session.")
        return CustomUser.objects.get(username=username)

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        self.request.session.save()
        serializer.save()

# 4단계) 질병
class UserRegistrationStep4View(generics.UpdateAPIView):
    serializer_class = UserDiseaseSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        username = self.request.session.get('registration_data', {}).get('username')
        if not username:
            raise PermissionDenied("No registration data found in session.")
        return CustomUser.objects.get(username=username)

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        self.request.session.save()
        serializer.save()

# 5단계) 키
class UserRegistrationStep5View(generics.UpdateAPIView):
    serializer_class = UserHeightSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        username = self.request.session.get('registration_data', {}).get('username')
        if not username:
            raise PermissionDenied("No registration data found in session.")
        return CustomUser.objects.get(username=username)

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        self.request.session.save()
        serializer.save()

# 6단계) 몸무게
class UserRegistrationStep6View(generics.UpdateAPIView):
    serializer_class = UserWeightSerializer
    permission_classes = [AllowAny]

    # 세션에서 사용자 이름을 가져와 해당 사용자 객체를 반환
    def get_object(self):
        username = self.request.session.get('registration_data', {}).get('username')
        if not username:
            raise PermissionDenied("No registration data found in session.")
        return CustomUser.objects.get(username=username)

    # 사용자가 몸무게를 업데이트할 때 호출
    def perform_update(self, serializer):
        # 세션에서 등록 데이터를 가져오기
        registration_data = self.request.session.get('registration_data', {})
        #  세션에 저장된 데이터에 새로운 몸무게 데이터를 추가
        registration_data.update(serializer.validated_data)

        self.request.session.save() # 세션 데이터를 저장

        # 사용자 객체를 가져와 세션 데이터를 통해 모든 필드를 업데이트
        user = CustomUser.objects.get(username=registration_data.get('username'))
        user.age = registration_data.get('age')
        user.gender = registration_data.get('gender')
        user.disease = registration_data.get('disease')
        user.height = registration_data.get('height')
        user.weight = registration_data.get('weight')
        user.set_password(registration_data.get('password'))    # 비밀번호를 설정
        
        user.save()     # 사용자 객체를 저장

        # 세션에서 등록 데이터를 삭제
        self.request.session.pop('registration_data', None)

        return serializer.data