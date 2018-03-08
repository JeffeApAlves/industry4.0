#!/usr/bin/env python

"""

@file    uatype.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""

from log import logger

class uaType(object):


    @staticmethod
    def create_type(parent,idx,type=None,handle=None):
        """
        Cria, no <parent> , um child do tipo indicado por <type>
        """

        try:
            child = parent.get_child(":".join([str(idx), type.CONFIG.UA_TYPE ]))
        except:
            child = parent.add_object_type(idx,type.CONFIG.UA_TYPE)

            # cria metodos do proriedades
            child = type.create_property(child,idx)

            # cria metodos do chield
            child = type.create_methods(child,idx,handle)

        return child


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
