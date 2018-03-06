#!/usr/bin/env python

"""

@file    uabarcoderreader.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos do tipo BarCodeReader

"""
from opcua import ua
from opcua import uamethod

from uadevice import uaDevice
from config import DEVICE_CONFIG

class uaBarCodeReader(uaDevice):

    _M_READ_BARCODE     = "read_barcode"


    CONFIG      = DEVICE_CONFIG(uaDevice.BAR_CODE_READER)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaDevice.create_type(server,idx,uaBarCodeReader.CONFIG.OBJECT_TYPE)
    
        # adiciona as variaveis
        #obj_type.add_variable(idx, uaBarCodeReader._V_A,      1.0).set_writable()

        # adiciona os metodos
        obj_type.add_method(idx,   uaBarCodeReader._M_READ_BARCODE,   uaBarCodeReader.read_barcode)

        return  obj_type

    @staticmethod
    @uamethod
    def read_barcode(parent):
        return None