#!/usr/bin/env python

"""

@file    uaplace.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))

from opcua import ua
from opc.uaobject import uaObject
from uatplace import uaTPlace
from startup.config import PLACE_CONFIG

class uaPlace(uaObject):

    CONFIG          = PLACE_CONFIG(uaTPlace.PLACE) 

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo cell no server OPC-UA
        """

        return  uaTPlace.create(parent,idx,handle)
