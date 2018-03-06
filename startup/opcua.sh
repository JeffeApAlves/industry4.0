#!/bin/bash

NAME="OPCUA-SERVER"
OPCUADIR=/home/opcua/opcua
USER=opcua
GROUP=opcua 
HOST=192.168.42.1
PORT=4840
PID_FILE=/tmp/opcua.pid
XML_MODEL="/home/opcua/model/model.xml"

ENVIROMENT=/home/jefferson/.virtualenvs/opcua

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $OPCUADIR
source $ENVIROMENT/bin/activate

python manage.py server
