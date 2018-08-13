from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import ComputingUnit
from .models import Sensor

import pdWebMonitoring.networkControl.unit_control as unit_control


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

        unit_control.update_db_unit(request.POST, unit_id)

        # controller = UnitController(request.POST, db_unit)
        # controller.apply_unit_changes()

    # A computing unit requests its unit's data to stay updated
    elif request.method == "GET" and request.META.get("HTTP_UNIT_UPDATE") == "True":
        unit_object = [ComputingUnit.objects.get(unit_id=unit_id)]
        unit_data = serializers.serialize("json", unit_object)
        return HttpResponse(unit_data, content_type='application/json')

    context = {'unit': db_unit}
    return render(request, 'computingUnits/unit_detail.html', context)
