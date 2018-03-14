#!/usr/bin/env python

"""

@file    uaraspberry.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""

import os
import sys
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))



from opcua import uamethod

from opc.uaobject import uaObject
from config.config import DEVICE_CONFIG
from raspberry.tlmsys import TlmSyS
from misc.net import get_ip_address
from devices.uatdevice import uaTDevice
from devices.uatraspberry import uaTRaspBerry
from devices.uadevice import uaDevice

# telemetria raspberry
tlmsys  = TlmSyS()


class uaRaspBerry(uaDevice):

    def __init__(self,idx,name,event_loop):

        super().__init__(None,idx,name,event_loop)

        self.logger = logging.getLogger(__name__)
    
        self._temperature   = uaObject(self.node,idx,uaTRaspBerry.pTEMPERATURE)
        self._memory        = uaObject(self.node,idx,uaTRaspBerry.pMEMORY)
        self._harddisk      = uaObject(self.node,idx,uaTRaspBerry.pHARDDISK)
        self._cpu           = uaObject(self.node,idx,uaTRaspBerry.pCPU)


    @property
    def temperature(self):
        return self._temperature.value

    @temperature.setter
    def temperature(self, value):
        self._temperature.value = value

    @property
    def cpu(self):
        return self._cpu.value

    @cpu.setter
    def cpu(self, value):
        self._cpu.value = value

    @property
    def memory(self):
        return self._memory.value

    @memory.setter
    def memory(self, value):
        self._memory.value = value

    @property
    def harddisk(self):
        return self._harddisk.value

    @harddisk.setter
    def harddisk(self, value):
        self._harddisk.value = value

 
    async def update(self):        
        """
        Execuatado em loop infinito da thread
        """
        
        self.host =  get_ip_address("wlan0")

        while True:
            memory              = tlmsys.memory
            temperature         = tlmsys.temperature
            hd                  = tlmsys.harddisk[0]
            cpu                 = tlmsys.cpu

            self.temperature    = temperature
            self.memory         = memory
            self.harddisk       = hd
            self.cpu            = cpu

            self.logger.info("tlm: memory:{} temperature:{} hd:{} cpu:{}".format(memory,temperature,hd,cpu))


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo raspberry no server OPC-UA
        """

        if handle is None:
            handle = HandleRaspBerry()

        dtype  = uaDevice.create(parent,idx)

        return  uaTRaspBerry.create(dtype,idx,handle)

    def get_SubHandler(self):

        return SubHandler()


class HandleRaspBerry(object):


    @uamethod
    def shutdown(self,parent):
        print("RaspBerry desligando...")

    @uamethod
    def reset(self,parent):
        print("RaspBerry reset")


class SubHandler(object):

    def datachange_notification(self, node, val, data):
        print("New data change event", node, val, data)

    def event_notification(self, event):
        print("New event", event)

