#!/usr/bin/env python

"""

@file    uaStorage.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""


from uacell import uaCell
from config import CELL_CONFIG
from opcua import ua
from uatcell import uaTCell
from uatstorage import uaTStorage

class uaStorage(uaCell):

    CONFIG   = CELL_CONFIG(uaTCell.STORAGE)


    @staticmethod
    def create_type(parent,idx,handle=None):
        """
        Cria o tipo storage no server OPC-UA
        """

        dtype  = uaCell.create(parent,idx)

        return  uaTStorage.create(dtype,idx,handle)

