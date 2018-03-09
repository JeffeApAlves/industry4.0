#!/usr/bin/env python

"""

@file    uamachining.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from cells.uacell import uaCell
from cells.uatcell import uaTCell
from cells.uatmachining import uaTMachining
from config.config import CELL_CONFIG

class uaMachining(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.MACHINING)


    @staticmethod
    def create_type(parent,idx,handle=None):
        """
        Cria o tipo machining no server OPC-UA
        """

        dtype  = uaCell.create(parent,idx)

        return  uaTMachining.create(dtype,idx,handle)

