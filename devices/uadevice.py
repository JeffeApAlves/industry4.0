#!/usr/bin/env python

"""

@file    uadevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe generalistas dos dispositivos 

"""

import os,sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))

from opcua import uamethod

from opc.uaobject import uaObject
from config.config import DEVICE_CONFIG
from workerdevice import WorkerDevice
from uatdevice import uaTDevice

class uaDevice(uaObject):

    CONFIG  = DEVICE_CONFIG(uaTDevice.DEVICE)

    def __init__(self,parent,idx,name ):

        super().__init__(parent,idx,name)

        self.logger = logging.getLogger(__name__)


        self._host      = uaObject(self.node,idx,uaTDevice.pHOST)
        self._version   = uaObject(self.node,idx,uaTDevice.pVERSION)
        self._model     = uaObject(self.node,idx,uaTDevice.pMODEL)
        self._sn        = uaObject(self.node,idx,uaTDevice.pSN)

        # cria o worker para o dispositivo
        WorkerDevice(self)

    @property
    def model(self):
        return self._model.value

    @property
    def serial_number(self):
        return self._sn.value

    @property
    def host(self):
        return self._host.value

    @host.setter
    def host(self, value):
        self._host.value = value

    @property
    def version(self):
        return self._version.value

    @version.setter
    def version(self, value):
        self._version.value = value

    def start_task(self):
        self.logger.warn("Worker não implementado")

    def loop_task(self):
        pass

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo device no server OPC-UA
        """

        if handle is None:
            handle = HandleDevice()

        return  uaTDevice.create(parent,idx,handle)


class HandleDevice(object):
    """
    Handle dos metodos do objeto OPC-UA
    """

    @uamethod
    def init(self,parent):
        print("init")

    @uamethod
    def deinit(self,parent):
        print("deinit")
