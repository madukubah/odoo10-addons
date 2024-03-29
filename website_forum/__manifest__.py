# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Forum',
    'category': 'Website',
    'sequence': 150,
    'summary': 'Forum, FAQ, Q&A',
    'version' : '1.1.1',
    'description': """
Ask questions, get answers, no distractions
        """,
    'website': 'https://www.odoo.com/page/community-builder',
    'depends': [
        'auth_signup',
        'gamification',
        'website_mail',
        'website_partner'
    ],
    'data': [
        'data/forum_data.xml',
        'views/forum.xml',
        'views/res_users.xml',
        'views/website_forum.xml',
        'views/ir_qweb.xml',
        'security/ir.model.access.csv',
        'data/badges_question.xml',
        'data/badges_answer.xml',
        'data/badges_participation.xml',
        'data/badges_moderation.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'demo': [
        'data/forum_demo.xml',
    ],
    'installable': True,
    'application': True,
}
