#!/usr/bin/env python

"""

@file    factory.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de objetos

"""

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from cells.uatcell import uaTCell
from places.uatplace import uaTPlace
from devices.uatdevice import uaTDevice
from opc.mapclass import str_to_class
from opc.uaobject import uaObject
from client.uaclient import uaClient
from config.config import CONFIG


logger = logging.getLogger(__name__)

class Factory(object):

    """
    Instruções para adicionar novos tipos

    1. Editar o arquivo industry40.conf adicionando o novo tipo
    2. Adicionar , na classe generalista (uaTXXX),  uma constante com o nome que foi usado no arquivo conf
    3. Implemetar as classes do novo tipo uaTXXX  (create) e uaXXX (create) (create_methods,create_pro,create)
    """


    @staticmethod
    def get_list_types():
        """
        Retorna a lista de tipos
        """
    
        types = []

        for t in [uaTCell , uaTDevice ,  uaTPlace]:
            types += t.get_list()

        return types


    @staticmethod
    def get_type_class(opc_type):
        """
        Retorna a classe do tipo respectiva do tipo
        """

        class_type = Factory.get_config(opc_type).TYPE

        return str_to_class(class_type)


    @staticmethod
    def get_entity_class(opc_type):
        """
        Retorna a classe do objeto respectiva do tipo
        """

        class_entity = Factory.get_config(opc_type).ENTITY

        return str_to_class(class_entity)

    @staticmethod
    def get_config(opc_type=None,entity=None):
        """
        Retorna a configuração respectiva do tipo
        """

        return CONFIG(opc_type = opc_type , entity=entity)

    @staticmethod
    def get_name_objects():
        """
        Retorna a lista de objetos a serem criados
        """

        return CONFIG.get_name_objects()

    @staticmethod
    def create_entity(idx,name,opc_type):
        """
        Cria um objeto python de um dispositivo do tipo <type> com o nome <name> e vincula com o objeto correspondente no OPC-UA
        """

        try:
            class_of_entity = Factory.get_entity_class(opc_type)

            # instancia o objeto
            py_obj      = class_of_entity(idx,name)

            Factory.create_data_change_events(idx,py_obj)
            
            #self.logger.info("Sucesso Dispositivo {} criado class {}".format(name,class_of_entity.__name__))    

        except IOError as e:
            py_obj = None
            logger.warning("Não foi possível criar o dispositivo {}\nI/O error({0}): {1}".format(name,e.errno, e.strerror))

        return  py_obj


    @staticmethod
    def create_type(parent,idx,opc_type):
        """
        Cria um node (tipo) com o nome <type>  no servidor OPC-UA
        """
   
        try:
            class_of_entity = Factory.get_entity_class(opc_type)

            logger.info("Inicio criando tipo {}-{} !".format(opc_type,class_of_entity.__name__))
               

            type_obj        = class_of_entity.create(parent,idx)

            #self.logger.info("Sucesso Parent {} - Tipo {} class {} chied {}".format(parent,opc_type,class_of_entity.__name__,type_obj))    
        
        except IOError as e:

            type_obj = None
            logger.warning("Não foi possível criar  : Parent {} - Tipo {} class {}".format(parent,opc_type,class_of_entity.__name__))    
            print(e)

        return type_obj

    @staticmethod
    def create_data_change_events(idx,entity_obj):
        """
        Cria eventos para o objeto
        """

        try:
            parent      = uaClient.get_objects_node()

            all_events  = CONFIG( entity = entity_obj ).EVENTS_DATA_CHANGE

            for e in all_events:
                
                n_obj,n_var     = e['data-source'].split(".")
                priority        = e['priority']
                name_handler    = e['handler']

                var             = uaObject(parent,idx,n_obj).get_child(n_var)
                handler         = entity_obj.create_handler(name_handler)

                uaClient.subscribe_event(var,priority,handler)

                logger.info("Sucesso evento data change do {} registrado em {}".format(entity_obj.display_name,var))

        except :

            logger.warning("Não foi encontrado eventos para esse objeto {}".format(entity_obj))
