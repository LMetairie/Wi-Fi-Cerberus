
from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('captures/', views.captures_list, name='captures_list'),
    path('<int:num>/', views.getFile),
] 