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
from devices.uadevice import uaDevice
from devices.uatrobot import uaTRobot
from devices.uatraspberry import uaTRaspBerry
from config.config import DEVICE_CONFIG


class uaRobot(uaDevice):

    def __init__(self,idx,name,event_loop):

        self.logger = logging.getLogger(__name__)

        self._task_temp = None

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


    def temperature_notification(self, node, val, data):

        future = asyncio.Future(loop= self._event_loop)

        self._task_temp = asyncio.ensure_future(self.hello_world(future,node,val,data),loop = self._event_loop)

        self._task_temp.add_done_callback(self.got_result)


    @asyncio.coroutine
    def hello_world(self,future,node,val,data):


        print("Hello World!")
  
        # uaClient.call_method("RB3")
        # rb3.call(uaTRaspBerry.mSHUTDOWN)

        future.set_result((node,val,data))

        return future


    def got_result(self,future):

        print(future.result())
        self._task_temp.stop()



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


    def __init__(self,device):

        self._device    = device
        self.logger     = logging.getLogger(__name__)


    def datachange_notification(self, node, val, data):
        
        print("Temperature {} - New data change event\n".format(val))

        self._device.temperature_notification(node,val,data)

    
    def event_notification(self, event):
        print("Temperature - New event\n")


class HandlerCPU(object):

    def __init__(self,device):

        self._device    = device
        self.logger     = logging.getLogger(__name__)

    def datachange_notification(self, node, val, data):
        print("CPU {} - New data change event\n".format(val))


    def event_notification(self, event):
        print("CPU-New event\n")


