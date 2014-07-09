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


class report_balance_completo_telematic(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_balance_completo_telematic, self).__init__(cr, uid, name, context)
        #En cada página se tienen que mostrar un rango de cuentas determinadas
        self._behave_first_one = [11000,11100,11110,11120,11130,11140,11150,11160,11180,11190,11170,11200,11210,11220,11230,11300,11310,11320,11400,11410,11420,11430,11440,11450,11460,11500,11510,11520,11530,11540,11550,11560]
        self._behave_first_two = [11600,11700,12000,12100,12200,12210,12220,12230,12231,12232,12240,12241,12242,12250,12260,12300,12310,12311,12312,12320,12330,12340,12350,12360,12370,12400,12410,12420,12430,12440,12450,12460]
        self._behave_first_three = [12500,12510,12520,12530,12540,12550,12560,12600,12700,12710,12720,10000]
        self._behave_second = [20000,21000,21100,21110,21120,21200,21300,21310,21320,21330,21400,21500,21510,21520,21600,21700,21800,21900,22000,22100,22200,22300,22400,22500,23000,31000,31100,31110,31120,31130,31140,31200,31210,31220]
        self._behave_third = [31230,31240,31250,31300,31400,31500,31600,31700,32000,32100,32200,32210,32220,32300,32310,32320,32330,32340,32350,32400,32500,32510,32511,32512,32520,32530,32540,32550,32560,32570,32600,32700,30000]
        
        #En estos arrays guardaremos las líneas correspondientes a cada página 
        self._array_first_one_pag = []
        self._array_first_two_pag = []
        self._array_first_three_pag = []
        self._array_second_pag = []
        self._array_third_pag = []
        self.localcontext.update(
                                 {
                                  'time': time,
                                  'putInArrays': self._put_in_arrays,
                                  'getFirstOneArray': self._getFirstOneArray,
                                  'getFirstTwoArray': self._getFirstTwoArray,
                                  'getFirstThreeArray': self._getFirstThreeArray,                                                                    
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
            if (int(line_obj.code) in self._behave_first_one):
                self._array_first_one_pag.append(line_obj)
            if (int(line_obj.code) in self._behave_first_two):
                self._array_first_two_pag.append(line_obj)
            if (int(line_obj.code) in self._behave_first_three):
                self._array_first_three_pag.append(line_obj)
            if (int(line_obj.code) in self._behave_second):
                self._array_second_pag.append(line_obj)
            if (int(line_obj.code) in self._behave_third):
                self._array_third_pag.append(line_obj)

    #Recuperamos las líneas de la primera página (1)         
    def _getFirstOneArray(self):
        return self._array_first_one_pag

    #Recuperamos las líneas de la primera página (2)      
    def _getFirstTwoArray(self):
        return self._array_first_two_pag
    
    #Recuperamos las líneas de la primera página (3)      
    def _getFirstThreeArray(self):
        return self._array_first_three_pag

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
                

report_sxw.report_sxw('report.report.account.balance.completo.reporting.spanish', 'account.balance.reporting',
      'addons/l10n_es_account_balance_report_telematic/report/balance_completo_telematic_report.odt', parser=report_balance_completo_telematic, header=False)