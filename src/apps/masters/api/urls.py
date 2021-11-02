from django.urls import path

from . import views


urlpatterns = [
    path('', views.MasterListAPIView.as_view(), name='masters'),
    path('register/', views.MasterRegisterAPIView.as_view(), name='register'),
]