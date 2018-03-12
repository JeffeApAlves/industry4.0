#!/usr/bin/env python

"""

@file    uamill.py
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
from devices.uatmill import uaTMill
from devices.uadevice import uaDevice
from config.config import DEVICE_CONFIG

class uaMill(uaDevice):


    CONFIG      = DEVICE_CONFIG(uaTDevice.MILL)


    def __init__(self,idx,name):

        super().__init__(None,idx,name)
        
        
    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo coveyor no server OPC-UA
        """

        if handle is None:
            handle = HandleMill()

        dtype  = uaDevice.create(parent,idx)

        return  uaTMill.create(dtype,idx,handle)


class HandleMill(object):

    @uamethod
    def open_protection(self,parent):
        pass

    @uamethod
    def close_protection(self,parent):
        pass

    @uamethod
    def make_part(self,parent):
        return None