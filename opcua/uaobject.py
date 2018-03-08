#!/usr/bin/env python

"""

@file    uaobject.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Abstrção de um objeto do opcua

"""

from concurrent.futures import Future, TimeoutError
import time
from datetime import datetime
from datetime import timedelta
import math
import copy
from contextlib import contextmanager

from opcua import ua
from opcua import Node
from opcua import instantiate
from opcua import copy_node
from opcua.common import ua_utils
from opcua.common.methods import call_method_full

from uaclient import uaClient
from log import logger

class uaObject(object):

    def __init__(self,parent,idx,name_obj):

        self._idx   = str(idx)
        self._node  = self.__get_node(parent,name_obj)

    @property
    def node(self):
        return self._node

    @property
    def display_name(self):
        return self._node.get_display_name()

    @property
    def value(self):
        return self._node.get_value()

    @value.setter
    def value(self, val):
        self._node.set_value(val)

    @property
    def idx(self):
        return self._idx

    def set_value(self,name,value):

        self.__get_child(name).set_value(value)

    def get_value(self,name):

        return self.__get_child(name).get_value()


    def __get_node(self,parent,name):
        """
        Retorna o node de nome 'name_object'
        """

        path = [":".join([self._idx,name])]

        if parent is None:
            parent = uaClient.get_objects_node()

        try:
            node = parent.get_child(path)
        except:
            logger.warn("Parent {} Node {} não foi encontrado".format(parent,path))
            node = None

        return node

    def __get_child(self,name):

        path = [":".join([self._idx,name])]

        self._node.get_child(path)
