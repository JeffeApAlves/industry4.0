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
import logging
import time
from distutils import *

# inclui os subdiretórios
dirs = [ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) ]

for dir in dirs:
    sys.path.insert(0, "./{}".format(dir))
    
from uaclient import uaClient
from uaobject import uaObject
from factorydevice import FactoryDevice
from uaserver import uaServer
from deploy import deploy_files

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        code.interact(local=dict(globals(), **locals()))

locale.setlocale(locale.LC_ALL, '')

@click.group()
@click.option('-v','--verbose', type =click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), default='WARNING')
@click.pass_context
def cli(ctx,verbose):

    ctx.obj['VERBOSE'] = verbose

    # logging.basicConfig(level=logging.WARN)
    #logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, verbose))


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
@click.option('--idx', type = click.INT, default = 1)
@click.option('--obj', type = click.STRING, default = None)
@click.option('--var', type = (click.STRING,click.FLOAT) , default = None)
def write(obj,var,idx):

    # Conecta no servidor opc
    uaClient.connect()

    name_var,value = var

    uaObject(None,idx,obj).set_value(name_var,value)

    uaClient.disconnect()


@cli.command()
@click.option('--idx', type = click.INT, default = 1)
@click.option('--obj', type = click.STRING, default = None)
@click.option('--var', type = click.STRING, default = None)
def read(obj,var,idx):
    """
    Acessando uma variavel atravé de path
    """

    # Conecta no servidor opc
    uaClient.connect()

    # cria um objeto e le o valor
    value = uaObject(None,idx,obj).get_value(var)
    
    # imprime a variavel
    click.echo("{}->{} = {}".format(obj,var,value))

    uaClient.disconnect()

@cli.command()
@click.option('--type', type = click.Choice(FactoryDevice.get_list_types()) , default = None)
@click.option('--name', type = click.STRING, default = None)
@click.option('--idx', type = click.INT, default = 1)
def device(type,idx,name):
    """
    Inicia a execução de um dispositivo
    """
    
    uaClient.connect()

    FactoryDevice.create(idx,name,type)

    click.echo("Running: Idx {} Device {} Type {}".format(idx,name,type))    
    
    input("Press Ctrl+c to stop\n")

    uaClient.disconnect()


@cli.command()
@click.option("-u","--url",default = None,
                help="URL do OPC UA server, default é definido via arquivo de configuração")
@click.option("-x","--xml",default = None,
                help="Populate address space with nodes defined in XML")
@click.option("--name",
                help="set server name")
@click.option('--clock/--no-clock',default = False,
                help="Disable clock, to avoid seeing many write if debugging an application")
@click.option('--shell/--no-shell',default = False,
                help="Start python shell instead of randomly changing node values")
@click.option("--certificate",
                help="set server certificate")
@click.option("--private-key",
                help="set server private key")
def server(url,xml,clock,shell,certificate,private_key,name):
    """
    Roda o servidor OPC-UA.
    """

    uaServer.start_uaserver(    url             = url,
                                name            = name,
                                xml             = xml,
                                certificate     = certificate,
                                private_key     = private_key, 
                                disable_clock   = clock)

    try:
        if shell:
            embed()
        else:
            input("Press Ctrl+c to stop\n")
    finally:
        server.stop()

    sys.exit(0)

if __name__ == '__main__':
    cli(obj={})
