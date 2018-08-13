#
# Created by Christophe Duchesne for Positive Degree
# 2018/08/08
#

from pdWebMonitoring.monitoring.models import ComputingUnit as CompUnit


# Updates the unit in the database
def update_db_unit(unit_attributes, unit_id):

    unit_to_update = CompUnit.objects.get(unit_id=unit_id)

    # Change unit process
    new_unit_process = unit_attributes.get('processchange')
    unit_to_update.running_process = new_unit_process
    unit_to_update.save()

# Constant to define the unit attribute changes
# unit_process_change = "1"
# unit_mining_process = "1"
# unit_gaming_process = "2"
# unit_webhosting_process = "3"
#
# unit_name_change = "2"
# unit_ip_change = "3"

##################################
# class UnitController:
#
#     def __init__(self, request_params, unit):
#         self.request_params = request_params
#         self.unit = ComputingUnit(unit)
#         self.changes = self.unit.get_changes(request_params)
#
#     def apply_unit_changes(self):
#         if self.changes[0]:
#             self.notify_distant_unit()
#             self.log_changes_in_db()
#
#     def log_changes_in_db(self):
#         # Todo : save the changes made to unit in the DB with datestamp
#         pass
#
#     # Notifies changes for the particular distant unit
#     def notify_distant_unit(self):
#         unit_client = UnitCommunicationClient(self.unit.id)
#         unit_client.send_changes_to_unit(self.changes[1])
#
#
# # Represents a computing unit, created with its DB entity equivalent
# class ComputingUnit:
#
#     def __init__(self, unit_db):
#         self.id = unit_db.unit_id
#         self.name = unit_db.name
#         self.ip_address = unit_db.ip_address
#         self.port_number = int(unit_db.port_number)
#         self.running_process = unit_db.running_process
#
#     # Get the changes requested on the unit with the post request params
#     def get_changes(self, request_params):
#         changes = ""
#         has_changed = False
#
#         # TODO : replace following with call to messaging protocol
#
#         new_process = request_params.get('processchange')
#         if not new_process == self.running_process:
#             has_changed = True
#
#             if new_process == "mining":
#                 changes = changes + unit_process_change + unit_mining_process
#
#             if new_process == "gaming":
#                 changes = changes + unit_process_change + unit_gaming_process
#
#             if new_process == "webhosting":
#                 changes = changes + unit_process_change + unit_webhosting_process
#
#         # Add other parameters verification for unit changes here
#
#         return has_changed, changes
