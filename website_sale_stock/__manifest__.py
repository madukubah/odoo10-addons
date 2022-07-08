# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Sale Stock - Website Delivery Information',
    'version' : '1.1.1',
    'category': 'Website',
    'description': """
    Display delivery orders (picking) infos on the website
""",
    'depends': [
        'website_sale',
        'sale_stock',
    ],
    'auto_install': True,
    'data': [
        'views/website_sale_stock_templates.xml',
    ]
}
