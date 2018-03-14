#!/usr/bin/env python

"""

@file    uatrash.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para locias do tipo trash

"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


from places.uaplace import uaPlace
from places.uatplace import uaTPlace
from places.uattrash import uaTTrash

class uaTrash(uaPlace):

    @staticmethod
    def create(parent,idx,handle=None):

        dtype = uaPlace.create(parent,idx)

        return  uaTTrash.create(dtype,idx,handle)
