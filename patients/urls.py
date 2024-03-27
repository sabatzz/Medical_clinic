from django.urls import path
from . import views


app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('new/', views.patient_new, name='patient_new'),
    # path('<int:pk>/', views.patient_detail, name='patient_detail'),
    # path('<int:pk>/', views.patient_edit, name='patient_edit'),
    path('<int:patient_id>/edit/', views.edit_patient_and_address, name='edit_patient_and_address'),
    path('<int:pk>/delete/', views.patient_delete, name='patient_delete'),
]
