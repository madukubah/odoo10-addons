# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Gauge Widget for Kanban',
    'version' : '1.1.1',
    'category': 'Hidden',
    'description': """
This widget allows to display gauges using d3 library.
""",
    'version': '1.0',
    'depends': ['web_kanban'],
    'data' : [
        'views/web_kanban_gauge_templates.xml',
    ],
    'qweb': [
    ],
    'auto_install': True,
}
