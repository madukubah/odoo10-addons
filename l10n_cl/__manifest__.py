# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Cubic ERP - Teradata SAC. (http://cubicerp.com).

{
    'name': 'Chile - Accounting',
    'version': '1.1.1',
    'description': """
Chilean accounting chart and tax localization.
==============================================
Plan contable chileno e impuestos de acuerdo a disposiciones vigentes

    """,
    'author': 'Cubic ERP',
    'website': 'http://cubicERP.com',
    'category': 'Localization',
    'depends': ['account'],
    'data': [
        'data/l10n_cl_chart_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.yml',
    ],
}
