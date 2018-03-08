#!/usr/bin/env python

"""

@file    uatplacepy
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from misc.log import logger
from uatplace import uaTPlace
from startup.config import PLACE_CONFIG

class uaTBuffer(uaTPlace):


    CONFIG      = PLACE_CONFIG(uaTPlace.BUFFER)


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTPlace.create_type(parent,idx,uaTBuffer,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """

        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """
        
        return obj_type
