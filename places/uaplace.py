#!/usr/bin/env python

"""

@file    uaplace.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from opc.uaobject import uaObject
from places.uatplace import uaTPlace

class uaPlace(uaObject):

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo cell no server OPC-UA
        """

        return  uaTPlace.create(parent,idx,handle)
