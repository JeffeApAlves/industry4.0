#!/usr/bin/env python

"""

@file    config.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Carrega as configurações do arquivo

"""


import os,sys
import getpass
import json

from distutils import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


class CONFIG(object):

    # diretrio raiz do projeto
    WORKDIR         = os.getenv('OPCUA_PROJECT_HOME','.')

    # Nome do projeto
    PROJECT_NAME    =  os.getenv('OPCUA_PROJECT_NAME','industry40')

    # path do arquivo de configuração
    SETUP_CONF      = os.getenv('OPCUA_CONF',"".join([WORKDIR, "/{}.conf".format(PROJECT_NAME)] ))

    # carrega  o json com as configurações
    with open(SETUP_CONF) as json_data_file:
        _configuration = json.load(json_data_file)

    # diretrio raiz do projeto
    HOMEDIR     = WORKDIR

    # diretrio com o modelo em xml
    SERVERDIR   = "/".join([HOMEDIR,"server"])

    # diretorio program devices
    CLIENDIR    = "/".join([HOMEDIR,"client"])

    # diretorio com o processo de inicialização
    STARTUPDIR  = "/".join([HOMEDIR,"startup"])

    # diretorio com o processo de inicialização
    CONFIGDIR   = "/".join([HOMEDIR,"config"])

    # arquivo de eventos
    FILE_EVENTS = "/".join([CONFIGDIR,"events.conf"])

   
    @staticmethod
    def get_map_class():
        """
        Retorna um dicionarios com os tipos usado no arquivo conf e sua respectiva class
        """

        sections = ['devices','places','cells']

        out = {}

        for s in sections:

            itens = list(CONFIG._configuration[s].keys())

            for i in itens:

                out[i] = CONFIG._configuration[s][i]['py-obj']

        return  out


class OPCUA_SERVER_CONFIG(CONFIG):
    '''
    Configurações relacionadas ao servidor OPCUA
    '''

    HOST    = CONFIG._configuration['opcua-server']['host']
    NAME    = CONFIG._configuration['opcua-server']['name']
    PORT    = CONFIG._configuration['opcua-server']['port']
    HOMEDIR = CONFIG._configuration['opcua-server']['homedir']
    URI     = CONFIG._configuration['opcua-server']['uri']
    DEPLOY  = CONFIG._configuration['opcua-server']['deploy']

    # string de conexão
    # END_POINT  = "opc.tcp://{}:{}/freeopcua/server/".format(OPCUA_SERVER_CONFIG.HOST,OPCUA_SERVER_CONFIG.PORT)
    URL     = "opc.tcp://{}@{}:{}/freeopcua/server/".format(getpass.getuser(),HOST,PORT)

    # adiciona diretorio de ferramentas no path
    sys.path.append(os.path.join(HOMEDIR, ''))



class DEVICE_CONFIG(CONFIG):
    '''
    Configurações relacionadas aos dispositivos 
    '''

    # tipos de dispositivos da rede
    TYPES           = list(CONFIG._configuration['devices'].keys())

    def __init__(self,name_device):
        self.__name_device = name_device



    @property
    def PY_OBJ(self):
        return CONFIG._configuration['devices'][self.__name_device]['py-obj']

    @property
    def PY_TYPE(self):
        return CONFIG._configuration['devices'][self.__name_device]['py-type']


    @property
    def HOMEDIR(self):
        return CONFIG._configuration['devices'][self.__name_device]['homedir']

    @property
    def UA_TYPE(self):
        return CONFIG._configuration['devices'][self.__name_device]['ua-type']

    @property
    def OBJECTS(self):
        try:
            objects = CONFIG._configuration['devices'][self.__name_device]['objects']
        except:
            objects = []

        return objects

    @property
    def DEPLOY(self):
        try:
            deploys = CONFIG._configuration['devices'][self.__name_device]['deploy']
        except:
            deploys = []

        return deploys

class CELL_CONFIG(CONFIG):
    '''
    Configurações relacionadas as celulas 
    '''

    # celulas de montagemm
    TYPES= list(CONFIG._configuration['cells'].keys())

    def __init__(self,name_device):
        self.__name_device = name_device



    @property
    def PY_OBJ(self):
        return CONFIG._configuration['cells'][self.__name_device]['py-obj']

    @property
    def PY_TYPE(self):
        return CONFIG._configuration['cells'][self.__name_device]['py-type']


    @property
    def UA_TYPE(self):
        return CONFIG._configuration['cells'][self.__name_device]['ua-type']

    @property
    def OBJECTS(self):
        try:
            objects = CONFIG._configuration['cells'][self.__name_device]['objects']
        except:
            objects = []

        return objects

class PLACE_CONFIG(CONFIG):
    '''
    Configurações relacionadas aos locais 
    '''

    # celulas de montagemm
    TYPES= list(CONFIG._configuration['places'].keys())

    def __init__(self,name_device):
        self.__name_device = name_device



    @property
    def PY_OBJ(self):
        return CONFIG._configuration['places'][self.__name_device]['py-obj']

    @property
    def PY_TYPE(self):
        return CONFIG._configuration['places'][self.__name_device]['py-type']

    @property
    def UA_TYPE(self):
        return CONFIG._configuration['places'][self.__name_device]['ua-type']

    @property
    def OBJECTS(self):
        try:
            objects = CONFIG._configuration['places'][self.__name_device]['objects']
        except:
            objects = []

        return objects

