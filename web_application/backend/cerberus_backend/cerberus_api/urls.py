from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('devices/', views.DetectedDeviceList.as_view()),
    path('devices/<int:pk>/', views.DetectedDeviceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)