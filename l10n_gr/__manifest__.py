# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2009 P. Christeas <p_christ@hol.gr>. All Rights Reserved

{
    'name': 'Greece - Accounting',
    'author': 'P. Christeas, OpenERP SA.',
    'website': 'http://openerp.hellug.gr/',
    'category': 'Localization',
    'version': '1.1.1',
    'description': """
This is the base module to manage the accounting chart for Greece.
==================================================================

Greek accounting chart and localization.
    """,
    'depends': ['base', 'account', 'base_iban', 'base_vat'],
    'data': [ 'data/account_type_data.xml',
              'data/l10n_gr_chart_data.xml',
              'data/account_chart_template_data.xml',
              'data/account_tax_data.xml',
              'data/account_chart_template_data.yml'
    ],
}
