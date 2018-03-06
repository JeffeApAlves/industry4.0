#!/usr/bin/env python

"""

@file    deploy.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Baseado no ip existem no arquivo .conf copia os arquivos para cada host

"""

import os
import getpass
import subprocess
import shlex
from distutils import *
from factorydevice import FactoryDevice
from config import DEVICE_CONFIG,OPCUA_SERVER_CONFIG

def deploy_files(devices,servers):
    """
    Copia  os arquivos para todos os hosts
    """

    if devices:
        deploy_servers()

    if servers:
        deploy_devices()
 
def deploy_devices():
    """
    Deploy os diretorios e o conteudo nos dispositivos
    """

    #TODO verificar se existe a necessidade fazer deploy de todos os diretorios
    directories = [ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) ]

    for type in FactoryDevice.get_list_types():

        config = FactoryDevice.get_config(type)
        
        for ip_host in config.DEPLOY:
            cl =  "rsync -rv --include='*.conf' --include='*.sh' --include='*.py' --exclude='*' --prune-empty-dirs {}/ {}@{}:{}".format(config.WORKDIR,getpass.getuser(),ip_host,config.HOMEDIR)
            args = shlex.split(cl)
            subprocess.call(args)

            cl = "rsync -avz --exclude='*pyc' --prune-empty-dirs {} {}@{}:{}".format(" ".join(directories),getpass.getuser(),ip_host,config.HOMEDIR)
            args = shlex.split(cl)
            subprocess.call(args)


def deploy_servers():
    """
    Deploy os diretorios e o conteudo para o servidor opcua
    """

    #TODO verificar se existe a necessidade fazer deploy de todos os diretorios
    directories = [ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) ]


    for ip_host in OPCUA_SERVER_CONFIG.DEPLOY:
        
        cl =  "rsync -rv --include='*.conf' --include='*.sh' --include='*.py' --exclude='*' --prune-empty-dirs {}/ {}@{}:{}".format(OPCUA_SERVER_CONFIG.WORKDIR,getpass.getuser(),ip_host,OPCUA_SERVER_CONFIG.HOMEDIR)
        args = shlex.split(cl)
        subprocess.call(args)

        cl = "rsync -avz --exclude='*.pyc' --prune-empty-dirs {} {}@{}:{}".format(" ".join(directories),getpass.getuser(),ip_host,OPCUA_SERVER_CONFIG.HOMEDIR)
        args = shlex.split(cl)
        subprocess.call(args)
