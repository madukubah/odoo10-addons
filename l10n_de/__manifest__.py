# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Deutschland - Accounting',
    'author': 'openbig.org',
    'version': '1.1.1',
    'website': 'http://www.openbig.org',
    'category': 'Localization',
    'description': """
Dieses  Modul beinhaltet einen deutschen Kontenrahmen basierend auf dem SKR03.
==============================================================================

German accounting chart and localization.
    """,
    'depends': ['account', 'base_iban', 'base_vat'],
    'data': [
        'data/account_account_types_data.xml',
        'data/account_account_tags_data.xml',
        'data/menuitem_data.xml',
    ],
}
