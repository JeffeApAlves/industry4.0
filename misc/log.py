#!/usr/bin/env python

"""

@file    log.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Configuração do log

"""

import logging
import logging.config


logging.config.fileConfig('./startup/logging.conf')

# create logger
logger = logging.getLogger("industry-4.0")
