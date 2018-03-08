#!/usr/bin/env python

"""

@file    uaassembly.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""


from uacell import uaCell
from uatcell import uaTCell
from uatassembly import uaTAssembly
from config import CELL_CONFIG

class uaAssembly(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.ASSEMBLY)

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo assembly no server OPC-UA
        """

        dtype  = uaCell.create(parent,idx)

        return  uaTAssembly.create(dtype,idx,handle)