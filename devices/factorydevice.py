#!/usr/bin/env python

"""

@file    factorydevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Fabrica de dispositivos

"""

from uaraspberry import uaRaspBerry
from uarobot import uaRobot
from uavision import uaVision
from uadevice import uaDevice
from uacoveyor import uaCoveyor
from uamill import uaMill
from uabarcodereader import uaBarCodeReader
from ualathe import uaLathe
from log import logger

class FactoryDevice(object):

    """
    Instruções para adicionar novos tipos de dispositivos

    1. Editar o arquivo industry.conf adicionando o novo tipo de local
    2. Adicionar , na classe generalista (uaDevice), uma constante com o nome que foi usado no arquivo conf
    3. Implemetar a classe do novo tipo  (init,create_type)
    4. Mapear a constante com a classe em factoryXXX
    """

    MAP_TYPE = {
        uaDevice.RASPBERRY:         uaRaspBerry ,
        uaDevice.ROBOT:             uaRobot ,
        uaDevice.VISION:            uaVision ,
        uaDevice.COVEYOR:           uaCoveyor ,
        uaDevice.MILL:              uaMill ,
        uaDevice.LATHE:             uaLathe ,
        uaDevice.BAR_CODE_READER:   uaBarCodeReader ,
        uaDevice.DEVICE:            uaDevice 
    }

    @staticmethod
    def get_obj_class(type):
        """
        Retorna a class respectiva do tipo
        """

        obj_class = FactoryDevice.MAP_TYPE.get(type, None)

        if obj_class is  None:
            logger.warn("Classe para o tipo {} não mapeado".format(type))

        return obj_class


    @staticmethod
    def get_list_types():
        """
        Retorna a lista de tipos de dispositos
        TODO: Aproveitar os keys do map porem reordenar
        """

        #list_types = list(FactoryDevice.MAP_TYPE.keys())

        list_types = [  uaDevice.DEVICE,
                        uaDevice.RASPBERRY,
                        uaDevice.ROBOT ,
                        uaDevice.VISION ,
                        uaDevice.COVEYOR ,
                        uaDevice.MILL ,
                        uaDevice.LATHE ,
                        uaDevice.BAR_CODE_READER]
         

        return list_types


    @staticmethod
    def create(idx,name,type):
        """
        Cria um dispositivo do tipo <type> com o nome <name>
        """

        obj_class = FactoryDevice.get_obj_class(type)
    
        if obj_class is  None:
            logger.warn("Não foi possível criar o dispositivo do tipo {}".format(type))

        return obj_class(idx,name)


    @staticmethod
    def get_list_objects(type):
        """
        Retorna a lista de objetos a serem criados
        """

        return FactoryDevice.get_config(type).OBJECTS

    @staticmethod
    def get_config(type):
        """
        Retorna a configuração respectiva do tipo
        """

        return FactoryDevice.get_obj_class(type).CONFIG