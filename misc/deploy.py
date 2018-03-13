#!/usr/bin/env python

"""

@file    deploy.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Baseado no ip existem no arquivo .conf copia os arquivos para cada host


TODO verificar se existe a necessidade fazer deploy de todos os diretorios
"""

import os
import sys
import getpass
import subprocess
import shlex
from distutils import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

# inclui os subdiretórios
#dirs = [ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) ]

#for dir in dirs:
#    sys.path.insert(0, "./{}".format(dir))


from devices.uatdevice import uaTDevice
from opc.factory import Factory
from config.config import DEVICE_CONFIG,OPCUA_SERVER_CONFIG


def deploy_files(devices,servers):
    """
    Copia  os arquivos para todos os hosts o destino é definido no arquivo objects.conf
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

    all_objects = Factory.get_name_objects()

    for entity in all_objects:

        config = Factory.get_config(entity=entity)
        
        for ip_host in config.DEPLOY:

            # copia os arquvivos do home do projeto
            cl =  "rsync -av --include='*.conf' --include='*.sh' --include='*.py' --include='*.txt' --exclude='*' --prune-empty-dirs {}/ {}@{}:{}".format(config.WORKDIR,getpass.getuser(),ip_host,config.HOMEDIR)
            args = shlex.split(cl)
            subprocess.call(args)

            # copia os diretorios e seu conteudo  de forma recursiva
            cl = "rsync -avz --exclude='*pyc' --prune-empty-dirs {} {}@{}:{}".format(" ".join(directories),getpass.getuser(),ip_host,config.HOMEDIR)
            args = shlex.split(cl)
            subprocess.call(args)



def deploy_servers():
    """
    Deploy os diretorios e o conteudo para o servidor opcua
    """

    directories = [ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) ]

    for ip_host in OPCUA_SERVER_CONFIG.DEPLOY:
        
        # copia os arquvivos do home do projeto
        cl =  "rsync -av --include='*.conf' --include='*.sh' --include='*.py' --exclude='*' --prune-empty-dirs {}/ {}@{}:{}".format(OPCUA_SERVER_CONFIG.WORKDIR,getpass.getuser(),ip_host,OPCUA_SERVER_CONFIG.HOMEDIR)
        args = shlex.split(cl)
        subprocess.call(args)

        # copia os diretorios e seu conteudo  de forma recursiva
        cl = "rsync -avz --exclude='*.pyc' --prune-empty-dirs {} {}@{}:{}".format(" ".join(directories),getpass.getuser(),ip_host,OPCUA_SERVER_CONFIG.HOMEDIR)
        args = shlex.split(cl)
        subprocess.call(args)
