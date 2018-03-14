#!/usr/bin/env python

"""

@file    uatdevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import ua

from opc.uatype import uaType

class uaTDevice(uaType):

    # tipos de dispositivos no OPC-UA
    DEVICE          = "DeviceType" 
    RASPBERRY       = "RaspBerryType"
    ROBOT           = "RobotType"
    VISION          = "VisionType"
    COVEYOR         = "CoveyorType"
    BAR_CODE_READER = "BarCodeReaderType"
    LATHE           = "LatheType"
    MILL            = "MillType"

    # proppriedades OPC-UA
    pMODEL          = "Model"
    pSN             = "SerialNumber"
    pHOST           = "Host"
    pVERSION        = "Version"

    # metodos OPC-UA
    mDEINIT         = "deinit"
    mINIT           = "init"

    OPC_TYPE        = DEVICE

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
