#!/usr/bin/env python

"""

@file    uaserver.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""


import os,sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from opcua import Server
from startup.config import OPCUA_SERVER_CONFIG
from server.model import uaModel
from misc.log import logger

class uaServer(object):

    @staticmethod
    def start_uaserver(name , url = None , xml = None,certificate = None,private_key = None, disable_clock = False):
        """
        Inicializa o servidor OPC-UA
        """

        if url is None:
            url = OPCUA_SERVER_CONFIG.URL

        if name is None:
            name = OPCUA_SERVER_CONFIG.NAME

        server = Server()

        server.set_endpoint(url)

        server.set_server_name(name)
        
        server.disable_clock(disable_clock)

        idx = server.register_namespace(OPCUA_SERVER_CONFIG.URI)

        if certificate is not None:
            server.load_certificate(certificate)
        
        if private_key is not None:
            server.load_private_key(private_key)
        
        if xml is not None:
            server.import_xml(xml)

        uaModel.create(server,idx)

        # exporta o modelo para um xml
        server.export_xml_by_ns("/".join([OPCUA_SERVER_CONFIG.HOMEDIR,"server","model_ns.xml"])   ,[OPCUA_SERVER_CONFIG.URI])

        server.start()

        logger.info("Servidor iniciado com sucesso {}".format(url))
