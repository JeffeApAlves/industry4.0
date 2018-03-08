#!/usr/bin/env python

"""

@file    uatmachining.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
#sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))


from opcua import ua

from misc.log import logger
from cells.uatcell import uaTCell
from startup.config import CELL_CONFIG

class uaTMachining(uaTCell):

    CONFIG = CELL_CONFIG(uaTCell.MACHINING)

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTCell.create_type(parent,idx,uaTMachining,handle)

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
