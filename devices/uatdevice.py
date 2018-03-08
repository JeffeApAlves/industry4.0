#!/usr/bin/env python

"""

@file    uatdevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from opcua import ua
from log import logger
from uatype import uaType
from config import DEVICE_CONFIG

class uaTDevice(uaType):

    # tipos de dispositivos no OPC-UA
    DEVICE          = "device" 
    RASPBERRY       = "raspberry"
    ROBOT           = "robot"
    VISION          = "vision"
    COVEYOR         = "coveyor"
    BAR_CODE_READER = "bar-code-reader"
    LATHE           = "lathe"
    MILL            = "mill"

    # proppriedades OPC-UA
    pMODEL          = "Model"
    pSN             = "SerialNumber"
    pHOST           = "Host"
    pVERSION        = "Version"

    # metodos OPC-UA
    mDEINIT         = "deinit"
    mINIT           = "init"

    CONFIG          = DEVICE_CONFIG(DEVICE)

    @staticmethod
    def get_list():
        return  [        
            uaTDevice.RASPBERRY,
            uaTDevice.ROBOT,
            uaTDevice.VISION,
            uaTDevice.COVEYOR,
            uaTDevice.MILL,
            uaTDevice.LATHE,
            uaTDevice.BAR_CODE_READER
        ]

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaType.create_type(parent,idx,uaTDevice,handle)


    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """

        obj_type.add_property(idx,  uaTDevice.pHOST,    "199.999.999.999").set_writable()
        obj_type.add_property(idx,  uaTDevice.pVERSION, "0.1").set_writable()
        obj_type.add_property(idx,  uaTDevice.pMODEL,   "Model1").set_writable()
        obj_type.add_property(idx,  uaTDevice.pSN,      "123456789").set_writable()

        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """

        obj_type.add_method(idx,    uaTDevice.mINIT,   handle.init)
        obj_type.add_method(idx,    uaTDevice.mDEINIT, handle.deinit)

        return obj_type