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


class report_pg_completo_telematic(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_pg_completo_telematic, self).__init__(cr, uid, name, context)

        #En cada página se tienen que mostrar un rango de cuentas determinadas
        self._behave_first = ['A','40100','40110','40120','40130','40200','40300','40400','40410','40420','40430','40440','40500','40510','40520','40600','40610','40620','40630','40700','40710','40720','40730','40740','40750','40800','40900','41000','41100','41110','41120','41130']
        self._behave_second = ['41200','41300','49100','41400','41410','41411','41412','41420','41421','41422','41430','41500','41510','41520','41530','41600','41610','41620','41700','41800','41810','41820','42100','42110','42120','42130','49200','49300','41900','49400']
        self._behave_third = ['B','42000','49500']
        
        #En estos arrays guardaremos las líneas correspondientes a cada página 
        self._array_first_pag = []
        self._array_second_pag = []
        self._array_third_pag = []
        
        self.localcontext.update(
                                 {
                                  'time': time,
                                  'nifCompany':self._getNifCompany,
                                  'denominacionSocial':self._getDenominacionSocial,
                                  'putInArrays': self._put_in_arrays,
                                  'getFirstArray': self._getFirstArray,
                                  'getSecondArray': self._getSecondArray,
                                  'getThirdArray': self._getThirdArray,                                  
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
            if (str(line_obj.code) in self._behave_first):
                self._array_first_pag.append(line_obj)
            if (str(line_obj.code) in self._behave_second):
                self._array_second_pag.append(line_obj)
            if (str(line_obj.code) in self._behave_third):
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
                

report_sxw.report_sxw('report.report.account.pg.completo.reporting.spanish', 'account.balance.reporting',
      'addons/l10n_es_account_balance_report_telematic/report/pg_completo_telematic_report.odt', parser=report_pg_completo_telematic, header=False)