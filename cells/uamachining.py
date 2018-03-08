#!/usr/bin/env python

"""

@file    uamachining.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""


from uacell import uaCell

from config import CELL_CONFIG
from uatcell import uaTCell
from uatmachining import uaTMachining

class uaMachining(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.MACHINING)


    @staticmethod
    def create_type(parent,idx,handle=None):
        """
        Cria o tipo machining no server OPC-UA
        """

        dtype  = uaCell.create_type(parent,idx)

        return  uaTMachining.create(dtype,idx,handle)

