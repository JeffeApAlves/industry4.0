#!/usr/bin/env python

"""

@file    uamill.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos tipo Raspberry

"""

from uatdevice import uaTDevice
from opcua import uamethod
from uatmill import uaTMill
from uadevice import uaDevice
from config import DEVICE_CONFIG

class uaMill(uaDevice):


    CONFIG      = DEVICE_CONFIG(uaTDevice.MILL)

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