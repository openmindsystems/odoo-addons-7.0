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

class identificacion_wizard(osv.osv_memory):
    
    def _get_selection(self, cr, uid, context=None):
        obj = self.pool.get('res.company.datos.generales.identificacion')
        ids = obj.search(cr, uid, [])
        res = obj.read(cr, uid, ids, ['nombre_ejercicio', 'id'], context)
        res = [(r['id'], r['nombre_ejercicio']) for r in res]
        
        return res

    _name = 'identificacion.wizard'
    _description = 'Identificacion Wizard'

    _columns = {
        'ejercicio': fields.selection(_get_selection,'Ejercicio base'),
        'compare': fields.boolean('Comparar con el ejercicio anterior'),
        'adopcion_conjunta': fields.boolean('Adopción conjunta'),  
    }
    _defaults = {
        'compare': False,
    }
    

    def create_report(self, cursor, uid, ids, context):
        #Recuperem les dades del filtre (wizard)
        res = self.read(cursor, uid, ids, ['ejercicio','compare','adopcion_conjunta'], context=context)
        #Posem les dades en un array
        res = res and res[0] or {}
        #Recuperem els camps desitjats
        ejercicio = res['ejercicio']
        compare = res['compare']
        adopcion_conjunta = res['adopcion_conjunta']

        if context is None:
            context = {}
        
        res['info'] = [ejercicio,compare,adopcion_conjunta]
        data = res
        datas = {
                     'ids': [],
                     'model': 'res.company.datos.generales.identificacion',
                     'form': data
        }
        return {'type': 'ir.actions.report.xml', 'report_name': 'report.datos.generales.identificacion.pyme', 'datas': datas}

identificacion_wizard()

class identificacion_abreviado_wizard(osv.osv_memory):
    
    def _get_selection(self, cr, uid, context=None):
        obj = self.pool.get('res.company.datos.generales.identificacion')
        ids = obj.search(cr, uid, [])
        res = obj.read(cr, uid, ids, ['nombre_ejercicio', 'id'], context)
        res = [(r['id'], r['nombre_ejercicio']) for r in res]
        
        return res

    _name = 'identificacion.abreviado.wizard'
    _description = 'Identificacion Abreviado Wizard'

    _columns = {
        'ejercicio': fields.selection(_get_selection,'Ejercicio base'),
        'compare': fields.boolean('Comparar con el ejercicio anterior'),
        'unidades': fields.selection([('euros','Euros'), ('miles','Miles de Euros'), ('millones','Millones de Euros')], 'Unidad'), 
    }
    _defaults = {
        'compare': False,
    }
    

    def create_report(self, cursor, uid, ids, context):
        #Recuperem les dades del filtre (wizard)
        res = self.read(cursor, uid, ids, ['ejercicio','compare','unidades'], context=context)
        #Posem les dades en un array
        res = res and res[0] or {}
        #Recuperem els camps desitjats
        ejercicio = res['ejercicio']
        compare = res['compare']
        unidades = res['unidades']

        if context is None:
            context = {}
        
        res['info'] = [ejercicio,compare,unidades]
        data = res
        datas = {
                     'ids': [],
                     'model': 'res.company.datos.generales.identificacion',
                     'form': data
        }
        return {'type': 'ir.actions.report.xml', 'report_name': 'report.datos.generales.identificacion.abreviado', 'datas': datas}

identificacion_abreviado_wizard()

class identificacion_normal_wizard(osv.osv_memory):
    
    def _get_selection(self, cr, uid, context=None):
        obj = self.pool.get('res.company.datos.generales.identificacion')
        ids = obj.search(cr, uid, [])
        res = obj.read(cr, uid, ids, ['nombre_ejercicio', 'id'], context)
        res = [(r['id'], r['nombre_ejercicio']) for r in res]
        
        return res

    _name = 'identificacion.normal.wizard'
    _description = 'Identificacion normal Wizard'

    _columns = {
        'ejercicio': fields.selection(_get_selection,'Ejercicio base'),
        'compare': fields.boolean('Comparar con el ejercicio anterior'),
        'unidades': fields.selection([('euros','Euros'), ('miles','Miles de Euros'), ('millones','Millones de Euros')], 'Unidad'), 
    }
    _defaults = {
        'compare': False,
    }
    

    def create_report(self, cursor, uid, ids, context):
        #Recuperem les dades del filtre (wizard)
        res = self.read(cursor, uid, ids, ['ejercicio','compare','unidades'], context=context)
        #Posem les dades en un array
        res = res and res[0] or {}
        #Recuperem els camps desitjats
        ejercicio = res['ejercicio']
        compare = res['compare']
        unidades = res['unidades']

        if context is None:
            context = {}
        
        res['info'] = [ejercicio,compare,unidades]
        data = res
        datas = {
                     'ids': [],
                     'model': 'res.company.datos.generales.identificacion',
                     'form': data
        }
        return {'type': 'ir.actions.report.xml', 'report_name': 'report.datos.generales.identificacion.normal', 'datas': datas}

identificacion_normal_wizard()