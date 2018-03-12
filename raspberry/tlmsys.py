#!/usr/bin/env python

"""

@file    project.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Carrega as configurações do arquivo

"""


import os
import sys
import logging
import psutil
import shlex
from subprocess import PIPE, Popen


class TlmSyS (object):
    """
    Realiza a telemetria da raspberry
    """

    #sense = SenseHat()

    def __init__(self):

        self.logger = logging.getLogger(__name__)


    @property
    def temperature(self):
        """
        get cpu temperature using vcgencmd
        """

        try:
            process = Popen(shlex.split("sudo vcgencmd measure_temp"), stdout=PIPE)
            output, _error = process.communicate()
            output = output.decode("utf-8") 
            val = output[output.index("=") + 1:output.rindex("'")]

        except:
            self.logger.error("Não foi possível efetuar a leitura da temperatura")


        return float(val)
        
    @property
    def cpu(self):
        return psutil.cpu_percent(interval=5)

    @property
    def memory(self):
        return psutil.virtual_memory().percent

    @property
    def harddisk(self):
        disk = psutil.disk_usage('/')
        free = round(disk.free/1024.0/1024.0/1024.0,1)
        total = round(disk.total/1024.0/1024.0/1024.0,1)
        return total,free

    @property
    def pressure(self):
        return 0.0
	    #return self.sense.pressure

    @property
    def humidity(self):
        return 0.0
	    #return self.sense.humidity
