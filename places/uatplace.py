#!/usr/bin/env python

"""

@file    uatplace.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from opcua import ua
from uatype import uaType
from log import logger
from uatype import uaType
from config import PLACE_CONFIG

class uaTPlace(uaType):

    # tipos de lugares
    PLACE           = "place"
    BUFFER          = "buffer"
    TRASH           = "trash"

    #propriedades
    pID             = "Id"
    pMAX            = "Max"
    pFREE           = "Free"

    CONFIG          = PLACE_CONFIG(PLACE)


    @staticmethod
    def get_list():
        return [
            uaTPlace.BUFFER ,
            uaTPlace.TRASH
        ]


    @staticmethod
    def create(parent,idx,handle=None):
        """
        Cria o tipo
        """

        return  uaType.create_type(parent,idx,uaTPlace,handle)

    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """

        obj_type.add_property(idx,  uaTPlace.pID,    999).set_writable()
        obj_type.add_property(idx,  uaTPlace.pMAX,   100).set_writable()
        obj_type.add_property(idx,  uaTPlace.pFREE,  100).set_writable()

        return obj_type


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """
        
        return obj_type
