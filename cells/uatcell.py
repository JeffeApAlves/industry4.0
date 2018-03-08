#!/usr/bin/env python

"""

@file    uatcellpy
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os,sys
from opcua import ua

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))

from misc.log import logger
from opc.uatype import uaType
from startup.config import CELL_CONFIG

class uaTCell(uaType):

    # tipos de celulas
    CELL            = "cell"
    QUALITY_CONTROL = "quality-control"
    OFFICE          = "office"
    STORAGE         = "storage"
    ASSEMBLY        = "assembly"
    MACHINING       = "machining"

    CONFIG          = CELL_CONFIG(CELL)

    @staticmethod
    def get_list():
        return [
             uaTCell.QUALITY_CONTROL,
             uaTCell.MACHINING,
             uaTCell.ASSEMBLY,
             uaTCell.STORAGE
        ] 

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaType.create_type(parent,idx,uaTCell,handle)
