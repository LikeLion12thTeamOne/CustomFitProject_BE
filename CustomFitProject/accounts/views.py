from django.views import View  
from django.shortcuts import redirect, render  
from django.urls import reverse  
from django.core.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserRegistrationSerializer, UserAgeSerializer, UserGenderSerializer, 
    UserDiseaseSerializer, UserHeightSerializer, UserWeightSerializer
)
from .models import CustomUser

# 이 단계별로 회원가입

# 1단계) 회원 정보, 약관  >> 여기 코드 추가해야함
class UserRegistrationStep1View(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]     # 미로그인 상태 가능하게

    def perform_create(self, serializer):
        self.request.session['registration_data'] = serializer.validated_data
        serializer.save()

# 2단계) 나이
class UserRegistrationStep2View(generics.UpdateAPIView):
    serializer_class = UserAgeSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return CustomUser.objects.get(username=self.request.session['registration_data']['username'])

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        serializer.save()

# 3단계) 성별
class UserRegistrationStep3View(generics.UpdateAPIView):
    serializer_class = UserGenderSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return CustomUser.objects.get(username=self.request.session['registration_data']['username'])

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        serializer.save()

# 4단계) 질병
class UserRegistrationStep4View(generics.UpdateAPIView):
    serializer_class = UserDiseaseSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return CustomUser.objects.get(username=self.request.session['registration_data']['username'])

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        serializer.save()

# 5단계) 키
class UserRegistrationStep5View(generics.UpdateAPIView):
    serializer_class = UserHeightSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return CustomUser.objects.get(username=self.request.session['registration_data']['username'])

    def perform_update(self, serializer):
        self.request.session['registration_data'].update(serializer.validated_data)
        serializer.save()


# 6단계) 몸무게 >> 여기서 회원이 저장되도록 함
class UserRegistrationStep6View(generics.UpdateAPIView):
    serializer_class = UserWeightSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return CustomUser.objects.get(username=self.request.session['registration_data']['username'])

    def perform_update(self, serializer):
        registration_data = self.request.session.pop('registration_data')
        registration_data.update(serializer.validated_data)
        user = CustomUser.objects.get(username=registration_data['username'])
        user.age = registration_data['age']
        user.gender = registration_data['gender']
        user.disease = registration_data['disease']
        user.height = registration_data['height']
        user.weight = registration_data['weight']
        user.set_password(registration_data['password'])
        user.save()