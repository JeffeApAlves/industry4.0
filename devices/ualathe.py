#!/usr/bin/env python

"""

@file    ualathe.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos tipo Raspberry

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import uamethod
from devices.uatdevice import uaTDevice
from devices.uadevice import uaDevice
from devices.uatlathe import uaTLathe
from config.config import DEVICE_CONFIG

class uaLathe(uaDevice):

    CONFIG      = DEVICE_CONFIG(uaTDevice.LATHE)


    def __init__(self,idx,name):

        super().__init__(None,idx,name)
        
        
    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo coveyor no server OPC-UA
        """

        if handle is None:
            handle = HandleLathe()

        dtype  = uaDevice.create(parent,idx)

        return  uaTLathe.create(dtype,idx,handle)


class HandleLathe(object):

    @uamethod
    def open_protection(self,parent):
        pass

    @uamethod
    def close_protection(self,parent):
        pass

    @uamethod
    def make_part(self,parent):
        return None