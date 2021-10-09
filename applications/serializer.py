from rest_framework import serializers
from .models import Application


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['name', 'pkg_name', 'icon', 'url', 'store_type', 'version_number']
