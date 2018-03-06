#!/usr/bin/env python

"""

@file    factorycell.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de celulas

"""

from uacell import uaCell
from config import CELL_CONFIG
from uaqc import uaQC
from log import logger
from uamachining import uaMachining
from uastorage import uaStorage
from uaassembly import uaAssembly

class FactoryCell(object):

    """
    Instruções para adicionar novos tipos de células

    1. Editar o arquivo industry.conf adicionando o novo tipo de local
    2. Adicionar , na classe generalista (uaCell), uma constante com o nome que foi usado no arquivo conf
    3. Implemetar a classe do novo tipo  (init,create_type)
    4. Mapear a constante com a classe em factoryXXX
    """

    MAP_CELL = {
        uaCell.CELL:                uaCell ,
        uaCell.QUALITY_CONTROL:     uaQC ,
        uaCell.MACHINING:           uaMachining ,
        uaCell.ASSEMBLY:            uaAssembly,
        uaCell.STORAGE:             uaStorage
    }

    @staticmethod
    def get_obj_class(type):
        """
        Retorna a class respectiva do tipo
        """

        obj_class = FactoryCell.MAP_CELL.get(type, None)

        if obj_class is  None:
            logger.warn("Tipo {} não mapeado".format(type))

        return obj_class

    @staticmethod
    def get_list_types():
        """
        Retorna a lista de tipos de células
        """

        list_types = [uaCell.CELL,uaCell.QUALITY_CONTROL,uaCell.ASSEMBLY,uaCell.MACHINING,uaCell.STORAGE]
        
        return list_types

    @staticmethod
    def get_list_objects(type):
        """
        Retorna a lista de objetos que seráo criados
        """

        return FactoryCell.get_config(type).OBJECTS

    @staticmethod
    def create(idx,name,type):
        """
        Cria uma célula do tipo <type> com o nome <name>
        """

        obj_class = FactoryCell.get_obj_class(type)
    
        if obj_class is  None:
            logger.warn("Não foi possível criar a célula do tipo {}".format(type))

        return obj_class(idx,name)


    @staticmethod
    def get_config(type):
        """
        Retorna a configuração respectiva do tipo
        """

        return FactoryCell.get_obj_class(type).CONFIG
