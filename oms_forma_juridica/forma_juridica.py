# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015
#        Openmindsystems. (http://www.openmindsystems.com.es) All Rights Reserved
#
##############################################################################
from osv import osv, fields

class forma_juridica(osv.osv):
    _name = "forma.juridica"
    _description = "Forma juridica"
    _columns = {
        'name': fields.char('Nombre'),      
    }
    
forma_juridica()