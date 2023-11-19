from django.urls import path
from .views import *

urlpatterns = [
    path('patients/',PatientListAPIView.as_view(),name='patient_list'),
    path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient-detail'),
]