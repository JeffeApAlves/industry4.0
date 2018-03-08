#!/usr/bin/env python

"""

@file    uabarcoderreader.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos do tipo BarCodeReader

"""
import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import uamethod
from uatdevice import uaTDevice
from uadevice import uaDevice
from uatbarcodereader import uaTBarCodeReader
from startup.config import DEVICE_CONFIG

class uaBarCodeReader(uaDevice):

    CONFIG      = DEVICE_CONFIG(uaTDevice.BAR_CODE_READER)


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