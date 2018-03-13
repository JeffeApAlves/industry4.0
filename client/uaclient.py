#!/usr/bin/env python

"""

@file    opc.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Conexão com  o servidor OPC

"""

import sys
import os
import logging
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import Client,ua
from opc.uaobject import uaObject
from config.config import OPCUA_SERVER_CONFIG

logger = logging.getLogger(__name__)

class uaClient(object):

    __Client    = None
    __idx       = 1
    __Objects   = None

    @staticmethod
    def connect():
        '''
        Conecta ao servidor OPC-UA
        '''

        logger.info("Client conectando em {}".format(OPCUA_SERVER_CONFIG.HOST))

        # singleton 
        if uaClient.__Client is None:

            # Rntidade client
            uaClient.__Client = Client(OPCUA_SERVER_CONFIG.URL)

            # Conectando ...
            uaClient.__Client.connect()

            uaClient.__Objects = uaClient.__Client.get_objects_node() 

            logger.info("Client conectado ao servidor OPC-UA")
            logger.info("Children in objects: {}".format(uaClient.get_objects_node().get_children()))
            logger.info("Encontrado 1 !!!!!!!!!!! {}".format(uaClient.get_objects_node().get_child(["1:RB3"])))



    @staticmethod
    def disconnect():
        """
        Desconecta do servidor OPC-UA 

        """
        uaClient.__Client.disconnect()
        uaClient.__Client = None
        logger.info("Client desconectado")


    @staticmethod
    def get_root_node():
        """
        Retorna o root node
        """

        return uaClient.__Client.get_root_node()

    @staticmethod
    def get_objects_node():
        """
        Retorna o objects node
        """
        return uaClient.__Objects
        #return uaClient.__Client.get_objects_node()


    @staticmethod
    def get_idx():
        """
        Retorna o objects node
        """

        return uaClient.__idx


    @ staticmethod
    def subscribe_event(var_nodeid,priority,handler):
        """
        Registra um handler no evento data change de um determinado nodeid

        :param handler: callback que serão chamadas para processamento do evento.
 
        """

        sub = uaClient.__Client.create_subscription(priority, handler)
        sub.subscribe_data_change(var_nodeid)
        logger.info("Registrado o data change evento em {}".format(var_nodeid))

    @staticmethod
    def get_object(name):
        """
        Retorna um objeto
        """
    
        return uaObject(uaClient.get_objects_node(),uaClient.__idx,name)
