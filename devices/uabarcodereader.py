#!/usr/bin/env python

"""

@file    uabarcoderreader.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos do tipo BarCodeReader

"""

from opcua import uamethod
from uatdevice import uaTDevice
from uadevice import uaDevice
from uatbarcodereader import uaTBarCodeReader
from config import DEVICE_CONFIG

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