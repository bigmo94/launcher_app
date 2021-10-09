from rest_framework import serializers


class DeviceRegisterSerializer(serializers.Serializer):
    serial_number = serializers.IntegerField()
    device_model = serializers.CharField()
    imei = serializers.IntegerField()
    mac_address = serializers.CharField()
    android_id = serializers.IntegerField()
