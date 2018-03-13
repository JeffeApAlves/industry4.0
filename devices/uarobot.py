#!/usr/bin/env python

"""

@file    uarobot.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Robot

"""

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import uamethod
from client.uaclient import uaClient
from opc.uaobject import uaObject
from devices.uatdevice import uaTDevice
from devices.uadevice import uaDevice
from devices.uatrobot import uaTRobot
from devices.uatraspberry import uaTRaspBerry
from config.config import DEVICE_CONFIG


class uaRobot(uaDevice):

    def __init__(self,idx,name):

        self.logger = logging.getLogger(__name__)

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


    def create_handler(self,name):

        class_handler = globals()[name]

        return class_handler()


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


class HandlerTemperature(object):

    def __init__(self):

        self.logger = logging.getLogger(__name__)

    def datachange_notification(self, node, val, data):
        
        print("Temperature {} - New data change event\n".format(val))


        #self.logger.info("Encontrado 3 !!!!!!!!!!! {}".format(uaClient.get_object("Robot2").node))

        #input("Chegou")****************************************************************************************************************************************************

        #rb3 = uaClient.get_object("RB3")
        
        #rb3.call(uaTRaspBerry.mSHUTDOWN)

    
    def event_notification(self, event):
        print("Temperature - New event\n")


class HandlerCPU(object):

    def datachange_notification(self, node, val, data):
        print("CPU {} - New data change event\n".format(val))

    def event_notification(self, event):
        print("CPU-New event\n")