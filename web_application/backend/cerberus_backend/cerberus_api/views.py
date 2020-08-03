from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import DetectedDevices
from .serializers import DetectedDevicesSerializer

# Create your views here.
# TODO Check error if no items in database.
# TODO Check error if items doesn't exist.
class DetectedDeviceList(generics.ListCreateAPIView):
    queryset = DetectedDevices.objects.all()
    serializer_class = DetectedDevicesSerializer

class DetectedDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetectedDevices.objects.all()
    serializer_class = DetectedDevicesSerializer