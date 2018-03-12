#!/usr/bin/env python

"""

@file    mapclass.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de celulas

"""

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from cells.uacell import uaCell
from cells.uaqc import uaQC
from cells.uamachining import uaMachining
from cells.uastorage import uaStorage
from cells.uaassembly import uaAssembly

from cells.uatcell import uaTCell
from cells.uatqc import uaTQC
from cells.uatmachining import uaTMachining
from cells.uatstorage import uaTStorage
from cells.uatassembly import uaTAssembly

from devices.uadevice import uaDevice
from devices.uaraspberry import uaRaspBerry
from devices.uarobot import uaRobot
from devices.uavision import uaVision
from devices.uacoveyor import uaCoveyor
from devices.uamill import uaMill
from devices.uabarcodereader import uaBarCodeReader
from devices.ualathe import uaLathe

from devices.uatdevice import uaTDevice
from devices.uatraspberry import uaTRaspBerry
from devices.uatrobot import uaTRobot
from devices.uatvision import uaTVision
from devices.uatcoveyor import uaTCoveyor
from devices.uatmill import uaTMill
from devices.uatbarcodereader import uaTBarCodeReader
from devices.uatlathe import uaTLathe

from places.uaplace import uaPlace
from places.uabuffer import uaBuffer
from places.uatrash import uaTrash

from places.uatplace import uaTPlace
from places.uatbuffer import uaTBuffer
from places.uattrash import uaTTrash



logger = logging.getLogger(__name__)


def str_to_class(py_type):
    """
    Retorna a classe respectiva ao tipo
    """

    try:

        type_class = globals()[py_type]

        if type_class is  None:
            logger.error("Classe para o tipo {} não mapeado".format(type))
    
    except:
        type_class = None
        logger.error("Classe para o tipo {} não mapeado".format(type))
        
    return type_class