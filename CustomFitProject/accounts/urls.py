from django.urls import path, include
from .views import (
    UserRegistrationView, UserAgeUpdateView, UserGenderUpdateView, 
    UserDiseaseUpdateView, UserHeightUpdateView, UserWeightUpdateView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/age/', UserAgeUpdateView.as_view(), name='register-age'),
    path('register/gender/', UserGenderUpdateView.as_view(), name='register-gender'),
    path('register/disease/', UserDiseaseUpdateView.as_view(), name='register-disease'),
    path('register/height/', UserHeightUpdateView.as_view(), name='register-height'),
    path('register/weight/', UserWeightUpdateView.as_view(), name='register-weight'),
    
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
]