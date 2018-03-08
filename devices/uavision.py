#!/usr/bin/env python

"""

@file    uavision.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""
from uatdevice import uaTDevice
from opcua import uamethod
from uatvision import uaTVision
from uadevice import uaDevice
from config import DEVICE_CONFIG

class uaVision(uaDevice):

    CONFIG      = DEVICE_CONFIG(uaTDevice.VISION)

    @staticmethod
    def create_type(parent,idx,handle=None):
        """
        Cria o tipo coveyor no server OPC-UA
        """

        if handle is None:
            handle = HandleVision()

        dtype  = uaDevice.create_type(parent,idx)

        return  uaTVision.create(dtype,idx,handle)


class HandleVision(object):

    @uamethod
    def check_part(self,parent):
        return None