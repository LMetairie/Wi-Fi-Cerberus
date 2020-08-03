from .models import DetectedDevices
from rest_framework import serializers


# Serialisateur pour l'API
class DetectedDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectedDevices
        fields = ['id', 'date', 'mac_address', 'signal_strength', 'lat', 'lon']