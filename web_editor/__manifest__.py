# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Editor',
    'version' : '1.1.1',
    'category': 'Hidden',
    'description': """
Odoo Web Editor widget.
==========================

""",
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/editor.xml',
        'views/iframe.xml',
        'views/snippets.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
