from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserRegistrationSerializer, UserAgeSerializer, UserGenderSerializer, 
    UserDiseaseSerializer, UserHeightSerializer, UserWeightSerializer
)
from .models import CustomUser

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserAgeUpdateView(generics.UpdateAPIView):
    serializer_class = UserAgeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserGenderUpdateView(generics.UpdateAPIView):
    serializer_class = UserGenderSerializer
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
