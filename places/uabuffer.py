#!/usr/bin/env python

"""

@file    uabuffer.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locais do tipo buffer

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from uaplace import uaPlace
from uatplace import uaTPlace
from config.config import PLACE_CONFIG

class uaBuffer(uaPlace):

    CONFIG   = PLACE_CONFIG(uaTPlace.BUFFER)

    @staticmethod
    def create(parent,idx):

        obj_type = uaPlace.create(parent,idx)

        return  obj_type