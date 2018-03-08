#!/usr/bin/env python

"""

@file    uatassembly.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from opcua import ua
from log import logger
from uatcell import uaTCell
from config import CELL_CONFIG

class uaTAssembly(uaTCell):

    CONFIG = CELL_CONFIG(uaTCell.ASSEMBLY)

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTCell.create_type(parent,idx,uaTAssembly,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """

        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """
       
        return obj_type
