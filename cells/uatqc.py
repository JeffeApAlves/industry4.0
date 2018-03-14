#!/usr/bin/env python

"""

@file    uatqcpy
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from cells.uatcell import uaTCell


logger = logging.getLogger(__name__)

class uaTQC(uaTCell):

    OPC_TYPE    = uaTCell.QUALITY_CONTROL

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """
        logger.info(uaTQC.OPC_TYPE)

        return  uaTCell.create_type(parent,idx,uaTQC,handle)

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
