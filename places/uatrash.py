#!/usr/bin/env python

"""

@file    uatrash.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locias do tipo trash

"""


from uaplace import uaPlace
from uatplace import uaTPlace
from config import PLACE_CONFIG

class uaTrash(uaPlace):

    CONFIG   = PLACE_CONFIG(uaTPlace.TRASH)

    @staticmethod
    def create(parent,idx):

        obj_type = uaPlace.create(parent,idx)

        return  obj_type