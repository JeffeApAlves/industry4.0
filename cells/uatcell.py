#!/usr/bin/env python

"""

@file    uatcellpy
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from opc.uatype import uaType

class uaTCell(uaType):

    # tipos de celulas
    CELL            = "CellType"
    QUALITY_CONTROL = "QCType"
    STORAGE         = "StorageType"
    ASSEMBLY        = "AssemblyType"
    MACHINING       = "MachiningType"

    OPC_TYPE        = CELL

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
