#!/usr/bin/env python

"""

@file    opc.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Conexão com  o servidor OPC

"""

from opcua import Client
from opcua import ua
from config import OPCUA_SERVER_CONFIG
from log import logger

class uaClient(object):

    __CLIENT    = None

    @staticmethod
    def connect():
        '''
        Conecta ao servidor OPC-UA
        '''

        try:

            if uaClient.__CLIENT is None:

                # Rntidade client
                uaClient.__CLIENT = Client(OPCUA_SERVER_CONFIG.URL)

                # Conectando ...
                uaClient.__CLIENT.connect()

                logger.info("Conectado ao servidor OPC-UARoot: {}\nChildren {}".format(uaClient.get_root_node(),uaClient.get_root_node().get_children()))

        except :
            logger.error("Erro ao tentar conectar no servidor opcua {} !".format(OPCUA_SERVER_CONFIG.HOST))
            uaClient.__CLIENT.disconnect()
            uaClient.__CLIENT = None

        return uaClient.__CLIENT

    @staticmethod
    def get_client():
        return uaClient.__CLIENT

    @staticmethod
    def disconnect():
        """
        Desconecta do servidor OPC-UA 
        """

        uaClient.__CLIENT.disconnect()


    @staticmethod
    def get_root_node():
        """
        Retorna o root node
        """

        return uaClient.__CLIENT.get_root_node()

    @staticmethod
    def get_objects_node():
        """
        Retorna o objects node
        """

        return uaClient.__CLIENT.get_objects_node()