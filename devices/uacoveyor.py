#!/usr/bin/env python

"""

@file    coveyor.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade do dispositivo Coveyor

"""
from opcua import uamethod

from uatdevice import uaTDevice
from uadevice import uaDevice
from uatcoveyor import uaTCoveyor
from config import DEVICE_CONFIG

class uaCoveyor(uaDevice):


    CONFIG          = DEVICE_CONFIG(uaTDevice.COVEYOR)


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo coveyor no server OPC-UA
        """

        if handle is None:
            handle = HandleCoveyor()

        dtype  = uaDevice.create(parent,idx)

        return  uaTCoveyor.create(dtype,idx,handle)


class HandleCoveyor(object):
    
    @uamethod
    def on(self,parent):
        pass

    @uamethod
    def off(self,parent):
        pass