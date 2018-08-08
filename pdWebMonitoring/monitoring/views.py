from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import db_ComputingUnit
from .models import Sensor

from pdWebMonitoring.networkControl.unit_control import UnitController


def temperatures_monitoring(request):
    sensor_list = Sensor.objects.all()
    context = {'sensors': sensor_list}
    return render(request, 'temperatures/temps_dashboard.html', context)


def units_monitoring(request):
    unit_list = db_ComputingUnit.objects.all()
    context = {'units': unit_list}
    return render(request, 'computingUnits/units_dashboard.html', context)


def monitoring_dashboard(request):
    return render(request, 'monitoring_dashboard.html')


def sensor_detail(request, sensor_id):
    sensor = get_object_or_404(Sensor, sensor_id=sensor_id)
    context = {'sensor': sensor}
    return render(request, 'temperatures/sensor_detail.html', context)


def unit_detail(request, unit_id):

    db_unit = get_object_or_404(db_ComputingUnit, unit_id=unit_id)

    # A change has been requested for that unit
    if request.method == "POST":
        UnitController(request.POST, db_unit)

    context = {'unit': db_unit}
    return render(request, 'computingUnits/unit_detail.html', context)
