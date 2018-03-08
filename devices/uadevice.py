#!/usr/bin/env python

"""

@file    uadevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe generalistas dos dispositivos 

"""

from opcua import uamethod
from uaobject import uaObject
from config import DEVICE_CONFIG
from workerdevice import WorkerDevice
from uatdevice import uaTDevice
from log import logger

class uaDevice(uaObject):

    CONFIG  = DEVICE_CONFIG(uaTDevice.DEVICE)

    def __init__(self,parent,idx,name ):

        super().__init__(parent,idx,name)

        self._host      = uaObject(self.node,idx,uaDevice._P_HOST)
        self._version   = uaObject(self.node,idx,uaDevice._P_VERSION)
        self._model     = uaObject(self.node,idx,uaDevice._P_MODEL)
        self._sn        = uaObject(self.node,idx,uaDevice._P_SN)

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
        return self._temperature.value

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
        logger.warn("Worker não implementado")

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
