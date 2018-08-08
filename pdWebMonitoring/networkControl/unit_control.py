#
# Created by Christophe Duchesne for Positive Degree
# 2018/08/08
#

from django.http import HttpRequest
from pdWebMonitoring.monitoring.models import db_ComputingUnit
from pdWebMonitoring.networkControl import commands


class UnitController:

    def __init__(self, request_params, db_unit):
        self.actual_db_unit = ComputingUnit(db_unit)
        self.request_params = request_params
        self.create_command()

    def create_command(self):
        pass


# Represents a computing unit, created with its DB entity equivalent
class ComputingUnit:

    def __init__(self, unit_db):
        self.id = unit_db.unit_id
        self.name = unit_db.name

    def has_changed(self):
        different = False
        return different

    def notify_network_entity(self):
        if self.has_changed():
            # TODO : envoyer update a l'unité via network comm
            pass
