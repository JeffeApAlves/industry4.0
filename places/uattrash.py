#!/usr/bin/env python

"""

@file    uaTTRASH.PY
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from opcua import ua
from log import logger
from uatplace import uaTPlace
from config import PLACE_CONFIG

class uaTTrash(uaTPlace):


    CONFIG      = PLACE_CONFIG(uaTPlace.TRASH)


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaTPlace.create_type(parent,idx,uaTTrash,handle)

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
