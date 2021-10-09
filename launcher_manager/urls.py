from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('device/', include('devices.urls')),
    path('apps/', include('applications.urls')),
]
