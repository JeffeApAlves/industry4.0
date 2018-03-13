#!/usr/bin/env python

"""

@file    uabuffer.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locais do tipo buffer

"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from places.uaplace import uaPlace
from places.uatplace import uaTPlace
from places.uatbuffer import uaTBuffer
from config.config import PLACE_CONFIG

class uaBuffer(uaPlace):

    @staticmethod
    def create(parent,idx,handle=None):

        dtype = uaPlace.create(parent,idx)

        return  uaTBuffer.create(dtype,idx,handle)
