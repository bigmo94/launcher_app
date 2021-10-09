import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import ValidationError

from .models import RegisterLog


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request, **kwargs):
        auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header_value:
            token_type, auth = request.META["HTTP_AUTHORIZATION"].split(" ", 1)
            if not auth:
                return None
            if not token_type.lower() == "bearer":
                return None
            payload = jwt.decode(auth, settings.SECRET_KEY, settings.ALGORITHM)
            tid = payload['tid']
            did = payload['did']
            qs = RegisterLog.objects.filter(device__serial_number=did).last()
            if not tid == str(qs.track_id):
                raise ValidationError('Your token is expired')
        pass
