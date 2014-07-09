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


class report_datos_identificacion_abreviado(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_datos_identificacion_abreviado, self).__init__(cr, uid, name, context)
        
        self.company = None
        self.info_ejercicio_actual = None
        self.info_ejercicio_anterior = None
        self.localcontext.update(
                                 {
                                  'time': time,
                                  'loadCompanyInfo':self._load_info_company,
                                  'getCompany':self._get_company,
                                  'getProvincia':self._get_provincia,    
                                  'getFormaJuridica':self._get_forma_juridica,  
                                  'loadInfoEjercicioActual': self._load_info_ejercicio_actual,
                                  'loadInfoEjercicioAnterior': self._load_info_ejercicio_anterior,
                                  'getEjercicioActual': self._get_info_ejercicio_actual,  
                                  'getEjercicioAnterior': self._get_info_ejercicio_anterior,
                                  'getAno': self._get_ano,
                                  'getMes': self._get_mes,
                                  'getDia': self._get_dia,
                                  'checkUnidades': self._check_unidades,
                                  })
        
    def _load_info_company(self):
        company_obj = self.pool.get('res.company').browse(self.cr, self.uid, 1)
        self.company = company_obj

    def _get_company(self):
        return self.company
    
    def _get_provincia(self, state_id):
        state_obj = self.pool.get('res.country.state').browse(self.cr, self.uid, state_id.id)
        
        if (state_obj != None):
            return state_obj.name
        else:
            return ''
        
    def _get_forma_juridica(self,tipo):
        if(tipo == 'sa'):
            if (self.company.forma_juridica == 'sa'):
                return 'X'
            else:
                return ''
        if(tipo == 'sl'):
            if (self.company.forma_juridica == 'sl'):
                return 'X'
            else:
                return '' 
        if(tipo == 'otra'):
            return self.company.forma_juridica_otras
        
    def _load_info_ejercicio_actual(self, ejercicio_id):
        self.info_ejercicio_actual = self.pool.get('res.company.datos.generales.identificacion').browse(self.cr, self.uid, int(ejercicio_id))
        
    def _get_info_ejercicio_actual(self):
        return self.info_ejercicio_actual
        
    def _load_info_ejercicio_anterior(self, ejercicio_id, comparar=False):
        print "comprar ",comparar
        if (comparar == True):
            ejercicio_obj = self.pool.get('res.company.datos.generales.identificacion').browse(self.cr, self.uid, int(ejercicio_id))
            
            if (ejercicio_obj != None):
                anterior = int(ejercicio_obj.nombre_ejercicio)-1
                
                ejercicio_anterior_id = self.pool.get('res.company.datos.generales.identificacion').search(self.cr, self.uid, 
                [('nombre_ejercicio', '=', str(anterior))])
                
                if (ejercicio_anterior_id != None):
                    result = self.pool.get('res.company.datos.generales.identificacion').browse(self.cr, self.uid, ejercicio_anterior_id)
                    self.info_ejercicio_anterior = result[0]

    def _get_info_ejercicio_anterior(self):
        return self.info_ejercicio_anterior
    
    def _get_ano(self, fecha):
        return fecha[:4]
        
    def _get_mes(self, fecha):
        return fecha[5:7]
            
    def _get_dia(self, fecha):
        return fecha[8:]
    
    def _check_unidades(self, unidad, selected):
        if (unidad == selected):
            return 'X'
        else:
            return ''


report_sxw.report_sxw('report.report.datos.generales.identificacion.abreviado', 'res.company.datos.generales.identificacion',
      'l10n_es_identificacion_empresa/report/identificacion_abreviado.odt', parser=report_datos_identificacion_abreviado, header=False)