#!/usr/bin/env python

"""

@file    uatrobot.py
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

class uaTRobot(uaTDevice):

    # metodos OPC
    mMOVE           = "move"
    mEXECUTE        = "execute"
    mHOME           = "home"
    mGET_PART       = "get_part"
    mPUT_PART       = "put_part"
           
    OPC_TYPE        = uaTDevice.ROBOT

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTDevice.create_type(parent,idx,uaTRobot,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Adiciona as propriedades
        """

        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Adiciona os metodos
        """

        obj_type.add_method(idx,   uaTRobot.mHOME,    handle.home)
        obj_type.add_method(idx,   uaTRobot.mMOVE,    handle.move,    [ua.VariantType.Float,ua.VariantType.Float,ua.VariantType.Float])
        obj_type.add_method(idx,   uaTRobot.mEXECUTE, handle.execute, [ua.VariantType.String,ua.VariantType.String])
        obj_type.add_method(idx,   uaTRobot.mGET_PART,handle.get_part,[ua.VariantType.UInt16])
        obj_type.add_method(idx,   uaTRobot.mPUT_PART,handle.put_part,[ua.VariantType.UInt16])
        
        return obj_type
