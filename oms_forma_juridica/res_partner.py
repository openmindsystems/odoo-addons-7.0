# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015
#        Openmindsystems. (http://www.openmindsystems.com.es) All Rights Reserved
#
##############################################################################
from osv import osv, fields

    
class res_partner(osv.osv):
    _inherit = "res.partner"
    _columns = {
        'forma_juridica_id': fields.many2one('forma.juridica', 'Forma Juridica', ondelete='cascade', select=True),
    }    

res_partner()