#!/usr/bin/env python

"""

@file    uaplace.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""

from opcua import ua
from uaobject import uaObject
from uatplace import uaTPlace
from config import PLACE_CONFIG

class uaPlace(uaObject):

    CONFIG          = PLACE_CONFIG(uaTPlace.PLACE) 

    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo cell no server OPC-UA
        """

        return  uaTPlace.create(parent,idx,handle)
