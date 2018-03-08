#!/usr/bin/env python

"""

@file    mapclass.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de celulas

"""

from uacell import uaCell
from uaqc import uaQC
from uamachining import uaMachining
from uastorage import uaStorage
from uaassembly import uaAssembly

from uatcell import uaTCell
from uatqc import uaTQC
from uatmachining import uaTMachining
from uatstorage import uaTStorage
from uatassembly import uaTAssembly

from uadevice import uaDevice
from uaraspberry import uaRaspBerry
from uarobot import uaRobot
from uavision import uaVision
from uacoveyor import uaCoveyor
from uamill import uaMill
from uabarcodereader import uaBarCodeReader
from ualathe import uaLathe

from uatdevice import uaTDevice
from uatraspberry import uaTRaspBerry
from uatrobot import uaTRobot
from uatvision import uaTVision
from uatcoveyor import uaTCoveyor
from uatmill import uaTMill
from uatbarcodereader import uaTBarCodeReader
from uatlathe import uaTLathe

from uaplace import uaPlace
from uabuffer import uaBuffer
from uatrash import uaTrash

from uatplace import uaTPlace
from uatbuffer import uaTBuffer
from uattrash import uaTTrash

from config import CONFIG
from log import logger

class MapClass(object):



    @staticmethod
    def get_config(type):
        """
        Retorna o config respectivo ao tipo
        """

        return MapClass.get_class(CONFIG.get_map_class()[type]).CONFIG


    @staticmethod
    def get_class(py_type):
        """
        Retorna a classe respectiva ao tipo
        """

        type_class = globals()[py_type]

        if type_class is  None:
            logger.warn("Classe para o tipo {} não mapeado".format(type))

        return type_class
