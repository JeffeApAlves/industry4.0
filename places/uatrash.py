#!/usr/bin/env python

"""

@file    uatrash.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locias do tipo trash

"""


from uaplace import uaPlace

from config import PLACE_CONFIG
from opcua import ua

class uaTrash(uaPlace):

    CONFIG   = PLACE_CONFIG(uaPlace.TRASH)

    @staticmethod
    def create_type(server,idx):

        obj_type = uaPlace.create_type(server,idx,uaTrash.CONFIG.OBJECT_TYPE)

        return  obj_type