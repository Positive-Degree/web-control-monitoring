from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Temperatures monitoring here")


def temperatures_monitoring(request):
    return render(request, 'temperatures/temp_monitoring.html')
