#!/usr/bin/env python

"""

@file    uaqc.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""


import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from cells.uacell import uaCell
from cells.uatcell import uaTCell
from cells.uatqc import uaTQC

from config.config import CELL_CONFIG

class uaQC(uaCell):


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo qc no server OPC-UA
        """

        dtype  = uaCell.create(parent,idx)

        return  uaTQC.create(dtype,idx,handle)