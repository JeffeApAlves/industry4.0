#!/usr/bin/env python

"""

@file    manage.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entrada do CL

"""

import sys
import os
import locale
import click
import time
import asyncio
from distutils import *

import logging
import logging.config


logging.config.fileConfig("./logging.conf")
        
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "."))

from client.uaclient import uaClient
from opc.uaobject import uaObject
from opc.factory import Factory
from server.uaserver import uaServer
from devices.uatdevice import uaTDevice
from misc.deploy import deploy_files
from config.config import CONFIG 

logger = logging.getLogger(__name__)

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        code.interact(local=dict(globals(), **locals()))

locale.setlocale(locale.LC_ALL, '')


event_loop = asyncio.get_event_loop()

@click.group()
@click.option('-v','--verbose', type =click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), default=None)
@click.pass_context
def cli(ctx,verbose):

    ctx.obj['VERBOSE'] = verbose

    if verbose is not None:
        logging.basicConfig(level=verbose)


@cli.command()

@click.option('--devices/--no-devices',default = True,
                help="Atualiza os dispositivos")

@click.option('--servers/--no-servers',default = True,
                help="Atualiza os servidores")

def deploy(devices,servers):
    """
    Faz deploy de todos os arquivos do projeto para o seu respectivo host (server ou devices)
    """
    deploy_files(devices,servers)

@cli.command()
@click.option('--idx', type = click.INT, default = 1,
                help="Index do namespace")

@click.option('--name', type = click.STRING, default = None,
                help="Nome do dispositvo")

@click.option('--prop', type = (click.STRING,click.FLOAT), default = None,
                help="Propriedade a ser acessada")

def write(name,prop,idx):

    # Conecta no servidor opc
    uaClient.connect()

    name_var,value = prop

   # cria um objeto e le o valor
    obj = uaObject(None,idx,name)
    var = uaObject(obj.node,idx,name_var)
 
    var.value = value

    uaClient.disconnect()


@cli.command()
@click.option('--idx', type = click.INT, default = 1,
                help="Index do namespace")

@click.option('--name', type = click.STRING, default = None,
                help="Nome do dispositvo")

@click.option('--prop', type = click.STRING, default = None,
                help="Propriedade a ser acessada")

def read(name,prop,idx):
    """
    Acessando uma variável através de path
    """

    uaClient.connect()

    # cria um objeto e le o valor
    obj = uaObject(None,idx,name)
    var = uaObject(obj.node,idx,prop)
    
    # imprime a variavel
    click.echo("{}->{} = {}".format(name,prop,var.value))

    uaClient.disconnect()


@cli.command()
@click.option('--type', type = click.Choice(CONFIG.get_name_devices_choice()) , default = None,
                help="Tipo do dispositivo a ser criado")

@click.option('--name', type = click.STRING, default = None,
                help="Nome do dispositvo")

@click.option('--idx', type = click.INT, default = 1,
                help="Index do namespace")

def device(type,idx,name):
    """
    Inicia a execução de um dispositivo
    """

    try:
        
        uaClient.connect()
        
        class_type = CONFIG.choice_to_classe(type)

        Factory.create_device(idx,name,class_type,event_loop)

    except IOError as e:
        print(e)
        logger.error("Erro ao tentar criar se conectar no servidor opcua !")
        uaClient.disconnect()

    click.echo("Pressione [Ctrl+c] para interronper a execução\n")

    try:
        event_loop.run_forever()
    except (asyncio.CancelledError , KeyboardInterrupt ):
        pass
    finally:
        event_loop.close()

    uaClient.disconnect()


@cli.command()
@click.option("-u","--url",default = None,
                help="URL do OPC UA server, default é definido via arquivo de configuração")
@click.option("-x","--xml",default = None,
                help="Popula o address space com um modelo no formato XML")
@click.option("--name",
                help="define server name")
@click.option('--clock/--no-clock',default = False,
                help="Disable clock, to avoid seeing many write if debugging an application")
@click.option('--shell/--no-shell',default = False,
                help="Inicia python shell instead of randomly changing node values")
@click.option("--certificate",
                help="set server certificate")
@click.option("--private-key",
                help="set server private key")
def server(url,xml,clock,shell,certificate,private_key,name):
    """
    Inicia o servidor OPC-UA baseado nas configurações contida em um arquivo .conf indicado em CONF.SETUP_CONF
    """

    try:
            
        logger.info("Configurando o servidor")

        uaServer.config(    url             = url,
                            name            = name,
                            xml             = xml,
                            certificate     = certificate,
                            private_key     = private_key, 
                            disable_clock   = clock)

        uaServer.start()

        logger.info("Servidor iniciado com sucesso")
    except IOError as e:
        print(e)
        logger.error("Problemas na inicialização do servidor")

    try:
        if shell:
            embed()
        else:

            click.echo("Pressione [Ctrl+c] para interronper a execução\n")

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass

    finally:
        uaServer.stop()

    sys.exit(0)

if __name__ == '__main__':
    cli(obj={})
