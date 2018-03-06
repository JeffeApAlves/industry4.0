#!/usr/bin/env python

"""

@file    uademo.py
@author  Jefferson Alves
@date    2018-03-02
@version 0.1

Entidade de teste

"""

from opcua import uamethod
from uadevice import uaDevice
from config import DEVICE_CONFIG


class uaDemo(uaDevice):

    @staticmethod
    def get_list_objects():
        return ["DEMO1","DEMO2"]

    @staticmethod
    def create_type(server,idx):

        types   = server.get_node(ua.ObjectIds.BaseObjectType)
        obj_type= types.add_object_type(idx, RASPBERRY_CONFIG.OBJECT_TYPE)

        super.create_type(server,idx,obj_type)
        
        objects = server.get_objects_node()
        myobj   = objects.add_object(idx, "MyObject")
        mywritablevar   = myobj.add_variable(idx, "MyWritableVariable", 6.7)
        mywritablevar.set_writable()    # Set MyVariable to be writable by clients
        myvar       = myobj.add_variable(idx,   "MyVariable", 6.7)
        myarrayvar  = myobj.add_variable(idx,   "MyVarArray", [6.7, 7.9])
        myprop      = myobj.add_property(idx,   "MyProperty", "I am a property")
        mymethod    = myobj.add_method(idx,     "MyMethod", uaDemo.multiply, [ua.VariantType.Double, ua.VariantType.Int64], [ua.VariantType.Double])


    @uamethod
    @staticmethod
    def multiply(parent, x, y):
        print("multiply method call with parameters: ", x, y)
        return x * y
