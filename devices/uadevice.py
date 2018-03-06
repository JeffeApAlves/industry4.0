#!/usr/bin/env python

"""

@file    uadevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os dispositivos 

"""

from opcua import uamethod
from opcua import ua

from uaobject import uaObject
from config import DEVICE_CONFIG
from workerdevice import WorkerDevice
from log import logger

class uaDevice(uaObject):

    # tipos de dispositivos
    DEVICE          = "device" 
    RASPBERRY       = "raspberry"
    ROBOT           = "robot"
    VISION          = "vision"
    COVEYOR         = "coveyor"
    BAR_CODE_READER = "bar-code-reader"
    LATHE           = "lathe"
    MILL            = "mill"

    # proppriedades
    _P_MODEL        = "Model"
    _P_SN           = "SerialNumber"
    _P_HOST         = "Host"
    _P_VERSION      = "Version"

    # metodos
    _M_SHUTDOWN     = "shutdown"
    _M_STARTUP      = "startup"

    CONFIG          = DEVICE_CONFIG(DEVICE)

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
        return self.value

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
    def create_type(server,idx,type=None):

        types   = server.get_node(ua.ObjectIds.BaseObjectType)

        try:
            obj_type = types.get_child(":".join([str(idx), uaDevice.CONFIG.OBJECT_TYPE]))
        except:
            
            obj_type= types.add_object_type(idx, uaDevice.CONFIG.OBJECT_TYPE)

            obj_type.add_property(idx,  uaDevice._P_HOST,    "199.999.999.999").set_writable()
            obj_type.add_property(idx,  uaDevice._P_VERSION, "0.1").set_writable()
            obj_type.add_property(idx,  uaDevice._P_MODEL,   "Model1").set_writable()
            obj_type.add_property(idx,  uaDevice._P_SN,      "123456789").set_writable()

            # adiciona os metodos
            obj_type.add_method(idx,    uaDevice._M_SHUTDOWN,  uaDevice.shutdown)
            obj_type.add_method(idx,    uaDevice._M_STARTUP,   uaDevice.startup)


        if type is not None:

            try:
                child = obj_type .get_child(":".join([str(idx), type ]))
            except:
                child = obj_type.add_object_type(idx, type)

        else:
            child = obj_type
    
        return  child

    @staticmethod
    @uamethod
    def shutdown(parent):
        pass

    @staticmethod
    @uamethod
    def startup(parent):
        pass 