from django.urls import path

from . import views

urlpatterns = [
    path('', views.monitoring_dashboard, name='monitoring_dashboard'),
    path('temperatures/', views.temperatures_monitoring, name='temp_monitoring'),
    path('units/', views.units_monitoring, name='unit_monitoring'),


    # With sensor details page
    #path('sensor/<str:sensor_id>', views.temperatures_monitoring, name='temp_monitoring'),

]
