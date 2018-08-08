#
# Created by Christophe Duchesne for Positive Degree
# 2018/08/08
#
# Command pattern reference : https://sourcemaking.com/design_patterns/command/python/1
#

import abc


# The command interface
class Command(metaclass=abc.ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


# Change the current main running process or application of a unit
class ChangeUnitProcess(Command):

    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self):
        self._receiver.change_process()

