from django.urls import path
from .views import UserAgeUpdateView, UserDiseaseUpdateView, UserHeightUpdateView, UserWeightUpdateView
from .views import NoticeListView, NoticeDetailView

urlpatterns = [
    #키워드 변경 
    path('update/age/', UserAgeUpdateView.as_view(), name='update-age'), #age
    path('update/disease/', UserDiseaseUpdateView.as_view(), name='update-disease'), #disease
    path('update/height/', UserHeightUpdateView.as_view(), name='update-height'), #height
    path('update/weight/', UserWeightUpdateView.as_view(), name='update-weight'), #weight

    path('notices/', NoticeListView.as_view(), name='notice-list'), #전체 공지조회
    path('notices/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'), #개별 공지확인
]