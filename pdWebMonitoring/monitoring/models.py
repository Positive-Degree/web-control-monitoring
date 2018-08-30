from django.db import models
from django.core.validators import MaxValueValidator


class ComputingUnit(models.Model):

    CONTROL_MODES = (
        ('autonomous', 'Autonomous'),
        ('manual', 'Manual')
    )

    unit_id = models.AutoField(primary_key=True, max_length=30)
    name = models.CharField(default="Unit", max_length=30)
    ip_address = models.GenericIPAddressField(default="0.0.0.0", max_length=30)
    port_number = models.PositiveIntegerField(default=2000, validators=[MaxValueValidator(99999)])
    running_process = models.CharField(default="mining", max_length=30)
    ping_frequency = models.PositiveIntegerField(default=60, validators=[MaxValueValidator(1800)])
    control_mode = models.CharField(default="autonomous", choices=CONTROL_MODES, max_length=10)

    def __str__(self):
        return "%s - %s" % (self.unit_id, self.name)


class Sensor(models.Model):
    sensor_id = models.CharField(primary_key=True, max_length=20)
    unit = models.ForeignKey(ComputingUnit, on_delete=models.CASCADE, null=True)
    name = models.CharField(default="Sensor", max_length=30)
    temperature = models.FloatField(default=0.0)

    def __str__(self):
        return "%s - %s" % (self.sensor_id, self.name)
