# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Survey CRM',
    'version' : '1.1.1',
    'category': 'Marketing',
    'complexity': 'easy',
    'website': 'https://www.odoo.com/page/survey',
    'description': """
Survey - CRM (bridge module)
=================================================================================
This module adds a Survey mass mailing button inside the more option of lead/customers views
""",
    'depends': ['crm', 'survey'],
    'data': [
        'views/survey_crm_views.xml',
    ],
    'installable': True,
    'auto_install': True
}
