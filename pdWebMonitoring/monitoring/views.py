from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Temperatures monitoring here")


def temperatures_monitoring(request):
    return render(request, 'temperatures/temps_dashboard.html')


def units_monitoring(request):
    return render(request, 'computingUnits/units_dashboard.html')


def monitoring_dashboard(request):
    return render(request, 'monitoring_dashboard.html')
