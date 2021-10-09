from django.urls import path

from .views import AppListAPIView

urlpatterns = [
    path('', AppListAPIView.as_view())
]
