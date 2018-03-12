#!/usr/bin/env python

"""

@file    uabarcoderreader.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos do tipo BarCodeReader

"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import uamethod
from devices.uatdevice import uaTDevice
from devices. uadevice import uaDevice
from devices.uatbarcodereader import uaTBarCodeReader
from config.config import DEVICE_CONFIG

class uaBarCodeReader(uaDevice):

    CONFIG      = DEVICE_CONFIG(uaTDevice.BAR_CODE_READER)


    def __init__(self,idx,name):

        super().__init__(None,idx,name)
        

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo device no server OPC-UA
        """

        if handle is None:
            handle = HandleBarCodeReader()

        dtype  = uaDevice.create(parent,idx)

        return  uaTBarCodeReader.create(dtype,idx,handle)


class HandleBarCodeReader(object):


    @uamethod
    def read_barcode(self,parent):
        pass