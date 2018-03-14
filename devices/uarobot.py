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
import asyncio

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import uamethod
from client.uaclient import uaClient
from opc.uaobject import uaObject
from devices.uatdevice import uaTDevice
from devices.uadevice import uaDevice,HandlerEvents
from devices.uatrobot import uaTRobot
from devices.uatraspberry import uaTRaspBerry


class uaRobot(uaDevice):

    def __init__(self,idx,name,event_loop):

        self.logger     = logging.getLogger(__name__)

        super().__init__(None,idx,name,event_loop)

        
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
        """
        Retorna um objeto handler criado que irá fazer o processamento dos eventos 
        """

        class_handler = globals()[name]

        return class_handler(self)


    def on_datachange_temperature(self, node, val, data):

        obj = uaClient.get_object("RB3")

        print("|--------------Temperatura----------------------")
        print("| Objeto:{} ".format(obj))
        print("| node   {} value {}".format(node.get_display_name().Text,val))
        print("| Data   {}".format(data))
        print("|-----------------------------------------------")


    def on_datachange_cpu(self, node, val, data):

        rb3 = uaClient.get_object("RB3")

        print("Teste")
 
        rb3.call_method(uaTRaspBerry.mRESET)

        print("|-------------CPU-------------------------------")
        print("| Objeto:{} ".format(rb3))
        print("| node   {} value {}".format(node.get_display_name().Text,val))
        print("| Data   {}".format(data))
        print("|-----------------------------------------------")


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


class HandlerTemperature(HandlerEvents):


    def datachange_notification(self, node, val, data):


        method = getattr(self._device,"on_datachange_temperature")

        HandlerEvents._event_loop.call_soon(method , node , val , data)
        
        self.logger.info("Criado evento(call_soon) Data change notification - Temperature {}".format(data))

    
    def event_notification(self, event):
        self.logger.info("Event - Temperature")


class HandlerCPU(HandlerEvents):


    def datachange_notification(self, node, val, data):
        
        HandlerEvents._event_loop.call_soon(self._device.on_datachange_cpu,node, val, data)
        
        self.logger.info("Criado evento(call_soon) Data change notification - CPU {}".format(data))


    def event_notification(self, event):
        self.logger.info("Event - CPU")
