from django.urls import path

from . import views

urlpatterns = [
    path('', views.temperatures_monitoring, name='temp_monitoring'),

    # With sensor details page
    #path('sensor/<str:sensor_id>', views.temperatures_monitoring, name='temp_monitoring'),

]
