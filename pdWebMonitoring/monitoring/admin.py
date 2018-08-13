from django.contrib import admin

from .models import Sensor
from .models import ComputingUnit

admin.site.register(Sensor)
admin.site.register(ComputingUnit)
