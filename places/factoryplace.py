#!/usr/bin/env python

"""

@file    factoryplace.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de locais na produção
"""

from uaplace import uaPlace
from config import PLACE_CONFIG
from uabuffer import uaBuffer
from uatrash import uaTrash

from log import logger

class FactoryPlace(object):

    """
    Instruções para adicionar novos tipos de locais

    1. Editar o arquivo industry.conf adicionando o novo tipo de local
    2. AdiciOnar , na classe generalista (uaPlace),  uma constante com o nome que foi usado no arquivo conf
    3. Implemetar a classe do novo tipo  (init,create_type)
    4. Mapear a constante com a classe em factoryXXX
    """

    MAP_PLACE = {
        uaPlace.PLACE:      uaPlace ,
        uaPlace.BUFFER:     uaBuffer ,
        uaPlace.TRASH:      uaTrash
    }

    @staticmethod
    def get_obj_class(type):
        """
        Retorna a class respectiva do tipo
        """

        obj_class = FactoryPlace.MAP_PLACE.get(type, None)

        if obj_class is  None:
            logger.warn("Tipo {} não mapeado".format(type))

        return obj_class

    @staticmethod
    def get_list_types():
        """
        Retorna a lista de tipos de células
        TODO: Aproveitar os keys do map porem reordenar
        """

        list_types = [uaPlace.PLACE,uaPlace.BUFFER,uaPlace.TRASH]
        
        return list_types

    @staticmethod
    def get_list_objects(type):
        """
        Retorna a lista de objetos a serem criados
        """

        return FactoryPlace.get_config(type).OBJECTS


    @staticmethod
    def get_config(type):
        """
        Retorna a configuração respectiva do tipo
        """

        return FactoryPlace.get_obj_class(type).CONFIG


    @staticmethod
    def create(idx,name,type):
        """
        Cria um local do tipo <type> com o nome <name>
        """

        obj_class = FactoryPlace.get_obj_class(type)
    
        if obj_class is  None:
            logger.warn("Não foi possível criar um locla do tipo {}".format(type))

        return obj_class(idx,name)
