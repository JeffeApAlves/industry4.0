#!/usr/bin/env python

"""

@file    uarobot.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Robot

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import uamethod

from uatdevice import uaTDevice
from uadevice import uaDevice
from uatrobot import uaTRobot
from startup.config import DEVICE_CONFIG


class uaRobot(uaDevice):

    CONFIG         = DEVICE_CONFIG(uaTDevice.ROBOT)


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo robot no server OPC-UA
        """

        if handle is None:
            handle = HandleRobot()

        dtype  = uaDevice.create(parent,idx)

        return  uaTRobot.create(dtype,idx,handle)


class HandleRobot(object):

    @uamethod
    def move(self,parent):
        pass

    @uamethod
    def execute(self,parent,format,program):
        pass

    @uamethod
    def home(self,parent):
        pass

    @uamethod
    def get_part(self,parent,id):
        pass

    @uamethod
    def put_part(self,parent,id):
        pass