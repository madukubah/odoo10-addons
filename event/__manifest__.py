# -*- coding: utf-8 -*-
{
    'name': 'Events Organization',
    'version': '1.1.1',
    'website': 'https://www.odoo.com/page/events',
    'category': 'Marketing',
    'summary': 'Trainings, Conferences, Meetings, Exhibitions, Registrations',
    'description': """
Organization and management of Events.
======================================

The event module allows you to efficiently organize events and all related tasks: planning, registration tracking,
attendances, etc.

Key Features
------------
* Manage your Events and Registrations
* Use emails to automatically confirm and send acknowledgments for any event registration
""",
    'depends': ['base_setup', 'mail', 'report'],
    'data': [
        'security/event_security.xml',
        'security/ir.model.access.csv',
        'wizard/event_confirm_view.xml',
        'views/event_views.xml',
        'report/report_event_registration_view.xml',
        'report/event_event_templates.xml',
        'report/event_event_reports.xml',
        'data/event_data.xml',
        'views/event_config_settings_views.xml',
        'views/event_templates.xml',
        'data/email_template_data.xml',
    ],
    'demo': [
        'data/event_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
