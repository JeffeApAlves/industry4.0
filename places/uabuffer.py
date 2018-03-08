#!/usr/bin/env python

"""

@file    uabuffer.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locais do tipo buffer

"""


from uaplace import uaPlace
from uatplace import uaTPlace
from config import PLACE_CONFIG

class uaBuffer(uaPlace):

    CONFIG   = PLACE_CONFIG(uaTPlace.BUFFER)

    @staticmethod
    def create(parent,idx):

        obj_type = uaPlace.create(parent,idx)

        return  obj_type