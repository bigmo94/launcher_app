from rest_framework import generics
from rest_framework.response import Response

from .serializer import DeviceRegisterSerializer
from .models import Device, RegisterLog


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = DeviceRegisterSerializer
    queryset = Device.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        device = Device.create_device_instance(serializer.validated_data)

        instance = RegisterLog.objects.create(device=device, ip_address=get_client_ip(self.request))
        token = instance.get_token
        return Response({'token': token})
