from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:Patient_id>/', views.detail, name='detail'),
    path('create_patient/',views.create_patient,name='create_patient'),
]