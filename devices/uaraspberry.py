#!/usr/bin/env python

"""

@file    uaraspberry.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""

from opcua import uamethod

from uatdevice import uaTDevice
from uatraspberry import uaTRaspBerry
from uadevice import uaDevice
from uaobject import uaObject
from config import DEVICE_CONFIG
from tlmsys import TlmSyS
from net import get_ip_address
from log import logger

# telemetria raspberry
tlmsys  = TlmSyS()


class uaRaspBerry(uaDevice):


    CONFIG              = DEVICE_CONFIG(uaTDevice.RASPBERRY)

    def __init__(self,idx,name):

        super().__init__(None,idx,name)
 
        self._temperature   = uaObject(self.node,idx,uaTRaspBerry.pTEMPERATURE)
        self._memory        = uaObject(self.node,idx,uaTRaspBerry.pMEMORY)
        self._harddisk      = uaObject(self.node,idx,uaTRaspBerry.pHARDDISK)
        self._cpu           = uaObject(self.node,idx,uaTRaspBerry.pCPU)
        self._handle_temperatura    = None

        self.create_event(self._temperature)
 
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

    def start_task(self):
        """
        Executado na inicialização da thread
        """

        self.host =  get_ip_address("wlan0")


    def loop_task(self):        
        """
        Execuatado em loop infinito da thread
        """
        
        memory              = tlmsys.memory
        temperature         = tlmsys.temperature
        hd                  = tlmsys.harddisk[0]
        cpu                 = tlmsys.cpu

        self.temperature    = temperature
        self.memory         = memory
        self.harddisk       = hd
        self.cpu            = cpu

        logger.info("tlm: memory:{} temperature:{} hd:{} cpu:{}".format(memory,temperature,hd,cpu))


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo raspberry no server OPC-UA
        """

        if handle is None:
            handle = HandleRaspBerry()

        dtype  = uaDevice.create(parent,idx)

        return  uaTRaspBerry.create(dtype,idx,handle)


class HandleRaspBerry(object):


    @uamethod
    def shutdown(self,parent):
        pass

    @uamethod
    def reset(self,parent):
        pass

class SubHandlerTemperature(object):

    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another
    thread if you need to do such a thing
    """

    def data_change (self,event):
        print("Alteração no dado da temperatura")

    def event_notification(self, event):
        print("New event recived: ", event)