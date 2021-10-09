import uuid

import jwt
from django.conf import settings
from django.db import models


class Device(models.Model):
    serial_number = models.CharField(verbose_name="Serial ID", max_length=50, unique=True, null=False)
    device_model = models.CharField(verbose_name="Device Model", max_length=100, null=False)
    imei = models.IntegerField(verbose_name="IMEI", unique=True, null=False)
    mac_address = models.CharField(verbose_name="MAC Address", max_length=32, unique=True, blank=False, null=False)
    android_id = models.IntegerField(verbose_name="Android ID", )
    created_time = models.DateField(verbose_name="Created Time", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Updated Time", auto_now=True)

    @classmethod
    def create_device_instance(cls, validated_data):
        instance, created = cls.objects.get_or_create(serial_number=validated_data['serial_number'],
                                                      imei=validated_data['imei'],
                                                      mac_address=validated_data['mac_address'],
                                                      defaults={'android_id': validated_data['android_id'],
                                                                'device_model': validated_data['device_model'],
                                                                })
        return instance

    class Meta:
        db_table = 'devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'


class RegisterLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    ip_address = models.GenericIPAddressField(verbose_name=" IP Address")
    track_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    created_time = models.DateField(verbose_name="Created Time", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Updated Time", auto_now=True)

    @property
    def get_token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        device_id = self.device.serial_number

        token = jwt.encode({
            'tid': str(self.track_id),
            'did': str(device_id)
        }, settings.SECRET_KEY, settings.ALGORITHM)

        return token
