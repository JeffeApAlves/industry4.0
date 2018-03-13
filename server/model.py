#!/usr/bin/env python

"""

@file    model.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Cria os nodes no servidor opc-ua

"""

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from opc.uatype import uaType
from devices.uatdevice import uaTDevice
from cells.uatcell import uaTCell
from places.uatplace import uaTPlace
from opc.factory import Factory
from config.config import CONFIG

logger = logging.getLogger(__name__)

class uaModel(object):

    @staticmethod
    def create(server,idx):
        """
        Cria o tipo de dispositivos e seus respectivos objetos no servidor opc-ua
        """
              
        uaModel.__create_type(server,idx)
        uaModel.__create_objects(server,idx)    


    @staticmethod
    def __create_type(server,idx):
        """
        Cria os tipos de objeto/variaveis no servidor OPC-UA
        """

        types       = Factory.get_list_types()

        # node de tipos no opcua
        uatypes     = server.get_base_objectType_node()
 
        try:
                
            for t in types:

                # cria os tipos de objeto/variaveis no servidor opcua
                ua_type = Factory.create_type(uatypes,idx,t) 

                logger.info("Criado o tipo: {} {}".format(t,ua_type))

        except :
            logger.error("Problema ao cria os tipos {}".format(types))

    @staticmethod
    def __create_objects(server,idx):
        """
        Cria os objetos no servidor OPC-UA
        """


        # node de todos os objetos (parent)                
        objects     = server.get_objects_node()

        # node dos tipos
        uatypes     = server.get_base_objectType_node()

        # lista de objetos a serem criados
        obj_list    = CONFIG.get_objects()

        try:

            for name_obj in obj_list:

                config  = CONFIG(entity=name_obj)

                path    =  [ ":".join( [str(idx), config.INHERIT ] ) , ":".join( [str(idx), config.OPC_TYPE ] ) ] 

                type    = uatypes.get_child(path)

                # cria no servidor opc os objetos
                objects.add_object(idx, name_obj , objecttype = type.nodeid)

                logger.info("Criado com sucesso objeto {} do tipo {} em {}".format( name_obj , type , objects))

        except :
            logger.error("Parametros Nome do objeo {} Path {} incorretos para criação dos objetos".format(name_obj,path))
