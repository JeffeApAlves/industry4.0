#!/usr/bin/env python

"""

@file    uabarcodereadertype.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from devices.uatdevice import uaTDevice
from config.config import DEVICE_CONFIG


class uaTBarCodeReader(uaTDevice):

    # metodos OPC-UA
    mREAD_BARCODE   = "read_barcode"

    OPC_TYPE        = uaTDevice.BAR_CODE_READER


    def __init__(self,idx,name,event_loop):

        super().__init__(None,idx,name,event_loop)
        
        
    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTDevice.create_type(parent,idx,uaTBarCodeReader,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """
        
        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """

        obj_type.add_method(idx,   uaTBarCodeReader.mREAD_BARCODE,   handle.read_barcode)

        return obj_type
