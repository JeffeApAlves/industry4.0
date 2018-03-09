#!/usr/bin/env python

"""

@file    factory.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de objetos

"""

import os,sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from cells.uatcell import uaTCell
from places.uatplace import uaTPlace
from devices.uatdevice import uaTDevice
from opc.mapclass import MapClass
from opc.events import Events
from config.config import CONFIG


class Factory(object):

    """
    Instruções para adicionar novos tipos

    1. Editar o arquivo industry.conf adicionando o novo tipo de local
    2. Adicionar , na classe generalista (uaTXXX),  uma constante com o nome que foi usado no arquivo conf
    3. Implemetar as classes do novo tipo uaTXXX (create_methods,create_pro,create) e uaXXX (init,create_type)
    """


    def __init__(self,type):

    
        self.logger = logging.getLogger(__name__)


        # Lista com os tipos
        self.__Type = type 

    def get_list_types(self):
        """
        Retorna a lista de tipos de dispositos
        """

        return self.__Type.get_list()


    def get_type_class(self,type):
        """
        Retorna a classe do tipo respectiva do tipo
        """

        class_name = self.get_config(type).PY_TYPE

        return MapClass.get_class(class_name)


    def get_obj_class(self,type):
        """
        Retorna a classe do objeto respectiva do tipo
        """

        class_name = self.get_config(type).PY_OBJ

        return MapClass.get_class(class_name)


    def get_config(self,type):
        """
        Retorna a configuração respectiva do tipo
        """

        return MapClass.get_config(type)


    def get_list_objects(self,type):
        """
        Retorna a lista de objetos a serem criados
        """

        return self.get_config(type).OBJECTS


    def create_object(self,idx,name,type):
        """
        Cria um objeto python de um dispositivo do tipo <type> com o nome <name> e vincula com o objeto correspondente no OPC-UA
        """


        try:

            class_of_obj= self.get_obj_class(type)

            # instancia o objeto
            py_obj      = class_of_obj(idx,name)

            Events.create_data_change_events(idx,py_obj)
            
            self.logger.info("Sucesso Dispositivo {} criado class {}".format(name,class_of_obj))    

        except IOError as e:
            py_obj = None
            self.logger.warn("Não foi possível criar o dispositivo {}\nI/O error({0}): {1}".format(name,e.errno, e.strerror))

        return  py_obj


    def create_ua_type(self,parent,idx,type):
        """
        Cria um tipo de dispositivo com o nome <type>  no servidor OPC-UA
        """
   
        try:
            obj_class   = self.get_obj_class(type)
            ua_obj      = obj_class.create(parent,idx)
            self.logger.info("Sucesso : Parent {} - Tipo {}  Objeto  {} chield {}".format(parent,type,obj_class,ua_obj))    
        except:

            ua_obj = None
            self.logger.warn("Não foi possível criar  : Parent {} - Tipo {} class {} chield {}".format(parent,type,obj_class,ua_obj))    

        return ua_obj
