#!/usr/bin/env python

"""

@file    coveyor.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade do dispositivo Coveyor

"""
from opcua import ua
from opcua import uamethod

from uadevice import uaDevice
from config import DEVICE_CONFIG

class uaCoveyor(uaDevice):

    # metodos
    _M_ON       = "on"
    _M_OFF      = "off"

    CONFIG          = DEVICE_CONFIG(uaDevice.COVEYOR)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaDevice.create_type(server,idx,uaCoveyor.CONFIG.OBJECT_TYPE)
 
        # adiciona os metodos
        obj_type.add_method(idx,   uaCoveyor._M_ON,     uaCoveyor.on)
        obj_type.add_method(idx,   uaCoveyor._M_OFF,    uaCoveyor.off)

        return  obj_type

    @staticmethod
    @uamethod
    def on(parent):
        pass

    @staticmethod
    @uamethod
    def off(parent):
        pass