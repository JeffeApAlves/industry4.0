#!/usr/bin/env python

"""

@file    ualathe.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade para dispostivos tipo Raspberry

"""
from opcua import ua
from opcua import uamethod

from uadevice import uaDevice
from config import DEVICE_CONFIG

class uaLathe(uaDevice):

    _M_OPEN     = "open_protection"
    _M_CLOSE    = "close_protection"
    _M_MAKE_PART= "make_part"

    CONFIG      = DEVICE_CONFIG(uaDevice.LATHE)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaDevice.create_type(server,idx,uaLathe.CONFIG.OBJECT_TYPE)
 
        # adiciona as variaveis
        #obj_type.add_variable(idx, uaLathe._V_A,      1.0).set_writable()

        # adiciona os metodos
        obj_type.add_method(idx,   uaLathe._M_OPEN,         uaLathe.open_protectio)
        obj_type.add_method(idx,   uaLathe._M_CLOSE,        uaLathe.close_protectio)
        obj_type.add_method(idx,   uaLathe._M_MAKE_PART,    uaLathe.make_part)

        return  obj_type

    @staticmethod
    @uamethod
    def open_protectio(parent):
        pass

    @staticmethod
    @uamethod
    def close_protectio(parent):
        pass

    @staticmethod
    @uamethod
    def make_part(parent):
        return None