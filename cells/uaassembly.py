#!/usr/bin/env python

"""

@file    uaassembly.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from cells.uacell import uaCell
from cells.uatcell import uaTCell
from cells.uatassembly import uaTAssembly
from config.config import CELL_CONFIG

class uaAssembly(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.ASSEMBLY)

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo assembly no server OPC-UA
        """

        dtype  = uaCell.create(parent,idx)

        return  uaTAssembly.create(dtype,idx,handle)