#!/usr/bin/env python

"""

@file    uatvision.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import ua
from devices.uatdevice import uaTDevice

class uaTVision(uaTDevice):

    mCHECK_PART     = "check_part"

    OPC_TYPE        = uaTDevice.VISION


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """
 
        return  uaTDevice.create_type(parent,idx,uaTVision,handle)

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

        obj_type.add_method(idx,   uaTVision.mCHECK_PART,   handle.check_part)

        return obj_type
