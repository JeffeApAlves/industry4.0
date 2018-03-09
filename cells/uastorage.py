#!/usr/bin/env python

"""

@file    uaStorage.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import ua
from cells.uacell import uaCell
from cells.uatcell import uaTCell
from cells.uatstorage import uaTStorage
from config.config import CELL_CONFIG

class uaStorage(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.STORAGE)


    @staticmethod
    def create_type(parent,idx,handle=None):
        """
        Cria o tipo storage no server OPC-UA
        """

        dtype  = uaCell.create(parent,idx)

        return  uaTStorage.create(dtype,idx,handle)

