#!/usr/bin/env python

"""

@file    uadevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe generalistas dos dispositivos 

"""

import os
import sys
import asyncio
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import uamethod

from opc.uaobject import uaObject
from devices.uatdevice import uaTDevice
from client.uaclient import uaClient

class uaDevice(uaObject):

    _event_loop = asyncio.get_event_loop()


    def __init__(self,parent,idx,name,event_loop ):

        # default node de objetos
        if parent is None:
            parent = uaClient.get_objects_node()

        super().__init__(parent,idx,name)

        self.logger             = logging.getLogger(__name__)
        
        if event_loop is not None:
            uaDevice._event_loop    = event_loop

        self._host              = uaObject(self.node,idx,uaTDevice.pHOST)
        self._version           = uaObject(self.node,idx,uaTDevice.pVERSION)
        self._model             = uaObject(self.node,idx,uaTDevice.pMODEL)
        self._sn                = uaObject(self.node,idx,uaTDevice.pSN)
        self.__task             = self.create_periodic_update()

    @property
    def event_loop(self):
        return uaDevice._event_loop

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


    async def update(self):

        while True:
            
            await asyncio.sleep(10,loop=uaDevice._event_loop)
            
            self.logger.warning("Worker não implementado")


    def create_periodic_update(self):

        try:
            task = asyncio.ensure_future(self.update(),loop=uaDevice._event_loop)

            self.logger.info("Task-update do dispositivo criado com sucesso")

        except:
            self.logger.error("Erro na criação do Task-update do dispositivo")

        return task


    def stop(self):
        self.__task.cancel()

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo device no server OPC-UA
        """

        if handle is None:
            handle = HandleDevice()

        return  uaTDevice.create(parent,idx,handle)


    @staticmethod
    def run_forever():

        try:
            uaDevice._event_loop.run_forever()
        except (asyncio.CancelledError , KeyboardInterrupt ):
            pass
        finally:
            uaDevice._event_loop.close()



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


class HandlerEvents(object):
    """
    Class generalista de handler events
    """

    _event_loop =  None


    def __init__(self,device):

        HandlerEvents._event_loop   = device.event_loop
        self._device                = device
        self.logger                 = logging.getLogger(__name__)


    def datachange_notification(self, node, val, data):
        self.logger.warn("Data change notification não implementado")

    def event_notification(self, event):
        self.logger.warn("Event não implementado")

