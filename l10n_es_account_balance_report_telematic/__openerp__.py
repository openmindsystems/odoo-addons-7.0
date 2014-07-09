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
    "name" : "Informes de cuentas anuales españoles - Formato telemático",
    "version" : "0.1",
    "author" : "Openmindsystems",
    "license" : "AGPL-3",
    "website" : "http://www.openmindsystems.com.es",
    "category" : "Localisation/Accounting",
    "description": """
Informes de cuentas anuales oficiales españoles en formato telemático.
================================================

Incluye las siguientes plantillas para el motor de informes de cuentas provisto
por el módulo *account_balance_reporting*:

    * Balance PYMEs
    * Balance Abreviado
    * Balance Normal
    * PyG PYMEs
    * PyG Abreviado
    * PyG Normal

    """,
    "depends": [
        'l10n_es',
        'account_balance_reporting',
    ],
    "demo" : [ ],
    "data" : [
        'report/account_balance_report_telematic.xml',
        'data/balance_pymes_telematic.xml',
        'data/balance_abreviado_telematic.xml',
        'data/balance_completo_telematic.xml',
        'data/pg_pymes_telematic.xml',
        'data/pg_abreviado_telematic.xml',
        'data/pg_completo_telematic.xml',        
    ],
    "installable": True,
}
