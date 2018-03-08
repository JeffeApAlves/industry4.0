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
from uatcell import uaTCell
from uatqc import uaTQC

class uaQC(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.QUALITY_CONTROL)


    @staticmethod
    def create_type(parent,idx,handle=None):
        """
        Cria o tipo qc no server OPC-UA
        """

        dtype  = uaCell.create_type(parent,idx)

        return  uaTQC.create(dtype,idx,handle)