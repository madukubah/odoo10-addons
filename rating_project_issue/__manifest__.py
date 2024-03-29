# -*- coding: utf-8 -*-
{
    'name': 'Issue Rating',
    'version': '1.1.1',
    'category': 'Project',
    'description': """
This module allows a customer to give rating on Project Issue.
""",
    'website': 'http://odoo.com',
    'depends': [
        'rating_project',
        'project_issue'
    ],
    'data': [
        'data/project_issue_data.xml',
        'views/project_issue_view.xml',
    ],
    'demo': [
        'data/project_issue_demo.xml',
    ],
    'installable': True,
}
