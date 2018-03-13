#!/usr/bin/env python

"""

@file    uaobject.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Abstrção de um objeto do opcua

"""

import os
import sys
import logging
import time
import math
import copy
from concurrent.futures import Future, TimeoutError
from datetime import datetime,timedelta
from contextlib import contextmanager

from opcua import ua
from opcua import Node
from opcua import instantiate
from opcua import copy_node
from opcua.common import ua_utils
from opcua.common.methods import call_method_full

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

class uaObject(object):


    def __init__(self,parent,idx,name):

        self.logger = logging.getLogger(__name__)

        self._idx   = idx
        self._node  = self.__get_node(parent,idx,name)

    @property
    def node(self):
        return self._node

    @property
    def nodeid(self):
        return self._node.nodeid

    @property
    def idx(self):
        return self._idx

    @property
    def display_name(self):
        return self._node.get_display_name().Text

    @property
    def value(self):
        return self._node.get_value()

    @value.setter
    def value(self, val):
        self._node.set_value(val)


    def get_child(self,name):
        """
        Retorna um node filho de nome indicado em 'name' 
        """

        path = [":".join([str(self._idx),name])]

        try:
            node = self._node.get_child(path)
            self.logger.info("Objeto {} encontrado em {}: Node {}".format(path,self._node,node))
        except:
            node = None
            self.logger.error("Não foi encontrado {} em  Parent {} - Children: {}".format(path,self._node,self._node.get_children()))
        return node


    def __get_node(self,parent,idx,name):
        """
        Retorna o node de nome 'name_object'
        """

        path = [":".join([str(idx),name]),]

        try:
            node = parent.get_child(path)
            self.logger.info("Objeto {} encontrado em {}: Node {}".format(path,parent,node))
        except:
            self.logger.error("Não foi encontrado {} em  Parent {} - Children:".format(path,parent))
            node = None

        return node


    def call(self,method_name, *args):
        """
        Executa um método do objeto
        """

        method = self.get_child(method_name)
 
        result_variants = self._node.call_method( method, *args )

        return result_variants

