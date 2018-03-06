#!/usr/bin/env python

"""

@file    uaraspberry.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""

from opcua import uamethod
from uadevice import uaDevice
from opcua import ua
from uaobject import uaObject
from config import DEVICE_CONFIG
from tlmsys import TlmSyS
from net import get_ip_address
from log import logger

# telemetria raspberry
tlmsys  = TlmSyS()


class uaRaspBerry(uaDevice):

    # propriedades
    _P_TEMPERATURE    = "Temperature"
    _P_CPU            = "CPU"
    _P_MEMORY         = "Memory"
    _P_HARDDISK       = "HardDisk"


    CONFIG              = DEVICE_CONFIG(uaDevice.RASPBERRY)

    def __init__(self,idx,name):

        super().__init__(None,idx,name)
 
        self._temperature   = uaObject(self.node,idx,uaRaspBerry._P_TEMPERATURE)
        self._memory        = uaObject(self.node,idx,uaRaspBerry._P_MEMORY)
        self._harddisk      = uaObject(self.node,idx,uaRaspBerry._P_HARDDISK)
        self._cpu           = uaObject(self.node,idx,uaRaspBerry._P_CPU)


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
    def create_type(server,idx):
        """
        Cria o tipo Raspberry
        """
        
        obj_type = uaDevice.create_type(server,idx,uaRaspBerry.CONFIG.OBJECT_TYPE)
        
        # adiciona as variaveis
        obj_type.add_property(idx, uaRaspBerry._P_HARDDISK,      1.0).set_writable()
        obj_type.add_property(idx, uaRaspBerry._P_CPU,           1.0).set_writable()
        obj_type.add_property(idx, uaRaspBerry._P_MEMORY,        1.0).set_writable()
        obj_type.add_property(idx, uaRaspBerry._P_TEMPERATURE,   1.0).set_writable()

        return  obj_type
