#!/usr/bin/env python

"""

@file    uacell.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""

from uaobject import uaObject
from uatcell import uaTCell
from config import CELL_CONFIG

class uaCell(uaObject):

    CONFIG          = CELL_CONFIG(uaTCell.CELL) 

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo cell no server OPC-UA
        """

        return  uaTCell.create(parent,idx,handle)
