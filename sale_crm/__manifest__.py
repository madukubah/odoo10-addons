# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Opportunity to Quotation',
    'version' : '1.1.1',
    'category': 'Hidden',
    'description': """
This module adds a shortcut on one or several opportunity cases in the CRM.
===========================================================================

This shortcut allows you to generate a sales order based on the selected case.
If different cases are open (a list), it generates one sale order by case.
The case is then closed and linked to the generated sales order.

We suggest you to install this module, if you installed both the sale and the crm
modules.
    """,
    'website': 'https://www.odoo.com/page/crm',
    'depends': ['sale', 'crm', 'web_kanban_gauge'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/sale_order_views.xml',
        'views/crm_lead_views.xml',
        'views/crm_team_views.xml',
        'views/sale_crm_template.xml',
    ],
    'auto_install': True,
}
