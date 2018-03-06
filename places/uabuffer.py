#!/usr/bin/env python

"""

@file    uabuffer.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locais do tipo buffer

"""


from uaplace import uaPlace

from config import PLACE_CONFIG
from opcua import ua

class uaBuffer(uaPlace):

    CONFIG   = PLACE_CONFIG(uaPlace.BUFFER)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaPlace.create_type(server,idx,uaBuffer.CONFIG.OBJECT_TYPE)

        return  obj_type