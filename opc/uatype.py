#!/usr/bin/env python

"""

@file    uatype.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

"""


import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


logger = logging.getLogger(__name__)

class uaType(object):


    @staticmethod
    def create_type(parent,idx,type=None,handle=None):
        """
        Adiciona <parent> , um child do tipo indicado por <type>
        """

        opc_type = type.CONFIG.OPC_TYPE


        try:
            child = parent.get_child(":".join([str(idx), opc_type ]))
        except:

            try:
                child = parent.add_object_type(idx,opc_type )

                # cria metodos do proriedades
                type.create_property(child,idx )

                # cria metodos do child
                type.create_methods(child,idx,handle)

            except IOError as e:
                
                print(e)

        
        logger.info("Created child: Parent {} Tipo {} Child {} - children: {}".format(parent,opc_type,child,child.get_children()))    

        return child


    @staticmethod
    def create_property(obj_type,idx):
        """
        Cria as propriedades
        """
        pass


    @staticmethod
    def create_methods(obj_type,idx,handle):
        """
        Cria os metodos
        """
        pass
