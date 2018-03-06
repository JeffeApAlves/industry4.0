#!/usr/bin/env python

"""

@file    uaraspberry.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Funções diversas
"""

import socket
import fcntl
import struct
import netifaces as ni

def get_ip_address(ifname):
    """
    Retorna o IP do computador
    Wifi:   ifname = wlan0
    Cabo:   ifname = eth0
    """

    ni.ifaddresses(ifname)
    ip = ni.ifaddresses(ifname)[ni.AF_INET][0]['addr']

    return ip
