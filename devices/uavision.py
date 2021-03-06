#!/usr/bin/env python

"""

@file    uavision.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade Raspberry

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import uamethod
from devices.uatdevice import uaTDevice
from devices.uatvision import uaTVision
from devices.uadevice import uaDevice

class uaVision(uaDevice):

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo coveyor no server OPC-UA
        """

        if handle is None:
            handle = HandleVision()

        dtype  = uaDevice.create(parent,idx)

        return  uaTVision.create(dtype,idx,handle)


class HandleVision(object):

    @uamethod
    def check_part(self,parent):
        return None