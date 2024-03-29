# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Cubic ERP - Teradata SAC. (http://cubicerp.com).

{
    'name': 'Peru - Accounting',
    'description': """
Peruvian accounting chart and tax localization. According the PCGE 2010.
========================================================================

Plan contable peruano e impuestos de acuerdo a disposiciones vigentes de la
SUNAT 2011 (PCGE 2010).

    """,
    'author': ['Cubic ERP'],
    'website': 'http://cubicERP.com',
    'version': '1.1.1',
    'category': 'Localization',
    'depends': ['account'],
    'data': [
        'data/l10n_pe_chart_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.yml',
    ],
}
