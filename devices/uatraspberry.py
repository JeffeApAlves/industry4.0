#!/usr/bin/env python

"""

@file    uatraspberry.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import ua

from uadevice import uaTDevice
from startup.config import DEVICE_CONFIG
from misc.log import logger


class uaTRaspBerry(uaTDevice):


    # propriedades
    pTEMPERATURE    = "Temperature"
    pCPU            = "CPU"
    pMEMORY         = "Memory"
    pHARDDISK       = "HardDisk"

    #metodos
    mSHUTDOWN       = "shutdown"
    mRESET          = "reset"

    CONFIG          = DEVICE_CONFIG(uaTDevice.RASPBERRY)


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTDevice.create_type(parent,idx,uaTRaspBerry,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Adiciona as propriedades
        """

        obj_type.add_property(idx, uaTRaspBerry.pHARDDISK,      1.0).set_writable()
        obj_type.add_property(idx, uaTRaspBerry.pCPU,           1.0).set_writable()
        obj_type.add_property(idx, uaTRaspBerry.pMEMORY,        1.0).set_writable()
        obj_type.add_property(idx, uaTRaspBerry.pTEMPERATURE,   1.0).set_writable()

        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Adiciona os metodos
        """

        obj_type.add_method(idx,   uaTRaspBerry.mSHUTDOWN,      handle.shutdown)
        obj_type.add_method(idx,   uaTRaspBerry.mRESET,         handle.shutdown)
    
        return obj_type



    @staticmethod
    def create_event(temperature,handle):
        pass

#        client  = uaClient.get_client()
#        root    = uaClient.get_root_node()
#
#        event   = root.get_child(["0:Types", "0:EventTypes", "0:BaseEventType", "2:MyFirstEvent"])
#
#        sub                         = client.create_subscription(100, SubHandlerTemperature())
#        self._handle_temperatura    = sub.subscribe_events(temperature.node, event)


