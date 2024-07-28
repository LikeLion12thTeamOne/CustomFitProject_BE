from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from .serializers import UserAgeSerializer, UserDiseaseSerializer, UserHeightSerializer, UserWeightSerializer
from .models import Notice
from .serializers import NoticeListSerializer, NoticeDetailSerializer

#키워드 업데이트
class UserAgeUpdateView(generics.UpdateAPIView):
    serializer_class = UserAgeSerializer
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

#공지사항   
class NoticeListView(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeListSerializer

class NoticeDetailView(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeDetailSerializer
