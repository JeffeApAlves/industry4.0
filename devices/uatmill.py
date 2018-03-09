#!/usr/bin/env python

"""

@file    uatmill.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""


import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from uadevice import uaTDevice
from config.config import DEVICE_CONFIG

class uaTMill(uaTDevice):

    # metodos
    mOPEN           = "open_protection"
    mCLOSE          = "close_protection"
    mMAKE_PART      = "make_part"

    CONFIG          = DEVICE_CONFIG(uaTDevice.MILL)

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTDevice.create_type(parent,idx,uaTMill,handle)

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
        
        obj_type.add_method(idx,   uaTMill.mOPEN,         handle.open_protection)
        obj_type.add_method(idx,   uaTMill.mCLOSE,        handle.close_protection)
        obj_type.add_method(idx,   uaTMill.mMAKE_PART,    handle.make_part)

        return obj_type
