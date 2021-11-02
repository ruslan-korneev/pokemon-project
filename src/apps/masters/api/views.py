from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import MasterListSerializer, MasterRegisterSerializer


Master = get_user_model()


class MasterRegisterAPIView(CreateAPIView):
    serializer_class = MasterRegisterSerializer
    queryset = Master.objects.all()

class MasterListAPIView(ListAPIView):
    serializer_class = MasterListSerializer
    queryset = Master.objects.all()