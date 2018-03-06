#!/usr/bin/env python

"""

@file    uaqc.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""


from uacell import uaCell

from config import CELL_CONFIG
from opcua import ua

class uaQC(uaCell):

    CONFIG   = CELL_CONFIG(uaCell.QUALITY_CONTROL)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaCell.create_type(server,idx,uaQC.CONFIG.OBJECT_TYPE)

        return  obj_type