from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import ComputingUnit
from .models import Sensor


def temperatures_monitoring(request):
    sensor_list = Sensor.objects.all()
    context = {'sensors': sensor_list}
    return render(request, 'temperatures/temps_dashboard.html', context)


def units_monitoring(request):
    unit_list = ComputingUnit.objects.all()
    context = {'units': unit_list}
    return render(request, 'computingUnits/units_dashboard.html', context)


def monitoring_dashboard(request):
    return render(request, 'monitoring_dashboard.html')


def sensor_detail(request, sensor_id):
    sensor = get_object_or_404(Sensor, sensor_id=sensor_id)
    context = {'sensor': sensor}
    return render(request, 'temperatures/sensor_detail.html', context)


def unit_detail(request, unit_id):

    db_unit = get_object_or_404(ComputingUnit, unit_id=unit_id)

    # A client has changed that unit's data
    if request.method == "POST":
        update_unit(request.POST, unit_id)

    # A computing unit requests its unit's data to stay updated
    elif request.method == "GET" and request.META.get("HTTP_UNIT_UPDATE") == "True":
        unit_object = [ComputingUnit.objects.get(unit_id=unit_id)]
        unit_data = serializers.serialize("json", unit_object)
        return HttpResponse(unit_data, content_type='application/json')

    context = {'unit': db_unit}
    return render(request, 'computingUnits/unit_detail.html', context)


# Updates the unit in the database
def update_unit(unit_attributes, unit_id):

    unit_to_update = ComputingUnit.objects.get(unit_id=unit_id)

    # Change unit process
    if unit_attributes.get('processchange') is not None:
        unit_to_update.running_process = unit_attributes.get('processchange')

    # Change unit control mode
    if unit_attributes.get('controlmode') is not None:
            unit_to_update.control_mode = unit_attributes.get('controlmode')

    unit_to_update.save()


def update_sensor_temperature(temperature, sensor_id):
    sensor_to_update = Sensor.objects.get(sensor_id=sensor_id)

    sensor_to_update.temperature = temperature
    sensor_to_update.save()
