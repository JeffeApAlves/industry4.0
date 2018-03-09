#!/usr/bin/env python

"""

@file    uaserver.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""


import os,sys
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
    def start_uaserver(name , url = None , xml = None,certificate = None,private_key = None, disable_clock = False):
        """
        Inicializa o servidor OPC-UA
        """

        if url is None:
            url = OPCUA_SERVER_CONFIG.URL

        if name is None:
            name = OPCUA_SERVER_CONFIG.NAME

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

        uaModel.create(uaServer,idx)

        # exporta o modelo para um xml
        uaServer.__SERVER.export_xml_by_ns("/".join([OPCUA_SERVER_CONFIG.HOMEDIR,"server","model_ns.xml"])   ,[OPCUA_SERVER_CONFIG.URI])

        uaServer.__SERVER.start()

        logger.info("Servidor iniciado com sucesso {}".format(url))


    @staticmethod
    def get_objects_node():
        return uaServer.__SERVER.get_objects_node()


    @staticmethod
    def get_base_objectType_node():
        
        return uaServer.__SERVER.get_node(ua.ObjectIds.BaseObjectType)
