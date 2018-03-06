#!/usr/bin/env python

"""

@file    workerdevice.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Thread para dispositivos
"""

import time
from threading import Thread
from log import logger


class WorkerDevice(Thread):


    def __init__(self,device,time =0):

        Thread.__init__(self)
        
        self.__device   = device
        self.__time     = time
        
        # inicia a thread
        self.start()


    def run(self):

        self.__device.start_task()
 
        while(True):

            try:
                self.__device.loop_task()

            except (KeyboardInterrupt):
                break

            except:
                logger.error("Problema na execução da thread do dispositivo {}".format(self.__device.display_name))

            if self.__time:
                time.sleep(self.__time)

        self._stop()
