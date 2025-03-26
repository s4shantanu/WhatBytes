from django.urls import path
from .views import *

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

    path('patients/', PatientListCreateView.as_view(), name='patients-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    path('doctors/', DoctorListCreateView.as_view(), name='doctors-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    path('mappings/', PatientDoctorMappingView.as_view(), name='mapping-list'),
]
