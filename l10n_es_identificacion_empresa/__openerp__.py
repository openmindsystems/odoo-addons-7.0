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

{
    "name" : "Datos generales de identificación de la empresa",
    "version" : "0.1",
    "author" : "Openmindsystems",
    "license" : "AGPL-3",
    "website" : "http://www.openmindsystems.com.es",
    "category" : "Localisation/Accounting",
    "description": """
Datos generales de identificación de la empresa.
================================================

Permite guardar los datos de identificación de la empresa y después extraer los informes necesarios
para presentarlos al registro mercantil.

    * Datos generales de identificación PYMEs
    * Datos generales de identificación Abreviado
    * Datos generales de identificación Normal

    """,
    "depends": [],
    "demo" : [],
    "data" : [],
    "update_xml" : [
        'identificacion_view.xml',
        'report/datos_generales_identificacion_report.xml',
        'wizard/identificacion_wizard.xml'],
    "installable": True,
}