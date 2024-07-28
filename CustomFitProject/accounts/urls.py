from django.urls import path, include
from .views import (
    UserRegistrationStep1View, UserRegistrationStep2View, UserRegistrationStep3View, 
    UserRegistrationStep4View, UserRegistrationStep5View, UserRegistrationStep6View
)

urlpatterns = [
    path('register/step1/', UserRegistrationStep1View.as_view(), name='register-step1'),
    path('register/step2/', UserRegistrationStep2View.as_view(), name='register-step2'),
    path('register/step3/', UserRegistrationStep3View.as_view(), name='register-step3'),
    path('register/step4/', UserRegistrationStep4View.as_view(), name='register-step4'),
    path('register/step5/', UserRegistrationStep5View.as_view(), name='register-step5'),
    path('register/step6/', UserRegistrationStep6View.as_view(), name='register-step6'),

    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('password/', include('django.contrib.auth.urls')), #비밀번호 수정
]