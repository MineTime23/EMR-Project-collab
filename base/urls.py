from django.urls import path
from . import views
from patient_info_API.views import PatientListAPIView

app_name = 'base'

urlpatterns = [
    path('',PatientListAPIView.as_view(),name='index'),
    path('<int:Patient_id>/', views.detail, name='detail'),
    path('create_patient/',views.create_patient,name='create_patient'),
]