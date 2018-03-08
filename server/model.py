from opcua import ua
from uatdevice import uaTDevice
from uatcell import uaTCell
from uatplace import uaTPlace
from factory import Factory
from log import logger

class uaModel(object):

    @staticmethod
    def create(server,idx):
        """
        Cria o tipo de dispositivos e seus respectivos objetos no servidor opc-ua
        """

        types = [uaTDevice,uaTCell,uaTPlace]

        for t in types:
            uaModel.__create_type(server,idx,t)


    @staticmethod
    def __create_type(server,idx,type):
        """
        Cria o tipo de objeto e seus respectivos objetos no servidor OPC-UA
        """

        factory =  Factory(type) 


        # node de objetos no opcua
        objects = server.get_objects_node()
        uatypes = server.get_node(ua.ObjectIds.BaseObjectType)
        types   = factory.get_list_types()


        logger.info("Criando os tipos: {}".format(types))

        for t in types:

            # cria no servidor opc o tipo de objeto
            ua_obj_type = factory.create_ua_type(uatypes,idx,t) 
            
            # lista de objetos a serem criados
            ua_obj_list = factory.get_list_objects(t)

            if ua_obj_type is not None and ua_obj_list is not None:

                # cria no servidor opc os objetos
                for obj in ua_obj_list:
                    objects.add_object(idx, obj , ua_obj_type.nodeid)

            else:
                logger.error("Parametros '{}' incorretos para criação do tipo".format(t))
