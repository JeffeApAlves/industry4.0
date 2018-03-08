#!/usr/bin/env python

"""

@file    ualathe.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos tipo Raspberry

"""
from opcua import uamethod
from uatdevice import uaTDevice
from uadevice import uaDevice
from uatlathe import uaTLathe
from config import DEVICE_CONFIG

class uaLathe(uaDevice):

    CONFIG      = DEVICE_CONFIG(uaTDevice.LATHE)

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