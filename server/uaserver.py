#!/usr/bin/env python

"""

@file    uaserver.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""


import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from opcua import ua
from opcua import Server
from config.config import OPCUA_SERVER_CONFIG
from server.model import uaModel

logger = logging.getLogger(__name__)

class uaServer(object):

    __SERVER = None

    @staticmethod
    def config(name , url = None , xml = None,certificate = None,private_key = None, disable_clock = False):
        """
        configura e cria o odelo no servidor OPC-UA
        """

        if url is None:
            url = OPCUA_SERVER_CONFIG.URL

        if name is None:
            name = OPCUA_SERVER_CONFIG.NAME


        logger.info("url: {}".format(url))
        logger.info("name: {}".format(name))
        logger.info("xml: {}".format(xml))
        logger.info("certificate: {}".format(certificate))
        logger.info("private key: {}".format(private_key))
        logger.info("clock: {}".format(disable_clock))

        uaServer.__SERVER = Server()
        uaServer.__SERVER.set_endpoint(url)
        uaServer.__SERVER.set_server_name(name)
        uaServer.__SERVER.disable_clock(disable_clock)
        idx = uaServer.__SERVER.register_namespace(OPCUA_SERVER_CONFIG.URI)

        if certificate is not None:
            uaServer.__SERVER.load_certificate(certificate)
        
        if private_key is not None:
            uaServer.__SERVER.load_private_key(private_key)
        
        if xml is not None:
            uaServer.__SERVER.import_xml(xml)

        logger.info("Servidor {} configurado com sucesso {}".format(name,url))

        uaServer.create_model(idx)


    @staticmethod
    def create_model(idx):
        """
        Cria o modelo
        """

        uaModel.create(uaServer,idx)

        # exporta o modelo para um xml
        uaServer.__SERVER.export_xml_by_ns("/".join([OPCUA_SERVER_CONFIG.HOMEDIR,"server","model_ns.xml"])   ,[OPCUA_SERVER_CONFIG.URI])

    @staticmethod
    def start():
        """
        Inicia o servidor
        """

        uaServer.__SERVER.start()

    @staticmethod
    def stop():
        uaServer.__SERVER.stop()

    @staticmethod
    def get_objects_node():
        return uaServer.__SERVER.get_objects_node()


    @staticmethod
    def get_base_objectType_node():
        
        return uaServer.__SERVER.get_node(ua.ObjectIds.BaseObjectType)
