#!/usr/bin/env python

"""

@file    uacell.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))


from uatcell import uaTCell
from opc.uaobject import uaObject
from config.config import CELL_CONFIG

class uaCell(uaObject):

    CONFIG          = CELL_CONFIG(uaTCell.CELL) 

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo cell no server OPC-UA
        """

        return  uaTCell.create(parent,idx,handle)
