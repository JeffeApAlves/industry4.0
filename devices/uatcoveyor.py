#!/usr/bin/env python

"""

@file    uacoveyortype.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from opcua import ua
from uadevice import uaTDevice
from log import logger
from config import DEVICE_CONFIG


class uaTCoveyor(uaTDevice):

    # metodos
    mON         = "on"
    mOFF        = "off"

    CONFIG      = DEVICE_CONFIG(uaTDevice.COVEYOR)


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTDevice.create_type(parent,idx,uaTCoveyor,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """
        
        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """

        obj_type.add_method(idx,   uaTCoveyor.mON,     handle.on)
        obj_type.add_method(idx,   uaTCoveyor.mOFF,    handle.off)

        return obj_type
