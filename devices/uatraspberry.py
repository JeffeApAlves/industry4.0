#!/usr/bin/env python

"""

@file    uatraspberry.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import ua

from devices.uadevice import uaTDevice
from config.config import DEVICE_CONFIG


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

