# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'WMS Accounting',
    'version' : '1.1.1',
    'summary': 'Inventory, Logistic, Valuation, Accounting',
    'description': """
WMS Accounting module
======================
This module makes the link between the 'stock' and 'account' modules and allows you to create accounting entries to value your stock movements

Key Features
------------
* Stock Valuation (periodical or automatic)
* Invoice from Picking

Dashboard / Reports for Warehouse Management includes:
------------------------------------------------------
* Stock Inventory Value at given date (support dates in the past)
    """,
    'website': 'https://www.odoo.com/page/warehouse',
    'depends': ['stock', 'account'],
    'category': 'Hidden',
    'sequence': 16,
    'demo': [
        'data/stock_account_demo.yml'
    ],
    'data': [
        'security/stock_account_security.xml',
        'security/ir.model.access.csv',
        'wizard/stock_change_standard_price_views.xml',
        'wizard/wizard_valuation_history_views.xml',
        'views/product_views.xml',
        'views/stock_account_views.xml',
        'views/stock_config_settings_views.xml',
        'report/stock_history_views.xml',
        'data/product_data.xml',
        'data/stock_account_data.xml',
        'data/stock_account_data_post_install.yml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': True,
}
