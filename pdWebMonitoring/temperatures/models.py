from django.db import models


class Temperature(models.Model):
    temperature_float = models.FloatField(default=0.0)
    measure_datetime = models.DateTimeField('time of the measure')

    # Helpful and readable representation of the object
    def __str__(self):
        return str(self.temperature_float)

