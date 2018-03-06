#!/usr/bin/env python

"""

@file    uavision.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""
from opcua import ua
from opcua import uamethod

from uadevice import uaDevice
from config import DEVICE_CONFIG

class uaVision(uaDevice):

    _M_CHECK_PART   = "check_part"

    CONFIG      = DEVICE_CONFIG(uaDevice.VISION)


    @staticmethod
    def create_type(server,idx):

        obj_type = uaDevice.create_type(server,idx,uaVision.CONFIG.OBJECT_TYPE)
    
        # adiciona as variaveis
        #obj_type.add_variable(idx, uaVision._V_A,      1.0).set_writable()

        # adiciona os metodos
        obj_type.add_method(idx,   uaVision._M_CHECK_PART,   uaVision.check_part)

        return  obj_type

    @staticmethod
    @uamethod
    def check_part(parent):
        return None