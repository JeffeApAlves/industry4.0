#!/usr/bin/env python

"""

@file    uacell.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para as celulas 

"""

from opcua import ua
from uaobject import uaObject
from config import CELL_CONFIG

class uaCell(uaObject):

    # tipos de celulas
    CELL            = "cell"
    QUALITY_CONTROL = "quality-control"
    OFFICE          = "office"
    STORAGE         = "storage"
    ASSEMBLY        = "assembly"
    MACHINING       = "machining"

    CONFIG          = CELL_CONFIG(CELL) 

    @staticmethod
    def create_type(server,idx,type=None):

        types   = server.get_node(ua.ObjectIds.BaseObjectType)

        try:
            obj_type = types.get_child(":".join([str(idx), uaCell.CONFIG.OBJECT_TYPE]))
        except:
            
            obj_type = types.add_object_type(idx, uaCell.CONFIG.OBJECT_TYPE)

        if type is not None:

            try:
                child = obj_type .get_child(":".join([str(idx), type ]))
            except:
                child = obj_type.add_object_type(idx, type)

        else:
            child = obj_type
    
        return  child
