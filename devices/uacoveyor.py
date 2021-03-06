#!/usr/bin/env python

"""

@file    coveyor.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade do dispositivo Coveyor

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import uamethod

from devices.uatdevice import uaTDevice
from devices.uadevice import uaDevice
from devices.uatcoveyor import uaTCoveyor


class uaCoveyor(uaDevice):


    def __init__(self,idx,name,event_loop):

        super().__init__(None,idx,name,event_loop)
        
        
    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo coveyor no server OPC-UA
        """

        if handle is None:
            handle = HandleCoveyor()

        dtype  = uaDevice.create(parent,idx)

        return  uaTCoveyor.create(dtype,idx,handle)


class HandleCoveyor(object):
    
    @uamethod
    def on(self,parent):
        pass

    @uamethod
    def off(self,parent):
        pass