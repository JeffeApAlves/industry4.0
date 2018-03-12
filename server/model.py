#!/usr/bin/env python

"""

@file    model.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))

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

        # node de objetos no opcua
        uatypes     = server.get_base_objectType_node()
 
        logger.info("Criando os tipos: {}".format(types))

        for t in types:

            # cria os tipos de objeto/variaveis no servidor opcua
            ua_type = Factory.create_type(uatypes,idx,t) 


    @staticmethod
    def __create_objects(server,idx):
        """
        Cria os objetos no servidor OPC-UA
        """

        try:

            # node de todos os objetos (parent)                
            objects     = server.get_objects_node()

            # node dos tipos
            uatypes     = server.get_base_objectType_node()
    
            # lista de objetos a serem criados
            obj_list    = CONFIG.get_objects()


            for key in obj_list:

                config = CONFIG(entity=key)

                path =  [ ":".join( [str(idx), config.INHERIT ] ) , ":".join( [str(idx), config.OPC_TYPE ] ) ] 

                opc_type = uatypes.get_child(path)

                # cria no servidor opc os objetos
                objects.add_object(idx, key , opc_type.nodeid)

                logger.info("Criado objeto {} do tipo {} em {}".format( key , opc_type , objects))

        except :
            #print(e)
            logger.error("Parametros key {}  path {} incorretos para criação dos objetos".format(key,path))
