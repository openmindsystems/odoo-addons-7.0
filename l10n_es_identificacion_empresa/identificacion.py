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

from osv import osv, fields
from datetime import datetime

#Añadimos los campos de identificación al objeto res.company
class res_company(osv.osv):
    _inherit = 'res.company'
    _columns = {
            'actividad_empresa': fields.char('Actividad'),
            'codigo_cnae': fields.char('Código CNAE'), 
            'forma_juridica': fields.selection([('sa','S.A.'), ('sl','S.L.')], 'Forma jurídica', required=False), 
            'forma_juridica_otras': fields.char('Otra forma jurídica'),  
            'dominante_directa': fields.char('Sociedad dominante directa'),
            'dominante_ultima_grupo': fields.char('Sociedad dominante última del grupo'),
            'nif_directa': fields.char('NIF sociedad dominante directa'),
            'nif_ultima_grupo': fields.char('NIF sociedad dominante última del grupo'),
    } 
  

res_company()

#Contendrá la información de cada ejercicio para los datos generales de identificación
class res_company_datos_generales_identificacion(osv.osv):
    _name = 'res.company.datos.generales.identificacion'
    _columns = {
            'active': fields.boolean('Active'),
            'nombre_ejercicio': fields.char('Ejercicio'),
            'asalariado_fijo': fields.char('Asalariado fijo'),
            'asalariado_no_fijo': fields.char('Asalariado no fijo'),
            'asalariado_discapacidad': fields.char('Asalariado con discapacidad'),
            'asalariado_fijo_hombre': fields.char('Asalariado fijo hombre'),
            'asalariado_fijo_mujer': fields.char('Asalariado fijo mujer'),
            'asalariado_no_fijo_hombre': fields.char('Asalariado no fijo hombre'),
            'asalariado_no_fijo_mujer': fields.char('Asalariado no fijo mujer'),            
            'fecha_inicio': fields.date('Fecha de inicio'),
            'fecha_cierre': fields.date('Fecha de cierre'), 
            'paginas_deposito': fields.integer('Páginas presentadas al deposito'),
            'causa_no_figurar': fields.char('Causa de no figurar consignadas cifras'),  
    }
    
    _defaults = {
        'active' : True,
        'nombre_ejercicio': datetime.now().strftime("%Y"),
    }    