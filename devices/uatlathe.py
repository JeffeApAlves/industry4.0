#!/usr/bin/env python

"""

@file    uatlathe.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from opcua import ua
from uadevice import uaTDevice
from log import logger
from config import DEVICE_CONFIG


class uaTLathe(uaTDevice):

    # metodos
    mOPEN       = "open_protection"
    mCLOSE      = "close_protection"
    mMAKE_PART  = "make_part"

    CONFIG      = DEVICE_CONFIG(uaTDevice.LATHE)

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTDevice.create_type(parent,idx,uaTLathe,handle)

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
        
        obj_type.add_method(idx,   uaTLathe.mOPEN,         handle.open_protection)
        obj_type.add_method(idx,   uaTLathe.mCLOSE,        handle.close_protection)
        obj_type.add_method(idx,   uaTLathe.mMAKE_PART,    handle.make_part)

        return obj_type
