#!/usr/bin/env python

"""

@file    uaplace.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Classe de abstrata para os locais

"""

from opcua import ua
from uaobject import uaObject
from config import PLACE_CONFIG

class uaPlace(uaObject):

    # tipos de lugares
    PLACE           = "place"
    BUFFER          = "buffer"
    TRASH           = "trash"


    #propriedades
    _P_ID           = "Id"
    _P_MAX          = "Max"
    _P_FREE         = "Free"

    CONFIG          = PLACE_CONFIG(PLACE) 

    @staticmethod
    def create_type(server,idx,type=None):

        types   = server.get_node(ua.ObjectIds.BaseObjectType)

        try:
            obj_type = types.get_child(":".join([str(idx), uaPlace.CONFIG.OBJECT_TYPE]))
        except:
            
            obj_type = types.add_object_type(idx, uaPlace.CONFIG.OBJECT_TYPE)

            obj_type.add_property(idx,  uaPlace._P_ID,    999).set_writable()
            obj_type.add_property(idx,  uaPlace._P_MAX,   100).set_writable()
            obj_type.add_property(idx,  uaPlace._P_FREE,  100).set_writable()


        if type is not None:

            try:
                child = obj_type .get_child(":".join([str(idx), type ]))
            except:
                child = obj_type.add_object_type(idx, type)

        else:
            child = obj_type
    
        return  child
