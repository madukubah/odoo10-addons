# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) conexus.at

{
    'name': 'Austria - Accounting',
    'version': '1.1.1',
    'author': 'conexus.at',
    'website': 'http://www.conexus.at',
    'category': 'Localization',
    'depends': ['base_vat'],
    'description': """
This module provides the standard Accounting Chart for Austria which is based on the Template from BMF.gv.at.
============================================================================================================= 
Please keep in mind that you should review and adapt it with your Accountant, before using it in a live Environment.
""",
    'data': ['data/l10n_at_chart_data.xml',
             'data/account_tax_data.xml',
             'data/account_chart_template_data.yml'],
}
