#!/usr/bin/env python

"""

@file    config.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Carrega e popula as configurações dos arquivos .conf

"""

import os
import sys
import getpass
import json
import logging

from distutils import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

class CONFIG(object):
    """
    Configurações gerais e comuns
    """

    _OPC_SERVER_SECTION     = "opcua-server"
    _SECTION_DEVICES        = "devices"
    _SECTION_CELLS          = "cells"
    _SECTION_PLACES         = "places"

    _EVENTS                 = "events"
    _DATA_CHANGE            = "data-change"
    _HOMEDIR                = "homedir"
    _TYPE                   = "type"
    _DEPLOY                 = "deploy"
    _INHERIT                = "inherit"
    _ENTITY                 = "entity"


    # diretrio raiz do projeto
    WORKDIR                 = os.getenv('OPCUA_PROJECT_HOME','.')

    # Nome do projeto
    PROJECT_NAME            =  os.getenv('OPCUA_PROJECT_NAME','industry40')

    # path do arquivo de configuração
    SETUP_CONF              = os.getenv('OPCUA_CONF',"/".join([WORKDIR, "{}.conf".format(PROJECT_NAME)] ))

    # diretrio raiz do projeto
    HOMEDIR                 = WORKDIR

    # diretrio com o modelo em xml
    SERVERDIR               = "/".join([HOMEDIR,"server"])

    # diretorio program devices
    CLIENDIR                = "/".join([HOMEDIR,"client"])

    # diretorio com o processo de inicialização
    STARTUPDIR              = "/".join([HOMEDIR,"startup"])

    # diretorio com o processo de inicialização
    CONFIGDIR               = "/".join([HOMEDIR,"config"])

    # arquivo de eventos
    FILE_EVENTS             = "/".join([CONFIGDIR,"objects.conf"])

    # carrega  o json com as configurações
    with open(SETUP_CONF) as json_data_file:
        _configuration = json.load(json_data_file)

    # carrega  o json com as configurações
    with open(FILE_EVENTS) as json_data_file:
        __objects = json.load(json_data_file)


    def __init__(self,section=None,opc_type=None,entity=None):

        self.logger = logging.getLogger(__name__)

        self._section           = section
        self._entity            = entity
        self._opc_type          = opc_type
        
        self._config_entity     = None
        self._config_type       = None

        
        if entity is not None:

            # nome do objeto
            if type(entity) is str:
                name_entity = entity
            else:
                name_entity = entity.display_name

            # configuração especifica do objeto
            self._config_entity = CONFIG.__objects[name_entity]
            
            # atualiza o tipo conforme o objeto
            self._opc_type      = self._config_entity[CONFIG._TYPE]

            # atualiza o diretorio de trabalho
            CONFIG.HOMEDIR      = self._config_entity[CONFIG._HOMEDIR] 


        # sessão não definida então procura no conf baseado no opc_type  
        if section is None:
            self._section       = self.search_section()

        # configuração especifica do tipo
        if self._opc_type is not None:
            
            self._config_type   = CONFIG._configuration[self._section][self._opc_type] 


    @staticmethod
    def choice_to_classe(choice):
        """
        Retorna a classe respectiva da opção de dispositivo
        """
        
        devices = CONFIG._configuration[CONFIG._SECTION_DEVICES]

        for key in devices:
            if choice == devices[key]['choice']:
                device = key
                break
        else:
            device = ""

        return device


    @staticmethod
    def get_name_devices_choice():
        """
        Retorna a lista de opções de dispositivos usada  no CL 
        """
        
        choices = []

        devices = CONFIG._configuration[CONFIG._SECTION_DEVICES]

        for key in devices:
            if key != "---":
                choices.append(devices[key]['choice'])

        return choices

    @staticmethod
    def get_name_devices():
        return list(CONFIG._configuration[CONFIG._SECTION_DEVICES].keys())

    @staticmethod
    def get_name_objects():
        return list(CONFIG.__objects.keys())

    @staticmethod
    def get_objects():
        return CONFIG.__objects

    @property
    def EVENTS_DATA_CHANGE (self):
        return self._config_entity[CONFIG._EVENTS][CONFIG._DATA_CHANGE]

    @property
    def ENTITY(self):
        return self._config_type[CONFIG._ENTITY]

    @property
    def INHERIT(self):
        return self._config_type[CONFIG._INHERIT]

    @property
    def TYPE(self):
        return self._config_type[CONFIG._TYPE]

    @property
    def DEPLOY(self):
        return self._config_entity[CONFIG._DEPLOY]

    @property
    def OPC_TYPE(self):
        return  self._opc_type


    def search_section(self):
        """
        Procura a sessão no arquivo de configuração baseado no opc_type
        """

        sections = ["devices","places","cells"]

        for section in sections:

            opc_types = CONFIG._configuration[section].keys()

            for opc_type in opc_types:

                if opc_type == self._opc_type:
                    break
            else:
                continue
            break
        else:
            self.logger.error("Sessão para o tipo {} não encontrada.".format(self._opc_type))
            section = ""
    
        return  section

class OPCUA_SERVER_CONFIG(CONFIG):
    '''
    Configurações especificas ao servidor OPCUA
    '''

    def __init__(self):
        super().__init__(CONFIG._OPC_SERVER_SECTION)

    HOST    = CONFIG._configuration[CONFIG._OPC_SERVER_SECTION]['host']
    NAME    = CONFIG._configuration[CONFIG._OPC_SERVER_SECTION]['name']
    PORT    = CONFIG._configuration[CONFIG._OPC_SERVER_SECTION]['port']
    HOMEDIR = CONFIG._configuration[CONFIG._OPC_SERVER_SECTION][CONFIG._HOMEDIR]
    URI     = CONFIG._configuration[CONFIG._OPC_SERVER_SECTION]['uri']
    DEPLOY  = CONFIG._configuration[CONFIG._OPC_SERVER_SECTION][CONFIG._DEPLOY]

    # string de conexão
    # END_POINT  = "opc.tcp://{}:{}/freeopcua/server/".format(OPCUA_SERVER_CONFIG.HOST,OPCUA_SERVER_CONFIG.PORT)
    URL     = "opc.tcp://{}@{}:{}/freeopcua/server/".format(getpass.getuser(),HOST,PORT)

class DEVICE_CONFIG(CONFIG):
    """ Configurações especificas ao tipo Device"""

    def __init__(self,opc_type=None,entity=None):
        super().__init__(section = DEVICE_CONFIG._SECTION_DEVICES,opc_type = opc_type,entity=entity)


class CELL_CONFIG(CONFIG):
    """ Configurações especificas ao tipo Cell"""

    def __init__(self,opc_type=None,entity=None):
        super().__init__(section=CELL_CONFIG._SECTION_CELLS,opc_type = opc_type,entity=entity)


class PLACE_CONFIG(CONFIG):
    """ Configurações especificas ao tipo Place"""

    def __init__(self,opc_type=None,entity=None):
        super().__init__(section=PLACE_CONFIG._SECTION_PLACES,opc_type = opc_type,entity=entity)