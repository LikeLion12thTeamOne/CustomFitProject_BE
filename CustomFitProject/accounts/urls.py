from django.urls import path, include
# from .views import (
#     UserRegistrationView, UserAgeUpdateView, UserGenderUpdateView, 
#     UserDiseaseUpdateView, UserHeightUpdateView, UserWeightUpdateView
# )
from .views import (
    UserRegistrationStep1View, UserRegistrationStep2View, UserRegistrationStep3View, 
    UserRegistrationStep4View, UserRegistrationStep5View, UserRegistrationStep6View
)

urlpatterns = [
    # path('register/', UserRegistrationView.as_view(), name='register'),
    # path('register/age/', UserAgeUpdateView.as_view(), name='register-age'),
    # path('register/gender/', UserGenderUpdateView.as_view(), name='register-gender'),
    # path('register/disease/', UserDiseaseUpdateView.as_view(), name='register-disease'),
    # path('register/height/', UserHeightUpdateView.as_view(), name='register-height'),
    # path('register/weight/', UserWeightUpdateView.as_view(), name='register-weight'),
    
    path('register/step1/', UserRegistrationStep1View.as_view(), name='register-step1'),
    path('register/step2/', UserRegistrationStep2View.as_view(), name='register-step2'),
    path('register/step3/', UserRegistrationStep3View.as_view(), name='register-step3'),
    path('register/step4/', UserRegistrationStep4View.as_view(), name='register-step4'),
    path('register/step5/', UserRegistrationStep5View.as_view(), name='register-step5'),
    path('register/step6/', UserRegistrationStep6View.as_view(), name='register-step6'),

    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
]