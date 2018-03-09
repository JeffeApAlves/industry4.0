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
from config.config import DEVICE_CONFIG


class uaRobot(uaDevice):

    CONFIG         = DEVICE_CONFIG(uaTDevice.ROBOT)



    def __init__(self,idx,name):

        super().__init__(None,idx,name)
        
        
    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo robot no server OPC-UA
        """

        if handle is None:
            handle = HandleMethods()

        dtype  = uaDevice.create(parent,idx)

        return  uaTRobot.create(dtype,idx,handle)


    def get_SubHandler(self):

        return SubHandler()


class HandleMethods(object):

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


class SubHandler(object):

    def datachange_notification(self, node, val, data):
        print("New data change event", node, val, data)

    def event_notification(self, event):
        print("New event", event)

