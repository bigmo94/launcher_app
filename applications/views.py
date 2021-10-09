from rest_framework import generics
from .serializer import AppSerializer
from .models import Application
from devices.authentication_backend import CustomAuthentication


class AppListAPIView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = AppSerializer
    authentication_classes = [CustomAuthentication, ]
