#!/usr/bin/env python

"""

@file    uarobot.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Robot

"""

from opcua import ua
from opcua import uamethod

from uadevice import uaDevice
from config import DEVICE_CONFIG


class uaRobot(uaDevice):

    _M_MOVE        = "move"
    _M_EXECUTE     = "execute"
    _M_HOME        = "home"
    _M_GET_PART    = "get_part"
    _M_PUT_PART    = "put_part"

    CONFIG         = DEVICE_CONFIG(uaDevice.ROBOT)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaDevice.create_type(server,idx,uaRobot.CONFIG.OBJECT_TYPE)

        # adiciona os metodos
        obj_type.add_method(idx,   uaRobot._M_HOME,    uaRobot.home)
        obj_type.add_method(idx,   uaRobot._M_MOVE,    uaRobot.move,    [ua.VariantType.Float,ua.VariantType.Float,ua.VariantType.Float])
        obj_type.add_method(idx,   uaRobot._M_EXECUTE, uaRobot.execute, [ua.VariantType.String,ua.VariantType.String])
        obj_type.add_method(idx,   uaRobot._M_GET_PART,uaRobot.get_part,[ua.VariantType.UInt16])
        obj_type.add_method(idx,   uaRobot._M_PUT_PART,uaRobot.put_part,[ua.VariantType.UInt16])

        return  obj_type

    @staticmethod
    @uamethod
    def move(parent):
        pass

    @staticmethod
    @uamethod
    def execute(parent,format,program):
        pass

    @staticmethod
    @uamethod
    def home(parent):
        pass

    @staticmethod
    @uamethod
    def get_part(parent,id):
        pass

    @staticmethod
    @uamethod
    def put_part(parent,id):
        pass