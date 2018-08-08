from django.urls import path

from . import views

app_name = "monitoring"
urlpatterns = [
    path('', views.monitoring_dashboard, name='monitoring_dashboard'),
    path('temperatures/', views.temperatures_monitoring, name='temp_monitoring'),
    path('units/', views.units_monitoring, name='unit_monitoring'),
    path('units/<str:unit_id>/', views.unit_detail, name='unit_detail'),
    path('temperatures/<str:sensor_id>/', views.sensor_detail, name='sensor_detail'),


    # With sensor details page
    # path('sensor/<str:sensor_id>', views.temperatures_monitoring, name='temp_monitoring'),

]
