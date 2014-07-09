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


class report_balance_abreviado_telematic(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_balance_abreviado_telematic, self).__init__(cr, uid, name, context)
        #En cada página se tienen que mostrar un rango de cuentas determinadas
        self._behave_first = [11000,11100,11200,11300,11400,11500,11600,11700,12000,12100,12200,12300,12380,12381,12382,12370,12390,12400,12500,12600,12700,10000]
        self._behave_second = [20000,21000,21100,21110,21120,21200,21300,21400,21500,21600,21700,21800,21900,22000,23000,31000,31100,31200,31220,31230,31290,31300,31400,31500,31600,31700]
        self._behave_third = [32000,32100,32200,32300,32320,32330,32390,32400,32500,32580,32581,32582,32590,32600,32700,30000]
        
        #En estos arrays guardaremos las líneas correspondientes a cada página 
        self._array_first_pag = []
        self._array_second_pag = []
        self._array_third_pag = []
        self.localcontext.update(
                                 {
                                  'time': time,
                                  'putInArrays': self._put_in_arrays,
                                  'getFirstArray': self._getFirstArray,
                                  'getSecondArray': self._getSecondArray,
                                  'getThirdArray': self._getThirdArray,
                                  'nifCompany':self._getNifCompany,
                                  'denominacionSocial':self._getDenominacionSocial,
                                  })
    
    #Esta función pondrá las líneas según a la página que le corresponda
    def _put_in_arrays(self, report):
        #browse_record(account.balance.reporting, 3)
        
        #Recuperamos las líneas del report
        lines_ids = self.pool.get('account.balance.reporting.line').search(self.cr, self.uid, 
            [('report_id', '=', report.id)])
 
        #Recuperamos los objetos de estas líneas
        lines_objs = self.pool.get('account.balance.reporting.line').browse(self.cr, self.uid, lines_ids) 
        
        #Por cada línea, miramos que código tiene para poner el objeto en un array u otro
        for line_obj in lines_objs:
            if (int(line_obj.code) in self._behave_first):
                self._array_first_pag.append(line_obj)
            if (int(line_obj.code) in self._behave_second):
                self._array_second_pag.append(line_obj)
            if (int(line_obj.code) in self._behave_third):
                self._array_third_pag.append(line_obj)

    #Recuperamos las líneas de la primera página          
    def _getFirstArray(self):
        return self._array_first_pag

    #Recuperamos las líneas de la segunda página   
    def _getSecondArray(self):
        return self._array_second_pag
    
    #Recuperamos las líneas de la tercera página   
    def _getThirdArray(self):
        return self._array_third_pag
    
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
                

report_sxw.report_sxw('report.report.account.balance.abreviado.reporting.spanish', 'account.balance.reporting',
      'addons/l10n_es_account_balance_report_telematic/report/balance_abreviado_telematic_report.odt', parser=report_balance_abreviado_telematic, header=False)