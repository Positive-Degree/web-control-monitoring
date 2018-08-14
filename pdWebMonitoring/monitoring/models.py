from django.db import models
from django.core.validators import MaxValueValidator


class ComputingUnit(models.Model):
    unit_id = models.AutoField(primary_key=True, max_length=30)
    name = models.CharField(default="Unit", max_length=30)
    ip_address = models.GenericIPAddressField(default="0.0.0.0", max_length=30)
    port_number = models.PositiveIntegerField(default=2000, validators=[MaxValueValidator(9999)])
    running_process = models.CharField(default="mining", max_length=30)

    def __str__(self):
        return "%s - %s" % (self.unit_id, self.name)


class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True, max_length=30)
    unit = models.ForeignKey(ComputingUnit, on_delete=models.CASCADE, null=True)
    name = models.CharField(default="Sensor", max_length=30)

    def __str__(self):
        return "%s - %s" % (self.sensor_id, self.name)
