# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Decimal Precision Configuration',
	'version' : '1.1.1',
    'description': """
Configure the price accuracy you need for different kinds of usage: accounting, sales, purchases.
=================================================================================================
""",
    'version': '1.1.1',
    'depends': ['base'],
    'category' : 'Hidden',
    'data': [
        'views/decimal_precision_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
}
