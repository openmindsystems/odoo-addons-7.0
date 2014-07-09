# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014
#        Openmindsystems. (http://www.openmindsystems.com.es) All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from report import report_sxw


class report_pg_abreviado_telematic(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_pg_abreviado_telematic, self).__init__(cr, uid, name, context)
        self.localcontext.update(
                                 {
                                  'time': time,
                                  'nifCompany':self._getNifCompany,
                                  'denominacionSocial':self._getDenominacionSocial,
                                  })
       
    #Recuperamos el NIF de la empresa
    def _getNifCompany(self):
        partner_obj = self.pool.get('res.partner').browse(self.cr, self.uid, 1) 
        vat = partner_obj.vat
        
        return vat
    
    #Recuperamos la denominación social de la empresa
    def _getDenominacionSocial(self):
        company_obj = self.pool.get('res.company').browse(self.cr, self.uid, 1) 
        name = company_obj.name
        
        return name
                

report_sxw.report_sxw('report.report.account.pg.abreviado.reporting.spanish', 'account.balance.reporting',
      'addons/l10n_es_account_balance_report_telematic/report/pg_abreviado_telematic_report.odt', parser=report_pg_abreviado_telematic, header=False)