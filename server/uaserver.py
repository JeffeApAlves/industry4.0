from opcua import ua
from opcua import Client
from opcua import Server
from opcua import Node

from config import OPCUA_SERVER_CONFIG
from factorydevice import FactoryDevice
from factorycell import FactoryCell
from factoryplace import FactoryPlace
from log import logger

class uaServer(object):

    @staticmethod
    def start_uaserver(name , url = None , xml = None,certificate = None,private_key = None, disable_clock = False):
        """
        Inicializa o servidor OPC-UA
        """

        if url is None:
            url = OPCUA_SERVER_CONFIG.URL

        if name is None:
            name = OPCUA_SERVER_CONFIG.NAME

        server = Server()

        server.set_endpoint(url)

        server.set_server_name(name)
        
        server.disable_clock(disable_clock)

        idx = server.register_namespace(OPCUA_SERVER_CONFIG.URI)

        if certificate is not None:
            server.load_certificate(certificate)
        
        if private_key is not None:
            server.load_private_key(private_key)
        
        if xml is not None:
            server.import_xml(xml)

        uaServer.__create_model(server,idx)

        # exporta o modelo para um xml
        server.export_xml_by_ns("/".join([OPCUA_SERVER_CONFIG.HOMEDIR,"server","model_ns.xml"])   ,[OPCUA_SERVER_CONFIG.URI])

        server.start()

        logger.info("Servidor iniciado com sucesso {}".format(url))

    @staticmethod
    def __create_model(server,idx):
        """
        Cria o tipo de dispositivos e seus respectivos objetos no servidor opc-ua
        """

        # Cria todos os tipos de dispositivos
        uaServer.create(server,idx,FactoryDevice)

        # Cria todos os tipos de locais
        uaServer.create(server,idx,FactoryPlace)

        # Cria todos os tipos de celulas
        uaServer.create(server,idx,FactoryCell)

    @staticmethod
    def create(server,idx,factory):
        """
        Cria o tipo de objeto e seus respectivos objetos no servidor OPC-UA
        """
           
        # node de objetos no opcua
        objects = server.get_objects_node()
        types   = factory.get_list_types()

        for t in types:

            obj_class = factory.get_obj_class(t)

            # cria no servidor opc o tipo
            ua_obj_type = obj_class.create_type(server,idx)
            
            # lista de objetos a serem criados
            ua_obj_list = factory.get_list_objects(t)
    
            if ua_obj_type is not None and ua_obj_list is not None:

                # cria no servidor opc os objetos
                for obj in ua_obj_list:
                    objects.add_object(idx, obj , ua_obj_type.nodeid)

                logger.info("Criado o tipo {} e {} objetos no servidor OPC-UA".format(t,len(ua_obj_list)))

            else:

                logger.error("Não foi possivel criar o tipo  {}".format(t))

