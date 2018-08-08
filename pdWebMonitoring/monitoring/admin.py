from django.contrib import admin

from .models import Sensor
from .models import db_ComputingUnit

admin.site.register(Sensor)
admin.site.register(db_ComputingUnit)
