#!/usr/bin/env python

"""

@file    events.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Carrega as configurações do arquivo

"""

import os,sys
import json
import logging

from distutils import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from client.uaclient import uaClient
from opc.uaobject import uaObject
from config.config import CONFIG

    
logger = logging.getLogger(__name__)


class Events(object):


    DATA_CHANGE = "data-change"

    # carrega  o json com as configurações
    with open(CONFIG.FILE_EVENTS) as json_data_file:
        __events = json.load(json_data_file)


    @staticmethod
    def create_data_change_events(idx,obj):

        try:

            e = Events.__events[Events.DATA_CHANGE][obj.display_name]

            src         = e['source']['obj']
            name_var    = e['source']['var']
            priority    = e['PRIORITY']

            var         = uaObject(uaClient.get_objects_node(),idx,src).get_child(name_var)

            handler = obj.get_SubHandler()

            uaClient.subscribe_event(var,priority,handler)

            logger.info("Sucesso subscribe {} on {} ".format(obj.display_name,src))

        except :

            logger.warn("Não foi encontrado eventos para esse objeto {}".format(obj))
